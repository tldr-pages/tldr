# comby

> Számos nyelvet támogató eszköz strukturális kódok keresésére és cseréjére. További információ: <https://github.com/comby-tools/comby>.

- Sablonok egyeztetése és átírása, valamint a változtatások kinyomtatása:

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b], :[a])}}' {{.rs}}`

- Egyezés és átírás átírási tulajdonságokkal:

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b].Capitalize, :[a])}}' {{.rs}}`

- Helyben történő egyeztetés és átírás:

`comby -in-place '{{match_pattern}}' '{{rewrite_pattern}}'`

- Csak illesztés végrehajtása és a találatok nyomtatása:

`comby -match-only '{{match_pattern}}' ""`
