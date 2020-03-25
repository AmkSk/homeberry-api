#!/home/pi/homeberryApi/bin/python
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def helloWorld():
	return "Hello World\n"

@app.route("/bt_speaker/stop")
def stopBtSpeaker():
	subprocess.run("sudo systemctl stop bt_speaker".split())
	return "Stopping bt_speaker service"

@app.route("/bt_speaker/start")
def startBtSpeaker():
	subprocess.run("sudo systemctl start bt_speaker".split())
	return "Starting bt_speaker service"

@app.route("/kodi/kill")
def killKodi():
	subprocess.run("sudo systemctl stop kodi".split())
	return "Killing Kodi service"

@app.route("/kodi/start")
def startKodi():
	subprocess.run("sudo systemctl start kodi".split())
	return "Starting Kodi service"

@app.route("/shutdown")
def shutdown():
	subprocess.run("sudo shutdown -h now".split())
	return "Shutting down Raspberry"

@app.route("/reboot")
def reboot():
	subprocess.run("sudo shutdown -r now".split())
	return "Restarting Raspberry"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

