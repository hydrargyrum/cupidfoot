#!/usr/bin/env python3
# this project is licensed under the WTFPLv2, see COPYING.WTFPL

from argparse import ArgumentParser
from collections import OrderedDict
import sys

from cupidfoot import lib


parser = ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-1', dest='pedal', action='store_const', const=1)
group.add_argument('-2', dest='pedal', action='store_const', const=2)
group.add_argument('-3', dest='pedal', action='store_const', const=3)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--get', action='store_true')
group.add_argument('--short-press')
group.add_argument('--long-press')
group.add_argument('--combine')
group.add_argument('--string')

parser.add_argument('--ctrl', action='store_true')
parser.add_argument('--shift', action='store_true')
parser.add_argument('--alt', action='store_true')
parser.add_argument('--super', action='store_true')

args = parser.parse_args()

try:
	dev = lib.Device()
except ValueError:
	print('Could not find device, is it plugged?', file=sys.stderr)
	sys.exit(1)


mods = lib.Mod.NONE
if args.ctrl:
	mods |= lib.Mod.CTRL
if args.shift:
	mods |= lib.Mod.SHIFT
if args.super:
	mods |= lib.Mod.SUPER
if args.alt:
	mods |= lib.Mod.ALT

def parse_keys(s):
	if not s:
		return (lib.Key.NONE, lib.Mod.NONE)

	keys = OrderedDict()
	keys.update((v, k) for k, v in lib.Key.__annotations__.items())
	keys.update(lib.Key.__members__)

	s = s.upper()
	parts = s.split('+')

	mods = lib.Mod.NONE
	res = lib.Key.NONE
	for p in parts:
		if p == '':
			p = '+'

		if p in ('CTRL', 'SHIFT', 'ALT', 'SUPER'):
			mods |= getattr(lib.Mod, p)
		elif res:
			raise ValueError()
		else:
			res = keys[p]

	return (res, mods)


def parse_keys_multi(s):
	if not s:
		return ([], lib.Mod.NONE)

	keys = OrderedDict()
	keys.update((v, k) for k, v in lib.Key.__annotations__.items())
	keys.update(lib.Key.__members__)

	s = s.upper()
	parts = s.split('+')

	mods = lib.Mod.NONE
	res = []
	for p in parts:
		if p == '':
			p = '+'

		if p in ('CTRL', 'SHIFT', 'ALT', 'SUPER'):
			mods |= getattr(lib.Mod, p)
		else:
			res.append(keys[p])

	return (res, mods)


if args.get:
	action = 'get'
elif args.string:
	action = lib.StringAction(args.string)
elif args.short_press is not None:
	key, m2 = parse_keys(args.short_press)
	mods |= m2
	action = lib.ShotKeyAction(key, mods)
elif args.long_press is not None:
	key, m2 = parse_keys(args.long_press)
	mods |= m2
	action = lib.KeyAction(key, mods)
elif args.combine is not None:
	keys, m2 = parse_keys_multi(args.combine)
	mods |= m2
	action = lib.KeyCombination(keys, mods)
else:
	raise ValueError()

dev.disable_kernel(0)
dev.disable_kernel(1)

try:
	if action == 'get':
		print(dev.get_switch_config(args.pedal - 1))
	else:
		dev.set_switch_config(args.pedal - 1, action)
finally:
	dev.enable_kernel(0)
