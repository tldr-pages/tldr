# gem

> Interakció a Ruby programozási nyelv csomagkezelőjével. További információ: <https://rubygems.org>.

- Távoli gem(ek) keresése és az összes elérhető verzió megjelenítése:

`gem search {{regular_expression}} --all`

- Telepítse egy gem legújabb verzióját:

`gem install {{gemname}}`

- Egy gem adott verziójának telepítése:

`gem install {{gemname}} --version {{1.0.0}}`

- Telepítse egy gem legfrissebb megfelelő (SemVer) verzióját:

`gem install {{gemname}} --version '~> {{1.0}}'`

- Egy gem frissítése:

`gem update {{gemname}}`

- Az összes helyi drágakő listázása:

`gem list`

- Egy drágakő eltávolítása:

`gem uninstall {{gemname}}`

- Egy gem adott verziójának eltávolítása:

`gem uninstall {{gemname}} --version {{1.0.0}}`
