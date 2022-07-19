# calc

> An interactive arbitrary-precision calculator in the terminal.
> More information: <https://github.com/lcn2/calc>.

- Start `calc` in interactive mode:

`calc`

- Perform a calculation in non-interactive mode:

`calc '{{85 * (36 / 4)}}'`

- Perform a calculation without any output formatting (for use with pipes):

`calc -p '{{4/3 * pi() * 5^3}}'`

- Perform a calculation and then switch to [i]nteractive mode:

`calc -i '{{sqrt(2)}}'`

- Start `calc` in a specific permission [m]ode (0 to 7, defaults to 7):

`calc -m {{mode}}`

- View an introduction to `calc`:

`calc help intro`

- View an overview of `calc`:

`calc help overview`

- Open the `calc` manual:

`calc help`
