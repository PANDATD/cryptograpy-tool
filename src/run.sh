#bin/bash

echo "[+] Starting Inital setup"
echo "---------------------------------"
echo "[+] Checking Dependencies"
echo "---------------------------------"
echo "[+] Checking for Python3"
echo "---------------------------------"
echo "[+] Checking for pip3"
echo "---------------------------------"
echo "[+] Installing Dependencies"
echo "---------------------------------"
pip3 install -r requirements.txt

echo "[+] Starting the server"
echo "---------------------------------"
flet main.py

