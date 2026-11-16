# rg

> Ripgrep, yinelemeli satır-odaklı bir CLI arama aracıdır.
> Grep'e daha hızlı bir alternatif olmayı hedefler.
> Daha fazla bilgi için: <https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md>.

- Normal bir ifade için geçerli dizini yinelemeli olarak ara:

`rg {{normal_ifade}}`

- Bir dosyada veya dizinde normal bir ifadeyi yinelemeli olarak ara:

`rg {{normal_ifade}} {{yol/dosya_veya_dizin}}`

- Değişmez bir dize desenini ara:

`rg {{[-F|--fixed-strings]}} -- {{dize}}`

- Gizli dosyaları ve `.gitignore` içinde listelenen girdileri de dahil et:

`rg {{[-.|--hidden]}} --no-ignore {{normal_ifade}}`

- Yalnızca bir `glob` desenine uyan dosyalarda ara (örn. `README.*`; hariç tutmak için `!dosya_adı_deseni` kullan):

`rg {{normal_ifade}} {{[-g|--glob]}} '{{dosya_adı_glob_deseni}}'`

- Geçerli dizindeki dosya adlarını yinelemeli olarak listele ve bir desenle eşleşenleri vurgula:

`rg --files | rg {{[--passthru|--passthrough]}} {{normal_ifade}}`

- Yalnızca eşleşen dosyaları listele (diğer komutlara yönlendirirken kullanışlıdır):

`rg {{[-l|--files-with-matches]}} {{normal_ifade}}`

- Desenle eşleşmeyen satırları göster:

`rg {{[-v|--invert-match]}} {{normal_ifade}}`
