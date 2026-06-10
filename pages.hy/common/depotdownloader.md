# depotdownloader

> Բովանդակություն/պահեստային ներբեռնիչ Steam-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/SteamRE/DepotDownloader>:.

- Ներբեռնեք հավելված.:

`depotdownloader -app {{108600}}`

- Ներբեռնեք հատուկ պահեստը մաքսային ելքային գրացուցակում.:

`depotdownloader -app {{108600}} -depot {{108603}} -dir {{path/to/directory}}`

- Ներբեռնեք Steam հաշվի միջոցով.:

`depotdownloader -app {{108600}} -depot {{108603}} -username "{{gabecube}}"`

- Ներբեռնեք պահեստ և հիշեք գաղտնաբառը հետագա ներբեռնումների համար.:

`depotdownloader -app {{108600}} -depot {{108603}} -username "{{gabecube}}" -remember-password`

- Ներբեռնեք հատուկ պահեստային մանիֆեստ.:

`depotdownloader -app {{346110}} -depot {{346111}} -manifest {{6154025194991279746}}`

- Ներբեռնեք կոնկրետ մասնաճյուղից.:

`depotdownloader -app {{108600}} -depot {{108603}} -branch "{{unstable}}"`

- Ներբեռնեք միայն ներքին մանիֆեստը, բացառությամբ բովանդակության.:

`depotdownloader -app {{108600}} -depot {{108603}} -manifest-only`

- Ներբեռնեք սեմինարի բովանդակությունը՝ օգտագործելով pubfile/workshop id-ը.:

`depotdownloader -app {{108600}} -pubfile {{2503622437}}`
