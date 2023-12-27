# calcurse

> Um calendário e agenda baseados em texto para a linha de comando.
> Mais informações: <https://calcurse.org>.

- Inicia o calcurse em modo interativo:

`calcurse`

- Mostra os agendamentos e eventos para o presente dia:

`calcurse --appointment`

- Apaga todos os objetos gravados localmente e importa os objetos remotos:

`calcurse-caldav --init=keep-remote`

- Apaga todos os objetos remotos e envia os objetos gravados localmente:

`calcurse-caldav --init=keep-local`

- Copia os objetos gravados localmente para o servidor CalDAV e vice-versa:

`calcurse-caldav --init=two-way`
