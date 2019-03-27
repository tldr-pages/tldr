# dpkg

> Gerenciador de pacotes Debian.

- Instala um pacote:

`dpkg -i {{path/to/file.deb}}`

- Remove um pacote:

`dpkg -r {{package_name}}`

- Exibe os pacotes instalados:

`dpkg -l {{pattern}}`

- Exibe o conteúdo do pacote:

`dpkg -L {{package_name}}`

- Exibe o conteúdo do arquivo de um pacote:

`dpkg -c {{path/to/file.deb}}`

- Apresenta o pacote proprietário de um determinado arquivo:

`dpkg -S {{file_name}}`
