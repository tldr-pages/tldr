# pycodestyle

> A Python kód PEP 8 stíluskonvenciókkal való ellenőrzésére szolgáló eszköz. További információ: <https://pycodestyle.readthedocs.io>.

- Egyetlen fájl stílusának ellenőrzése:

`pycodestyle {{file.py}}`

- Több fájl stílusának ellenőrzése:

`pycodestyle {{file1.py}} {{file2.py}} {{file3.py}}`

- Csak a hiba első előfordulásának megjelenítése:

`pycodestyle --first {{file.py}}`

- Minden egyes hiba forráskódjának megjelenítése:

`pycodestyle --show-source {{file.py}}`

- Megjeleníti az egyes hibák PEP 8 szövegét:

`pycodestyle --show-pep8 {{file.py}}`
