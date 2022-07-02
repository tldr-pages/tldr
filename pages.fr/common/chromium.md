# chromium

> Navigateur Web open source principalement développé et maintenu par Google.
> Plus d'informations : <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Ouvre une URL ou un fichier spécifique :

`chromium {{https://exemple.com|chemin/vers/fichier.html}}`

- Ouvre en mode navigation privée :

`chromium --incognito {{exemple.com}}`

- Ouvre dans une nouvelle fenêtre :

`chromium --new-window {{exemple.com}}`

- Ouvre en mode application (sans barres d'outils, barre d'URL, boutons, etc) :

`chromium --app={{https://exemple.com}}`

- Utilise un serveur proxy :

`chromium --proxy-server="{{://hostname:66}}" {{exemple.com}}`

- Ouvre dans un répertoire de profil personnalisé :

`chromium --user-data-dir={{chemin/vers/répertoire}}`

- Ouvre sans validation CORS (utile pour tester une API) :

`chromium --user-data-dir={{chemin/vers/répertoire}} --disable-web-security`

- Ouvre avec une fenêtre outils de développement pour chaque onglet ouvert :

`chromium --auto-open-devtools-for-tabs`
