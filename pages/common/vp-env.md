# vp env

> Manage Node.js and package manager runtime environments for Vite+.
> More information: <https://viteplus.dev/guide/env>.

- Create or update shims for Node.js and package managers:

`vp env setup`

- Display the currently resolved environment and runtime versions:

`vp env current`

- Activate a specific Node.js version in the current shell session:

`vp env use {{node_version}}`

- Pin Node.js or a package manager version for the current project:

`vp env pin {{node_version|package_manager@version}}`

- Remove project environment pins:

`vp env unpin`

- Run diagnostics and verify environment configuration:

`vp env doctor`

- Execute a command within a specific Node.js or package manager environment:

`vp env exec --node {{version}} {{command}}`

- Remove all unused managed runtime versions:

`vp env clean`
