# z

> Tracks your most used directories, based on 'frecency'. After a short learning phase, z will take you to the most 'frecent' directory that matches ALL of the regexes given on the command line, in order.

- Change directory to most frecent dir matching foo:

`z foo`

- Change directory to most frecent dir matching foo, then bar:

`z foo bar`

- Change directory to highest ranked dir matching foo:

`z -r foo`

- Change directory to most recently accessed dir matching foo:

`z -t foo`

- List all dirs matching foo (by frecency):

`z -l foo`

- Remove the current directory from the datafile:

`z -x .`
