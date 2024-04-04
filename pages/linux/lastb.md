# lastb

> List last logged in users.
> More information: <https://manned.org/lastb>.

- List last logged in users:

`sudo lastb`

- List all last logged in users since a given time:

`sudo lastb --since {{YYYY-MM-DD}}`

- List all last logged in users until a given time:

`sudo lastb --until {{YYYY-MM-DD}}`

- List all logged in users at a specific time:

`sudo lastb --present {{hh:mm}}`

- List all last logged in users and translate the IP into a hostname:

`sudo lastb --dns`
