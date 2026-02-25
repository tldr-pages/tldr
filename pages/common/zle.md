# zle

> Manage Zsh Line Editor widgets.
> Note: Some operations require ZLE to be active (typically inside a user-defined widget).
> More information: <https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Zle-Builtins>.

- [l]ist user-defined widgets:

`zle -l`

- [l]ist [a]ll widgets, including built-in ones:

`zle -la`

- Create a [N]ew user-defined widget (function defaults to same name as widget):

`zle -N {{widget_name}} {{optional_shell_function_name}}`

- [D]elete a widget:

`zle -D {{widget_name}}`

- Create an [A]lias of a widget:

`zle -A {{original_widget}} {{alias_name}}`

- Invoke a widget from inside another widget function (requires active ZLE):

`zle {{widget_name}}`

- Push text into ZLE's input queue as if it were typed (requires active ZLE):

`zle -U "{{text}}"`
