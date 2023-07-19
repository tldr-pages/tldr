# conda install

> Install packages into an existing conda environment.
> More information: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

- Install a single package into the currently active conda environment:

`conda install {{package_name}}`

- Install a single package into the currently active conda environment using channel conda-forge:

`conda install -c conda-forge {{package_name}}`

- Install a single package into the currently active conda environment using channel conda-forge and ignoring other channels:

`conda install -c conda-forge --override-channels {{package_name}}`

- Install multiple packages:

`conda install {{package_name1}} {{package_name2}}`

- Install a specific version of a package:

`conda install {{package_name}}={{version}}`

- Install a package into a specific environment:

`conda install --name {{environment_name}} {{package_name}}`

- Update a package in the current environment:

`conda install --upgrade {{package_name}}`

- Install a package and agree to the transactions without prompting:

`conda install --yes {{package_name}}`
