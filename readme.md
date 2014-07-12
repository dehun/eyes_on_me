# Intro #
eyes_on_me is simple utility which allows you to control your screen backlight and temperature according to lighning.
This project is very similar to x.flux and redshift. This is attempt to combine all the best stuff about eyes care on PC.

# Installation #

    sudo pip install eyes_on_me
    sudo apt-get install xbacklight fswebcam

# Configuration #
Create a file ~/.eyes_on_me_rc.
Put the following content into it

    {
        "strategy": "webcam",

        "daemon": {
            "pid": "/tmp/eyes_on_me.pid",
            "update-interval": 360
        },

        "backlight": {
            "min": 5,
            "normal": 20,
            "max": 45
        },

        "wb_balance": {
            "min": 3500,
            "normal": 4500,
            "max": 6000
        },

        "timed-strategy": {
            "city": "Amsterdam",
            "light-table": {
                "dawn": 0.2,
                "sunrise": 0.6,
                "noon": 1.0,
                "sunset": 0.6,
                "dusk": 0.2
            }
        },

        "webcam-strategy": {
            "shot-path": "/tmp/eyes-on-me-shoot.jpg",
            "command": "fswebcam %(shot_path)s",
            "coeff": 0.7
        }
    }

# Launch #
All the commands are executed with a eyes_on_me binary.

    eyes_on_me --help

You can manually set temperature by calling

    eyes_on_me --set-wb 4500
    eyes_on_me --get-wb            # get current wb

Or backlight

    eyes_on_me --set-backlight 45
    eyes_on_me --get-backlight     # get cucrent backlight


But the main feature is to auto adjust these params.

    eyes_on_me --once

Will adjust parameters and exit.

    eyes_on_me --daemon

Will launch daemon which will autoadjust with some interval of time.
