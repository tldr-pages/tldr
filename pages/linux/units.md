# units

> Provide the conversion between two units of measure.
> Typing `search {{text}}` in the prompt will display a list of all of the units containing `{{text}}`.
> More information: <https://www.gnu.org/software/units/units.html>.

- Run in interactive mode:

`units`

- Show the conversion between two simple units:

`units {{quarts}} {{tablespoons}}`

- Convert between units with quantities:

`units {{15 pounds}} {{kilograms}}`

- Show the conversion between two compound units:

`units "{{meters / second}}" "{{inches / hour}}"`

- Show the conversion between units with different dimensions:

`units "{{acres}}" "{{ft^2}}"`
