# fuzzel

> A Wayland-native application launcher and fuzzy finder, inspired by `rofi` and `dmenu`.
> More information: <https://codeberg.org/dnkl/fuzzel>.

- Run applications:

`fuzzel`

- Run `fuzzel` in dmenu mode:

`fuzzel {{-d|--dmenu}}`

- Display a menu of the output of the `ls` command:

`{{ls}} | fuzzel -d`

- Display a menu with custom items separated by a new line (`\n`):

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel -d`

- Let the user choose between multiple items and save the selected one to a file:

`echo -e "{{red}}\n{{green}}\n{{blue}}" | fuzzel -d > {{color.txt}}`

- Reset apps usage count (default cache directory: `$XDG_CACHE_HOME/fuzzel`):

`rm -v $HOME/.cache/fuzzel`

- Launch `fuzzel` on a specific monitor, see `wlr-randr` or `swaymsg -t get_outputs`:

`fuzzel -o "{{DP-1}}"`

- Use `fuzzel` to do an online search:

`fuzzel -d -l 0 --placeholder "{{Type your search}}" | sed 's/^/\"/g;s/$/\"/g' | xargs firefox --search`
