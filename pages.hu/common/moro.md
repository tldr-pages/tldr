# moro

> A munkaidő nyomon követése. További információ: <https://moro.js.org>.

- A `moro` paraméterek nélküli futtatásával az aktuális időpontot állíthatja be a munkanap kezdetének:

`moro`

- Egyéni időpont megadása a munkanap kezdetéhez:

`moro hi {{09:30}}`

- A `moro` második paraméter nélküli meghívása a munkanap végi aktuális idő beállításához:

`moro`

- Adjon meg egy egyéni időpontot a munkanap végére:

`moro bye {{17:30}}`

- Megjegyzés hozzáadása az aktuális munkanaphoz:

`moro note {{3 hours on project Foo}}`

- Az aktuális munkanapra vonatkozó időnaplók és jegyzetek jelentésének megjelenítése:

`moro report`

- Az összes nyilvántartott munkanapra vonatkozó időnaplók és jegyzetek jelentésének megjelenítése:

`moro report --all`
