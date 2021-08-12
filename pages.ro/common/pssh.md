# pssh

> Programul SSH paralel.

- Rulați o comandă pe două gazde și imprimați ieșirea pe fiecare server în linie:

`pssh -i -H "{{host1}} {{host2}}" {{hostname -i}}`

- Rulați o comandă și salvați ieșirea în fișiere separate:

`pssh -H {{host1}} -H {{host2}} -o {{path/to/output_dir}} {{hostname -i}}`

- Rulați o comandă pe mai multe gazde, specificate într-un fișier separat de linie nouă:

`pssh -i -h {{path/to/hosts_file}} {{hostname -i}}`

- Rulați o comandă ca root (aceasta solicită parola rădăcină):

`pssh -i -h {{path/to/hosts_file}} -A -l {{root_username}} {{hostname -i}}`

- Rulați o comandă cu argumente suplimentare SSH:

`pssh -i -h {{path/to/hosts_file}} -x "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- Rulați o comandă care limitează numărul de conexiuni paralele la 10:

`pssh -i -h {{path/to/hosts_file}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
