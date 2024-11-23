#constants.py

#MQTT broker address (public broker or private IP).Replace with your own broker if needeD.
BROKER = "localhost"

#MQTT broker port(default is 1883 for non-SSL connections).
PORT = 1883

#MQTT topic for subscribing to home automation device updates.
TOPIC_SUB = "home/automation/devices/status"

#MQTT topic for publishing control ,essages to devices.
TOPIC_PUB = "home/automation/devices/control"

#Unique client ID for the subscriber.Must be unique per client connected to the same broker 
CLIENT_ID_SUB = "home_automation_subscriber_01"

#Unique client ID for the subscriber.Must be unique per client connected to the same broker 
CLIENT_ID_PUB = "home_automation_publisher_01"

#keep-alive interval (in seconds) for MQTT connection ensures the client stays connected.
KEEP_ALIVE = 60