# duc

> A collection of tools for indexing, inspecting and visualizing disk usage.
> Duc maintains a database of accumulated sizes of directories in the file system, allowing to query this database, or creating fancy graphs to show where data is.
> More information: <https://duc.zevv.nl/>.

- Index the `/usr` directory, writing to the default database location `~/.duc.db`:

`duc index {{/usr}}`

- List all files and directories under `/usr/local`, showing relative file sizes in a [g]raph:

`duc ls --classify --graph {{/usr/local}}`

- List all files and directories under `/usr/local` using treeview recursively:

`duc ls --classify --graph --recursive {{/usr/local}}`

- Start the graphical interface to explore the file system using sunburst graphs:

`duc gui {{/usr}}`

- Run the ncurses console interface to explore the file system:

`duc ui {{/usr}}`

- Dump database info:

`duc info`
