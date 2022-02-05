# ugrep

> Ultra fast search tool with query UI, fuzzy search and more.
> Try also `ugrep --help {{something}}`.
> More information: <https://github.com/Genivia/ugrep>

- Start a [q]uery TUI to search files in the working directory recursively (CTRL-Z for help):

`ugrep -Q`

- Search the working directory recursively for files containing a regex pattern:

`ugrep "{{pattern}}"`

- Search for a case-[i]nsensitive regex pattern:

`ugrep -i "{{pattern}}"`

- [L]ist the matching files:

`ugrep -l "{{pattern}}"`

- Search compressed files, [z]ip and tar archives recursively:

`ugrep -z "{{pattern}}"`

- Fu[z]zy search files with up to 3 extra, missing or mismatching characters in the pattern:

`ugrep -Z3 "{{pattern}}"`

- Search only files whose filenames match a [g]lob pattern:

`ugrep -g "{{glob}}" "{{pattern}}"`

- Search only files of a specific [t]ype or another type and not a type:

`ugrep -t {{type}},{{or_type}},^{{not_type}} "{{pattern}}"`
