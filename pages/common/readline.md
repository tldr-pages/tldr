# readline

> The GNU Readline library for command-line editing and history.
> Used by many interactive command-line programs for line editing and history.
> More information: <https://tiswww.case.edu/php/chet/readline/rltop.html>.

- Move the cursor one character to the left/right:

`Ctrl + b / Ctrl + f`

- Move the cursor one word to the left/right:

`Alt + b / Alt + f`

- Move the cursor to the start/end of the line:

`Ctrl + a / Ctrl + e`

- Delete the character under/before the cursor:

`Ctrl + d / Ctrl + h`

- Delete the word before/after the cursor:

`Alt + Backspace / Alt + d`

- Delete all characters from the cursor to the start/end of the line:

`Ctrl + u / Ctrl + k`

- Delete the entire line:

`Ctrl + x + Backspace`

- Search command history backwards/forwards:

`Ctrl + r / Ctrl + s`

- Move through history one line at a time:

`Ctrl + p / Ctrl + n`

- Move to the first/last line in history:

`Alt + < / Alt + >`

- Insert the last argument from the previous command:

`Alt + . / Alt + _`

- Clear the screen while keeping the current line:

`Ctrl + l`

- Transpose characters before the cursor:

`Ctrl + t`

- Transpose words before the cursor:

`Alt + t`

- Capitalize the current word:

`Alt + c`

- Make the current word uppercase/lowercase:

`Alt + u / Alt + l`

- Undo the last edit:

`Ctrl + _ / Ctrl + x + Ctrl + u`

- Enable case-insensitive tab completion in your `~/.inputrc`:

`echo 'set completion-ignore-case on' >> {{~/.inputrc}}`

- Enable single tab completion instead of having to press tab twice:

`echo 'set show-all-if-ambiguous on' >> {{~/.inputrc}}`

- Use vi-style keyboard shortcuts:

`echo 'set editing-mode vi' >> {{~/.inputrc}}`

- Enable colored tab completion for files and directories:

`echo 'set colored-stats on' >> {{~/.inputrc}}`

- Configure what characters to use to mark files of different types when completing (as in ls -F):

`echo 'set visible-stats on' >> {{~/.inputrc}}`

- Keep lines starting with a common prefix together when scrolling through history:

`echo 'set history-preserve-point on' >> {{~/.inputrc}}`

- Display help:

`info readline`
