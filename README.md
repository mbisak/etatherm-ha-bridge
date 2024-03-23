# MQTT bridge to Etatherm IRC heating system
Etatherm is great Czech IRC heating control system, see here https://www.etatherm.cz/.

It runs in my home since 2005 without issues. The first version of the control unit did not have Web GUI, but it had changed with introduction of the ETH1e and ETH1i control units. Unfortunately it cannot be integrated with other systems because communication protocol is proprietary. I was lucky asking the manufacturer for the protocol documentation. I don't have a permission to share it but I was able to code this library so that Etatherm can be controlled from other systems, e.g. Home Assistant.

I use this library and slightly modified sample program to control Etatherm system from Home Assistant for two years already. It runs without any issue. I run it on Turris in LXC container.


Repository content:

**etatherm.py** is library

**mqtt.py** is sample program that controls Etatherm system using MQTT messages

## Functionality:
1) allows to read most of the control unit parameters
2) allows to activate automatic, heating and off mode
3) when heating mode is activated it actually activates *ROZ* (Rychlá operativní změna in Czech)
4) when off mode is activated it sets target temperature to 6°C
5) in heating mode, target temperature can be set between 6°C and 35°C; after time set in *ROZ* elapses, control unit automatically switches back to the automatic mode
6) the off mode is set until set manually to the automatic or heat mode
7) allows to switch between different named heating maps. Heating maps must be preconfigured using Web GUI or Windows program
8) allows to activate and deactivate *HOZ* (Hromadná operativní změna in Czech); I use it in Home Assistant automations to set holiday temperature when leaving home and automatic before arrival

## Limitations:
1) does not support setting of system parameters, like passwords, programs, heating maps, ...
2) does not allow to configure bus devices

## Functionality principles
