# yacas

> Yet Another Computer Algebra System.
> More information: <http://www.yacas.org>.

- Start an interactive `yacas` session:

`yacas`

- In the `yacas` session, execute a statement:

`In> {{Integrate(x)Cos(x);}}`

- In the `yacas` session, display an example:

`In> {{Example();}}`

- Quit from the `yacas` session:

`In> {{quit}}`

- Execute one or more `yacas` scripts (without terminal or prompts), then exit:

`yacas -p -c {{path/to/script1}} {{path/to/script2}}`

- Execute and print the result of one statement, then exit:

`echo "{{Echo( Deriv(x)Cos(1/x) );}}" | yacas -p -c /dev/stdin`
