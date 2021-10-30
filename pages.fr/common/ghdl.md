# ghdl

> Simulateur à source ouvert pour le langage VHDL.
> Plus d'informations : <http://ghdl.free.fr>.

- Analyse un fichier de source VHDL et génère un fichier objet :

`ghdl -a {{fichier.vhdl}}`

- Élabore un design (où `{{design}}` est le nom d'une unité de configuration, d'entité, ou d'architecture) :

`ghdl -e {{design}}`

- Exécute un design élaboré :

`ghdl -r {{design}}`

- Exécute un design élaboré et sauvegarde la sortie à un fichier de forme d'onde :

`ghdl -r {{design}} --wave={{sortie.ghw}}`

- Vérifie le syntaxe d'un fichier de source VHDL :

`ghdl -s {{fichier.vhdl}}`

- Affiche l'aide générale :

`ghdl --help`
