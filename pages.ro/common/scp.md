# scp

> Copie securizată.
> Copiați fișiere între gazde utilizând Secure Copy Protocol prin SSH.
> Mai multe informaţii: <https://man.openbsd.org/scp>

- Copiați un fișier local pe o gazdă la distanță:

`scp {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Utilizați un anumit port atunci când vă conectați la gazda de la distanță:

`scp -P {{port}} {{path/to/local_file}} {{remote_host}}:{{path/to/remote_file}}`

- Copiați un fișier dintr-o gazdă la distanță într-un director local:

`scp {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Copiați recursiv conținutul unui director de la o gazdă la distanță într-un director local:

`scp -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Copiați un fișier între două gazde la distanță transferând prin gazda locală:

`scp -3 {{host1}}:{{path/to/remote_file}} {{host2}}:{{path/to/remote_directory}}`

- Utilizați un nume de utilizator specific atunci când vă conectați la gazda de la distanță:

`scp {{path/to/local_file}} {{remote_username}}@{{remote_host}}:{{path/to/remote_directory}}`

- Utilizați o cheie privată ssh specifică pentru autentificare cu gazda de la distanță:

`scp -i {{~/.ssh/private_key}} {{local_file}} {{remote_host}}:{{/path/remote_file}}`
