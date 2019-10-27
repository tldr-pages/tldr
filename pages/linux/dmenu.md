# dmenu

> Dynamic menu.
> Creates a menu from a text input with each item on a new line.

- Display a menu of the output of the "ls" command:

`{{ls}} | dmenu`

- Display a menu with custom items seperated by a new line (\n):

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu`

- Let the user choose between multiple items and save the selected one into a file:

`echo -e "{{red}}\n{{green}}\n{{blue}}" | dmenu > {{color.txt}}`

- Launch dmenu on specific monitor:

`ls | dmenu -m {{1}}`

- Display dmenu at the botton of the screen:

`ls | dmenu -b`
