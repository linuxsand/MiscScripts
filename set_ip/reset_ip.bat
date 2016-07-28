@echo off

set network=本地连接
netsh interface ipv4 set address name=%network% source=dhcp

pause