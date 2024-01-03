# ippeveprinter

> Um servidor de impressão IPP Everywhere simples.
> Veja também: `ippeveps`, `ippevepcl`.
> Mais informações: <https://openprinting.github.io/cups/doc/man-ippeveprinter.html>.

- Executa o servidor com um nome de serviço específico:

`ippeveprinter "{{nome_do_serviço}}"`

- Carrega os atributos da impressora de um arquivo PPD:

`ippeveprinter -P {{caminho/para/arquivo.ppd}} "{{nome_do_serviço}}"`

- Executa o comando `file` sempre que um trabalho é enviado para o servidor:

`ippeveprinter -c {{/usr/bin/file}} "{{nome_do_serviço}}"`

- Especifica o diretório que vai conter os arquivos de impressão (por padrão, um diretório dentro do diretório temporário do usuário):

`ippeveprinter -d {{diretório_spool}} "{{nome_do_serviço}}"`

- Mantém os documentos de impressão no diretório de spool em vez de exclui-los:

`ippeveprinter -k "{{nome_do_serviço}}"`

- Especifica a velocidade da impressora na unidade páginas/minuto (10 por padrão):

`ippeveprinter -s {{velocidade}} "{{nome_do_serviço}}"`
