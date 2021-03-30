# units

> Provide the conversion between two units of measure.
> More information: <https://www.gnu.org/software/units/>.

- Run in interactive mode:

`units`

- List all units containing a specific string in interactive mode:

`search {{string}}`

- Show the conversion between two simple units:

`units {{quarts}} {{tablespoons}}`

- Convert between units with quantities:

`units "{{15 pounds}}" {{kilograms}}`

- Show the conversion between two compound units:

`units "{{meters / second}}" "{{inches / hour}}"`

- Show the conversion between units with different dimensions:

`units "{{acres}}" "{{ft^2}}"`

- Show the conversion of byte multipliers:

`units "{{15 megabytes}}" {{bytes}}`
