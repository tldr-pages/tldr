# setsid

> Egy program futtatása egy új munkamenetben, ha a hívó folyamat nem folyamatcsoport-vezető. A létrehozott munkamenetet alapértelmezés szerint nem az aktuális terminál vezérli. További információ: <https://manned.org/setsid>.

- Program futtatása új munkamenetben:

`setsid {{program}}`

- Egy program futtatása új munkamenetben, a kapott kimenet és hiba elvetésével:

`setsid {{program}} > /dev/null 2>&1`

- Új folyamatot létrehozó program futtatása:

`setsid --fork {{program}}`

- Egy program kilépési kódjának visszaadása a setsid kilépési kódjaként, amikor a program kilép:

`setsid --wait {{program}}`

- Egy program futtatása új munkamenetben az aktuális terminált vezérlő terminálként beállítva:

`setsid --ctty {{program}}`
