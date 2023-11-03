# aapt

> Android Asset Packaging Tool.
> Compila e empacotar os recursos de uma aplicação Android.
> Mais informações: <https://elinux.org/Android_aapt>.

- Listar os ficheiros contidos num arquivo APK:

`aapt list {{path/to/app.apk}}`

- Exibir os metadados da aplicação (versão, permissões, etc.):

`aapt dump badging {{path/to/app.apk}}`

- Criar um novo arquivo APK com os arquivos do directório especificado:

`aapt package -F {{path/to/app.apk}} {{path/to/directory}}`
