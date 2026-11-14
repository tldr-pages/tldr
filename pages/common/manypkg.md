# manypkg

> Linter and fixer for package manifest files in Yarn, Bolt, and pnpm monorepos.
> More information: <https://github.com/Thinkmill/manypkg>.

- Check all packages in the monorepo for dependency and configuration errors:

`manypkg check`

- Automatically fix all fixable package manifest issues in the monorepo:

`manypkg fix`

- Run a command or script in a specific workspace package:

`manypkg run {{package_name}} {{script_name}}`

- Upgrade a dependency across every package in the monorepo that uses it:

`manypkg upgrade {{dependency_name}}`
