# kosmorro

> Calcule les éphémérides et les évènements pour une date donnée, à un emplacement donné sur Terre.
> Plus d'informations : <https://kosmorro.space/cli/manpage/>.

- Obtient les éphémérides pour Paris (France) :

`kosmorro {{[-p|--position]}} "48.7996,2.3511"`

- Obtient les éphémérides pour Paris (France), sur le fuseau horaire local :

`kosmorro {{[-p|--position]}} "48.7996,2.3511" {{[-t|--timezone]}} "Europe/Paris"`

- Obtient les éphémérides du 9 juin 2020 pour Paris (France) :

`kosmorro {{[-p|--position]}} "48.7996,2.3511" {{[-d|--date]}} "2020-06-09"`

- Obtient les éphemerides pour Paris (France) dans deux jours :

`kosmorro {{[-p|--position]}} "48.7996,2.3511" {{[-d|--date]}} "+2d"`

- Génère un fihier PDF (TeXLive doit être installé) :

`kosmorro {{[-o|--output]}} "{{chemin/vers/fichier.pdf}}"`
