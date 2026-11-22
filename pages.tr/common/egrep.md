# egrep

> Genişletilmiş düzenli ifadeler (`regex`) kullanarak dosyalardaki kalıpları bul.
> Not: Bu komut `grep --extended-regexp` için bir takma addır.
> Ayrıca bakınız: `regex`.
> Daha fazla bilgi için: <https://manned.org/egrep>.

- Bir veya daha fazla kez yinelenen bir karakteri ara:

`egrep '{{a}}+' {{dosya/yolu}}`

- Bir karakterin sıfır ya da bir kez geçtiği yerleri ara (isteğe bağlı eşleşme):

`egrep '{{a}}?' {{dosya/yolu}}`

- Bir karakterin art arda 10 kez yinelendiği yerleri ara:

`egrep '{{a}}{10}' {{dosya/yolu}}`

- Bir karakterin art arda 3 ile 7 kez yinelendiği yerleri ara:

`egrep '{{a}}{3,7}' {{dosya/yolu}}`

- Listelenen seçeneklerden birini ara:

`egrep '{{kedi}}|{{köpek}}|{{fare}}' {{dosya/yolu}}`

- Daha büyük bir kalıbın içinde listelenen seçeneklerden birini ara:

`egrep 'c({{a}}|{{o}}|{{u}})p' {{dosya/yolu}}`

- Bir veya daha fazla kez yinelenen bir karakter grubunu ara:

`egrep '({{aeiou}})+' {{dosya/yolu}}`

- Standart karakter sınıflarını kullanarak ara (daha fazla bilgi için: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{dosya/yolu}}`
