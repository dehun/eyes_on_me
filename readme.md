# Intro #
eyes_on_me is simple utility which allows you to control your screen backlight and temperature according to lighting.
This project is very similar to x.flux and redshift. This is attempt to combine all the best stuff about eyes care on PC.

# Installation #
Variant A

    hg clone https://bitbucket.org/dehun/eyes_on_me
    cd eyes_on_me
    sudo python setup.py install
    sudo apt-get install fswebcam xbacklight
    cp eyes_on_me/etc/.eyes_on_me_rc ~/

Variant B

    sudo pip install eyes_on_me
    sudo apt-get install xbacklight fswebcam

# Configuration #
Create a file ~/.eyes_on_me_rc.
Put the following content into it

    {
        "strategy": "webcam",

        "daemon": {
            "pid": "/tmp/eyes_on_me.pid",
            "update-interval": 30
        },

        "backlight": {
            "min": 5,
            "normal": 30,
            "max": 60
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
            "coeff": 0.6
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

# Config file #
Config file should be placed at ~/.eyes_on_me_rc
The content is next

    {
        "strategy": "webcam",             // choosen strategy. webcam or timed

        "daemon": {                       // daemon setting
            "pid": "/tmp/eyes_on_me.pid", // path to daemon's pid
            "update-interval": 60,        // update interval in seconds
            "log-path": "/home/dehun/.eyes-on-me.log" // path to log file. optional.
        },

        "backlight": {                    // backlight adjusting settings
            "min": 5,                     // minimal backlight
            "normal": 20,                 // normal backlight level
            "max": 45                     // maximal backlight level
        },

        "wb_balance": {
            "min": 3500,                  // minimal temparature
            "normal": 4500,               // normal temperature
            "max": 6000                   // maximal temperature
        },

        "timed-strategy": {               // settings for timed strategy
            "city": "Amsterdam",          // your city name
            "light-table": {              // levels of light for different times. should be [0; 1.0]
                "dawn": 0.2,
                "sunrise": 0.6,
                "noon": 1.0,
                "sunset": 0.6,
                "dusk": 0.2
            }
        },

        "webcam-strategy": {              // settings for webcam strategy
            "shot-path": "/tmp/eyes-on-me-shoot.jpg",  // where to put temporary photo
            "command": "fswebcam %(shot_path)s",       // command for launching webcam
            "coeff": 0.6                               // coefficient for adjusting light level
        }
    }


# Adjusting fswebcam #
You can achieve a better results by adjusting fswebcam software.
To see the list of adjustments run

    fswebcam --list-controls

Good results can be achieved by turning off auto adjustments.
On my thinkpad I use the following set of commands

    fswebcam --set "Exposure, Auto"="Manual Mode"
    fswebcam --set "Exposure (Absolute)"=1000
    fswebcam --set "Exposure, Auto Priority"="False"
