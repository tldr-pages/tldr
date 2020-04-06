# hydra

> Online password guessing tool.
> More information: <https://github.com/vanhauser-thc/thc-hydra>.

- Start Hydra's wizard:

`hydra-wizard`

- Guess SSH credentials using a given username and a list of passwords:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} {{host_ip}} {{ssh}}`

- Guess Telnet credentials using a list of usernames and a single password, specifying a non-standard port:

`hydra -L {{path/to/usernames.txt}} -p {{password}} -s {{port}} {{host_ip}} {{telnet}}`

- Guess FTP credentials using usernames and passwords lists, specifying the number of tasks:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- Guess MySQL credentials using a username and a passwords list, exiting when a username/password pair is found:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -f {{host_ip}} {{mysql}}`

- Guess RDP credentials using a username and a passwords list, showing each attempts:

`hydra -V -l {{username}} -P {{path/to/wordlist.txt}} {{rdp://host_ip}}`

- Guess SSH credentials on a range of hosts using a list of colon-separated username/password pairs:

`hydra -C {{path/to/username_password_pairs.txt}} {{host_range_cidr}} {{ssh}}`

- Guess FTP credentials on a list of hosts using usernames and passwords lists, exiting when a username/password pair is found:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -M {{path/to/hosts.txt}} {{ftp}}`
