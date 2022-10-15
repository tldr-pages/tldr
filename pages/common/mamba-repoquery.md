# mamba repoquery

> Efficiently query package repositories and package dependencies.
> More information: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>.

- Search for all available versions of a particular package:

`mamba repoquery search {{package_name}}`

- Search for all packages satisfying constraints on this query:

`mamba repoquery search {{sphinx<5}}`

- List the dependencies of a package installed in the currently activated environment, in a tree format:

`mamba repoquery depends --tree {{scipy}}`

- Look for other packages who need a particular package installed in the currently activated environment (i.e., inverse of `depends`):

`mamba repoquery whoneeds {{ipython}}`
