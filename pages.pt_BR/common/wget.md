# wget

> Baixar arquivos da Internet.
> Suporta HTTP, HTTPS, e FTP.
> Mais informações: <https://www.gnu.org/software/wget/manual/wget.html>.

- Baixa o conteúdo de uma URL para o arquivo (nomeado como "foo" neste caso):

`wget {{https://example.com/foo}}`

- Baixa o conteúdo de uma URL para o arquivo (nomeado como "bar" neste caso):

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- Baixa uma única página web e todo os seus recursos com intervalos de 3 segundos entre requisições (scripts, stylesheets, imagens, etc.):

`wget {{[-p|--page-requisites]}} {{[-k|--convert-links]}} {{[-w|--wait]}} 3 {{https://example.com/algumapagina.html}}`

- Baixa todos os arquivos listados dentro de um diretório e seus sub-diretórios (não baixa elementos de página incorporados):

`wget {{[-m|--mirror]}} {{[-np|--no-parent]}} {{https://example.com/algumcaminho/}}`

- Limita a velocidade de download e o número de novas tentativas de conexão:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/algumcaminho/}}`

- Baixa um arquivo de um servidor HTTP usando Autenticação Básica (também funciona para FTP):

`wget --user {{nomeusuario}} --password {{senha}} {{https://example.com}}`

- Continua um download incompleto:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Baixa todas as URLs armazenadas em um arquivo de texto para um diretório específico:

`wget {{[-P|--directory-prefix]}} {{caminho/para/diretorio}} {{[-i|--input-file]}} {{URLs.txt}}`
