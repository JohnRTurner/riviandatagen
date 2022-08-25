# KAFKA Setup

## Create Server in AWS
- Server: c6a.2xlarge
- OS: ubuntu 22.04lts

- Tags:

| Tag Name   | Value            |
|------------|------------------|
| Name       | Riven_Test_Kafka |
| Owner      | jturner          |
| CostCenter | SE               |
| Project    | Riven_Test       |

- Key Pair: xxxxx
- Storage: 256G

## Setup Kafka

### Login and upgrade box
```
ssh -i $HOME/Downloads/xxxxx.pem ubuntu@yyyyy.compute-1.amazonaws.com
sudo apt update
sudo apt upgrade -y
```
### Reboot then login and install docker
```
ssh -i $HOME/Downloads/xxxxx.pem ubuntu@yyyyy.compute-1.amazonaws.com
sudo apt install docker.io docker-compose nmon kafkacat -y
sudo usermod -a -G docker ubuntu
exit
```
### Login, docker-compose and run the docker
```
ssh -i $HOME/Downloads/xxxxx.pem ubuntu@yyyyy.compute-1.amazonaws.com
git clone https://github.com/JohnRTurner/riviandatagen.git
cp riviandatagen/kafkasetup/docker-compose.yml .
export MNAME=$(curl http://checkip.amazonaws.com 2>/dev/null |nslookup| grep "name =" |sed "s/.*name = //"|sed "s/.$//")
docker-compose up -d
```
## General Instructions
### Stop Kafka
```
docker-compose stop
```
### Start Kafka
```
docker-compose start
```
