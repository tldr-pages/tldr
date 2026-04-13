# zargs

> A version of `xargs` for use with `zsh` glob patterns to avoid "argument list too long" errors.
> More information: <https://zsh.sourceforge.io/Doc/Release/User-Contributions.html>.

- Run a command using glob-expanded files as arguments:

`zargs {{**/*.log}} -- {{rm}}`

- Run a command with at most N arguments per invocation:

`zargs -n {{5}} {{**/*.txt}} -- {{cat}}`

- Run up to N parallel processes:

`zargs -P {{4}} {{**/*.jpg}} -- {{jpegoptim}}`

- Prompt before executing each command:

`zargs -p {{**/*.tmp}} -- {{rm}}`

- Print each command line before executing it:

`zargs -t {{**/*.md}} -- {{wc}} -l`

- Run a command on files modified more than 6 hours ago:

`zargs {{**/*(mh+6)}} -- {{rm}} -f`
