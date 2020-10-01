# direnv

> Direnv is an extension for your shell. It augments existing shells with a new feature that can load and unload environment variables depending on the current directory.
> More information: <https://github.com/direnv/direnv>.

- Grant direnv to load the given .envrc:

`direnv allow`

- Revoke the authorization of a given .envrc:

`direnv deny`

- Edit .envrc file into an $EDITOR and reload env afterwards:

`direnv allow`

- Trigger an env reload:

`direnv reload`

- Print some debug status information:

`direnv status`
