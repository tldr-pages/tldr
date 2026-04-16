# papermill

> Tool for parameterizing and executing Jupyter Notebooks.
> More information: <https://github.com/nteract/papermill>.

- Execute a notebook and save the output to a new notebook:

`papermill {{input.ipynb}} {{output.ipynb}}`

- Execute a notebook with specific parameters:

`papermill {{input.ipynb}} {{output.ipynb}} -p {{key}} {{value}}`

- Execute a notebook using a YAML file for parameters:

`papermill {{input.ipynb}} {{output.ipynb}} -f {{parameters.yaml}}`

- Execute a notebook and specify a custom kernel:

`papermill {{input.ipynb}} {{output.ipynb}} -k {{python3}}`

- Execute a notebook while injecting parameters via a JSON string:

`papermill {{input.ipynb}} {{output.ipynb}} -b '{"{{key}}": "{{value}}"}'`
