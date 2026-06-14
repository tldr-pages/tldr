# pio ci

> Կառուցեք PlatformIO նախագծեր կամայական կոդերի կառուցվածքով:.
> Սա կստեղծի նոր ժամանակավոր նախագիծ, որում կպատճենվի սկզբնական կոդը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>:.

- Ստեղծեք PlatformIO նախագիծ լռելյայն համակարգի ժամանակավոր գրացուցակում և այնուհետև ջնջեք այն.:

`pio ci {{path/to/project}}`

- Կառուցեք PlatformIO նախագիծ և նշեք հատուկ գրադարաններ.:

`pio ci {{[-l|--lib]}} {{path/to/library_directory}} {{path/to/project}}`

- Կառուցեք PlatformIO նախագիծ և նշեք հատուկ տախտակ (`pio boards` թվարկում է բոլորը).:

`pio ci {{[-b|--board]}} {{board}} {{path/to/project}}`

- Ստեղծեք PlatformIO նախագիծ հատուկ գրացուցակում.:

`pio ci --build-dir {{path/to/build_directory}} {{path/to/project}}`

- Կառուցեք PlatformIO նախագիծ և մի ջնջեք կառուցման գրացուցակը.:

`pio ci --keep-build-dir {{path/to/project}}`

- Կառուցեք PlatformIO նախագիծ՝ օգտագործելով հատուկ կազմաձևման ֆայլ.:

`pio ci {{[-c|--project-conf]}} {{path/to/platformio.ini}}`
