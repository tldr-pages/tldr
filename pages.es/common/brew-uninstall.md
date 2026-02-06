# brew uninstall

> Desinstala una fórmula/cask de Homebrew.
> Utiliza `brew autoremove` para eliminar las dependencias no utilizadas posteriormente.
> Más información: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->.

- Desinstala una fórmula/cask:

`brew {{[rm|uninstall]}} {{formula|cask}}`

- Desinstala un cask y elimina todos los archivos asociados:

`brew {{[rm|uninstall]}} --zap {{cask}}`
