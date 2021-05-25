# direnv

> Shell extension to load and unload environment variables depending on the current directory.
> More information: <https://github.com/direnv/direnv>.

- Grant direnv permission to load the specified `.envrc`:

`direnv allow`

- Revoke the authorization of a given `.envrc`:

`direnv deny`

- Edit the `.envrc` file in the default text editor and reload the environment on exit:

`direnv edit .`

- Trigger a reload of the environment:

`direnv reload`

- Print some debug status information:

`direnv status`
