# xmodmap

> Utility for modifying keymaps and pointer button mappings in X.
> More information: <https://manned.org/xmodmap>.

- Swap `<LeftClick>` and `<RightCLick>` on the pointer:

`xmodmap -e 'pointer = 3 2 1'`

- Reassign a key on the keyboard to another key:

`xmodmap -e 'keycode {{keycode}} = {{keyname}}'`

- Disable a key on the keyboard:

`xmodmap -e 'keycode {{keycode}} ='`

- Execute all xmodmap expressions in the specified file:

`xmodmap {{path/to/file}}`
