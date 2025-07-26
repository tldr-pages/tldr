# dnf config-manager

> Configure DNF repositories.
> Part of the `dnf-plugins-core` package.
> More info: <https://dnf.readthedocs.io/en/latest/command_ref.html#config-manager>

- Enable a specific repository:
`dnf config-manager --set-enabled {{repo_id}}`

- Disable a specific repository:
`dnf config-manager --set-disabled {{repo_id}}`

- Add a new repository from a URL:
`dnf config-manager --add-repo {{https://example.com/repo.repo}}`