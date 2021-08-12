# electron-packager

> Un instrument folosit pentru a construi executabile de aplicații Electron pentru Windows, Linux și macOS.
> Necesită un pachete.json valid în directorul aplicației.
> Mai multe informaţii: <https://github.com/electron/electron-packager>

- Pachet o aplicatie pentru arhitectura si platforma actuala:

`electron-packager "{{path/to/app}}" "{{app_name}}"`

- Pachet o aplicație pentru toate arhitecturile și platformele:

`electron-packager "{{path/to/app}}" "{{app_name}}" --all`

- Pachet o cerere pentru 64-bit Linux:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{linux}}" --arch="{{x64}}"`

- Pachet o aplicație pentru ARM macOS:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{darwin}}" --arch="{{arm64}}"`
