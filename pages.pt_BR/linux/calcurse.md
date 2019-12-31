# calcurse

> Um calendário e agenda baseados em texto para a linha de comando.
> Mais informações: <https://calcurse.org>.

- Iniciar o calcurse em modo interativo:

`calcurse`

- Mostrar os agendamentos e eventos para o presente dia:

`calcurse --appointment`

- Apagar todos os objetos gravados localmente e importar os objetos remotos:

`calcurse-caldav --init=keep-remote`

- Apagar todos os objetos remotos e enviar os objetos gravados localmente:

`calcurse-caldav --init=keep-local`

- Copiar os objetos gravados localmente para o servidor CalDAV e vice-versa:

`calcurse-caldav --init=two-way`
