# acme.sh

> Script shell implémentant le protocole client ACME, une alternative à certbot.
> Voir aussi `acme.sh dns`.
> Plus d'informations : <https://github.com/acmesh-official/acme.sh>.

- Publie un certificat en utilisant le mode webroot :

`acme.sh --issue --domain {{exemple.com}} --webroot {{/chemin/vers/webroot}}`

- Publie un certificat pour plusieurs domaines en utilisant le mode autonome avec le port 80 :

`acme.sh --issue --standalone --domain {{exemple.com}} --domain {{www.exemple.com}}`

- Publie un certificat en utilisant le mode autonome TLS avec le port 443 :

`acme.sh --issue --alpn --domain {{exemple.com}}`

- Publie un certificat en utilisant une configuration Nginx :

`acme.sh --issue --nginx --domain {{exemple.com}}`

- Publie un certificat en utilisant une configuration Apache :

`acme.sh --issue --apache --domain {{exemple.com}}`

- Publie un certificat wildcard (\*) en utilisant le mode automatique DNS API :

`acme.sh --issue --dns {{dns_cf}} --domain {{*.exemple.com}}`

- Installe les fichiers de certificat dans un dossier spécifique (Utile pour les renouvellements automatiques de certificat) :

`acme.sh --install-cert -d {{exemple.com}} --key-file {{/chemin/vers/exemple.com.key}} --fullchain-file {{/chemin/vers/exemple.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}`
