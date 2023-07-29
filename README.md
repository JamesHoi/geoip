# geoip
A toy for check domain location

## Usage
```bash
> geoip -6 google.com
ip1: 2404:6800:4012:4::200e
location: India Maharashtra Mumbai
lambda: 19.076 longitude: 72.8777

> geoip -4 google.com
ip1: 172.217.163.46
location: India Tamil Nadu Chennai
lambda: 13.0827 longitude: 80.2707
```

## Install
```bash
git clone https://github.com/JamesHoi/geoip
cd geoip & python setup.py install
```

## Todo
1. Support older python version
2. Add additional argument of specified dns
