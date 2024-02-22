# adb install

> Android Debug Bridge Install: Instalar apps em uma instância do Android emulator ou dispositivos conectados.
> Mais informações: <https://developer.android.com/tools/adb>.

- Instala um app Android em um emulador/dispositivo:

`adb install {{caminho/para/arquivo.apk}}`

- Instala um app Android em um emulador/dispositivo específico (sobrepõe `$ANDROID_SERIAL`):

`adb -s {{numero_de_serie}} install {{caminho/para/arquivo.apk}}`

- Reinstala um app existente, mantendo seus dados:

`adb install -r {{caminho/para/arquivo.apk}}`

- Instala um app Android permitindo um downgrade de versão de código (apenas pacotes depuráveis):

`adb install -d {{path/to/file.apk}}`

- Concede todas as permissões listadas no manifesto do app:

`adb install -g {{caminho/para/arquivo.apk}}`

- Atualiza rapidamente um app já instalado atualizando apenas as partes do APK que mudaram:

`adb install --fastdeploy {{caminho/para/arquivo.apk}}`
