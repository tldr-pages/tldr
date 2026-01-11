# kosmorro

> Calcule les éphémérides et les évènements pour une date donnée, à un emplacement donné sur Terre.
> Plus d'informations : <https://kosmorro.space/cli/manpage/>.

- Obtenir les éphémérides pour Paris (France) :

`kosmorro --position="48.7996,2.3511"`

- Obtenir les éphémérides pour Paris (France), sur le fuseau horaire local :

`kosmorro --position="48.7996,2.3511" --timezone="Europe/Paris"`

- Obtenir les éphémérides du 9 juin 2020 pour Paris (France) :

`kosmorro  --position="48.7996,2.3511" --date="2020-06-09"`

- Obtenir les éphemerides pour Paris (France) dans deux jours :

`kosmorro  --position="48.7996,2.3511" --date="+2d"`

- Générer un fihier PDF (TeXLive doit être installé):

`kosmorro --output="path/to/file.pdf"`
