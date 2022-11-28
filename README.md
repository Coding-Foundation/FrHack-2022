[![CI/CD](https://github.com/Coding-Foundation/FrHack-2022/actions/workflows/docker-build.yml/badge.svg)](https://github.com/Coding-Foundation/FrHack-2022/actions/workflows/docker-build.yml)

# FrHack 2022

## Playstore
[![FR Hack App](https://www.fcsok.org/wp-content/uploads/2020/04/get-it-on-google-play-badge.png)](https://www.fcsok.org/wp-content/uploads/2020/04/get-it-on-google-play-badge.png)

## Front
[![FR Hack](https://cdn.discordapp.com/attachments/703994640977756200/1043734855554433044/image.png)](https://frhack.marcpartensky.com)

## Back
[![API FR Hack](https://cdn.discordapp.com/attachments/703994640977756200/1043736664050237490/image.png)](https://api.frhack.marcpartensky.com/redoc)

## Lab
[![Lab FR Hack](https://cdn.discordapp.com/attachments/703994640977756200/1043736021076029450/image.png)](https://lab.frhack.marcpartensky.com)

## Database
[![Database FR Hack](https://cdn.discordapp.com/attachments/703994640977756200/1043738652695601232/image.png)](https://db.frhack.marcpartensky.com)


[Doosier Drive](https://drive.google.com/drive/folders/1V1yPBnZ0Bl0FzPhE1QPR9QVA9O73dmBE?usp=sharing)

# Deployment
## Prerequisites:
- make
- docker
- docker-compose
- docker swarm (optional)

## Commands
```sh
# clone the project
git clone https://github.com/coding-foundation/frhack-2022 frhack
cd frhack
```

```sh
# run with docker compose
make compose

# run with docker swarm
make swarm

# print help
make help
```

## Example on debian
```sh
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
sudo apt install -y make docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo usermod -aG docker $USER
git clone https://github.com/coding-foundation/frhack-2022 frhack
cd frhack
docker swarm init
docker network create --driver=overlay web
make swarm
```
