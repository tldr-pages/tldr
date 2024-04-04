# open

> Opens files, directories and applications.
> More information: <https://keith.github.io/xcode-man-pages/open.1.html>.

- Open a file with the associated application:

`open {{file.ext}}`

- Run a graphical macOS [a]pplication:

`open -a "{{Application}}"`

- Run a graphical macOS app based on the [b]undle identifier (refer to `osascript` for an easy way to get this):

`open -b {{com.domain.application}}`

- Open the current directory in Finder:

`open .`

- [R]eveal a file in Finder:

`open -R {{path/to/file}}`

- Open all the files of a given extension in the current directory with the associated application:

`open {{*.ext}}`

- Open a [n]ew instance of an application specified via [b]undle identifier:

`open -n -b {{com.domain.application}}`
