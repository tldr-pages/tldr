# curlie

> Curlie est un frontend pour curl qui ajoute la facilité d'utilisation de httpie.
> Plus d'informations : <https://github.com/rs/curlie>.

- Envoie une requête GET :

`curlie {{httpbin.org/get}}`

- Envoie une requête POST :

`curlie post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- Envoie une requête GET avec des paramètres de requête (par ex : `premier_param=5&deuxième_param=true`) :

`curlie get {{httpbin.org/get}} {{premier_param=5}} {{second_param=true}}`

- Envoie une requête GET avec un en-tête personnalisé :

`curlie get {{httpbin.org/get}} {{clef-d-en-tête:valeur-d-en-tête}}`
