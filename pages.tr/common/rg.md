# rg

> Ripgrep, yinelemeli satır-odaklı bir CLI arama aracıdır.
> Grep'e daha hızlı bir alternatif olmayı hedefler.
> Daha fazla bilgi: <https://github.com/BurntSushi/ripgrep>.

- Normal bir ifade için geçerli dizini yinelemeli olarak arayın:

`rg {{normal_ifade}}`

- Geçerli dizinde, gizli dosyalar ve ".gitignore" da listelenen dosyalar dahil olmak üzere normal ifadeleri yinelemeli olarak arayın:

`rg --no-ignore --hidden {{normal_ifade}}`

- Normal ifadeyi yalnızca bir dizin alt kümesinde arayın:

`rg {{normal_ifade}} {{dizin_alt_kümesi}}`

- Bir glob ile eşleşen dosyalarda normal bir ifade arayın (örn: `README.*`):

`rg {{normal_ifade}} --glob {{glob}}`

- Normal bir ifadeyle eşleşen dosya adlarını arayın:

`rg --files | rg {{normal_ifade}}`

- Yalnızca eşleşen dosyaları listeleyin (diğer komutlara yönlendirirken kullanışlıdır):

`rg --files-with-matches {{normal_ifade}}`

- Verilen normal ifadeyle eşleşmeyen satırları göster:

`rg --invert-match {{normal_ifade}}`

- Bir değişmez dizi deseni için arama yapın:

`rg --fixed-strings -- {{dizi}}`
