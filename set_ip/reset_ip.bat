@echo off

set network=��������
netsh interface ipv4 set address name=%network% source=dhcp

pause