# nice

> Execute a program with a custom scheduling priority (niceness).
> Niceness values range from -20 (the highest priority) to 19 (the lowest).
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- Launch a program with altered priority:

`nice -{{niceness_value}} {{command}}`

- Define the priority with an explicit option:

`nice {{[-n|--adjustment]}} {{niceness_value}} {{command}}`
