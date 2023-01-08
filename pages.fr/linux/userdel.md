# userdel

> Supprime un compte utilisateur ou supprime un utilisateur d'un groupe.
> Voir aussi `users`, `useradd`, `usermod`.
> Plus d'informations : <https://manned.org/userdel>.

- Supprime un utilisateur :

`sudo userdel {{nom_utilisateur}}`

- Supprime un utilisateur dans un autre répertoire racine :

`sudo userdel --root {{chemin/vers/autre_racine}} {{nom_utilisateur}}`

- Supprime un utilisateur, son répertoire personnel ainsi que son répertoire d'attente des courriels :

`sudo userdel --remove {{nom_utilisateur}}`
