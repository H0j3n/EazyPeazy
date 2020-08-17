# Linux - Enumeration

- [Manual Enumeration](#manual-enumeration)
- [Automatic Enumeration](#automatic-enumeration)

## Manual Enumeration

```
# Suid Binary
find / -perm -u=s -type f 2>/dev/null

# Capabilities
getcap -r / 2>/dev/null

# Find Files For Certain User
find / -user www

# Find Files With Certain Files
find . -iname "*config*" 2>/dev/null

# Find Files For Certain Group
find / -group kibana 2>/dev/null

# Check Process
ps -uax

# Display Port Open
ss -tln

# View Crontab
crontab -e 

# Grep Certain Words in all files
grep -r / -A1 -ie 'flag{' 2>/dev/null
```

## Automatic Enumeration

### Linpeas

[Linpeas](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)


### Linux Smart Enumeration

[Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)

