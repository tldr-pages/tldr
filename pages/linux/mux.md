# mux

> A utility for multiplexing streams of input events.
> More information: <https://gitlab.com/interception/linux/tools/-/blob/master/mux.cpp?ref_type=heads>.

- Create a new muxer with a specified name (can be repeated to create multiple):

`mux -c {{muxer_name}}`

- Set the muxer's internal queue size (default is 100):

`mux -size {{size}}`

- Read input from a named muxer (can be repeated in "switch mode"):

`mux -i {{input_muxer_name}}`

- Write output to a named muxer (can be repeated):

`mux -o {{output_muxer_name}}`
