# grep

> Düzenli ifadeler (Regex) kullanarak dosyalardaki kalıpları bul.
> Daha fazla bilgi için: <https://www.gnu.org/software/grep/manual/grep.html>.

- Bir dosya içinde kalıp ara:

`grep "{{aranan_kalıp}}" {{dosya/yolu}}`

- Tam bir dize ara (düzenli ifadeleri devre dışı bırakır):

`grep --fixed-strings "{{tam_dize}}" {{dosya/yolu}}`

- Bir dizindeki tüm dosyalarda bir kalıbı tekrarlı olarak ara, eşleşmelerin satır numaralarını göster, binary dosyaları göz ardı et:

`grep --recursive --line-number --binary-files={{without-match}} "{{aranan_kalıp}}" {{dosya/yolu}}`

- Büyük/küçük harfe duyarsız modda genişletilmiş düzenli ifadeleri (`?`, `+`, `{}`, `()` ve `|` destekler) kullan:

`grep --extended-regexp --ignore-case "{{aranan_kalıp}}" {{dosya/yolu}}`

- Her eşleşmenin etrafında, öncesinde veya sonrasında 3 satır içerik yazdır:

`grep --{{context|before-context|after-context}}={{3}} "{{aranan_kalıp}}" {{dosya/yolu}}`

- Renkli çıktı ile her eşleşme için dosya adını ve satır numarasını yazdır:

`grep --with-filename --line-number --color=always "{{aranan_kalıp}}" {{dosya/yolu}}`

- Bir kalıpla eşleşen satırları ara, yalnızca eşleşen metni yazdır:

`grep --only-matching "{{aranan_kalıp}}" {{dosya/yolu}}`

- Bir kalıpla eşleşmeyen satırlar için `stdin`'de arama yap:

`cat {{dosya/yolu}} | grep --invert-match "{{aranan_kalıp}}"`
