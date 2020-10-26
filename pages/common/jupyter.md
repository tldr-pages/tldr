# jupyter

> Web application to create and share documents that contain code, visualizations and notes.
> Primarily used for data analysis, scientific computing and machine learning.
> More information: <https://jupyter.org>.

- Start a Jupyter notebook server in the current directory:

`jupyter notebook`

- Open a specific Jupyter notebook:

`jupyter notebook {{example.ipynb}}`

- Export a specific Jupyter notebook into another format:

`jupyter nbconvert --to {{html|markdown|pdf|script}} {{example.ipynb}}`

- Start a server on a specific port:

`jupyter notebook --port={{port}}`

- List currently running notebook servers:

`jupyter notebook list`

- Stop the currently running server:

`jupyter notebook stop`

- Start JupyterLab, if installed, in the current directory:

`jupyter lab`
