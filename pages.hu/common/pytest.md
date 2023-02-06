# pytest

> Python tesztek futtatása. További információ: <https://docs.pytest.org/>.

- Tesztek futtatása meghatározott fájlokból:

`pytest {{path/to/test_file1.py path/to/test_file2.py ...}}`

- Olyan tesztek futtatása, amelyek neve megfelel egy adott \[k\]eyword kifejezésnek:

`pytest -k {{expression}}`

- Kilépés, amint egy teszt sikertelen vagy hibát észlel:

`pytest --exitfirst`

- Markerekre illeszkedő vagy azokat kizáró tesztek futtatása:

`pytest -m {{marker_name1 and not marker_name2}}`

- Futtatás a teszt sikertelenségéig, az utolsó sikertelen teszt folytatásával:

`pytest --stepwise`

- Tesztek futtatása kimenet rögzítése nélkül:

`pytest --capture=no`
