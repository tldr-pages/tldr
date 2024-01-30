# wget

> Baixar arquivos da Internet.
> Suporta HTTP, HTTPS, e FTP.
> Mais informações: <https://www.gnu.org/software/wget>.

- Baixa o conteúdo de uma URL para o arquivo (nomeado como "foo" neste caso):

`wget {{https://exemplo.com/foo}}`

- Baixa o conteúdo de uma URL para o arquivo (nomeado como "bar" neste caso):

`wget --output-document {{bar}} {{https://exemplo.com/foo}}`

- Baixa uma única página web e todo os seus recursos com intervalos de 3 segundos entre requisições (scripts, stylesheets, imagens, etc.):

`wget --page-requisites --convert-links --wait=3 {{https://exemplo.com/algumapagina.html}}`

- Baixa todos os arquivos listados dentro de um diretório e seus sub-diretórios (não baixa elementos de página incorporados):

`wget --mirror --no-parent {{https://exemplo.com/algumcaminho/}}`

- Limita a velocidade de download e o número de novas tentativas de conexão:

`wget --limit-rate={{300k}} --tries={{100}} {{https://exemplo.com/algumcaminho/}}`

- Baixa um arquivo de um servidor HTTP usando Autenticação Básica (também funciona para FTP):

`wget --user={{nomeusuario}} --password={{senha}} {{https://exemplo.com}}`

- Continua um download incompleto:

`wget --continue {{https://exemplo.com}}`

- Baixa todas as URLs armazenadas em um arquivo de texto para um diretório específico:

`wget --directory-prefix {{caminho/para/diretorio}} --input-file {{URLs.txt}}`
