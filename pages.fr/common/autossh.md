# autossh

> Lance, surveille et redémarre les connections SSH.
> Reconnecte automatiquement pour garder le tunnel de transfert de port ouvert. Accepte toutes les options de `ssh`.
> Plus d'informations : <https://www.harding.motd.ca/autossh>.

- Démarre une session SSH, redémarre quand le port échoue à renvoyer de la data :

`autossh -M {{port_surveillé}} "{{commande_ssh}}"`

- Fait suivre un port local vers un port distant, redémarre si nécessaire :

`autossh -M {{port_surveillé}} -L {{port_local}}:localhost:{{port_distant}} {{utilisateur}}@{{hôte}}`

- Diverge `autossh` en arrière plan avant de lancer `ssh` et n'ouvre pas de shell distant :

`autossh -f -M {{port_surveillé}} -N "{{commande_ssh}}"`

- Démarre en arrière plan, sans surveillance de port et à la place envoie des paquets SSH "keep-alive" toutes les 10 secondes pour détecter les échecs :

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{commande_ssh}}"`

- Démarre en arrière plan, sans surveillance de port ni shell distant et s’arrête si le partage de port échoue :

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{port_local}}:localhost:{{port_distant}} {{utilisateur}}@{{hôte}}`

- Démarre en arrière plan, logue la sortie de déboggage d'`autossh` et la sortie verbeuse de `ssh` dans des fichiers :

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{chemin/vers/fichier_logs_autossh.log}} autossh -f -M {{port_surveillé}} -v -E {{chemin/vers/fichier_logs_ssh.log}} {{commande_ssh}}`
