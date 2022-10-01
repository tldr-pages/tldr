# PHP-CS-Fixer

> Automatic coding style fixer for PHP.
> More information: <https://github.com/FriendsOfPHP/PHP-CS-Fixer>.

- Execute code style fixing in the current directory:

`php-cs-fixer fix`

- Execute code style fixing for a specific directory:

`php-cs-fixer fix {{path/to/directory}}`

- Execute code style linting without applying changes:

`php-cs-fixer fix --dry-run`

- Execute code style fixes using specific rules:

`php-cs-fixer fix --rules={{rules}}`

- Display the rules that have been applied:

`php-cs-fixer fix --verbose`

- Output the results in a different format:

`php-cs-fixer fix --format={{txt|json|xml|checkstyle|junit|gitlab}}`

- Display files that require fixing:

`php-cs-fixer list-files`

- Describe a rule or ruleset:

`php-cs-fixer describe {{rule}}`
