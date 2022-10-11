# chroot

> Exécute une commande ou un shell interactif avec un répertoire racine spécial.
> Plus d'informations : <https://www.gnu.org/software/coreutils/chroot>.

- Exécute la commande en tant que nouveau répertoire racine :

`chroot {{chemin/vers/nouveau/répertoire/racine}} {{command}}`

- Spécifie l'utilisateur et le groupe (ID ou nom) à utiliser :

`chroot --userspec={{utilisateur:groupe}}`
