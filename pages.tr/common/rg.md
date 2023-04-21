# rg

> Ripgrep, yinelemeli satır-odaklı bir CLI arama aracıdır.
> Grep'e daha hızlı bir alternatif olmayı hedefler.
> Daha fazla bilgi için: <https://github.com/BurntSushi/ripgrep>.

- Normal bir ifade için geçerli dizini yinelemeli olarak ara:

`rg {{normal_ifade}}`

- Geçerli dizinde, gizli dosyalar ve ".gitignore" da listelenen dosyalar dahil olmak üzere normal ifadeleri yinelemeli olarak ara:

`rg --no-ignore --hidden {{normal_ifade}}`

- Normal ifadeyi yalnızca bir dizin alt kümesinde ara:

`rg {{normal_ifade}} {{dizin_alt_kümesi}}`

- Bir glob ile eşleşen dosyalarda normal bir ifade ara (örn: `README.*`):

`rg {{normal_ifade}} --glob {{glob}}`

- Normal bir ifadeyle eşleşen dosya adlarını ara:

`rg --files | rg {{normal_ifade}}`

- Yalnızca eşleşen dosyaları listele (diğer komutlara yönlendirirken kullanışlıdır):

`rg --files-with-matches {{normal_ifade}}`

- Verilen normal ifadeyle eşleşmeyen satırları göster:

`rg --invert-match {{normal_ifade}}`

- Bir değişmez dizi deseni için arama yap:

`rg --fixed-strings -- {{dizi}}`
