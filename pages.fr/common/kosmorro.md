# kosmorro

> Calcule les éphémérides et les évènements pour une date donnée, à un emplacement donné sur Terre.
> Plus d'informations : <http://kosmorro.space>.

- Obtenir les éphémérides pour Paris (France) :

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}}`

- Obtenir les éphémérides pour Paris (France), sur le fuseau horaire UTC+2 :

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --timezone={{2}}`

- Obtenir les éphémérides du 9 juin 2020 pour Paris (France) :

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --date={{2020-06-09}}`

- Générer un fichier PDF (TeXLive doit être installé) :

`kosmorro --format={{pdf}} --output={{chemin/vers/le/fichier.pdf}}`
