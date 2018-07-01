#!/usr/bin/env python3
# this project is licensed under the WTFPLv2, see COPYING.WTFPL

import errno
from enum import IntFlag, IntEnum

import usb.core


class Mod(IntFlag):
	NONE = 0
	CTRL = 1
	SHIFT = 2
	ALT = 4
	SUPER = 8


class Key(IntEnum):
	NONE = 0x00

	MOD_LCTRL = 0x01
	MOD_LSHIFT = 0x02
	MOD_LALT = 0x04
	MOD_LMETA = 0x08
	MOD_RCTRL = 0x10
	MOD_RSHIFT = 0x20
	MOD_RALT = 0x40
	MOD_RMETA = 0x80
	ERR_OVF = 0x01

	A = 0x04
	B = 0x05
	C = 0x06
	D = 0x07
	E = 0x08
	F = 0x09
	G = 0x0a
	H = 0x0b
	I = 0x0c
	J = 0x0d
	K = 0x0e
	L = 0x0f
	M = 0x10
	N = 0x11
	O = 0x12
	P = 0x13
	Q = 0x14
	R = 0x15
	S = 0x16
	T = 0x17
	U = 0x18
	V = 0x19
	W = 0x1a
	X = 0x1b
	Y = 0x1c
	Z = 0x1d

	_1 : '1' = 0x1e
	_2 : '2' = 0x1f
	_3 : '3' = 0x20
	_4 : '4' = 0x21
	_5 : '5' = 0x22
	_6 : '6' = 0x23
	_7 : '7' = 0x24
	_8 : '8' = 0x25
	_9 : '9' = 0x26
	_0 : '0' = 0x27

	ENTER = 0x28
	ESC = 0x29
	BACKSPACE = 0x2a
	TAB : '\t' = 0x2b
	SPACE : ' ' = 0x2c
	MINUS : '-' = 0x2d
	EQUAL : '=' = 0x2e
	LEFTBRACE : '{' = 0x2f
	RIGHTBRACE : '}' = 0x30
	BACKSLASH : '\\' = 0x31
	HASHTILDE = 0x32
	SEMICOLON : ';' = 0x33
	APOSTROPHE : "'" = 0x34
	GRAVE = 0x35
	COMMA : ',' = 0x36
	DOT : '.' = 0x37
	SLASH : '/' = 0x38
	CAPSLOCK = 0x39

	F1 = 0x3a
	F2 = 0x3b
	F3 = 0x3c
	F4 = 0x3d
	F5 = 0x3e
	F6 = 0x3f
	F7 = 0x40
	F8 = 0x41
	F9 = 0x42
	F10 = 0x43
	F11 = 0x44
	F12 = 0x45

	SYSRQ = 0x46
	SCROLLLOCK = 0x47
	PAUSE = 0x48
	INSERT = 0x49
	HOME = 0x4a
	PAGEUP = 0x4b
	DELETE = 0x4c
	END = 0x4d
	PAGEDOWN = 0x4e

	RIGHT = 0x4f
	LEFT = 0x50
	DOWN = 0x51
	UP = 0x52

	NUMLOCK = 0x53
	KPSLASH = 0x54
	KPASTERISK = 0x55
	KPMINUS = 0x56
	KPPLUS = 0x57
	KPENTER = 0x58
	KP1 = 0x59
	KP2 = 0x5a
	KP3 = 0x5b
	KP4 = 0x5c
	KP5 = 0x5d
	KP6 = 0x5e
	KP7 = 0x5f
	KP8 = 0x60
	KP9 = 0x61
	KP0 = 0x62
	KPDOT = 0x63
	KPCOMMA = 0x85
	KPLEFTPAREN = 0xb6
	KPRIGHTPAREN = 0xb7

	_102ND = 0x64

	COMPOSE = 0x65
	POWER = 0x66
	KPEQUAL = 0x67

	F13 = 0x68
	F14 = 0x69
	F15 = 0x6a
	F16 = 0x6b
	F17 = 0x6c
	F18 = 0x6d
	F19 = 0x6e
	F20 = 0x6f
	F21 = 0x70
	F22 = 0x71
	F23 = 0x72
	F24 = 0x73

	OPEN = 0x74
	HELP = 0x75
	PROPS = 0x76
	FRONT = 0x77
	STOP = 0x78
	AGAIN = 0x79
	UNDO = 0x7a
	CUT = 0x7b
	COPY = 0x7c
	PASTE = 0x7d
	FIND = 0x7e
	MUTE = 0x7f
	VOLUMEUP = 0x80
	VOLUMEDOWN = 0x81

	RO = 0x87
	KATAKANAHIRAGANA = 0x88
	YEN = 0x89
	HENKAN = 0x8a
	MUHENKAN = 0x8b
	KPJPCOMMA = 0x8c
	HANGEUL = 0x90
	HANJA = 0x91
	KATAKANA = 0x92
	HIRAGANA = 0x93
	ZENKAKUHANKAKU = 0x94

	LEFTCTRL = 0xe0
	LEFTSHIFT = 0xe1
	LEFTALT = 0xe2
	LEFTMETA = 0xe3
	RIGHTCTRL = 0xe4
	RIGHTSHIFT = 0xe5
	RIGHTALT = 0xe6
	RIGHTMETA = 0xe7

	MEDIA_PLAYPAUSE = 0xe8
	MEDIA_STOPCD = 0xe9
	MEDIA_PREVIOUSSONG = 0xea
	MEDIA_NEXTSONG = 0xeb
	MEDIA_EJECTCD = 0xec
	MEDIA_VOLUMEUP = 0xed
	MEDIA_VOLUMEDOWN = 0xee
	MEDIA_MUTE = 0xef
	MEDIA_WWW = 0xf0
	MEDIA_BACK = 0xf1
	MEDIA_FORWARD = 0xf2
	MEDIA_STOP = 0xf3
	MEDIA_FIND = 0xf4
	MEDIA_SCROLLUP = 0xf5
	MEDIA_SCROLLDOWN = 0xf6
	MEDIA_EDIT = 0xf7
	MEDIA_SLEEP = 0xf8
	MEDIA_COFFEE = 0xf9
	MEDIA_REFRESH = 0xfa
	MEDIA_CALC = 0xfb


ACTIONS = []


def register_class(cls):
	ACTIONS.append(cls)
	return cls


class Action(object):
	pass


class SimpleKeyAction(Action):
	type_byte = None

	def __init__(self, key, mods=Mod.NONE):
		self.key = key
		self.mods = mods

	def __repr__(self):
		k = self.key
		if self.key in Key.__members__.values():
			k = Key(self.key)
		m = ''
		if self.mods:
			m = ' mods=%r' % Mod(self.mods)
		return '<%s key=%r%s>' % (type(self).__name__, k, m)

	@classmethod
	def decode(cls, buf):
		length, type = buf[:2]
		if length != 8 and type != cls.type_byte:
			return
		return cls(buf[3], Mod(buf[2]))

	def encode(self, n):
		intro = b'\x01\x81\x08%c\x00\x00\x00\x00' % (n + 1)
		data = b'\x08%c%c%c\x00\x00\x00\x00' % (self.type_byte, self.mods, self.key)
		return intro + data


@register_class
class ShotKeyAction(SimpleKeyAction):
	type_byte = 0x81


@register_class
class KeyAction(SimpleKeyAction):
	type_byte = 0x3


@register_class
class KeyCombination(Action):
	def __init__(self, keys, mods=Mod.NONE):
		if len(self.keys) > 6:
			raise ValueError('Cannot have more than 6 items')
		self.keys = keys
		self.mods = mods

	def __repr__(self):
		return '<%s keys=%r>' % (type(self).__name__, self.keys)

	@classmethod
	def decode(cls, buf):
		if buf[1] != 6:
			return

		end = buf[0]
		mods = buf[2]
		if mods:
			end -= 1
		keys = list(buf[3:end])
		return cls(keys)

	def encode(self, n):
		buf = b'\x06%c' % self.mods
		buf += bytes(self.keys)

		length = len(self.keys)
		if self.mods:
			length += 1
		buf = b'%c%s' % (length, buf)

		if len(buf) % 8:
			buf += b'\x00' * (8 - length % 8)
		return buf


@register_class
class StringAction(Action):
	lower = 4
	upper = 128 + 4

	def __init__(self, s):
		self.s = s

	def __repr__(self):
		return '<%s s=%r>' % (type(self).__name__, self.s)

	@classmethod
	def from_char(cls, c):
		if c in Key.__members__.values():
			name = Key(c).name
			if name in Key.__annotations__:
				return Key.__annotations__[name]
			assert len(name) == 1
			return name

		if 'a' <= c <= 'z':
			return ord(c) - ord('a') + cls.lower
		if 'A' <= c <= 'Z':
			return ord(c) - ord('A') + cls.upper

		if c in Key.__members__:
			return getattr(Key, c)
		# FIXME pretty inefficient
		d = {v: k for k, v in Key.__annotations__.items()}
		return getattr(Key, d[c])

	@classmethod
	def from_byte(cls, b):
		if b in Key.__members__.values():
			name = Key(b).name
			if name in Key.__annotations__:
				return Key.__annotations__[name]
			assert len(name) == 1
			return name

		if cls.lower <= b < cls.lower + 26:
			b -= cls.lower
			return chr(b + ord('a'))
		if cls.upper <= b < cls.upper + 26:
			b -= cls.upper
			return chr(b + ord('A'))

		raise ValueError('Cannot decode byte %d' % b)

	@classmethod
	def decode(cls, buf):
		if buf[1] == 0x4:
			end = buf[0]
			msg = buf[2:end]
			return cls(''.join(cls.from_byte(b) for b in msg))

	def encode(self, n):
		length = len(self.s) + 2
		buf = b'\x01\x81%c%c\x00\x00\x00\x00' % (length, n + 1)
		buf += b'%c\x04' % length
		buf += bytes(self.from_char(c) for c in self.s)
		if length % 8:
			buf += b'\x00' * (8 - length % 8)
		return buf


class Device(object):
	vendor = 0x413D
	product = 0x2107

	in_endpoint = 0x82
	out_endpoint = 0x2

	def __init__(self):
		self.dev = usb.core.find(idVendor=self.vendor, idProduct=self.product)
		if self.dev is None:
			raise ValueError('Our device is not connected')

	def hello_device(self):
		self.write(b'\x01\x83\x08\x00\x00\x00\00\x00')
		return self.readall()

	def get_switch_config(self, n):
		self.write(b'\x01\x82\x08%c\x00\x00\x00\x00' % (n + 1))
		buf = self.readall()
		for cls in ACTIONS:
			action = cls.decode(buf)
			if action is not None:
				return action

	def set_switch_config(self, n, action):
		buf = action.encode(n)
		self.writeall(buf)

	def disable_kernel(self, i):
		if self.dev.is_kernel_driver_active(i):
			self.dev.detach_kernel_driver(i)

	def enable_kernel(self, i):
		if not self.dev.is_kernel_driver_active(i):
			self.dev.attach_kernel_driver(i)

	def read(self):
		return self.dev.read(self.in_endpoint, 8)

	def readall(self):
		ret = b''
		while True:
			try:
				ret += bytes(self.dev.read(self.in_endpoint, 8, 100))
			except usb.core.USBError as e:
				if e.errno == errno.ETIMEDOUT:
					return ret
				raise

	def write(self, b):
		self.dev.write(self.out_endpoint, b)

	def writeall(self, b):
		for i in range(0, len(b), 8):
			self.write(b[i:i + 8])
