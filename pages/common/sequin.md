# sequin

> Make ANSI escape sequences human-readable.
> Useful for debugging, learning, or inspecting terminal output.
> More information: <https://github.com/charmbracelet/sequin>.

- Describe ANSI escape sequences from a string:

`printf "{{\x1b[38;5;4mCiao, \x1b[1;7mBaby.\x1b[0m\n}}" | sequin`

- Inspect colorized output from another command (e.g., `ls`):

`ls -l --color=always | sequin`

- Examine a file containing ANSI sequences (e.g., a TUI golden file):

`cat {{./testdata/MyCuteApp.golden}} | sequin`

- Execute a command directly within a fake TTY to inspect its output:

`sequin -- {{ls -l go.*}}`

- Highlight raw ANSI sequences inline for easier reading:

`git -c status.color=always status -sb | sequin -r`
