# runuser

> Parancsok futtatása egy adott felhasználóként és csoportként jelszó megkérdezése nélkül (root jogosultságok szükségesek). További információ: <https://manned.org/runuser>.

- Parancs futtatása más felhasználóként:

`runuser {{user}} -c '{{command}}'`

- Parancs futtatása más felhasználóként és csoportként:

`runuser {{user}} -g {{group}} -c '{{command}}'`

- Bejelentkezési héj indítása egy adott felhasználóként:

`runuser {{user}} -l`

- Egy shell megadása a futtatáshoz az alapértelmezett shell helyett (bejelentkezéshez is működik):

`runuser {{user}} -s {{/bin/sh}}`

- A root teljes környezetének megőrzése (csak ha a `--login` nincs megadva):

`runuser {{user}} --preserve-environment -c '{{command}}'`
