# tox

> Automate Python testing across multiple Python versions.
> Use tox.ini to configure environments and test command.

- Run tests on all test environments:

`tox`

- Create tox.ini configuration:

`tox-quickstart`

- List available environments:

`tox --listenvs-all`

- Run tests on a specific environment (e.g. python 3.6):

`tox -e py36`

- Force recreation of virtual environment:

`tox --recreate -e py27`
