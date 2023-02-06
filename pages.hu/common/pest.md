# pest

> Egy PHP tesztelési keretrendszer, amelynek középpontjában az egyszerűség áll. További információ: <https://pestphp.com>.

- Egy szabványos pesti konfiguráció inicializálása az aktuális könyvtárban:

`pest --init`

- Tesztek futtatása az aktuális könyvtárban:

`pest`

- A megadott csoporttal megjegyzett tesztek futtatása:

`pest --group {{name}}`

- A tesztek futtatása és a lefedettségi jelentés kinyomtatása a `stdout`:

`pest --coverage`

- Lefedettséggel rendelkező tesztek futtatása és hiba, ha a lefedettség kisebb, mint a minimális százalék:

`pest --coverage --min={{80}}`
