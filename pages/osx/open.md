# open

> Opens files, directories and applications.
> More information: <https://ss64.com/osx/open.html>.

- Open a file with the associated application:

`open {{file.ext}}`

- Run a graphical macOS application:

`open -a "{{Application}}"`

- Run a graphical macOS app based on the bundle identifier (refer to `osascript` for an easy way to get this):

`open -b {{com.domain.application}}`

- Open the current directory in Finder:

`open .`

- Reveal a file in Finder:

`open -R {{path/to/file}}`

- Open all the files of a given extension in the current directory with the associated application:

`open {{*.ext}}`
