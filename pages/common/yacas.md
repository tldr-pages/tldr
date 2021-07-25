# yacas

> Yet Another Computer Algebra System.
> More information: <http://www.yacas.org>.

- Start an interactive console session:

`yacas`

- In the console session, execute a statement:

`In> {{Integrate(x)Cos(x);}}`

- In the console session, display an example:

`In> {{Example();}}`

- Quit from the console session:

`In> {{gquit}}`

- Execute one or more yacas scripts, then exit:

`yacas -pc {{path/to/script1}} {{path/to/script2}}`

- Execute and print the result of one statement, then exit:

`echo "{{Echo( Deriv(x)Cos(1/x) );}}" | yacas -pc /dev/stdin`
