# hydra

> Online jelszó kitaláló eszköz. Támogatott protokollok: FTP, HTTP(S), SMTP, SNMP, XMPP, SSH, stb. További információk: <https://github.com/vanhauser-thc/thc-hydra>.

- Indítsa el a Hydra varázslóját:

`hydra-wizard`

- Találja ki az SSH hitelesítő adatokat egy megadott felhasználónév és egy jelszólista segítségével:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} {{host_ip}} {{ssh}}`

- HTTPS webes űrlapok hitelesítő adatainak kitalálása két adott felhasználónév és jelszó listájának felhasználásával ("https_post_request" lehet például "username=^USER^&password=^PASS^"):

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} {{host_ip}} {{https-post-form}} "{{url_without_host}}:{{https_post_request}}:{{login_failed_string}}"`

- FTP hitelesítő adatok kitalálása felhasználónevek és jelszavak listáinak felhasználásával, a szálak számának megadásával:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- MySQL hitelesítő adatok kitalálása egy felhasználónév és egy jelszó lista segítségével, kilépve, ha találtunk egy felhasználónév/jelszó párt:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -f {{host_ip}} {{mysql}}`

- RDP hitelesítő adatok kitalálása egy felhasználónév és egy jelszólista segítségével, minden egyes kísérletet bemutatva:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -V {{rdp://host_ip}}`

- IMAP hitelesítő adatok kitalálása egy sor hoszton, kettőspontokkal elválasztott felhasználónév/jelszó párok listája alapján:

`hydra -C {{path/to/username_password_pairs.txt}} {{imap://[host_range_cidr]}}`

- POP3 hitelesítő adatok megtippelése egy listán a hosztokon felhasználónevek és jelszavak listája alapján, kilépve, ha talált egy felhasználónév/jelszó párt:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -M {{path/to/hosts.txt}} -F {{pop3}}`
