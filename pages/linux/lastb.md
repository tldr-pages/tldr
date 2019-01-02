# lastb

> Show a listing of last logged in users.

- Show a list of all last logged in users:

`sudo lastb`

- Show a list of all last logged in users since(use `YYYY-MM-DD` or `hh:mm` as time format):

`sudo lastb --since {{time}}`

- Show a list of all last logged in users until(use `YYYY-MM-DD` or `hh:mm` as time format):

`sudo lastb --until {{time}}`

- Show a list of all logged in users at a specific time(use `YYYY-MM-DD` or `hh:mm` as time format):

`sudo lastb --present {{time}}`

- Show a list of all last logged in users and translate the IP into a hostname:

`sudo lastb --dns`
