# chfn

> Egy felhasználó `finger` adatainak frissítése. További információ: <https://manned.org/chfn>.

- A felhasználó "Név" mezőjének frissítése a `finger` kimenetében:

`chfn -f {{new_display_name}} {{username}}`

- Egy felhasználó "Office Room Number" mezőjének frissítése a `finger` kimeneténél:

`chfn -o {{new_office_room_number}} {{username}}`

- A felhasználó "Office Phone Number" mezőjének frissítése a `finger` kimeneténél:

`chfn -p {{new_office_telephone_number}} {{username}}`

- A felhasználó "Home Phone Number" mezőjének frissítése a `finger` kimeneténél:

`chfn -h {{new_home_telephone_number}} {{username}}`
