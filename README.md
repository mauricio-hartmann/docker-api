# docker-api

This project prints the identification of Docker containers that stop during the execution. To run this project you must to have Docker and Python installed and do some modifications on the configuration.

- [ ] Open the `docker.service` file (usually in `/usr/lib/systemd/system/docker.service`);
- [ ] Update the line to make docker able to listen HTTP requests:
```
ExecStart=/usr/bin/dockerd -H fd:// -H tcp:0.0.0.0:2375 —containerd=/run/containerd/containerd.sock
```
- [ ] Restart docker
```
sudo systemctl daemon-reload
sudo systemctl restart docker
```
- [ ] Create a venv in the root folder
```
python3 -m venv .venv
```
- [ ] Enter in the venv and install docker
```
source .venv/bin/activate
pip install docker
```
- [ ] Run the project with the following command:
```
python3 events.py
```
- [ ] Create and run some container. When the container stop the script will print the container identification. You can run an example container with the following code:
```
docker pull nginx
docker run --name docker-nginx -p 80:80 nginx
```