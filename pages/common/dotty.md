# dotty

> A customizable interactive graph editor for the X Window System.
> Note: This tool has been deprecated, but this entry is retained to aid anyone still using it.
> More information: <https://graphviz.org/pdf/dotty.1.pdf>.

- Open a graph file (`.gv` or `.dot`) in the Dotty editor:

`dotty {{path/to/graph.gv}}`

- Start Dotty with the [V]ersion information displayed:

`dotty -V`

- Set the [l]ayout [m]ode to synchronous or asynchronous:

`dotty -lm {{sync|async}} {{path/to/graph.gv}}`

- Set the m[e]ssage verbosity [l]evel (`0` for minimal, `1` for detailed):

`dotty -el {{0|1}} {{path/to/graph.gv}}`
