# turbo

> High-performance build system for JavaScript and TypeScript codebases.
> See also: `nx`.
> More information: <https://turborepo.org/docs/reference/command-line-reference>.

- Log in using the default web browser with a Vercel account:

`turbo login`

- Link the current directory to a Vercel organization and enable remote caching:

`turbo link`

- Build the current project:

`turbo run build`

- Run a task without concurrency:

`turbo run {{task_name}} --concurrency={{1}}`

- Run a task ignoring cached artifacts and forcibly re-execute all tasks:

`turbo run {{task_name}} --force`

- Run a task in parallel across packages:

`turbo run {{task_name}} --parallel --no-cache`

- Unlink the current directory from your Vercel organization and disable Remote Caching:

`turbo unlink`

- Generate a Dot graph of a specific task execution (the output file format can be controlled with the filename):

`turbo run {{task_name}} --graph={{path/to/file}}.{{html|jpg|json|pdf|png|svg}}`
