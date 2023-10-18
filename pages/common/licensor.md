# licensor

> Write licenses to `stdout`.
> More information: <https://github.com/raftario/licensor>.

- Write the MIT license to a file named `LICENSE`:

`licensor {{MIT}} > {{LICENSE}}`

- Write the MIT license with a [p]laceholder copyright notice to a file named `LICENSE`:

`licensor -p {{MIT}} > {{LICENSE}}`

- Specify a copyright holder named Bobby Tables:

`licensor {{MIT}} {{"Bobby Tables"}} > {{LICENSE}}`

- Specify licence exceptions with a WITH expression:

`licensor "{{Apache-2.0 WITH LLVM-exception}}" > {{LICENSE}}`

- List all available licenses:

`licensor --licenses`

- List all available exceptions:

`licensor --exceptions`
