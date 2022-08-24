# Local
1. `python3 -m venv .`
1. `pip install -r requirements.txt`
1. `python main.py -b 50 -t test -P 2 -k yourkafkaserver.com:29092`

# Docker
1. Obtain Server - can use AWS
1. Install Docker - `sudo apt install docker.io nmon -y`
1. Add Docker Group to User `sudo usermod -a -G docker ubuntu`
1. Relogin for the user to gain access to Docker.
1. Make a local copy of the application code found on [github][github] by `git clone https://github.com/JohnRTurner/riviandatagen.git`
1. Build the Docker image `docker build riviandatagen -t riviandatagen`
1. Run the Image `docker run -d --name riviandatagen -e KAFKA_SERVER=yourkafkaserver.com:29092 -t riviandatagen`
    1. Note: Add option[s] from below chart with -e
1. View the logs `docker logs -f riviandatagen`


| Option       | Description                            | Default  |
|--------------|----------------------------------------|----------|
| BATCH_SIZE   | Batch Size                             | 1000     | 
| KAFKA_TOPIC  | Topic                                  | test     |
| PROC_COUNT   | Processes to Concurrently Run          | 8        |
| KAFKA_SERVER | Kakfka Server                          |          |         

[github]: https://github.com/JohnRTurner/oltpnodejs