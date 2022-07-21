# ansible-vault

> Chiffre & déchiffre des valeurs, des structures de données et des fichiers dans un projet Ansible.
> Plus d'informations : <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Crée un nouveau fichier vault chiffré avec une invite à rentrer un mot passe :

`ansible-vault create {{fichier_vault}}`

- Crée un nouveau fichier vault chiffré avec un fichier clé vault pour le chiffrer :

`ansible-vault create --vault-password-file={{fichier_de_mot_de_passe}} {{fichier_vault}}`

- Chiffre un ficher existant avec un fichier de mot de passe optionnel :

`ansible-vault encrypt --vault-password-file={{fichier_de_mot_de_passe}} {{fichier_vault}}`

- Chiffre un texte avec le format de chiffrage pour textes d'Ansible, en affichant une invite interactif :

`ansible-vault encrypt_string`

- Affiche un fichier chiffré, en utilisant un fichier de mot de passe pour le déchiffrer :

`ansible-vault view --vault-password-file={{fichier_de_mot_de_passe}} {{fichier_vault}}`

- Remplace le fichier de mot de passe d'un fichier vault déjà chiffré par un autre :

`ansible-vault rekey --vault-password-file={{ancien_fichier_de_mot_de_passe}} --new-vault-password-file={{nouveau_fichier_de_mot_de_passe}} {{fichier_vault}}`
