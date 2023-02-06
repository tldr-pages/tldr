# gsettings

> A dconf beállítások lekérdezése és módosítása sémaérvényesítéssel. További információ: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_the_desktop_environment_in_rhel_8/configuring-gnome-at-low-level_using-the-desktop-environment-in-rhel-8#using-gsettings-command_configuring-gnome-at-low-level>.

- Egy kulcs értékének beállítása. Sikertelen, ha a kulcs nem létezik, vagy az érték tartományon kívül van:

`gsettings set {{org.example.schema}} {{example-key}} {{value}}`

- Kinyomtatja egy kulcs értékét vagy a séma által megadott alapértelmezett értéket, ha a kulcs nincs beállítva a `dconf` oldalon:

`gsetings get {{org.example.schema}} {{example-key}}`

- A kulcs beállításának feloldása, így a séma alapértelmezett értéke kerül felhasználásra:

`gsettings reset {{org.example.schema}} {{example-key}}`

- Az összes (nem áthelyezhető) séma, kulcs és érték megjelenítése:

`gsettings list-recursively`

- Egy séma összes kulcsának és értékének megjelenítése (alapértelmezett, ha nincs beállítva):

`gsettings list-recursively {{org.example.schema}}`

- A séma által megengedett értékek megjelenítése egy kulcshoz (hasznos enum kulcsok esetén):

`gsettings range {{org.example.schema}} {{example-key}}`

- A kulcs ember által olvasható leírásának megjelenítése:

`gsettings describe {{org.example.schema}} {{example-key}}`
