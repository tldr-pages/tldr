# wget

> Télécharge des fichiers depuis le Web.
> Prend en charge HTTP, HTTPS et FTP.
> Voir aussi : `wcurl`, `curl`.
> Plus d'informations : <https://www.gnu.org/software/wget/manual/wget.html>.

- Télécharge le contenu d'une URL vers un fichier (nommé « foo » dans ce cas) :

`wget {{https://example.com/foo}}`

- Télécharge le contenu d'une URL vers un fichier spécifique :

`wget {{[-O|--output-document]}} {{chemin/vers/fichier}} {{https://example.com/foo}}`

- Télécharge une page web et toutes ses ressources avec des intervalles de 3 secondes entre les requêtes (scripts, feuilles de style, images, etc.) :

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/une_page.html}}`

- Télécharge tous les fichiers listés dans un répertoire et ses sous-répertoires (ne télécharge pas les éléments intégrés de la page) :

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/un_chemin/}}`

- Limite la vitesse de téléchargement et le nombre de tentatives de connexion :

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/un_chemin/}}`

- Télécharge un fichier depuis un serveur HTTP avec l'authentification Basic (fonctionne aussi pour FTP) :

`wget --user {{nom_utilisateur}} --password {{mot_de_passe}} {{https://example.com}}`

- Reprend un téléchargement incomplet :

`wget {{[-c|--continue]}} {{https://example.com}}`

- Télécharge toutes les URLs stockées dans un fichier texte vers un répertoire spécifique :

`wget {{[-P|--directory-prefix]}} {{chemin/vers/répertoire}} {{[-i|--input-file]}} {{chemin/vers/URLs.txt}}`
