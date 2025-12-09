# rnm

> Bulk Rename Utility.
> More information: <https://github.com/neurobin/rnm#basic-options>.

- Replace a search string with a replacement string in filenames:

`rnm -ss {{old}} -rs {{new}} {{path/to/directory}}`

- Use a fixed (literal) search and replace string instead of `regex`:

`rnm -ssf {{old}} -rs {{new}} {{path/to/files}}`

- Add an auto-incremented index to filenames starting from 1:

`rnm -i 1 -inc 1 -rs {{_}} {{path/to/files}}`

- Rename files using a list of new names from a text file:

`rnm -ns/f {{path/to/names.txt}} {{path/to/files}}`

- Rename only files (ignoring directories and links):

`rnm -fo -ss {{pattern}} -rs {{replacement}} {{path/to/files}}`

- Sort input files by modification time before renaming:

`rnm -s/mt -ss {{pattern}} -rs {{replacement}} {{path/to/files}}`

- Run a simulation without making actual changes:

`rnm -sim -ss {{pattern}} -rs {{replacement}} {{path/to/files}}`

- Undo the last renaming operation:

`rnm -u`
