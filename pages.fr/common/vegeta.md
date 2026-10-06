# vegeta

> Un utilitaire de ligne de commande et une bibliothèque pour les tests de charge HTTP.
> Voir aussi : `ab`.
> Plus d'informations : <https://github.com/tsenart/vegeta#usage-manual>.

- Lance une attaque d'une durée de 30 secondes :

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- Lance une attaque sur un serveur avec un certificat HTTPS auto-signé :

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- Lance une attaque avec un taux de 10 demandes par seconde :

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- Lance une attaque et affiche un rapport :

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- Lance une attaque et reporte les résultats sur un graphique (latence en fonction du temps) :

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{chemin/au/results.html}}`

- Lance une attaque contre plusieurs URL à partir d'un fichier :

`vegeta attack -duration={{30s}} -targets={{requetes.txt}} | vegeta report`
