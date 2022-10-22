# git describe

> Bir nesneye varolan referans üzerinden insanlar tarafından okunabilecek biçimde olan bir isim ver.
> Daha fazla bilgi: <https://git-scm.com/docs/git-describe>.

- Mevcut commit için (en son eklenmiş etiket, ilave commit'lerin sayısı ve kısaltılmış commit değerini içeren) özel bir isim oluştur:

`git describe`

- Kısaltılmış commit değeri için 4 haneli bir isim oluştur:

`git describe --abbrev={{4}}`

- Etiket referans yolu ile bir isim oluştur:

`git describe --all`

- Bir Git etiketini açıkla:

`git describe {{v1.0.0}}`

- Belirtilen daldaki son commit için bir isim oluştur:

`git describe {{dal_ismi}}`
