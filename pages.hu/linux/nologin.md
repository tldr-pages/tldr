# nologin

> Alternatív shell, amely megakadályozza a felhasználó bejelentkezését. További információ: <https://manned.org/nologin.5>.

- A felhasználó bejelentkezési héjának beállítása `nologin`, hogy megakadályozza a felhasználó bejelentkezését:

`chsh -s {{user}} nologin`

- A `nologin` bejelentkezési héjjal rendelkező felhasználóknak szóló üzenet testreszabása:

`echo "{{declined_login_message}}" > /etc/nologin.txt`
