# dotty

> A customizable interactive graph editor for the X Window System.
> Note: The dotty tool has been depracated, but this entry is retained to aid anyone still using it.
> More information: <https://graphviz.org/pdf/dotty.1.pdf>.

- Open a graph file (.gv or .dot) in the Dotty editor:

`dotty {{path/to/graph.gv}}`

- Start Dotty with the version information displayed:

`dotty -V`

- Set the layout mode to synchronous (`sync`) or asynchronous (`async`):

`dotty -lmmode {{sync|async}} {{path/to/graph.gv}}`

- Set the message verbosity level (`0` for minimal, `1` for detailed):

`dotty -ellev {{1}} {{path/to/graph.gv}}`
