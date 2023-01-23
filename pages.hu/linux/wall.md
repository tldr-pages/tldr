# wall

> Üzenet írása az aktuálisan bejelentkezett felhasználók termináljaira. További információ: <https://manned.org/wall>.

- Üzenet küldése:

`echo "{{message}}" | wall`

- Üzenet küldése egy fájlból:

`wall {{file}}`

- Üzenet küldése időkorlátozással (alapértelmezett 300):

`wall -t {{seconds}} {{file}}`
