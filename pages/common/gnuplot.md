# gnuplot

> Optionally interactive graph plotter that outputs in several formats.

- Start the interactive graph plotting shell:

`gnuplot`

- Plot the graph for the specified graph definition file:

`gnuplot {{path/to/definition.plt}}`

- Set the output format by executing a command before loading the definition file (in this case output a PNG to stdout):

`gnuplot -e "{{set terminal png size 1024,768}}" {{path/to/definition.plt}} >{{path/to/output_graph.png}}`

- Persist the graph plot preview window after gnuplot exits:

`gnuplot --persist {{path/to/definition.plt}}`
