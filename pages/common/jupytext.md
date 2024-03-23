# jupytext

> Convert Jupyter notebooks to plain text documents, and back again.
> More information: <https://jupytext.readthedocs.io>.

- Turn a notebook into a paired `.ipynb`/`.py` notebook:

`jupytext --set-formats ipynb,py {{notebook.ipynb}}`

- Convert a notebook to a `.py` file:

`jupytext --to py {{notebook.ipynb}}`

- Convert a `.py` file to a notebook with no outputs:

`jupytext --to notebook {{notebook.py}}`

- Convert a `.md` file to a notebook and run it:

`jupytext --to notebook --execute {{notebook.md}}`

- Update the input cells in a notebook and preserve outputs and metadata:

`jupytext --update --to notebook {{notebook.py}}`

- Update all paired representations of a notebook:

`jupytext --sync {{notebook.ipynb}}`
