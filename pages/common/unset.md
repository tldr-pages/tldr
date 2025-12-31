# unset

> Remove shell variables or functions.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-unset>.

- Remove variable, or if the variable doesn't exist, remove the function of the same name:

`unset {{variable}}`

- Remove variables:

`unset -v {{variable1 variable2 ...}}`

- Remove the function:

`unset -f {{function_name1 function_name2}}`
