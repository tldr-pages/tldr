# Alien
> Converts different instalation packages to multiple other formats. More information: http://manpages.ubuntu.com/manpages/trusty/man1/alien.1p.html

- Converts the installation file to [d]ebian linux format [deb]:

`alien -d {{file}}`
`alien --to-deb {{file}}`

- Converts the installation file to [r]ed hat linux format [rpm]:

`alien -r {{file}`
`alien --to-rpm {{file}}`

- Converts the installation file to Stampede [SLP] format:

`alien --to-slp {{file}}`

- Converts the installation file to a Slackware [t]gz installation file [tgz]:

`alien -t {{file}}`
`alien --to-tgz {{file}}`

- [I]nstalls a package as soon as it finishes converting:

`alien {{options}} {{file}} -i`
