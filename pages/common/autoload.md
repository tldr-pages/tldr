# autoload

> Mark functions for lazy loading in Zsh.
> Functions are not loaded into memory until first called, improving shell startup time.
> More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Autoload a function by name:

`autoload {{function_name}}`

- Autoload a function and immediately resolve its definition:

`autoload +X {{function_name}}`

- Autoload a function using Zsh-style autoloading (recommended):

`autoload -Uz {{function_name}}`

- Make functions from a directory available by adding it to `fpath`:

`fpath=({{path/to/functions_dir}} $fpath) && autoload -Uz {{function_name}}`

- Autoload the Zsh completion system:

`autoload -Uz compinit && compinit`

- Autoload and use the `add-zsh-hook` utility:

`autoload -Uz add-zsh-hook`
