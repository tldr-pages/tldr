# dnf search

> Search for packages in repositories using DNF package manager.
> More information: <https://dnf.readthedocs.io/en/latest/command_ref.html#search-command>.

- Search for packages by name:

`dnf search {{package_name}}`

- Search for packages by name or summary:

`dnf search {{keyword}}`

- Search in all fields including description:

`dnf search --all {{keyword}}`

- Search for packages with exact name match:

`dnf search --exact {{package_name}}`

- Search for packages in a specific repository:

`dnf search --repo {{repository_name}} {{package_name}}`

- Search for packages and show detailed information:

`dnf search --verbose {{package_name}}`

- Search for packages containing specific files:

`dnf search --file {{/path/to/file}}`

- Search for packages but only display package names:

`dnf search --quiet {{package_name}}`
