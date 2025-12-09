# prompt

> Change the default DOS style prompt in a command window.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>.

- Reset the prompt to the default setting:

`prompt`

- Set a specific prompt:

`prompt {{prompt}}`

- Change the prompt to show the current date first:

`prompt $D $P$G`

- Change the prompt to show the current time first:

`prompt $T $P$G`

- Change the prompt by adding a specific text first:

`prompt {{text}} $P$G`
