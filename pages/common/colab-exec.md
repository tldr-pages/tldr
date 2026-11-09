# colab exec

> Execute code in an active Google Colab session.
> More information: <https://github.com/googlecolab/google-colab-cli#execution>.

- Execute code provided via `stdin`:

`echo "{{print('Hello from Colab')}}" | colab exec`

- Execute a local Python script in the active session:

`colab exec {{[-f|--file]}} {{path/to/script.py}}`

- Execute a local Jupyter notebook in a specific named session:

`colab exec {{[-s|--session]}} {{session_name}} {{[-f|--file]}} {{path/to/notebook.ipynb}}`

- Execute a script and save generated plots to an image file:

`colab exec {{[-f|--file]}} {{path/to/script.py}} --output-image {{path/to/plot.png}}`

- Execute code with a custom timeout in seconds:

`colab exec {{[-f|--file]}} {{path/to/script.py}} --timeout {{60.0}}`
