# virtualenv

> Virtuális izolált Python-környezetek létrehozása. További információ: <https://virtualenv.pypa.io/>.

- Új környezet létrehozása:

`virtualenv {{path/to/venv}}`

- A prompt előtag testreszabása:

`virtualenv --prompt={{prompt_prefix}} {{path/to/venv}}`

- A Python más verziójának használata a virtualenv segítségével:

`virtualenv --python={{path/to/pythonbin}} {{path/to/venv}}`

- Indítsa el (válassza ki) a környezetet:

`source {{path/to/venv}}/bin/activate`

- Állítsa le a környezetet:

`deactivate`
