# ssh-keygen

> Generați chei ssh utilizate pentru autentificare, autentificare fără parolă și alte lucruri.

- Generează o cheie interactiv:

`ssh-keygen`

- Specificați fișierul în care să salvați cheia:

`ssh-keygen -f ~/.ssh/{{filename}}`

- Generați o cheie ed25519 cu 100 runde de funcții de derivare cheie:

`ssh-keygen -t ed25519 -a 100`

- Generați o cheie de biți RSA 4096 cu e-mail ca comentariu:

`ssh-keygen -t rsa -b 4096 -C "{{email}}"`

- Recuperați amprenta cheie de la o gazdă (utilă pentru confirmarea autenticității gazdei atunci când se conectează prima dată la aceasta prin SSH):

`ssh-keygen -l -F {{remote_host}}`

- Eliminați cheile unei gazde din fișierul cunoscut_hosts (util atunci când o gazdă cunoscută are o cheie nouă):

`ssh-keygen -R {{remote_host}}`

- Recuperați amprenta unei chei în MD5 Hex:

`ssh-keygen -l -E md5 -f ~/.ssh/{{filename}}`

- Schimbați parola unei chei:

`ssh-keygen -p -f ~/.ssh/{{filename}}`
