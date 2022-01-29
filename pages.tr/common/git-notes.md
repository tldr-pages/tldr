# git notes

> Nesne notları ekle veya incele.
> Daha fazla bilgi: <https://git-scm.com/docs/git-notes>.

- Tüm notları ve bağlı oldukları nesneleri sırala:

`git notes list`

- Belirtilen nesneye bağlanan tüm notları sırala (varsayılan HEAD'dedir):

`git notes list [{{nesne}}]`

- Belirtilen nesneye bağlanan tüm notları göster (varsayılan HEAD'dedir):

`git notes show [{{nesne}}]`

- Belirtilen nesneye bir not ekle (varsayılan metin editörü açılır):

`git notes append {{nesne}}`

- Mesajı belirterek belirtilen nesneye bir not ekle:

`git notes append --message="{{messaj_yazısı}}"`

- Varolan bir notu düzenle (varsayılan HEAD'dedir):

`git notes edit [{{nesne}}]`

- Bir notu bir nesneden öbürüne kopyala:

`git notes copy {{kaynak_nesne}} {{hedef_nesne}}`

- Belirtilen nesneye eklenen tüm notları sil:

`git notes remove {{nesne}}`
