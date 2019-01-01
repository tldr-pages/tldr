# tox

> Automate Python testing across multiple Python versions.
> Use tox.ini to configure environments and test command.

- Run tests on all test environments:

`tox`

- Create a tox.ini configuration:

`tox-quickstart`

- List the available environments:

`tox --listenvs-all`

- Run tests on a specific environment (e.g. python 3.6):

`tox -e {{py36}}`

- Force the virtual environment to be recreated:

`tox --recreate -e {{py27}}`
