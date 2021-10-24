# apache2ctl

> L'outil d'Interface en Lignes de Commandes (ILC) pour administrer le serveur web HTTP Apache.
> Cette commande est disponible sur une distribution Debian. Pour les distributions basées Red Hat, voir `httpd`.
> Plus d'informations : <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- Démarre le démon Apache. Envoie un message s'il est déjà actif :

`sudo apache2ctl start`

- Arrête le démon Apache :

`sudo apache2ctl stop`

- Re-démarre le démon Apache :

`sudo apache2ctl restart`

- Teste la syntaxe du fichier de configuration :

`sudo apache2ctl -t`

- Liste les modules chargés :

`sudo apache2ctl -M`
