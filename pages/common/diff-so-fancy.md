# diff-so-fancy

> Colorize `diff` output in a more human readable way.
> More information: <https://github.com/so-fancy/diff-so-fancy#-usage>.

- Colorize `diff`:

`diff {{[-u|--unified]}} {{path/to/file1}} {{path/to/file2}} | diff-so-fancy`

- Set `diff-so-fancy` to colorize the output when Git compares commits:

`git config --global interactive.diffFilter "diff-so-fancy --patch"`
