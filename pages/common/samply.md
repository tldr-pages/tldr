# samply

> Sample and record CPU profiles for analysis.
> More information: <https://github.com/mstange/samply>.

- Record a profile of a command and open it in the browser:

`samply record {{path/to/command arg1 arg2 ...}}`

- Adjust sampling rate:

`samply record --rate {{rate_in_hz}} {{path/to/command arg1 arg2 ...}}`

- Record a profile to a file without opening the browser:

`samply record --save-only --output {{path/to/profile.json}} -- {{path/to/command arg1 arg2 ...}}`

- Load a previously saved profile in the browser:

`samply load {{path/to/profile.json}}`
