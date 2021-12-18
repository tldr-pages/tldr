# color

> Set the console foreground and background colors.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/color>.

- Set the console colors to the default values:

`color`

- List available color values and detailed information:

`color /?`

- Set the console foreground and background to a specific color:

`color {{foreground_code}}{{background_code}}`

Allowed values: `1-9,a-f`
| 1-9           | a-f             |
|---------------|-----------------|
| 0: Black      | a: L Green      |
| 1: Blue       | b: L Aqua       |
| 2: Green      | c: L Red        |
| 3: Aqua       | d: L Purple     |
| 4: Red        | e: L Yellow     |
| 5: Purple     | f: Bright White |
| 6: Yellow     |                 |
| 7: White      |                 |
| 8: Gray       |                 |
| 9: Light Blue |                 |
