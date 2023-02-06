# jupytext

> Eszköz a Jupyter jegyzetfüzetek egyszerű szöveges dokumentumokká konvertálására, és vissza. További információ: <https://jupytext.readthedocs.io>.

- Egy jegyzetfüzet átalakítása párosított `.ipynb`/`.py` jegyzetfüzetté:

`jupytext --set-formats ipynb,py {{notebook.ipynb}}`

- Egy jegyzetfüzet átalakítása egy `.py` fájlba:

`jupytext --to py {{notebook.ipynb}}`

- Egy `.py` fájl átalakítása kimenetek nélküli notebookká:

`jupytext --to notebook {{notebook.py}}`

- Egy `.md` fájl átalakítása notebookká és futtatása:

`jupytext --to notebook --execute {{notebook.md}}`

- Egy notebook bemeneti celláinak frissítése, a kimenetek és metaadatok megőrzése:

`jupytext --update --to notebook {{notebook.py}}`

- Egy jegyzetfüzet összes párosított ábrázolásának frissítése:

`jupytext --sync {{notebook.ipynb}}`
