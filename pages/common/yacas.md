# yacas

> Yet Another Computer Algebra System.
> More information: <http://www.yacas.org>.

- Start an interactive console session:

`yacas`

- In the console session, execute a statement:

`In> {{Integrate(x)Cos(x)}};`
`Out> {{Sin(x)}}`

- In the console session, display an example:

`In> Example();`

- Quit from the console session:

`In> quit`
`Quitting...`

- Execute a yacas script, then exit:

`yacas -pc {{path/to/script}}`

- Execute and print the result of one statement:

`echo "Echo( {{Deriv(x)Cos(1/x)}} );" | yacas -pc /dev/stdin`
