# aapt

> Ferramenta Android de empacotamento de recursos.
> Compila e empacota recursos de um aplicativo Android.
> Mais informações: <https://elinux.org/Android_aapt>.

- Lista os arquivos contigos em um arquivo APK:

`aapt list {{caminho/para/aplicativo.apk}}`

- Exibe os metadados de um aplicavio (versão, permissão, etc.):

`aapt dump badging {{caminho/para/aplicativo.apk}}`

- Cria um novo arquivo APK com os arquivos especificados no diretório:

`aapt package -F {{caminho/para/aplicativo.apk}} {{caminho/para/diretório}}`
