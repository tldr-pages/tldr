# vf

> VirtualFish is a fish shell tool for managing Python virtual environments.
> More information: <https://virtualfish.readthedocs.io/en/latest/>.

- Create a virtual environment:

`vf new {{virtualenv_name}}`

- Create a virtual environment for a specific Python version:

`vf new --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- Activate and use the specified virtual environment:

`vf activate {{virtualenv_name}}`

- Connect the current virtualenv to the current directory, so that it is activated automatically as soon as you enter it (and deactivated as soon as you leave):

`vf connect`

- Deactivate the current virtual environment:

`vf deactivate`

- List all virtual environments:

`vf ls`

- Remove a virtual environment:

`vf rm {{virtualenv_name}}`

- Display help:

`vf help`
