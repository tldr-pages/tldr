# gitlint

> Git commit message linter checks your commit messages for style.
> More information: <https://jorisroovers.com/gitlint/>.

- Check the last commit message:

`gitlint`

- Lint a specific range of commits:

`gitlint --commits {{single_refspec_argument}}`

- Use a directory or Python module with extra user-defined rules:

`gitlint --extra-path {{path/to/directory}}`

- Start a specific CI job:

`gitlint --target {{path/to/target_directory}}`

- Lint a commit message from a specific file:

`gitlint --msg-filename {{path/to/file}}`

- Read staged commit meta-info from the local repository:

`gitlint --staged`
