# jupyter

> Aplicație Web pentru a crea și a partaja documente care conțin cod, vizualizări și note.
> Utilizate în principal pentru analiza datelor, calcul științific și învățare automată.
> Mai multe informaţii: <https://jupyter.org>

- Porniți un server de notebook-uri Jupyter în directorul curent:

`jupyter notebook`

- Deschideți un anumit notebook Jupyter:

`jupyter notebook {{example.ipynb}}`

- Exportați un notebook Jupyter specific într-un alt format:

`jupyter nbconvert --to {{html|markdown|pdf|script}} {{example.ipynb}}`

- Porniți un server pe un anumit port:

`jupyter notebook --port={{port}}`

- Listă care rulează în prezent servere notebook-uri:

`jupyter notebook list`

- Opriți serverul care rulează în prezent:

`jupyter notebook stop`

- Porniți JupyterLab, dacă este instalat, în directorul curent:

`jupyter lab`
