# flock

> Zárolások kezelése shell szkriptekből. Használható annak biztosítására, hogy egy parancsnak csak egy folyamata fusson. További információ: <https://manned.org/flock>.

- Fájlzárral rendelkező parancs futtatása, amint a zárat mások nem igénylik:

`flock {{path/to/lock.lock}} --command "{{command}}"`

- Fájlzárral rendelkező parancs futtatása, és kilépés, ha a zár nem létezik:

`flock {{path/to/lock.lock}} --nonblock --command "{{command}}"`

- Fájlzárral rendelkező parancs futtatása, és kilépés egy adott hibakóddal, ha a zár nem létezik:

`flock {{path/to/lock.lock}} --nonblock --conflict-exit-code {{error_code}} -c "{{command}}"`
