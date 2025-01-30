# tput

> View and modify terminal settings and capabilities.
> More information: <https://manned.org/tput>.

- Move the cursor to a screen location:

`tput cup {{row}} {{column}}`

- Set foreground (af) or background (ab) color:

`tput {{setaf|setab}} {{ansi_color_code}}`

- Reset all terminal text attributes:

`tput sgr0`

- Show number of columns, lines, or colors:

`tput {{cols|lines|colors}}`

- Enable or disable word wrap:

`tput {{smam|rmam}}`

- Hide or show the terminal cursor:

`tput {{civis|cnorm}}`

- Save or restore terminal text status:

`tput {{smcup|rmcup}}`

- Reverse text and background colors:

`tput rev`
