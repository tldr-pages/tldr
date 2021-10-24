# unset

> Remove shell variables or functions.
> More information: <https://manned.org/unset>.

- Remove the variable `foo`, or if the variable doesn't exist, remove the function `foo`:

`unset {{foo}}`

- Remove the variables foo and bar:

`unset -v {{foo}} {{bar}}`

- Remove the function my_func:

`unset -f {{my_func}}`
