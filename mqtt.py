import schedule
import etatherm as etatherm
import logging

ETATHERMHOST= '{IP/hostname of the Etatherm control}'
ETATHERMPORT = {port}
MQTTBROKERHOST = '{MQTT Broker IP/hostname}'
MQTTBROKERPORT = {MQTT Broker port}
ETATHERMMQTTPREFIX = 'etatherm/'

print("Starting program")
etherm = etatherm.etatherm.etatherm(ETATHERMHOST, ETATHERMPORT)
if not(etherm.initAddressParameters()):
    etherm.initMqtt(MQTTBROKERHOST,MQTTBROKERPORT,"","")
    etherm.mqttSessionOpen()
    etherm.mqttSubscribeTopics()
    etherm.mqttRegisterCallback()
#etherm.mqttUpdateRealTemperature()
#etherm.mqttUpdateTargetTemperature()
    etherm.readConfigFile("")
    etherm.mqttUpdate()
    etherm.schedulePeriodicMqttUpdate()
    etherm.schedulePeriodicAddressParametersUpdate()
    etherm.etathermSessionOpen()
#    print(etherm.retrieveAllActiveHeatingPrograms())
    etherm.etathermSessionClose()
    etherm.mqttUpdateHeatingMaps()
    etherm.mqttUpdateActiveHeatingMap()
    print("Entering main loop")
    while True:
        etherm.mqttSession.loop()
        schedule.run_pending()
        etherm.processCmdQueue()
    etherm.mqttSessionClose()
else:
    print("Program end")