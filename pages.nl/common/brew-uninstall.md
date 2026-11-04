# brew uninstall

> Verwijder een Homebrew-formule/cask.
> Gebruik `brew autoremove` om ongebruikte afhankelijkheden achteraf te verwijderen.
> Meer informatie: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->.

- Verwijder een formule/cask:

`brew {{[rm|uninstall]}} {{formule|cask}}`

- Verwijder een cask en verwijder alle bijbehorende bestanden:

`brew {{[rm|uninstall]}} --zap {{cask}}`
