# pants

> Fast, scalable, user-friendly, open-source build and developer workflow tool.
> More information: <https://www.pantsbuild.org/2.20/docs/using-pants/command-line-help>.

- List all targets:

`pants list ::`

- Run all tests:

`pants test ::`

- Fix, format, and lint only uncommitted files:

`pants --changed-since=HEAD fix fmt lint`

- Typecheck only uncommitted files and their dependents:

`pants --changed-since=HEAD --changed-dependents=transitive check`

- Create a distributable package for the specified target:

`pants package {{path/to/directory:target-name}}`

- Auto-generate BUILD file targets for new source files:

`pants tailor ::`

- Display help:

`pants help`
