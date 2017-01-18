# [tput](http://man7.org/linux/man-pages/man1/tput.1.html)
> View and modify terminal settings and capabilities.

- Move the cursor to a screen location:

`tput cup {{y_coordinate}} {{x_coordinate}}`

- Set foreground (af) or background (ab) color:

`tput {{setaf|setab}} {{ansi_color_code}}`

- Show number of columns, lines, or colors:

`tput {{cols|lines|colors}}`

- Ring the terminal bell:

`tput bel`

- Reset all terminal attributes:

`tput sgr0`
