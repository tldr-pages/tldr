# chcon

> Change le contexte de sécurité de SELinux d'un ou plusieurs fichiers/dossiers.
> Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- Affiche le contexte de sécurité d'un fichier :

`ls {{[-lZ|-l --context]}} {{chemin/vers/fichier}}`

- Change le contexte de sécurité d'un fichier cible, en utilisant un fichier de référence :

`chcon --reference {{fichier_référence}} {{fichier_cible}}`

- Change le contexte de sécurité SELinux complet d'un fichier :

`chcon {{utilisateur}}:{{role}}:{{type}}:{{range/level}} {{fichier}}`

- Change seulement la partie utilisateur du contexte de sécurité SELinux :

`chcon {{[-u|--user]}} {{utilisateur}} {{fichier}}`

- Change seulement la partie role du contexte de sécurité SELinux :

`chcon {{[-r|--role]}} {{role}} {{fichier}}`

- Change seulement la partie type du contexte de sécurité SELinux :

`chcon {{[-t|--type]}} {{type}} {{fichier}}`

- Change seulement la partie plage/niveau du contexte de sécurité SELinux :

`chcon {{[-l|--range]}} {{plage/niveau}} {{fichier}}`
