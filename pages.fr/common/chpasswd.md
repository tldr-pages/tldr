# chpasswd

> Modifie les mots de passe de plusieurs utilisateurs en utilisant `stdin`.
> Voir aussi : `passwd`.
> Plus d'informations : <https://manned.org/chpasswd>.

- Modifie le mot de passe d'un utilisateur spécifique :

`printf "{{nom_utilisateur}}:{{nouveau_mot_de_passe}}" | sudo chpasswd`

- Modifie les mots de passe de plusieurs utilisateurs (le texte d'entrée ne doit pas contenir d'espaces) :

`printf "{{nom_utilisateur_1}}:{{nouveau_mot_de_passe_1}}\n{{nom_utilisateur_2}}:{{nouveau_mot_de_passe_2}}" | sudo chpasswd`

- Modifie le mot de passe d'un utilisateur spécifique, et le spécifie sous forme chiffrée :

`printf "{{nom_utilisateur}}:{{nouveau_mot_de_passe_chiffré}}" | sudo chpasswd {{[-e|--encrypted]}}`

- Modifie le mot de passe d'un utilisateur spécifique, et utilise un algorithme de chiffrement spécifique pour le mot de passe stocké :

`printf "{{nom_utilisateur}}:{{nouveau_mot_de_passe}}" | sudo chpasswd {{[-c|--crypt-method]}} {{NONE|DES|MD5|SHA256|SHA512}}`
