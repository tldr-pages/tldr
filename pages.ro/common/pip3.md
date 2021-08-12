# pip3

> Manager de pachete Python.
> Mai multe informaţii: <https://pip.pypa.io>

- Găsiţi pachetele disponibile:

`pip3 search {{package_name}}`

- Instalați un pachet:

`pip3 install {{package_name}}`

- Instalați o versiune specifică a unui pachet:

`pip3 install {{package_name}}=={{package_version}}`

- Upgrade un pachet:

`pip3 install --upgrade {{package_name}}`

- Dezinstalați un pachet:

`pip3 uninstall {{package_name}}`

- Salvați lista de pachete instalate într-un fișier:

`pip3 freeze > {{requirements.txt}}`

- Instalați pachete dintr-un fișier:

`pip3 install --requirement {{requirements.txt}}`

- Afișează informațiile despre pachetul instalat:

`pip3 show {{package_name}}`
