# flake8

> Instrument pentru a verifica stilul și calitatea codului Python.
> Mai multe informaţii: <https://flake8.pycqa.org/>

- Lint un fișier sau director recursiv:

`flake8 {{path/to/file_or_directory}}`

- Lint un fișier sau director recursiv și arată linia pe care a apărut fiecare eroare:

`flake8 --show-source {{path/to/file_or_directory}}`

- Lint un fișier sau director recursiv și ignorați o listă de reguli. (Toate regulile disponibile pot fi găsite la flake8rules.com):

`flake8 --ignore {{rule1,rule2}} {{path/to/file_or_directory}}`

- Lamă un fișier sau un director recursiv, dar excludeți fișierele care se potrivesc cu globurile sau substringurile date:

`flake8 --exclude {{substring1,glob2}} {{path/to/file_or_directory}}`
