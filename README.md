# MQTT bridge to Etatherm IRC heating system
Etatherm is great Czech IRC heating control system, see here https://www.etatherm.cz/.

It runs in my home since 2005 without issues. The first version of the control unit did not have Web GUI, but it had changed with introduction of the ETH1e and ETH1i control units. Unfortunately it cannot be integrated with other systems because communication protocol is proprietary. I was lucky asking the manufacturer for the protocol documentation. I don't have a permission to share it but I was able to code this library so that Etatherm can be controlled from other systems, e.g. Home Assistant.

I use this library and slightly modified sample program to control Etatherm system from Home Assistant for two years already. It runs without any issue. I run it on Turris in LXC container.


Repository content:

**etatherm.py** is library

**mqtt.py** is sample program that controls Etatherm system using MQTT messages
