# amass intel

> Collecte des renseignements open source sur une organisation comme les noms de domaines racine et les ASNs.
> Plus d'informations : <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Recherche les domaines racines inclus dans une plage d'adresse IP :

`amass intel -addr {{192.168.0.1-254}}`

- Utilise les méthodes de reconnaissance active :

`amass intel -active -addr {{192.168.0.1-254}}`

- Recherche les noms de domaines racines reliés à un domaine :

`amass intel -whois -d {{nom_de_domaine}}`

- Recherche les ASNs qui correspondent à une organisation :

`amass intel -org {{nom_de_l_organisation}}`

- Recherche les domaines racines qui correspondent à un ASN :

`amass intel -asn {{asn}}`

- Sauvegarde les résultats dans un fichier texte :

`amass intel -o {{fichier_de_sortie}} -whois -d {{nom_de_domaine}}`
