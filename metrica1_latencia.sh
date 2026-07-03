#!/bin/bash

for delay in 0 50 100 200 300 500 1000; do
    echo "Delay: ${delay}ms"
    sudo tc qdisc del dev docker0 root 2>/dev/null
    if [ $delay -gt 0 ]; then
        sudo tc qdisc add dev docker0 root netem delay ${delay}ms
    fi
    ping_result=$(ping -c 5 172.17.0.2 | tail -1 | awk '{print $4}' | cut -d'/' -f2)
    echo "RTT promedio: ${ping_result}ms"
    sleep 2
done

sudo tc qdisc del dev docker0 root 2>/dev/null
