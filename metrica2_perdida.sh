#!/bin/bash

for perdida in 0 5 10 20 30 50 70; do
    echo "PÃ©rdida de paquetes: ${perdida}%"
    sudo tc qdisc del dev docker0 root 2>/dev/null
    if [ $perdida -gt 0 ]; then
        sudo tc qdisc add dev docker0 root netem loss ${perdida}%
    fi
    ping_result=$(ping -c 10 172.17.0.2 | tail -2)
    echo "$ping_result"
    sleep 2
done

sudo tc qdisc del dev docker0 root 2>/dev/null
