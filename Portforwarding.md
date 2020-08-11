## SSH

`Remote PortForward` - we have instructed the remote server 10.10.10.48 to forward any connections directed at port 8080 to the local resource listening on port 9999.

```
ssh –R 9999:localhost:8080 root@10.10.10.48
```

## Socat


## Chisel


## Ngrok


# References
[1] https://phoenixnap.com/kb/ssh-port-forwarding#htoc-remote-port-forwarding-with-openssh