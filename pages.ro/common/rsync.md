# rsync

> Transferați fișiere fie către, fie de la o gazdă la distanță (nu între două gazde la distanță).
> Poate transfera fișiere unice sau mai multe fișiere care se potrivesc unui tipar.

- Transferați fișierul de la gazdă locală la distanță:

`rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transferați fișierul de la gazdă la distanță la local:

`rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transfer fișier în [a] rchive (pentru a păstra atributele) și comprimat ([z] ipped) modul cu [v] erbose și [h] uman-lizibil [P] rogress:

`rsync -azvhP {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transferați un director și toți copiii săi de la o telecomandă la locală:

`rsync -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Transferați conținutul directorului (dar nu și directorul în sine) de la o telecomandă la locală:

`rsync -r {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}`

- Transferați un director [r] ecursiv, în [a] rchive pentru a păstra atributele, rezolvarea conținută cerneluri moi [l] și ignorând fișierele deja transferate [u] nless mai noi:

`rsync -rauL {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transferați fișierul prin SSH și ștergeți fișierele locale care nu există pe gazdă la distanță:

`rsync -e ssh --delete {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

- Transferați fișierul prin SSH utilizând un port diferit decât cel implicit și arătați progresul global:

`rsync -e 'ssh -p {{port}}' --info=progress2 {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`
