# mux

> Intercept and multiplex streams of input events.
> More information: <https://gitlab.com/interception/linux/tools/-/tree/master#mux>.

- Create a new muxer with a specified name:

`mux -c {{muxer_name1 muxer_name2 ...}}`

- Set the muxer's internal queue size (default is 100):

`mux -s {{size}}`

- Read input from a named muxer (can be repeated in "switch mode"):

`mux -i {{input_muxer_name}}`

- Write output to a named muxer (can be repeated):

`mux -o {{output_muxer_name}}`
