# autopkg

> Automation framework for macOS software packaging and distribution.

- List available recipe identifiers:

`autopkg list-recipes`

- Run autopkg recipe:

`autopkg run {{recipe_identifier}}`

- Run autopkg with specified pkg:

`autopkg run {{recipe_identifier}} --pkg {{path/to/downloaded_pkg_or_dmg}}`

- Add a new repo to autopkg:

`autopkg repo-add {{repo_name}}`

- Update an autopkg repo:

`autopkg repo-update {{repo_name}}`

- Update all autopkg repos:

`autopkg repo-update all`

- Search available recipes:

`autopkg search {{application_name}}`

- Display autopkg help:

`autopkg help`
