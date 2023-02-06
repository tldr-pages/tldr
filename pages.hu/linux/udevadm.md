# udevadm

> Linux `udev` menedzsment eszköz. További információ: <https://www.freedesktop.org/software/systemd/man/udevadm>.

- Az összes eszközesemény figyelése:

`sudo udevadm monitor`

- A kernel által küldött `uevents` nyomtatása:

`sudo udevadm monitor --kernel`

- A `udev` által feldolgozott eszközesemények nyomtatása:

`sudo udevadm monitor --udev`

- Egy eszköz attribútumainak listázása:

`sudo udevadm info --attribute-walk --path {{/dev/sda1}}`

- Az összes `udev` szabály újratöltése:

`sudo udevadm control --reload-rules`

- Az összes `udev` szabály futtatásának elindítása:

`sudo udevadm trigger`
