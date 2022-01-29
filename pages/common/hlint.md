# hlint

> Haskell source code suggestions.
> more information: <https://github.com/ndmitchell/hlint>

- Display all hints in the standard output.

`hlint {{path/to/file/or/dir}}`

- Display all but ignored hints in the standard output.

`hlint {{path/to/file/or/dir}} --ignore="Message of hint to ignore"`

- Generate {{report.html}} containing a list of all issues.

`hlint {{path/to/file/or/dir}} --report`

- Generate a settings file ignoring all the hints currently outstanding.

`hlint {{path/to/file/or/dir}} --default > .hlint.yaml`
