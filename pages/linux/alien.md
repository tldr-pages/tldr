# alien

> Converts different instalation packages to multiple other formats. More information: http://manpages.ubuntu.com/manpages/trusty/man1/alien.1p.html.

- Convert the installation file to [d]ebian linux format [deb]:

`alien -d {{file}}`

- Convert the installation file to [r]ed hat linux format [rpm]:

`alien -r {{file}`

- Convert the installation file to Stampede [SLP] format:

`alien --to-slp {{file}}`

- Convert the installation file to a Slackware [t]gz installation file [tgz]:

`alien -t {{file}}`

- [I]nstall a package as soon as it finishes converting:

`alien {{options}} {{file}} -i`
