import datetime 
import docker

client = docker.DockerClient(base_url='tcp://127.0.0.1:2375')

for event in client.events(decode=True, filters={"event": "die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    date_time = datetime.datetime.fromtimestamp(event["time"])
    print("The container \"%s\" (%s) has stopped at %s" % (container_name, container_id, date_time))
