# a2dissite

> Désactive un hôte virtuel Apache sur une distribution Debian.
> Plus d'informations : <https://manpages.debian.org/latest/apache2/a2dissite.8.en.html>.

- Désactive un hôte virtuel :

`sudo a2dissite {{virtual_host}}`

- N'affiche aucun message (mode silencieux) :

`sudo a2dissite --quiet {{virtual_host}}`
