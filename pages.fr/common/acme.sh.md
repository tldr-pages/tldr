# acme.sh

> Script shell implémentant le protocole client ACME, une alternative à `certbot`.
> Voir aussi : `acme.sh dns`.
> Plus d'informations : <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Publie un certificat en utilisant le mode webroot :

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{chemin/vers/webroot}}`

- Publie un certificat pour plusieurs domaines en utilisant le mode autonome avec le port 80 :

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Publie un certificat en utilisant le mode autonome TLS avec le port 443 :

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Publie un certificat en utilisant une configuration `nginx` :

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Publie un certificat en utilisant une configuration Apache :

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Publie un certificat wildcard (\*) en utilisant le mode automatique DNS API :

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- Installe les fichiers de certificat dans un dossier spécifique (Utile pour les renouvellements automatiques de certificat) :

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{chemin/vers/example.com.key}} --fullchain-file /{{chemin/vers/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
