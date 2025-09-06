# ack

> Uma ferramenta de pesquisa similar ao `grep`, otimizada para programadores.
> Veja também: `rg`, que é muito mais rápido.
> Mais informações: <https://beyondgrep.com/documentation>.

- Procura por arquivos que contenham o termo, ou a expressão regular, no diretório atual:

`ack "{{padrão_de_busca}}"`

- Procura um padrão sem diferenciar maiúsculas e minúsculas:

`ack {{[-i|--ignore-case]}} "{{padrão_de_busca}}"`

- Procura por linhas correspondentes ao padrão, imprimindo apenas o texto correspondente e não o resto da linha:

`ack {{[-o|--output '$&']}} "{{padrão_de_busca}}"`

- Limita a busca a um tipo específico de arquivo:

`ack {{[-t|--type]}} {{ruby}} "{{padrão_de_busca}}"`

- Não busca arquivos de um tipo específico:

`ack {{[-t|--type]}} no{{ruby}} "{{padrão_de_busca}}"`

- Conta o total de correspondências encontradas:

`ack {{[-c|--count]}} {{[-h|--no-filename]}} "{{padrão_de_busca}}"`

- Imprime o nome dos arquivos e o número de correspondências para cada arquivo:

`ack {{[-c|--count]}} {{[-l|--files-with-matches]}} "{{padrão_de_busca}}"`

- Lista todos os valores que podem ser utilizados com `--type`:

`ack --help-types`
