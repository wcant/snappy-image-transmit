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
