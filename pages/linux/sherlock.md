# sherlock

> Find usernames across social networks.
> More information: <https://github.com/sherlock-project/sherlock>.

- Search for a specific username on social networks saving the results to a file:

`sherlock {{username}} --output {{path/to/file}}`

- Search for specific usernames on social networks saving the results into a directory:

`sherlock {{username1 username2 ...}} --folderoutput {{path/to/directory}}`

- Search for a specific username on social networks using the Tor network:

`sherlock --tor {{username}}`

- Make requests over Tor with a new Tor circuit after each request:

`sherlock --unique-tor {{username}}`

- Search for a specific username on social networks using a proxy:

`sherlock {{username}} --proxy {{proxy_url}}`

- Search for a specific username on social networks and open results in the default web browser:

`sherlock {{username}} --browse`

- Display help:

`sherlock --help`
