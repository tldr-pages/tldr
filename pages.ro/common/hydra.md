# hydra

> Instrument de ghicitul parolelor online.
> Protocoalele acceptate includ FTP, HTTP (S), SMTP, SNMP, XMPP, SSH și multe altele.
> Mai multe informaţii: <https://github.com/vanhauser-thc/thc-hydra>

- Porniţi expertul Hydrei:

`hydra-wizard`

- Ghici acreditările SSH folosind un anumit nume de utilizator și o listă de parole:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} {{host_ip}} {{ssh}}`

- Ghici acreditările Telnet utilizând o listă de nume de utilizator și o singură parolă, specificând un port non-standard și IPv6:

`hydra -L {{path/to/usernames.txt}} -p {{password}} -s {{port}} -6 {{host_ip}} {{telnet}}`

- Ghiciți acreditările FTP utilizând numele de utilizator și listele de parole, specificând numărul de fire:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- Ghiciți acreditările MySQL folosind un nume de utilizator și o listă de parole, ieșind atunci când se găsește o pereche de nume de utilizator/parolă:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -f {{host_ip}} {{mysql}}`

- Ghici acreditările RDP folosind un nume de utilizator și o listă de parole, care arată fiecare încercare:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -V {{rdp://host_ip}}`

- Ghici acreditările IMAP pe o serie de gazde utilizând o listă de perechi de nume de utilizator/parole separate prin două puncte:

`hydra -C {{path/to/username_password_pairs.txt}} {{imap://[host_range_cidr]}}`

- Ghici acreditările POP3 pe o listă de gazde folosind nume de utilizator și liste de parole, ieșind atunci când se găsește o pereche de nume de utilizator/parolă:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -M {{path/to/hosts.txt}} -F {{pop3}}`
