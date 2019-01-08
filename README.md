# piJenMon

## Raspberry Pi monitoring Jenkins jobs build status

This project is a collection of python scripts that has the sole purpose of showing the status of all builds on a Jenkins Server.
This is meant to be a multi unit application, so all configuration of the instance is kept in a [consul](https://www.consul.io/) property dictionary, i.e. keeping each running instance stateless.

The hardware components of this project is the following:
 - [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
 - [blinkt!](https://shop.pimoroni.com/products/blinkt) - an 8 LED display from [Pimoroni](https://shop.pimoroni.com/)

The third party python packages of this project is the following:
  - [blinkt!](https://shop.pimoroni.com/products/blinkt)
  - [Jenkins API](https://pypi.python.org/project/jenkinsapi/)
  - [python-consul](https://pypi.org/project/python-consul/)

Without these packages installed, this script will fail.
 - Install _Jenkins API_: `pip3 install jenkinsapi`
 - Install _python-consul_: `pip3 install python-consul`

The [blinkt!](https://shop.pimoroni.com/products/blinkt) library is currently only supported on a [Raspberry Pi](https://www.raspberrypi.org/)

## Local installation
The easiest way to run the system locally is to use [Docker](https://www.docker.com/) as a way to have [Jenkins](https://jenkins.io/) and [consul](https://www.consul.io/) available

### docker setup
The docker images do not run on a raspberry pi out of the box. There exists custom images, but I prefer just to use my laptop.
  - consul: [TODO: Add how to run consul locally via docker]
  - jenkins: `docker run -d -p 8080:8080 --name jenkins jenkins/jenkins:lts`
      - configure Jenkins so it can be used.
