# drill

> Effectue diverses requêtes DNS.
> Plus d'informations : <https://manned.org/drill>.

- Recherche des adresses IP(s) associées à un nom d'hôte (enregistrements A) :

`drill {{example.com}}`

- Recherche le(s) serveur(s) de messagerie associé(s) à un nom de domaine donné (enregistrement MX) :

`drill mx {{example.com}}`

- Obtient tous les types d'enregistrements pour un nom de domaine donné :

`drill any {{example.com}}`

- Spécifie un autre serveur DNS à interroger :

`drill {{example.com}} @{{8.8.8.8}}`

- Effectue une recherche DNS inversée sur une adresse IP (enregistrement PTR) :

`drill -x {{8.8.8.8}}`

- Suit la traçabilité DNSSEC des serveurs racines jusqu'à un nom de domaine :

`drill -TD {{example.com}}`

- Affiche le(s) enregistrement(s) DNSKEY d'un nom de domaine :

`drill -s dnskey {{example.com}}`
