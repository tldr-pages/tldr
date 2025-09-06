# defaults

> Lê e grava a configuração do usuário do macOS para aplicativos.
> Mais informações: <https://keith.github.io/xcode-man-pages/defaults.1.html>.

- Lê os padrões do sistema para uma opção do aplicativo:

`defaults read "{{aplicativo}}" "{{opção}}"`

- Lê os valores padrão para uma opção do aplicativo:

`defaults read -app "{{aplicativo}}" "{{opção}}"`

- Pesquisa uma palavra-chave em nomes de domínio, chaves, e valores:

`defaults find "{{palavra-chave}}"`

- Grava o valor padrão de uma opção do aplicativo:

`defaults write "{{aplicativo}}" "{{opção}}" {{-tipo}} {{valor}}`

- Acelera as animações do Mission Control:

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- Exclui todos os padrões de um aplicativo:

`defaults delete "{{aplicativo}}"`
