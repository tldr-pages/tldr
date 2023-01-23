# certutil

> Kulcsok és tanúsítványok kezelése mind az NSS-adatbázisokban, mind más NSS-tokenekben. További információ: <https://manned.org/certutil>.

- Új tanúsítvány-adatbázis létrehozása:

`certutil -N -d .`

- Az adatbázisban lévő összes tanúsítvány listázása:

`certutil -L -d .`

- Az összes magánkulcs listázása egy adatbázisban:

`certutil -K -d . -f {{path/to/password_file.txt}}`

- Importálja az aláírt tanúsítványt a kérelmező adatbázisába:

`certutil -A -n "{{server_certificate}}" -t ",," -i {{path/to/file.crt}} -d .`

- Alany alternatív nevek hozzáadása egy adott tanúsítványhoz:

`certutil -S -f {{path/to/password_file.txt}} -d . -t ",," -c "{{server_certificate}}" -n "{{server_name}}" -g {{2048}} -s "CN={{common_name}},O={{organization}}"`
