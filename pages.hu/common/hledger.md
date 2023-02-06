# hledger

> Egy egyszerű szöveges könyvelőprogram a parancssorhoz. További információ: <https://hledger.org>.

- Tranzakciók interaktív módon történő hozzáadása a naplóhoz:

`hledger add`

- A számlahierarchia megjelenítése, egy adott naplófájl használatával:

`hledger --file {{path/to/file.journal}} accounts --tree`

- Havi bevételi kimutatás megjelenítése:

`hledger incomestatement --monthly --depth 2`

- Nyomtassa ki az élelmiszerre költött készpénz összegét:

`hledger print assets:cash | hledger -f- -I balance expenses:food --depth 2`
