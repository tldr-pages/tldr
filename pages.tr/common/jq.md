# jq

> Alana özgü bir dil (DSL) kullanan JSON işlemcisi.
> Daha fazla bilgi için: <https://jqlang.org/manual/>.

- Yalnızca `jq` ikili dosyasını kullanarak belirli bir ifadeyi çalıştır (renkli ve biçimlendirilmiş JSON çıktısı yazdır):

`jq '.' {{yol/dosya.json}}`

- Belirli bir betiği çalıştır:

`{{cat yol/dosya.json}} | jq {{[-f|--from-file]}} {{yol/betik.jq}}`

- Belirli argümanlar geçir:

`{{cat yol/dosya.json}} | jq {{--arg "isim1" "değer1" --arg "isim2" "değer2" ...}} '{{. + $ARGS.named}}'`

- Birden fazla dosyadaki eski JSON nesnelerinden yeni bir JSON nesnesi oluştur:

`{{cat yol/birden_fazla_json_dosya_*.json}} | jq '{{{yeniAnahtar1: .anahtar1, yeniAnahtar2: .anahtar2.altAnahtar, ...}}}'`

- Dizideki belirli öğeleri yazdır:

`{{cat yol/dosya.json}} | jq '{{.[indeks1], .[indeks2], ...}}'`

- Tüm dizi/nesne değerlerini yazdır:

`{{cat yol/dosya.json}} | jq '.[]'`

- Dizideki nesneleri 2 koşullu bir filtreyle yazdır:

`{{cat yol/dosya.json}} | jq '.[] | select((.anahtar1=="değer1") and .anahtar2=="değer2")'`

- Belirli anahtarları ekle/kaldır:

`{{cat yol/dosya.json}} | jq '. {{+|-}} {{{"anahtar1": "değer1", "anahtar2": "değer2", ...}}}'`
