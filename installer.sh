#!/usr/bin/env bash

# Versoin: 1.0
# Author: evilfeonix
# Name: KeyLogger Generator
# Date: 02 - JANUARY - 2025
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com


S="\e[0m"
R="\e[91m"
G="\e[92m"
B="\e[94m"
P="\e[95m"
Y="\e[43m"


SCRIPT=$0
let TRACKER=0
ERR="$G[$S-$G]$R "
INFO="$R[$S+$R]$G "

pyLIB=(
    "colorama"
    "keyboard"
    "pyinstaller"
    "auto-py-to-exe"
)

function slow() {
    local F3="$1"
    for (( i=0; i<${#F3}; i++ ))
	do
        echo -n -e "${F3:$i:1}"
        sleep 0.003  # Delay between characters
    done
    echo
}

function installed()
{
	for i in "${pyLIB[@]}"
    do
        pip install $i
    done
	
	redirection
}

function redirection()
{
	clear || cls
	banner
	echo -n -e '\e[92m'
	slow "[!] Installation Successfully Finished."
	echo -n -e '\e[92m'
	slow "[*] Run: python3 keygen.py  "
	echo -n -e '\e[0m'
	exit
}

function banner()
{
	local B="
===========================================================
|         _  __                 ____                      |
|        | |/ /___ _   _       / ___| ___ _ __            |
|        | ' // _ \ | | |_____| |  _ / _ \ '_ \           |
|        | . \  __/ |_| |_____| |_| |  __/ | | |          |
|        |_|\_\___|\__, |      \____|\___|_| |_|          |
|          v[1.0]  |___/   Coded By EvilFeonix            |
===========================================================        
    "
    slow "$B"
}

function internet()
{
	wget -q --spider http://google.com
}

function main()
{
	internet
	if [[ $? != 0  ]]; then 
		echo -e -n '\e[91m'
		slow "[-] Please Check Your Internet Connection."
		echo -e -n '\e[0m'
		exit 
	fi

	installed
}


main
