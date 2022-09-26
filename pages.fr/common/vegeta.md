# vegeta

> Un utilitaire de ligne de commande et une bibliothèque pour les tests de charge HTTP.
> Voir aussi `ab`.
> Plus d'informations : <https://github.com/tsenart/vegeta>.

- Lancer une attaque d'une durée de 30 secondes :

`echo "{{GET https://exemple.com}}" | vegeta attack -duration={{30s}}`

- Lancez une attaque sur un serveur avec un certificat HTTPS auto-signé :

`echo "{{GET https://exemple.com}}" | vegeta attack -insecure -duration={{30s}}`

- Lancer une attaque avec un taux de 10 demandes par seconde :

`echo "{{GET https://exemple.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- Lancer une attaque et afficher un rapport :

`echo "{{GET https://exemple.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- Lancer une attaque et reporter les résultats sur un graphique (latence en fonction du temps) :

`echo "{{GET https://exemple.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{chemin/au/results.html}}`

- Lancer une attaque contre plusieurs URL à partir d'un fichier :

`vegeta attack -duration={{30s}} -targets={{requetes.txt}} | vegeta report`
