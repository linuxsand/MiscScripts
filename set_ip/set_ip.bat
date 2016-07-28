@echo off
set /p ip_addr="Input ip address: "
set ip_addr=%ip_addr%

set /p mask="If mask is 255.255.255.0, press <Enter> "
if [%mask%]==[] (
set mask=255.255.255.0
) 

set network=本地连接
echo setting %network%...

netsh interface ipv4 set address name=%network% source=static address=%ip_addr% mask=%mask%

pause