# chpasswd

> Több felhasználó jelszavainak módosítása a `stdin` segítségével. További információ: <https://manned.org/chpasswd.8>.

- Egy adott felhasználó jelszavának módosítása:

`printf "{{username}}:{{new_password}}" | sudo chpasswd`

- Több felhasználó jelszavának módosítása (A beírt szöveg nem tartalmazhat szóközöket.):

`printf "{{username_1}}:{{new_password_1}}\n{{username_2}}:{{new_password_2}}" | sudo chpasswd`

- Egy adott felhasználó jelszavának módosítása, és annak titkosított formában történő megadása:

`printf "{{username}}:{{new_encrypted_password}}" | sudo chpasswd --encrypted`

- Egy adott felhasználó jelszavának módosítása, és a tárolt jelszóhoz meghatározott titkosítást használ:

`printf "{{username}}:{{new_password}}" | sudo chpasswd --crypt-method {{NONE|DES|MD5|SHA256|SHA512}}`
