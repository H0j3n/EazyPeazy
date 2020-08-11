# Web Fuzzing 

- [Dirsearch](#dirsearch)
- [Gobuster](#gobuster)
- [Wfuzz](#wfuzz)
- [References](#references)

### Dirsearch

You can download dirsearch in the link below:

https://github.com/maurosoria/dirsearch

```
python3 dirsearch.py -u http://10.10.8.83/ -e php,html,txt -f -w wordlist.txt
```

### Gobuster

```
# Install
sudo apt-get install gobuster

# Use
gobuster dir -u http://10.10.8.83/ -x php,html,txt -w wordlist.txt
```

### Wfuzz

```
# Install
pip install wfuzz

# Use
wfuzz --hc 404,400,401 -c -u http://10.10.8.83/FUZZ -w wordlist.txt

wfuzz -v -z range,1-10000 http://10.10.8.83/index.php?id=FUZZ
```

# References
[1] https://github.com/maurosoria/dirsearch

[2] https://github.com/xmendez/wfuzz

[3] https://certcube.com/wfuzz-cheat-sheet-the-power-of-brute-forcer/