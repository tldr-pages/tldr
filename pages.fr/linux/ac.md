# ac

> Affiche les statistiques concernant la durée de connexion des utilisateurs.
> Plus d'informations : <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Affiche pendant combien de temps l'utilisateur actuel a été connecté, en heures :

`ac`

- Affiche pendant combien de temps les utilisateurs ont été connectés, en heures :

`ac --individual-totals`

- Affiche pendant combien de temps un utilisateur particulier a été connecté, en heures :

`ac --individual-totals {{nom_d_utilisateur}}`

- Affiche pendant combien de temps un utilisateur particulier a été connecté, en heures par jour (avec le total) :

`ac --daily-totals --individual-totals {{nom_d_utilisateur}}`

- Affiche des détails supplémentaires :

`ac --compatibility`
