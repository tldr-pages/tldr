# equery

> Vizualizaţi informaţii despre pachetele Portage.
> Mai multe informaţii: <https://wiki.gentoo.org/wiki/Equery>

- Listează toate pachetele instalate:

`equery list '*'`

- Căutarea pachetelor instalate în arborele Portage şi în suprapuneri:

`equery list -po {{package_name}}`

- Listează toate pachetele care depind de un anumit pachet:

`equery depends {{package_name}}`

- Listează toate pachetele pe care un anumit pachet depinde de:

`equery depgraph {{package_name}}`

- Listează toate fișierele instalate de un pachet:

`equery files --tree {{package_name}}`
