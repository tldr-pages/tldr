# pipenv

> Fluxul de lucru de dezvoltare Python simplu și unificat.
> Gestionează pachetele și mediul virtual pentru un proiect.
> Mai multe informaţii: <https://pypi.org/project/pipenv>

- Creați un nou proiect:

`pipenv`

- Creați un nou proiect folosind Python 3:

`pipenv --three`

- Instalați un pachet:

`pipenv install {{package_name}}`

- Instalați toate dependențele pentru un proiect:

`pipenv install`

- Instalați toate dependențele pentru un proiect (inclusiv pachetele dev):

`pipenv install --dev`

- Dezinstalați un pachet:

`pipenv uninstall {{package_name}}`

- Porniți o coajă în mediul virtual creat:

`pipenv shell`

- Generarea unei `cerinments.txt` (lista de dependențe) pentru un proiect:

`pipenv lock --requirements`
