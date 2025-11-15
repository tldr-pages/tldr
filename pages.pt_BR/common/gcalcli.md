# gcalcli

> Ferramenta de linha de comando para interagir com o Google Agenda.
> Solicita autorização da API do Google na primeira inicialização.
> Mais informações: <https://github.com/insanum/gcalcli>.

- Lista seus eventos para todos os seus calendários nos próximos 7 dias:

`gcalcli agenda`

- Mostra eventos começando em ou entre datas específicas (também recebe datas relativas, por exemplo, "amanhã"):

`gcalcli agenda {{mm/dd}} [{{mm/dd}}]`

- Lista eventos de um calendário específico:

`gcalcli --calendar {{nome_do_calendário}} agenda`

- Exibe um calendário ASCII de eventos por semana:

`gcalcli calw`

- Exibe um calendário ASCII de eventos para um mês:

`gcalcli calm`

- Adiciona um evento rapidamente ao seu calendário:

`gcalcli --calendar {{nome_do_calendário}} quick "{{mm/dd}} {{HH:MM}} {{nome_do_evento}}"`

- Adiciona um evento ao calendário. Dispara prompt interativo:

`gcalcli --calendar "{{nome_do_calendário}}" add`
