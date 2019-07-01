# lastb

> Show a listing of last logged in users.

- Show a list of all last logged in users:

`sudo lastb`

- Show a list of all last logged in users since a given time:

`sudo lastb --since {{YYYY-MM-DD}}`

- Show a list of all last logged in users until a given time:

`sudo lastb --until {{YYYY-MM-DD}}`

- Show a list of all logged in users at a specific time:

`sudo lastb --present {{hh:mm}}`

- Show a list of all last logged in users and translate the IP into a hostname:

`sudo lastb --dns`
