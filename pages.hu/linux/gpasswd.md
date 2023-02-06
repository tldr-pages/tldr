# gpasswd

> Adja meg a `/etc/group` és a `/etc/gshadow` címet. További információ: <https://manned.org/gpasswd>.

- Csoportos rendszergazdák meghatározása:

`sudo gpasswd -A {{user1,user2}} {{group}}`

- A csoporttagok listájának beállítása:

`sudo gpasswd -M {{user1,user2}} {{group}}`

- Hozzon létre jelszót a megnevezett csoporthoz:

`gpasswd {{group}}`

- Felhasználó hozzáadása a megnevezett csoporthoz:

`gpasswd -a {{user}} {{group}}`

- Felhasználó eltávolítása a megnevezett csoportból:

`gpasswd -d {{user}} {{group}}`
