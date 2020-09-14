# Port Enumeration

### Port 139 & 445 (SMB)

```
# Using smbclient

smbclient -L 10.10.68.12
smbclient \\\\192.168.57.134\\IPC$
smbclient \\\\10.10.68.12\\backup -U 'svc-admin'

# Using smbmap

smbmap -H 10.10.10.123 -R --depth 5
smbmap -H spooky.local -u svc-admin -p password -d spooky.local
```
