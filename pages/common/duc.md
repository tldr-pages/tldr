# duc

> Duc is a collection of tools for indexing, inspecting and visualizing disk usage. Duc maintains a database of accumulated sizes of directories of the file system, allowing queries this database, or create fancy graphs to show where data is.
> More information: <https://duc.zevv.nl/>.

- Index the /usr directory, writing to the default database location ~/.duc.db:

`duc index {{/usr}}`

- List all files and directories under /usr/local, showing relative file sizes in a [g]raph:

`duc ls -Fg {{/usr/local}}`

- List all files and directories under /usr/local using treeview recursively:

`duc ls -Fg -R {{/usr/local}}`

- Start the graphical interface to explore the file system using sunburst graphs:

`duc gui {{/usr}}`

- Run the ncurses console interface to explore the file system:

`duc ui {{/usr}}`

- Dump database info:

`duc info`
