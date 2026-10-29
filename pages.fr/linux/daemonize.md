# daemonize

> Lance une commande (qui ne se "démonise" pas elle-même) comme démon UNIX.
> Plus d'informations : <https://software.clapper.org/daemonize/>.

- Lance une commande comme démon :

`daemonize {{commande}} {{arguments_commande}}`

- Écrit le PID dans le fichier spécifié :

`daemonize -p {{chemin/vers/fichier/pid}} {{commande}} {{arguments_commande}}`

- Utilise un fichier verrou pour s'assurer que seulement une instance fonctionne à la fois :

`daemonize -l {{chemin/vers/fichier/verrou}} {{commande}} {{arguments_commande}}`

- Utilise le compte utilisateur spécifié :

`sudo daemonize -u {{utilisateur}} {{commande}} {{arguments_commande}}`
