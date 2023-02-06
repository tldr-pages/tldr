# jupyter

> Webes alkalmazás kódot, vizualizációt és jegyzeteket tartalmazó dokumentumok létrehozására és megosztására. Elsősorban adatelemzésre, tudományos számításokhoz és gépi tanuláshoz használják. További információ: <https://jupyter.org>.

- Indítson el egy Jupyter notebook kiszolgálót az aktuális könyvtárban:

`jupyter notebook`

- Egy adott Jupyter notebook megnyitása:

`jupyter notebook {{example.ipynb}}`

- Egy adott Jupyter notebook exportálása más formátumba:

`jupyter nbconvert --to {{html|markdown|pdf|script}} {{example.ipynb}}`

- Kiszolgáló indítása egy adott porton:

`jupyter notebook --port={{port}}`

- A jelenleg futó notebook-kiszolgálók listája:

`jupyter notebook list`

- A jelenleg futó kiszolgáló leállítása:

`jupyter notebook stop`

- A JupyterLab elindítása, ha telepítve van, az aktuális könyvtárban:

`jupyter lab`
