# eva

> Egyszerű számológép REPL, hasonlóan a `bc`, szintaxis kiemeléssel és állandó előzményekkel. További információ: <https://github.com/NerdyPepper/eva>.

- A számológép futtatása interaktív módban:

`eva`

- Kiszámítja egy kifejezés eredményét:

`eva "{{(1 + 2) * 2 ^ 2}}"`

- Kifejezés kiszámítása a tizedesjegyek számát 5-re kényszerítve:

`eva --fix {{5}} "{{5 / 3}}"`

- Kifejezés kiszámítása szinusz és koszinusz segítségével:

`eva "{{sin(1) + cos(1)}}"`
