# virtualenvwrapper

> Group of simple wrapper commands for Python's `virtualenv` tool. 
> More information: <http://virtualenvwrapper.readthedocs.org>.

- Create a new Python `virtualenv`; It will be created in `$WORKON_HOME`:

`mkvirtualenv {{virtual_env_name}}`

- Create a `virtualenv` for a specific Python version:

`mkvirtualenv --python {{/usr/local/bin/python2.7}} {{virtual_env_name}}`

- Activate or use a different `virtualenv`:

`workon {{virtual_env_name}}`

- Stop the `virtualenv`:

`deactivate`

- List all virtual environments:

`lsvirtualenv`

- Remove a `virtualenv`:

`rmvirtualenv {{virtual_env_name}}`

- Get summary of all virtualenvwrapper commands:

`virtualenvwrapper`
