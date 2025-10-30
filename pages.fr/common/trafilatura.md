# trafilatura

> Un outil Python pour l'extraction et le crawling de contenu web.
> Extrait le texte principal, les métadonnées et les commentaires des pages web.
> Plus d'informations : <https://trafilatura.readthedocs.io/en/latest/usage-cli.html#further-information>.

- Extraire le texte d'une URL :

`trafilatura {{[-u|--URL]}} {{url}}`

- Extraire le texte et sauve le résultat dans un fichier :

`trafilatura {{[-u|--URL]}} {{url}} {{[-o|--output-dir]}} {{chemin/vers/fichier.txt}}`

- Extraire le texte au format JSON :

`trafilatura {{[-u|--URL]}} {{url}} --json`

- Extraire le texte de plusieurs URLs listées dans un fichier :

`trafilatura {{[-i|--input-file]}} {{chemin/vers/liste_urls.txt}}`

- Crawle un site web en utilisant son sitemap :

`trafilatura --sitemap {{url_vers_sitemap.xml}}`

- Extraire le texte en conservant le formatage HTML :

`trafilatura {{[-u|--URL]}} {{url}} --formatting`

- Extraire le texte avec les commentaires :

`trafilatura {{[-u|--URL]}} {{url}} --with-comments`

- Affiche l'aide pour plus d'options :

`trafilatura {{[-h|--help]}}`
