#ապուր

> Ստատիկ վեբ կայքի գեներատոր, որը հիմնված է HTML տարրերի ծառի վերագրման վրա:.
> Այն կարող է օգտագործվել նաև որպես HTML հետպրոցեսոր կամ մետատվյալների արդյունահանող:.
> Լրացուցիչ տեղեկություններ. <https://soupault.net/reference-manual/>:.

- Նախաձեռնեք նվազագույն կայքի նախագիծ ընթացիկ աշխատանքային գրացուցակում.:

`soupault --init`

- Կառուցեք կայք.:

`soupault`

- Չեղարկել լռելյայն կազմաձևման ֆայլի և գրացուցակի տեղադրությունները.:

`soupault --config {{config_path}} --site-dir {{input_directory}} --build-dir {{output_directory}}`

- Արտահանեք մետատվյալները JSON ֆայլի մեջ՝ առանց էջեր ստեղծելու.:

`soupault --index-only --dump-index-json {{path/to/file.json}}`

- Ցույց տալ արդյունավետ կոնֆիգուրացիան (արժեքները `soupault.toml`-ից գումարած լռելյայն).:

`soupault --show-effective-config`
