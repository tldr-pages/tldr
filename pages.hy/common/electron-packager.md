# էլեկտրոն-փաթեթավորող

> Ստեղծեք Electron հավելվածի գործարկվող սարքեր Windows-ի, Linux-ի և macOS-ի համար:.
> Պահանջվում է վավեր `package.json` հավելվածի գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/electron/packager>:.

- Ներկայիս ճարտարապետության և հարթակի համար հավելված փաթեթավորեք.:

`electron-packager "{{path/to/app}}" "{{app_name}}"`

- Փաթեթավորեք հավելված բոլոր ճարտարապետությունների և հարթակների համար.:

`electron-packager "{{path/to/app}}" "{{app_name}}" --all`

- Փաթեթավորեք հավելված 64-բիթանոց Linux-ի համար.:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{linux}}" --arch="{{x64}}"`

- Փաթեթավորեք հավելված ARM macOS-ի համար.:

`electron-packager "{{path/to/app}}" "{{app_name}}" --platform="{{darwin}}" --arch="{{arm64}}"`
