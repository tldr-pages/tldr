# duti

> Define os aplicativos padrão para tipos de documentos e esquemas de URL no macOS.
> Mais informações: <https://github.com/moretension/duti>.

- Define o Safari como o manipulador padrão de documentos HTML:

`duti -s {{com.apple.Safari}} {{public.html}} all`

- Define o VLC como visualizador padrão para arquivos com extensões `.m4v`:

`duti -s {{org.videolan.vlc}} {{m4v}} viewer`

- Define o Finder como o manipulador padrão para esquema de URL ftp://:

`duti -s {{com.apple.Finder}} "{{ftp}}"`

- Exibe informações sobre o aplicativo padrão para uma determinada extensão:

`duti -x {{ext}}`

- Exibe o manipulador padrão para um determinado UTI:

`duti -d {{uti}}`

- Exibe todos os manipuladores de um determinado UTI:

`duti -l {{uti}}`
