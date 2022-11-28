#!/bin/sh

env $(grep -v "#" ./env/docker-compose.env | xargs) $@
