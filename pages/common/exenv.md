# exenv

> Easily install Elixir versions and manage application environments.
> More information: <https://github.com/mururu/exenv>.

- Display a list of installed versions:

`exenv versions`

- Use a specific version of Elixir across the whole system:

`exenv global {{version}}`

- Use a specific version of Elixir for the current application/project directory:

`exenv local {{version}}`

- Show the currently selected Elixir version:

`exenv {{version}}`

- Install a version of Elixir (requires `elixir-build` plugin <https://github.com/mururu/elixir-build>):

`exenv install {{version}}`
