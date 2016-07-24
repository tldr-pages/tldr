# composer

> Dependency Manager for PHP.

- Interactively create a composer.json file:

`composer init`

- Create new project from an existing package:

`composer create-project {{project_name}} {{target_path}} {{version}}`

- Install packages specified in composer.json file:

`composer install`

- Update packages specified in composer.json file:

`composer update`

- Add package as a dependency to the project:

`composer require "{{package_name}}={{package_version}}"`

- Update a single package:

`composer update "{{package_name}}"`

- List outdated packages:

`composer outdated`
