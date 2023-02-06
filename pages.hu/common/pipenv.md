# pipenv

> Egyszerű és egységes Python fejlesztési munkafolyamat. Kezeli a csomagokat és a virtuális környezetet egy projekthez. További információ: <https://pypi.org/project/pipenv>.

- Új projekt létrehozása:

`pipenv`

- Új projekt létrehozása a Python 3 használatával:

`pipenv --three`

- Csomag telepítése:

`pipenv install {{package_name}}`

- Telepítse az összes függőséget egy projekthez:

`pipenv install`

- Egy projekt összes függőségének telepítése (beleértve a dev csomagokat is):

`pipenv install --dev`

- Egy csomag eltávolítása:

`pipenv uninstall {{package_name}}`

- Héj indítása a létrehozott virtuális környezetben:

`pipenv shell`

- A `requirements.txt` (függőségi lista) létrehozása egy projekthez:

`pipenv lock --requirements`
