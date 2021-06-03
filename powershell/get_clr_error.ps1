# Set-ExecutionPolicy RemoteSigned
$temp = Get-EventLog Application -InstanceId 1026 -EntryType Error -Newest 1
$temp | Select-Object -Property *

Pause