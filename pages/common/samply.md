# samply

> CPU profiler using the Firefox Profiler UI.
> More information: <https://github.com/mstange/samply>.

- Record a profile of a command and open it in the browser:

`samply record {{./yourcommand yourargs}}`

- Adjust sampling rate:

`samply record --rate {{rate in Hz}} {{./yourcommand yourargs}} `

- Record a profile to a file without opening the browser:

`samply record --save-only --output {{path/to/profile.json}} -- {{./yourcommand yourargs}}`

- Load a previously saved profile in the browser:

`samply load {{path/to/profile.json}}`
