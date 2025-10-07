# vimdot

> Interactively edit Graphviz .dot files using Vim.
> More information: <https://graphviz.org/pdf/vimdot.1.pdf>.

- Open a DOT file for editing:

vimdot example.dot

- Save changes and quit Vim:

:wq

- Render the current graph to PNG and preview:

:!dot -Tpng % -o graph.png && xdg-open graph.png
