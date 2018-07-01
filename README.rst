CupidFoot is a project for configuring the `USB FootSwitch FS3_P <http://pcsensor.com/usb-foot-control-keyboard-mouse-button-three-switch-pedal-fs3_p-p180.html>`_.

The FS3_P is a cheap (cheaper on other sites) configurable USB 3 pedals HID. Each pedal can be configured to send keyboard keycodes or mouse codes.
It works out of the box under Linux, but the software for configuring the pedals is not free and only works on windows.

This project lets you configure the device on any OS thanks to `PyUSB <https://github.com/pyusb/pyusb>`_.

Version
-------
The project is in beta for now, it's usable as a lib but not yet as a command-line tool.

License
-------
It is licensed under the `WTFPLv2 <http://wtfpl.net>`_.

Dependencies
------------
It requires Python 3.6 and `PyUSB <https://github.com/pyusb/pyusb>`_.
