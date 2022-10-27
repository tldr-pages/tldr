# prompt

> Change the default DOS style prompt in a command window.
> More information: <https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/prompt>.

- Reset the prompt to default 'C:\>':

`prompt`

- Change the prompt line:

`prompt {{special_codes}}`

- Change the prompt to show current date first 'Thu 10/27/2022 C:\>':

`prompt $D $P$G`

- Change the prompt to show current time first '12:06:14.15 C:\>':

`prompt $T $P$G`

- Change the prompt with custom text '{{custom_text}} C:\>':

`prompt {{custom_text}} $P$G`
