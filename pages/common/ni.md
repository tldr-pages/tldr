# ni

> Use the right package manager (npm, yarn, pnpm, bun, or deno) automatically.
> Detect the current project's lockfile to run the corresponding commands.
> More information: <https://github.com/antfu-collective/ni>.

- Install all dependencies (equivalent to `npm install`, `yarn install`, etc.):

`ni`

- Install a specific package (-D for dev dependencies):

`ni {{package}} [-D]`

- Run a `package.json` script (interactively select if no script is provided):

`nr {{script}}`

- Download and execute a command from a package (equivalent to `npx`, `pnpm dlx`, etc.):

`nlx {{package}}`

- Upgrade dependencies:

`nup`

- Uninstall a package:

`nun {{package}}`

- Clean install dependencies (equivalent to `npm ci`, etc.):

`nci`

- Use the current package manager agent directly for arbitrary commands:

`na {{command}}`
