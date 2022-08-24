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
cp rivandatagen/kafkasetup/docker-compose.yml .
vi docker-compose.yml and replace yyyyy.compute-1.amazonaws.com with the proper host.
docker-compose up -d
```
## General Instructions
### Stop Kafka
```
docker-compose stop
```
### Start Kafka
```
docker-compose stop
```
