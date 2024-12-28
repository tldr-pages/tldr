# ppmdraw

> Draw lines, text and more on a PPM image by executing a script.
> Documentation on the utilized scripting language can be found by following the link below.
> More information: <https://netpbm.sourceforge.net/doc/ppmdraw.html>.

- Draw on the specified PPM image by executing the supplied script:

`ppmdraw -script '{{setpos 50 50; text_here "hello!"; }}' {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Draw on the specified PPM image by executing the script in the specified file:

`ppmdraw -scriptfile {{path/to/script}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
