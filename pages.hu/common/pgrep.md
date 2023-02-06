# pgrep

> Folyamatok keresése vagy jelzése név alapján. További információ: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>.

- Visszaadja az összes olyan futó folyamat PID-jét, amelynek a parancssorozata megegyezik:

`pgrep {{process_name}}`

- Folyamatok keresése a parancssori opcióikkal együtt:

`pgrep --full "{{process_name}} {{parameter}}"`

- Egy adott felhasználó által futtatott folyamatok keresése:

`pgrep --euid root {{process_name}}`
