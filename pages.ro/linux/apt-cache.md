# apt-cache

> Instrumentul de interogare a pachetelor Debian și Ubuntu.
> Mai multe informaţii: <https://manpages.debian.org/latest/apt/apt-cache.8.html>

- Căutați un pachet în sursele dvs. curente:

`apt-cache search {{query}}`

- Afișați informații despre un pachet:

`apt-cache show {{package}}`

- Arată dacă un pachet este instalat și actualizat:

`apt-cache policy {{package}}`

- Arată dependențele pentru un pachet:

`apt-cache depends {{package}}`

- Arată pachete care depind de un anumit pachet:

`apt-cache rdepends {{package}}`
