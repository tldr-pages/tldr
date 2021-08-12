# apt-file

> Căutați fișiere în pachete apt, inclusiv cele neinstalate încă.
> Mai multe informaţii: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>

- Actualizaţi baza de date cu metadate:

`sudo apt update`

- Căutați pachete care conțin fișierul sau calea specificată:

`apt-file {{search|find}} {{part/of/filename}}`

- Listați conținutul unui anumit pachet:

`apt-file {{show|list}} {{package_name}}`

- Caută pachete care se potrivesc cu expresia regulată dată în `pattern`:

`apt-file {{search|find}} --regexp {{regular_expression}}`
