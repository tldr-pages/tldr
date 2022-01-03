# sherlock

> Find usernames across social networks.

- Display help:

`sherlock --help`

- Save result to file (if using single username):

`sherlock {{username}} --output {{filename}}`

- Save result to folder (if using multiple usernames):

`sherlock {{[usernames]}} --folderoutput {{foldername}}`

- Make requests over Tor:

`sherlock --tor {{username}}`

- Make requests over Tor with new Tor circuit after each request:

`sherlock --unique-tor {{username}}`

- Make requests over a proxy:

`sherlock {{username}} --proxy {{proxyurl}}`

- Browse to all results on default browser:

`sherlock {{username}} --browse`

