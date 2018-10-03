# fisher

> Fisher, a fish-shell plugin manager
> Install plugins by name or from a managed `fishfile` for bundled installs

- Install one or more plugins:

`fisher {{plugin1}} {{plugin2}}`

- Install from a GitHub gist:

`fisher {{gist_url}}`

- Install multiple plugins from the `fishfile`:

`$EDITOR ~/.config/fish/fishfile; fisher`

- List installed plugins:

`fisher ls`

- Show available plugins:

`fisher ls-remote`

- Update plugins:

`fisher up`

- Remove plugins:

`fisher rm {{plugin1}} {{plugin2}}`
