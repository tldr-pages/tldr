# plesk

> Plesk hosting vezérlőpanel CLI felület. További információ: <https://docs.plesk.com>.

- Generáljon egy automatikus bejelentkezési linket az admin felhasználó számára, és nyomtassa ki:

`plesk login`

- Termékverziós információk megjelenítése:

`plesk version`

- Listázza ki az összes hosztolt tartományt:

`plesk bin domain --list`

- A `panel.log` fájl változásainak figyelésének megkezdése:

`plesk log {{panel.log}}`

- Indítsa el az interaktív MySQL konzolt:

`plesk db`

- Nyissa meg a Plesk fő konfigurációs fájlt az alapértelmezett szerkesztővel:

`plesk conf {{panel.ini}}`
