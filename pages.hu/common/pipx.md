# pipx

> Python alkalmazások telepítése és futtatása elszigetelt környezetben. További információ: <https://github.com/pypa/pipx>.

- Egy alkalmazás futtatása egy ideiglenes virtuális környezetben:

`pipx run {{pycowsay}} {{moo}}`

- Telepítsen egy csomagot virtuális környezetbe, és adjon hozzá belépési pontokat az elérési útvonalhoz:

`pipx install {{package}}`

- Telepített csomagok listázása:

`pipx list`

- Egy alkalmazás futtatása ideiglenes virtuális környezetben a futtathatótól eltérő csomagnévvel:

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`

- Függőségek beillesztése egy meglévő virtuális környezetbe:

`pipx inject {{package}} {{dependency1 dependency2 ...}}`

- Csomag telepítése virtuális környezetbe pip argumentumokkal:

`pipx install --pip-args='{{pip-args}}' {{package}}`
