# composer

> Dependency Manager for PHP.

- Interactively create a composer.json file defining the project's dependencies:

`composer init`

- Create a new project from a given version of an existing package:

`composer create-project {{project_name}} {{/path/to/my/project}} {{version}}`

- Install the packages specified in composer.json file in the current directory:

`composer install`

- Add package as a dependency to the project:

`composer require "{{package_name}}={{package_version}}"`

- List outdated packages:

`composer outdated`

- Update all packages specified in composer.json file:

`composer update`

- Update a single package:

`composer update "{{package_name}}"`
