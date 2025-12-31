# tofu fmt

> Format configuration according to OpenTofu language style conventions.
> More information: <https://opentofu.org/docs/cli/commands/fmt/>.

- Format the configuration in the current directory:

`tofu fmt`

- Format the configuration in the current directory and subdirectories:

`tofu fmt -recursive`

- Display diffs of formatting changes:

`tofu fmt -diff`

- Do not list files that were formatted to `stdout`:

`tofu fmt -list=false`
