# hydra

> Password brute forcing tool.
> More information: <https://github.com/vanhauser-thc/thc-hydra/>.

- Run hydra against an ftp server:

`hydra -l {{Username}} -P {{Password List}} ftp://{{IP Address}}`

- Run hydra against an imap server with plain authentication:

`hydra -L {{Username List}} -p {{Password}} imap://{{IP Address}}/PLAIN`

- Run hydra against a pop3s server. The credentials file should be a list in the form `user:password`:

`hydra -C {{Credentials File}} -6 pop3s://[{{IP v6 Address}}]:{{Port}}/TLS:DIGEST-MD5`

- Run hydra against all ftp servers in an ip range, testing a specific username and password:

`hydra -l {{Useaname}} -p {{Password}} ftp://[{{IP Address}}/{{Subnet}}]/`

- Run hydra against ssh on all a list of targets with every combination usernames and passwords:

`hydra -L {{Username List}} -P {{Password List}} -M {{Target list}} ssh`

- Run hydra against an online login post form:

`hydra -L {{Useaname List}} -P {{Password List}} {{IP Address}} http-post-form "/{{Path to login request}}:{{Useaname Parameter}}=^USER^&{{Password Parameter}}=^PASS^&{{Other parameters}}:{{String in failed responce}}"`
