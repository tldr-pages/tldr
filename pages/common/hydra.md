# hydra

> Password brute forcing tool.
> More information: <https://github.com/vanhauser-thc/thc-hydra/>.

- Run hydra against an ftp server with username `user` and a password list `passlist.txt`:

`hydra -l user -P passlist.txt ftp://192.168.0.1`

- Run hydra against an imap server with user list `userlist.txt` and password `defaultpw`:

`hydra -L userlist.txt -p defaultpw imap://192.168.0.1/PLAIN`

- Run hydra against a pop3s server. `defaults.txt` should be a list in the form `user:password`:

`hydra -C defaults.txt -6 pop3s://[2001:db8::1]:143/TLS:DIGEST-MD5`

- Run hydra against all ftp servers in the `192.168.0.0/24` range, testing username `admin` and password `password`:

`hydra -l admin -p password ftp://[192.168.0.0/24]/`

- Run hydra against ssh on all targets in `targets.txt` with every combination of usernames and passwords in `logins.txt` and `pws.txt`:

`hydra -L logins.txt -P pws.txt -M targets.txt ssh`

- Run hydra against an online login form. Put the username in the `username` post parameter and the password in the `password` parameter. Consider the request a failure if the response contains `Login Failed`:

`hydra -L logins.txt -P pws.txt 192.168.0.1 http-post-form "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed"`
