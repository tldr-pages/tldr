# acme.sh

> Script shell implémentant le protocole client ACME, une alternative à `certbot`.
> Voir aussi : `acme.sh dns`.
> Plus d'informations : <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Publie un certificat en utilisant le mode webroot :

`acme.sh --issue {{[-d|--domain]}} {{exemple.com}} {{[-w|--webroot]}} /{{chemin/vers/webroot}}`

- Publie un certificat pour plusieurs domaines en utilisant le mode autonome avec le port 80 :

`acme.sh --issue --standalone {{[-d|--domain]}} {{exemple.com}} {{[-d|--domain]}} {{www.exemple.com}}`

- Publie un certificat en utilisant le mode autonome TLS avec le port 443 :

`acme.sh --issue --alpn {{[-d|--domain]}} {{exemple.com}}`

- Publie un certificat en utilisant une configuration `nginx` :

`acme.sh --issue --nginx {{[-d|--domain]}} {{exemple.com}}`

- Publie un certificat en utilisant une configuration Apache :

`acme.sh --issue --apache {{[-d|--domain]}} {{exemple.com}}`

- Publie un certificat wildcard (\*) en utilisant le mode automatique DNS API :

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.exemple.com}}`

- Installe les fichiers de certificat dans un dossier spécifique (Utile pour les renouvellements automatiques de certificat) :

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{exemple.com}} --key-file /{{chemin/vers/exemple.com.key}} --fullchain-file /{{chemin/vers/exemple.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
