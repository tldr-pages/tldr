# color

> Set the console foreground and background colors.
> More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/color>.

- Set the console colors to the default values:

`color`

- List available color values and detailed information:

`color /?`

- Set the console foreground and background to a specific color:

`color {{foreground_code}}{{background_code}}`

- Allowed values: `1-9,a-f`
| 1-9           | a-f             |
|---------------|-----------------|
| 0: Black      |                 |
| 1: Blue       | a: L Green      |
| 2: Green      | b: L Aqua       |
| 3: Aqua       | c: L Red        |
| 4: Red        | d: L Purple     |
| 5: Purple     | e: L Yellow     |
| 6: Yellow     | f: Bright White |
| 7: White      |                 |
| 8: Gray       |                 |
| 9: Light Blue |                 |
