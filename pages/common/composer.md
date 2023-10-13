# composer

> A package-based dependency manager for PHP projects.
> More information: <https://getcomposer.org/>.

- Interactively create a `composer.json` file:

`composer init`

- Add a package as a dependency for this project, adding an entry to `composer.json`:

`composer require {{user/package}}`

- Install all the dependencies in this project's `composer.json` and create `composer.lock`:

`composer install`

- Uninstall a package from this project, removing it as a dependency from `composer.json` and `composer.lock`:

`composer remove {{user/package}}`

- Update all the dependencies in this project's `composer.json` and note new versions in `composer.lock` file:

`composer update`

- Update only `composer.lock` after updating `composer.json` manually:

`composer update --lock`

- Learn more about why a dependency can't be installed:

`composer why-not {{user/package}}`

- Update composer to its latest version:

`composer self-update`
