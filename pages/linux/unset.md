# unset

> Remove shell variables or functions.

- Remove the variable or function foo (only removes functions if the variable doesn't exist):

`unset {{foo}}`

- Remove the variables foo and bar:

`unset -v {{foo}} {{bar}}`

- Remove the function my_func:

`unset -f {{my_func}}`
