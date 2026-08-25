# grabc

> A tool to identify a pixel color of an X Window.
> More information: <https://manned.org/grabc>.

- Pick a pixel and print its color in hexadecimal:

`grabc`

- Pick a pixel and print its RGB values:

`grabc -rgb`

- Enable debug messages:

`grabc -d`

- Print the hex ID of the clicked window:

`grabc -W`

- Pick a pixel at a specific location on a specific window:

`grabc -w {{window_id}} -l +{{x}}+{{y}}`

- Print all 16 bits of color (default prints high 8 bits):

`grabc -a`

- Display help:

`grabc -h`
