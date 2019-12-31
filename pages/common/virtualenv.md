# virtualenv

> Create virtual isolated Python environments.
> More information: <https://virtualenv.pypa.io/>.

- Create a new environment:

`virtualenv {{path/to/venv}}`

- Customize the prompt prefix:

`virtualenv --prompt={{prompt_prefix}} {{path/to/venv}}`

- Use a different version of Python with virtualenv:

`virtualenv --python={{path/to/pythonbin}} {{path/to/venv}}`

- Start (select) the environment:

`source {{path/to/venv}}/bin/activate`

- Stop the environment:

`deactivate`
