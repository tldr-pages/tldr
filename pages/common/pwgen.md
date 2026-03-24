# pwgen

> Generate pronounceable passwords.
> More information: <https://manned.org/pwgen>.

- Generate 160 random passwords with character length of 8:

`pwgen`

- Generate passwords with character length of 20:

`pwgen 20`

- Generate 10 passwords with character length of 20:

`pwgen 20 10`

- Generate random passwords with symbols:

`pwgen {{[-y|--symbols]}} {{length}} {{count}}`

- Generate secure, hard-to-memorize passwords:

`pwgen {{[-s|--secure]}}`

- Generate password with at least one capital letter in them, specify their length, and how many to generate:

`pwgen {{[-c|--capitalize]}} {{length}} {{count}}`
