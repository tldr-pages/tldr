# poetry-python

> Manage Python versions through Poetry.
> See also: `asdf`.
> More information: <https://python-poetry.org/docs/cli/#python>.

- Install the specified Python version:

`poetry python install {{3.13.1}}`

- List all Python versions managed by System or Poetry:

`poetry python list`

- List all Python versions managed by Poetry:

`poetry python list --managed`

- Remove the specified Python version (if managed by Poetry):

`poetry python remove {{3.13.1}}`
