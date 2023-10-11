# daemonize

> Lance une commande (qui ne se "démonise" pas elle-même) comme démon UNIX.
> Plus d'informations : <http://software.clapper.org/daemonize/>.

- Lance une commande comme démon :

`daemonize {{commande}} {{arguments_de_commande}}`

- Écrit le PID dans le fichier spécifié :

`daemonize -p {{chemin/vers/le/fichier/pid}} {{commande}} {{arguments_de_commande}}`

- Utilise un fichier verrou pour s'assurer que seulement une instance fonctionne à la fois :

`daemonize -l {{chemin/vers/le/fichier/verrou}} {{commande}} {{arguments_de_commande}}`

- Utilise le compte utilisateur spécifié :

`sudo daemonize -u {{utilisateur}} {{commande}} {{arguments_de_commande}}`
