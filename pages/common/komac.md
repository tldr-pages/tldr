# komac

> Create WinGet manifests for the `winget-pkgs` repository.
> More information: <https://github.com/russellbanks/Komac>.

- Create a new package from scratch:

`komac new {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- Update an existing package with a new version:

`komac update {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe}}`

- Update a package with multiple URLs and automatically submit:

`komac update {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}} {{[-u|--urls]}} {{https://example.com/app.exe https://example.com/app.msi ...}} {{[-s|--submit]}}`

- Remove a version from winget-pkgs:

`komac remove {{Package.Identifier}} {{[-v|--version]}} {{1.2.3}}`

- List all versions for a package:

`komac {{[list|list-versions]}} {{Package.Identifier}}`

- Sync your fork of winget-pkgs with the upstream repository:

`komac {{[sync|sync-fork]}}`

- Update the stored GitHub token:

`komac token {{[add|update]}} {{[-t|--token]}} {{your_github_token}}`

- Generate shell autocompletion script:

`komac {{[complete|autocomplete]}} {{bash|elvish|fish|powershell|zsh}}`
