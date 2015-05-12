NOTE: I can't get pillow to install on RPi A+, not enough memory.  

Starting from a fresh Raspbian install:

1. sudo apt-get install python-dev python-setuptools

2. Python Pillow module installation:
    need the follow libraries
    sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev
        liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev

    sudo pip install virtualenv virtualenvwrapper
    workon (name)
    pip install pillow

3.  wget http://forums.synapse-wireless.com/upload/snapconnect-3.1.0-python2.7.zip


Opening Serial Ports on Raspberry Pi
(This may not be necessary, since I was able to use /dev/ttyUSB0)

By default /dev/ttyAMA0 is tied up by getty on Raspbian. I've read suggestions 
to free up ttyAMA0 and that it should be used for serial communication on
the Pi.  If using /dev/ttyUSB0 works then this is probably unnecessary.

1. Make sure your userid is a member of the dialout group.
  
     sudo usermod -a -G dialout pi

2. Remove references to /dev/ttyAMA0 from /boot/cmdline.txt

    dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 rootwait

3. Disable getty on ttyAMA0 in /etc/inittab

    Comment the line: #2:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100

4. Reboot
