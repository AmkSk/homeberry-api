# homeberry-api

Example REST API service for the [Homeberry project](https://github.com/AmkSk/homeberry)

## Installation
1. You need create a new virtual environment for the flask webserver. There is a [lot of tutorials online]( http://raspberryjamberlin.de/portfolio/install-flask-on-a-raspberry-pi/), but basically you want to create an virtual environment for the server:
```bash
$ virtualenv homeberryApi
```

2. Edit `homeberryApi.py` to your run your services / commands

3. Create and start service on boot by copying the homeberryApi.service file to `/etc/systemd/system/` directory and enabling it:
```bash
$ sudo systemctl enable homeberryApi.service
$ sudo systemctl start homeberryApi.service
```
