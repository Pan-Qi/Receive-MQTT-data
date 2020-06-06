#------------------------------------------
#--- Author: Qi Pan
#--- Date: 6/6/2020
#--- Version: 1.0
#--- Python Ver: 3.6.8
#------------------------------------------

import time
import json
import paho.mqtt.client as mqtt
import pandas as pd

# MQTT Settings 
MQTT_Broker = ""
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = ""

UserName = ""
Password = ""

# file path to store data
file_path = 'train.csv'


data = []
count = 0

def add_data(topic,payload):
	new_data = json.loads(payload)
	new_data["MQTT_Topic"] = topic
	
	gateways = new_data['metadata']['gateways'].copy()
	del new_data['metadata']['gateways']

	new_data.update(new_data["metadata"])
	del new_data['metadata']

	for gateway in gateways:
		new_data.update(gateway)
		data.append(new_data.copy())


#Subscribe to all Sensors at Base Topic
def on_connect(mqttc,mosq, obj, rc):
	print("Connect success")
	mqttc.subscribe(MQTT_Topic, 0)

#Save Data into DB Table
def on_message(mqttc, obj, msg):
	
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	global count
	print("MQTT Data Received...", str(count))
	count += 1
	add_data(msg.topic, msg.payload)


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribe success")

client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

mqttc = mqtt.Client(client_id)# ClientId不能重复，所以使用当前时间

mqttc.username_pw_set(UserName,Password)# 必须设置，否则会返回「Connected with result code 4」


# mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))



# Continue the network loop
try:
	mqttc.loop_forever()
except:
	print("Connection stopped")
	data = pd.DataFrame(data)
	data.to_csv(file_path)
	print("data write to: ", file_path)
