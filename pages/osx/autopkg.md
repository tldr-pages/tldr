# autopkg

> Automation framework for macOS software packaging and distribution.

- List available recipe identifier:

`autopkg list-recipes`

- Run autopkg recipe:

`autopkg run {{recipe_identifier}}`

- Run autopkg with specified pkg:

`autopkg run {{recipe_identifier}} --pkg {{path/to/downloaded_pkg_or_dmg}}`

- Add a new repo to autopkg:

`autopkg repo-add {{repo_name}}`

- Update one autopkg repo:

`autopkg repo-update {{repo_names}}`

- Update all autopkg repos:

`autopkg repo-update all`

- Search available recipes:

`autopkg search {{application_name}}`

- Display autopkg help:

`autopkg help`
