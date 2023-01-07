# go doc

> Bir paket veya sembolün dokümentasyonunu göster.
> Daha fazla bilgi için: <https://golang.org/cmd/go/#hdr-Show_documentation_for_package_or_symbol>.

- Mevcut paket için dokümentasyonu göster:

`go doc`

- Paket dokümentasyonunu ve dışa aktarılmış sembolleri göster:

`go doc {{encoding/json}}`

- Sembollerin de dokümentasyonunu göster:

`go doc -all {{encoding/json}}`

- Kaynakları da göster:

`go doc -all -src {{encoding/json}}`

- Belirtilen sembolü göster:

`go doc -all -src {{encoding/json.Number}}`
