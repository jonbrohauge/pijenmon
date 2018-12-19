# piJenMon

This project is a collection of python scripts that has the sole purpose of showing the status of all builds on a Jenkins Server.
This is meant to be a multi unit application, so all configuration of the instance is kept in an [etcd](https://coreos.com/etcd/) property dictionary, i.e. keeping each running instance stateless.

The hardware components of this project is the following:
 - [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
 - [blinkt!](https://shop.pimoroni.com/products/blinkt) - an 8 LED display from [Pimoroni](https://shop.pimoroni.com/)

The third party python packages of this project is the following:
  - [blinkt!](https://shop.pimoroni.com/products/blinkt)
  - [Jenkins API](https://pypi.python.org/pypi/jenkinsapi)
  - [etcd3](https://pypi.python.org/pypi/etcd3)

Without these packages installed, this script will fail.
 - Install _etcd_: `pip3 install etcd3`
 - Install _Jenkins API_: `pip3 install jenkinsapi`
 

The [blinkt!](https://shop.pimoroni.com/products/blinkt) library is currently only supported on a [Raspberry Pi](https://www.raspberrypi.org/)

## Local installation
The easiest way to run the system locally is to use [Docker](https://www.docker.com/) as a way to have [Jenkins](https://jenkins.io/) and [etcd](https://coreos.com/etcd/) available

### docker setup
  - etcd: `docker run -d -p 2379:2379 -p 2380:2380 --env "ETCDCTL_API=3" --name etcd quay.io/coreos/etcd:latest /usr/local/bin/etcd --listen-client-urls http://0.0.0.0:2379 --initial-advertise-peer-urls http://localhost:2380 --advertise-client-urls http://localhost:2379`
  - jenkins: `docker run -d -P jenkins:latest`
      - configure Jenkins so it can be used.
