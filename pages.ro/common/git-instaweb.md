# git instaweb

> Ajutor pentru lansarea unui server gitweb.
> Mai multe informaţii: <https://git-scm.com/docs/git-instaweb>

- Lansarea unui server gitweb pentru depozitul Git curent:

`git instaweb --start`

- Ascultați numai pe localhost:

`git instaweb --start --local`

- Ascultați pe un anumit port:

`git instaweb --start --port {{1234}}`

- Utilizați un daemon http specificat:

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- De asemenea, lansează automat un browser web:

`git instaweb --start --browser`

- Opriți serverul gitweb care rulează în prezent:

`git instaweb --stop`

- Reporniți serverul gitweb care rulează în prezent:

`git instaweb --restart`
