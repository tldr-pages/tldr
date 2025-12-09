# dunstify

> Uma ferramenta de notificação que é uma extensão do `notify-send`, mas com mais funcionalidades baseadas em `dunst`.
> Aceita todas as opções do `notify-send`.
> Mais informações: <https://dunst-project.org/documentation/dunstify>.

- Mostra uma notificação com um dado título e mensagem:

`dunstify "{{Título}}" "{{Mensagem}}"`

- Mostra uma notificação com uma urgência específica:

`dunstify "{{Título}}" "{{Mensagem}}" -u {{low|normal|critical}}`

- Especifica um ID para a mensagem (sobrescreve qualquer mensagem anterior com o mesmo ID):

`dunstify "{{Título}}" "{{Mensagem}}" -r {{123}}`

- Mostra opções de ajuda:

`dunstify --help`
