# dpkg-deb

> Împachetați, despachetați și furnizați informații despre arhivele Debian.
> Mai multe informaţii: <https://manpages.debian.org/buster/dpkg/dpkg-deb.1.en.html>

- Afișează informații despre un pachet:

`dpkg-deb --info {{path/to/file.deb}}`

- Afișează numele și versiunea pachetului pe o singură linie:

`dpkg-deb --show {{path/to/file.deb}}`

- Listați conținutul pachetului:

`dpkg-deb --contents {{path/to/file.deb}}`

- Extrageţi conţinutul pachetului într-un director:

`dpkg-deb --extract {{path/to/file.deb}} {{path/to/directory}}`

- Creați un pachet dintr-un director specificat:

`dpkg-deb --build {{path/to/directory}}`
