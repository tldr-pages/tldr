# jupytext

> Instrument pentru conversia blocnotesurilor Jupyter în documente text simplu și înapoi din nou.
> Mai multe informaţii: <https://jupytext.readthedocs.io/en/latest/>

- Transformați un notebook într-un blocnotes `.ipynb`/`.py` asociat:

`jupytext --set-formats ipynb,py {{notebook.ipynb}}`

- Conversia unui notebook într-un fișier `.py`:

`jupytext --to py {{notebook.ipynb}}`

- Conversia unui fișier `.py` într-un notebook fără ieșiri:

`jupytext --to notebook {{notebook.py}}`

- Convertiți un fișier `.md` într-un blocnotes și rulați-l:

`jupytext --to notebook --execute {{notebook.md}}`

- Actualizați celulele de intrare într-un notebook și păstrați ieșirile și metadatele:

`jupytext --update --to notebook {{notebook.py}}`

- Actualizați toate reprezentările asociate ale unui notebook:

`jupytext --sync {{notebook.ipynb}}`
