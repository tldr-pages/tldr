# [watch](http://man7.org/linux/man-pages/man1/watch.1.html)
> Execute a program periodically, showing output fullscreen.

- Repeatedly run a command and show the result:

`watch {{command}}`

- Re-run a command every 60 seconds:

`watch -n {{60}} {{command}}`

- Monitor the contents of a directory, highlighting differences as they appear:

`watch -d {{ls -l}}`
