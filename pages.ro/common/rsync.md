# rsync

> Transferați fișiere fie către, fie de la o gazdă la distanță (nu între două gazde la distanță).
> Poate transfera fișiere unice sau mai multe fișiere care se potrivesc unui tipar.

- Transferați fișierul de la gazdă locală la distanță:

`rsync {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transferați fișierul de la gazdă la distanță la local:

`rsync {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transferă fișier în [a]rhivă (cu păstrarea atributelor), [z] comprimat, cu [v]erbositate și [h] ușor de citit [P]rogres:

`rsync -azvhP {{path/to/local_file}} {{remote_host}}:{{path/to/remote_directory}}`

- Transferați un director și toți copiii săi de la o telecomandă la locală:

`rsync -r {{remote_host}}:{{path/to/remote_directory}} {{path/to/local_directory}}`

- Transferați conținutul directorului (dar nu și directorul în sine) de la o telecomandă la locală:

`rsync -r {{remote_host}}:{{path/to/remote_directory}}/ {{path/to/local_directory}}`

- Transferați un director [r]ecursiv, în [a]rhivă, cu păstrarea atributelor, inclusiv sym[l]inks și ignorând fișierele deja transferate, dacă n[u] sunt mai recente:

`rsync -rauL {{remote_host}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transferați fișierul prin SSH și ștergeți fișierele locale care nu există pe gazdă la distanță:

`rsync -e ssh --delete {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`

- Transferați fișierul prin SSH utilizând un port diferit decât cel implicit și arătați progresul global:

`rsync -e 'ssh -p {{port}}' --info=progress2 {{remote_host}}:{{path/to/remote_file}} {{path/to/local_file}}`
