# conda install

> Install packages into an existing conda environment.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

- Install one or more package into the currently active conda environment:

`conda install {{package1 package2 ...}}`

- Install a single package into the currently active conda environment using channel conda-forge:

`conda install -c conda-forge {{package}}`

- Install a single package into the currently active conda environment using channel conda-forge and ignoring other channels:

`conda install -c conda-forge --override-channels {{package}}`

- Install a specific version of a package:

`conda install {{package}}={{version}}`

- Install a package into a specific environment:

`conda install --name {{environment}} {{package}}`

- Update a package in the current environment:

`conda install --upgrade {{package}}`

- Install a package and agree to the transactions without prompting:

`conda install --yes {{package}}`
