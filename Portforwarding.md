- [Socat](#socat)

## SSH {#ssh}

**Local PortForward** 

```
ssh –L 5901:10.10.10.48:4492 root@10.10.10.47
```

**Remote PortForward** 

```
ssh –R 9999:localhost:8080 root@10.10.10.48
```

## Socat {#socat}

Make sure the machine have socat and if dont please get on that machine a socat binary.

```
./socat tcp-listen:9999,fork tcp:127.0.0.1:25 &
```


## Chisel {#chisel}

Please make sure both are the same version. Please download the latest release of Chisel on the link below:

https://github.com/jpillora/chisel/releases

```

```

## Ngrok {#ngrok}


# References {#references}
[1] https://phoenixnap.com/kb/ssh-port-forwarding#htoc-remote-port-forwarding-with-openssh

[2] https://github.com/jpillora/chisel