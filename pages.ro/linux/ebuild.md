# ebuild

> O interfaţă de nivel scăzut pentru sistemul Gentoo Portage.
> Mai multe informaţii: <https://wiki.gentoo.org/wiki/Ebuild>

- Creați sau actualizați manifestul pachetului:

`ebuild {{path/to/file.ebuild}} manifest`

- Curățați directoarele de compilare temporare pentru fișierul de compilare:

`ebuild {{path/to/file.ebuild}} clean`

- Fetch surse în cazul în care acestea nu există:

`ebuild {{path/to/file.ebuild}} fetch`

- Extrageţi sursele într-un director temporar de compilare:

`ebuild {{path/to/file.ebuild}} unpack`

- Compilarea surselor extrase:

`ebuild {{path/to/file.ebuild}} compile`

- Instalați pachetul într-un director temporar de instalare:

`ebuild {{path/to/file.ebuild}} install`

- Instalați fișierele temporare în sistemul de fișiere live:

`ebuild {{path/to/file.ebuild}} qmerge`

- Preluați, despachetați, compilați, instalați și qîmbinați fișierul ebuild specificat:

`ebuild {{path/to/file.ebuild}} merge`
