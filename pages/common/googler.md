# googler

> Search Google from command-line.
> More information: <https://github.com/jarun/googler>.

- Search Google for a keyword:

`googler {{keyword}}`

- Search Google and open the first result in web browser:

`googler {{[-j|--first]}} {{keyword}}`

- Show `n` search results (default: 10):

`googler {{[-n|--count]}} {{n}} {{keyword}}`

- Disable automatic spelling correction:

`googler {{[-x|--exact]}} {{keyword}}`

- Search one site for a keyword:

`googler {{[-w|--site]}} {{site}} {{keyword}}`

- Show Google search result in JSON format:

`googler --json {{keyword}}`

- Perform in-place self-upgrade:

`googler {{[-u|--upgrade]}}`

- Display help in interactive mode:

`<?>`
