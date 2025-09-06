# git checkout-index

> Dosyaları indeksten çalışma ağacına kopyala.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-checkout-index>.

- Son commit'den beri silinen dosyaları geri döndür:

`git checkout-index --all`

- Son commit'den beri silinen veya değiştirilen dosyaları geri döndür:

`git checkout-index --all --force`

- Son commit'den beri değiştirilen dosyaları geri döndür ancak silinenleri yoksay:

`git checkout-index --all --force --no-create`

- Tüm ağacın bir kopyasını belirtilen dizinde dışa aktar (sondaki eğik çizgi önemli):

`git checkout-index --all --force --prefix={{dışa/aktarılacak/dizin/}}`
