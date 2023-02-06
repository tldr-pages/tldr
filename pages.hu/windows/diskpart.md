# diskpart

> Lemez-, kötet- és partíciókezelő. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Futtassa a diskpartot önmagában egy rendszergazdai parancssorban, hogy belépjen a parancssorába:

`diskpart`

- List all disks:

`list disk`

- Válasszon ki egy kötetet:

`select volume {{volume}}`

- Meghajtóbetű hozzárendelése a kiválasztott kötethez:

`assign letter {{letter}}`

- Új partíció létrehozása:

`create partition primary`

- A kiválasztott kötet aktiválása:

`active`

- Kilépés a diskpartból:

`exit`
