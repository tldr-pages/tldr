# adb install

> Android Debug Bridge Install: Instalar apps em uma instância do Android emulator ou dispositivos conectados.
> Mais informações: <https://developer.android.com/studio/command-line/adb>.

- Instala um app Android em um emulador/dispositivo:

`adb install {{path/to/file.apk}}`

- Reinstala um app existente, mantendo seus dados:

`adb install -r {{path/to/file.apk}}`

- Concede todas as permissões listadas no manifesto do app:

`adb install -g {{path/to/file.apk}}`

- Atualiza rapidamente um app já instalado atualizando apenas as partes do APK que mudaram:

`adb install --fastdeploy {{path/to/file.apk}}`
