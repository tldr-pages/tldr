# [echo](http://man7.org/linux/man-pages/man1/echo.1.html)
> Print given arguments.

- Print a text message. Note: quotes are optional:

`echo {{"Hello World"}}`

- Print a message with environment variables:

`echo {{"My path is $PATH"}}`

- Print a message without the trailing newline:

`echo -n {{"Hello World"}}`

- Enable interpretation of backslash escapes (special characters):

`echo -e {{"Column 1\tColumn 2"}}`
