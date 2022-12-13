# tput

> View and modify terminal settings and capabilities.
> More information: <https://manned.org/tput>.

- Move the cursor to a screen location:

`tput cup {{row}} {{column}}`

- Set foreground (af) or background (ab) color:

`tput {{setaf|setab}} {{ansi_color_code}}`

- Show number of columns, lines, or colors:

`tput {{cols|lines|colors}}`

- Ring the terminal bell:

`tput bel`

- Reset all terminal attributes:

`tput sgr0`

- Enable or disable word wrap:

`tput {{smam|rmam}}`
