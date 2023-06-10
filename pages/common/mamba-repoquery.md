# mamba repoquery

> Efficiently query conda and mamba package repositories and package dependencies.
> More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>.

- Search for all available versions of a particular package:

`mamba repoquery search {{package}}`

- Search for all packages satisfying specific constraints:

`mamba repoquery search {{sphinx<5}}`

- List the dependencies of a package installed in the currently activated environment, in a tree format:

`mamba repoquery depends --tree {{scipy}}`

- Print packages in the current environment that require a particular package to be installed (i.e. inverse of `depends`):

`mamba repoquery whoneeds {{ipython}}`
