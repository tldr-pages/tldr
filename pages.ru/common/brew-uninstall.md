# brew uninstall

> Удалять формулы/каски Homebrew.
> Используйте `brew autoremove` для удаления неиспользуемых зависимостей после этого.
> Больше информации: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->.

- Удалить формулу/каск:

`brew {{[rm|uninstall]}} {{формула|каск}}`

- Удалить каск и удалить все связанные файлы:

`brew {{[rm|uninstall]}} --zap {{каск}}`
