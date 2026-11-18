# grep

> Düzenli ifadeler (`regex`) kullanarak dosyalardaki kalıpları bul.
> Ayrıca bakınız: `rg`, `regex`.
> Daha fazla bilgi için: <https://www.gnu.org/software/grep/manual/grep.html>.

- Dosyalar içinde kalıp ara:

`grep "{{aranan_kalıp}}" {{yol/dosya1 yol/dosya2 ...}}`

- Tam bir dize ara (düzenli ifadeleri devre dışı bırakır):

`grep {{[-F|--fixed-strings]}} "{{tam_dize}}" {{yol/dosya}}`

- Bir dizindeki tüm dosyalarda bir kalıbı tekrarlı olarak ara, binary dosyaları göz ardı et:

`grep {{[-rI|--recursive --binary-files=without-match]}} "{{aranan_kalıp}}" {{yol/dizin}}`

- Her eşleşmenin etrafında, öncesinde veya sonrasında 3 satır içerik yazdır:

`grep {{--context|--before-context|--after-context}} 3 "{{aranan_kalıp}}" {{yol/dosya}}`

- Renkli çıktı ile her eşleşme için dosya adını ve satır numarasını yazdır:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{aranan_kalıp}}" {{yol/dosya}}`

- Yalnızca eşleşen metni yazdır:

`grep {{[-o|--only-matching]}} "{{aranan_kalıp}}" {{yol/dosya}}`

- `stdin`'den veri oku ve bir kalıpla eşleşen satırları yazdırma:

`cat {{yol/dosya}} | grep {{[-v|--invert-match]}} "{{aranan_kalıp}}"`

- Büyük/küçük harfe duyarsız modda genişletilmiş düzenli ifadeleri (`?`, `+`, `{}`, `()`, ve `|` destekler) kullan:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{aranan_kalıp}}" {{yol/dosya}}`
