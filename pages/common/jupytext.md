# jupytext

> Convert Jupyter notebooks to plain text documents, and back again.
> More information: <https://jupytext.readthedocs.io/en/latest/using-cli.html>.

- Turn a notebook into a paired `.ipynb`/`.py` notebook:

`jupytext --set-formats ipynb,py {{path/to/notebook}}.ipynb`

- Convert a notebook to a `.py` file:

`jupytext --to py {{path/to/notebook}}.ipynb`

- Convert a `.py` file to a notebook with no outputs:

`jupytext --to notebook {{path/to/notebook}}.py`

- Convert a `.md` file to a notebook and run it:

`jupytext --to notebook --execute {{path/to/notebook}}.md`

- Update the input cells in a notebook and preserve outputs and metadata:

`jupytext --update --to notebook {{path/to/notebook}}.py`

- Update all paired representations of a notebook:

`jupytext {{[-s|--sync]}} {{path/to/notebook}}.ipynb`
