# z

> Tracks your most used directories, based on 'frecency'. After a short learning phase, z will take you to the most 'frecent' directory that matches ALL of the regexes given on the command line, in order.

- cd to most frecent dir matching foo:

`z foo`

- cd to most frecent dir matching foo, then bar:

`z foo bar`

- cd to highest ranked dir matching foo

`z -r foo`

- cd to most recently accessed dir matching foo

`z -t foo`

- list all dirs matching foo (by frecency)

`z -l foo`

- remove the current directory from the datafile

`z -x .`
