# emerge

> Utilitarul managerului de pachete Gentoo Linux.
> Mai multe informaţii: <https://wiki.gentoo.org/wiki/Portage#emerge>

- Sincronizează toate pachetele:

`emerge --sync`

- Actualizaţi toate pachetele, inclusiv dependenţele:

`emerge -uDNav @world`

- Reluați o actualizare eșuată, sărind peste pachetul nereușit:

`emerge --resume --skipfirst`

- Instalați un pachet nou, cu confirmare:

`emerge -av {{package_name}}`

- Eliminați un pachet, cu confirmare:

`emerge -Cav {{package_name}}`

- Eliminați pachetele orfane (care au fost instalate doar ca dependențe):

`emerge -avc`

- Caută în baza de date a pachetelor pentru un cuvânt cheie:

`emerge -S {{keyword}}`
