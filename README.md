# MQTT bridge to Etatherm IRC heating system
Etatherm is great Czech IRC heating control system, see here https://www.etatherm.cz/.

It runs in my home since 2005 without issues. The first version of the control unit did not have Web GUI, but it had changed with introduction of the ETH1e and ETH1i control units. Unfortunately it cannot be integrated with other systems because communication protocol is proprietary. I was lucky asking the manufacturer for the protocol documentation. I don't have a permission to share it but I was able to code this library so that Etatherm can be controlled from other systems, e.g. Home Assistant.

I use this library and slightly modified sample program to control Etatherm system from Home Assistant for two years already. It runs without any issue. I run it on Turris in LXC container.


Repository content:

**etatherm.py** is library

**mqtt.py** is sample program that controls Etatherm system using MQTT messages

## Functionality
1) allows to read most of the control unit parameters
2) allows to activate automatic, heating and off mode
3) when heating mode is activated it actually activates *ROZ* (Rychlá operativní změna in Czech)
4) when off mode is activated it sets target temperature to 6°C
5) in heating mode, target temperature can be set between 6°C and 35°C; after time set in *ROZ* elapses, control unit automatically switches back to the automatic mode
6) the off mode is set until set manually to the automatic or heat mode
7) allows to switch between different named heating maps. Heating maps must be preconfigured using Web GUI or Windows program
8) allows to activate and deactivate *HOZ* (Hromadná operativní změna in Czech); I use it in Home Assistant automations to set holiday temperature when leaving home and automatic before arrival

## Limitations
1) does not support setting of system parameters, like passwords, programs, heating maps, ...
2) does not allow to configure bus devices

## Functionality principles
The library transfers temperatures, heating modes and other parameters between MQTT Broker and ETH1x control unit. Since the CPU in the control unit is not powerful (I have no idea which CPU is currently used) the communication stucks from time to time, so packets are retransmitted after timeout. It may last quite long to retrieve or store data to the control unit and that is why I have implemented command queue that controls communication with the control unit. The library writes command and parameters to the queue and the queue manager executes them in serial order. The control unit is not overloaded and reads or writes to the control unit fully execute prior another read or write is executed.

MQTT topic configuration can be fully customized in the library by changing string costants.

## Home Assistant example configuration in the climate .yaml file
- name: "Work room"
  
  object_id: etatherm_workroom_heating

  unique_id: etatherm_workroom_heating

  current_temperature_topic: "etatherm/1/temperature/real"

  temperature_unit: "C"

  precision: 1.0

  min_temp: 6

  max_temp: 35

  initial: 19

  temp_step: 1

  temperature_state_topic: "etatherm/1/temperature/target"

  mode_state_topic: "etatherm/1/mode"

  mode_command_topic: "etatherm/1/mode/set"

  temperature_command_topic: "etatherm/1/temperature/target/set"
