# perldoc

> Look up Perl documentation in `.pod` format.
> More information: <https://perldoc.perl.org/perldoc>.

- View documentation for a builtin [f]unction, a [v]ariable or an [a]PI:

`perldoc -{{f|v|a}} {{name}}`

- Search in the question headings of Perl FAQ:

`perldoc -q {{regex}}`

- Send output directly to `stdout` (by default, it is send to a pager):

`perldoc -T {{page|module|program|URL}}`

- Specify the language code of the desired translation:

`perldoc -L {{language_code}} {{page|module|program|URL}}`
