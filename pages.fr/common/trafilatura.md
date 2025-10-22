# trafilatura

> Un outil Python pour l'extraction et le crawling de contenu web.
> Extrait le texte principal, les métadonnées et les commentaires des pages web.
> Plus d'informations : <https://trafilatura.readthedocs.io/en/latest/>.

- Extraire le texte d'une URL :

`trafilatura -u {{url}}`

- Extraire le texte et sauve le résultat dans un fichier :

`trafilatura -u {{url}} -o {{chemin/vers/fichier.txt}}`

- Extraire le texte au format JSON :

`trafilatura -u {{url}} --json-output`

- Extraire le texte de plusieurs URLs listées dans un fichier :

`trafilatura --input-file {{chemin/vers/liste_urls.txt}}`

- Crawle un site web en utilisant son sitemap :

`trafilatura --sitemap {{url_vers_sitemap.xml}}`

- Extraire le texte en conservant le formatage HTML :

`trafilatura -u {{url}} --formatting`

- Extraire le texte avec les commentaires :

`trafilatura -u {{url}} --with-comments`

- Afficher l'aide pour plus d'options :

`trafilatura --help`
