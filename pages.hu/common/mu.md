# mu

> E-mailek indexelése és keresése egy helyi Maildirből. További információ: <https://man.cx/mu>.

- Az e-mail adatbázis inicializálása, opcionálisan megadva a Maildir könyvtárat és az e-mail címeket:

`mu init --maildir={{path/to/directory}} --my-address={{name@example.com}}`

- Új e-mailek indexelése:

`mu index`

- Üzenetek keresése egy adott kulcsszó segítségével (az üzenet testében, tárgyában, feladójában, ...):

`mu find {{keyword}}`

- Alice-nak küldött olyan üzenetek keresése, amelyek tárgya `jellyfish` és a `apples` vagy `oranges` szavakat tartalmazza:

`mu find to:{{alice}} subject:{{jellyfish}} {{apples}} OR {{oranges}}`

- Olvasatlan üzenetek keresése a `soc` kezdetű szavakról (a `*` csak a keresési kifejezés végén működik) az Elküldött elemek mappában:

`mu find 'subject:{{soc}}*' flag:{{unread}} maildir:'/{{Sent Items}}'`

- Samtől származó, 2021-ben írt, 2 KiB és 2 MiB közötti méretű, csatolt képeket tartalmazó üzenetek keresése:

`mu find 'mime:{{image/*}} size:{{2k..2m}} date:{{20210101..20211231}} from:{{sam}}`

- Listázza ki azokat a kapcsolatokat, amelyeknek a neve vagy az e-mail címe `Bob`:

`mu cfind {{Bob}}`
