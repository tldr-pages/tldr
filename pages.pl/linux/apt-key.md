# apt-key

> Narzędzie do zarządzania kluczami APT Package Manager dla Debiana i Ubuntu.
> Notatka: `apt-key` jest aktualnie przestarzały (za wyjątkiem użycia `apt-key del` w skryptach opiekunów).
> Więcej informacji: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Wyświetl zaufane klucze:

`apt-key list`

- Dodanie klucza do magazynu zaufanych kluczy:

`apt-key add {{plik_z_kluczem_publicznym.asc}}`

- Usunięcie klucza z magazynu zaufanych kluczy:

`apt-key del {{id_klucza}}`

- Dodanie zdalnego klucza do magazynu zaufanych kluczy:

`wget -qO - {{https://host.tld/nazwa_pliku.key}} | apt-key add -`

- Dodanie klucza z serwera kluczy na podstawie id klucza:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{id_klucza}}`
