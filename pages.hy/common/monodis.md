#մոնոդիս

> Mono Common Intermediate Language (CIL) ապամոնտաժիչը:.
> Լրացուցիչ տեղեկություններ. <https://www.mono-project.com/docs/tools+libraries/tools/monodis/>:.

- Ապամոնտաժել մոնտաժը տեքստային CIL-ին.:

`monodis {{path/to/assembly.exe}}`

- Պահպանեք արդյունքը ֆայլում.:

`monodis --output={{path/to/output.il}} {{path/to/assembly.exe}}`

- Ցույց տալ հավաքի մասին տեղեկատվություն.:

`monodis --assembly {{path/to/assembly.dll}}`

- Թվարկեք ժողովի հղումները.:

`monodis --assemblyref {{path/to/assembly.exe}}`

- Թվարկեք հավաքման բոլոր մեթոդները.:

`monodis --method {{path/to/assembly.exe}}`

- Թվարկեք ժողովում ներկառուցված ռեսուրսները.:

`monodis --manifest {{path/to/assembly.dll}}`

- Բոլոր ներկառուցված ռեսուրսները հանեք ընթացիկ գրացուցակում.:

`monodis --mresources {{path/to/assembly.dll}}`
