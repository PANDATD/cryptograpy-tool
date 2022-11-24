#bin/bash


echo "[+] Starting Inital setup"
chmod +r main.py 
chmod +x run.sh
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
echo "---------------------------------"
echo "[+] Installed Dependencies"
echo "---------------------------------"

echo "[+] Starting the server"
echo "---------------------------------"
flet main.py
sleep 2
echo "[+] Application closed"

