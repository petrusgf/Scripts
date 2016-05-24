#!/bin/bash
# This script execute netcat commando to  try to connect to every port in a server.
# To scan a remote machine, script will be  enter "hostname", start ports and end ports. 

echo "Enter hostname: "
read hostname

echo "start port:"
read start_port

echo "end port:"
read end_port

nc -z -v "$hostname" "$start_port"-"$end_port"
