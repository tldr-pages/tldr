# pycodestyle

> Un instrument pentru a verifica codul Python împotriva convențiilor de stil PEP 8.
> Mai multe informaţii: <https://pycodestyle.readthedocs.io>

- Verificați stilul unui singur fișier:

`pycodestyle {{file.py}}`

- Verificați stilul mai multor fișiere:

`pycodestyle {{file1.py}} {{file2.py}} {{file3.py}}`

- Afișează doar prima apariție a unei erori:

`pycodestyle --first {{file.py}}`

- Afișați codul sursă pentru fiecare eroare:

`pycodestyle --show-source {{file.py}}`

- Afișați textul PEP 8 specific pentru fiecare eroare:

`pycodestyle --show-pep8 {{file.py}}`
