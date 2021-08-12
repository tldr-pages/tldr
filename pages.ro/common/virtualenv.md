# virtualenv

> Creați medii Python izolate virtuale.
> Mai multe informaţii: <https://virtualenv.pypa.io/>

- Creați un mediu nou:

`virtualenv {{path/to/venv}}`

- Particularizarea prefixului prompt:

`virtualenv --prompt={{prompt_prefix}} {{path/to/venv}}`

- Utilizați o versiune diferită de Python cu virtualenv:

`virtualenv --python={{path/to/pythonbin}} {{path/to/venv}}`

- Porniți (selectați) mediul:

`source {{path/to/venv}}/bin/activate`

- Opriţi mediul:

`deactivate`
