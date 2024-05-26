# lstopo

> Show the hardware topology of the system.
> More information: <https://manned.org/lstopo>.

- Show the summarized system topology in a graphical window (or print to console if no graphical display is available):

`lstopo`

- Show the full system topology without summarizations:

`lstopo --no-factorize`

- Show the summarized system topology with only [p]hysical indices (i.e. as seen by the OS):

`lstopo --physical`

- Write the full system topology to a file in the specified format:

`lstopo --no-factorize --output-format {{console|ascii|tex|fig|svg|pdf|ps|png|xml}} {{path/to/file}}`

- Output in monochrome or greyscale:

`lstopo --palette {{none|grey}}`
