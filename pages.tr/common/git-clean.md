# git clean

> Takip edilmeyen dosyaları çalışma ağacından sil.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-clean>.

- Git tarafından takip edilmeyen dosyaları etkileşimli bir nizamda sil:

`git clean {{[-i|--interactive]}}`

- Hangi dosyaların silinmeye aday olduğunu onları silmeden göster:

`git clean {{[-n|--dry-run]}}`

- Git tarafından takip edilmeyen dosyaları zorla sil:

`git clean {{[-f|--force]}}`

- Git tarafından takip edilmeyen dizinleri zorla sil:

`git clean {{[-f|--force]}} -d`

- Sadece belirli yollarla ya da `glob` desenleriyle eşleşen takip edilmeyen dosyaları sil:

`git clean {{[-f|--force]}} -- {{yol/dizin}} '{{*.uzantı}}'`

- Verilen desenlerle eşleşenler dışındaki takip edilmeyen dosyaları sil:

`git clean {{[-f|--force]}} {{[-e|--exclude]}} '{{*.uzantı}}' {{[-e|--exclude]}} {{yol/dizin}}/`

- Takip edilmeyen dosyaları ve hariç tutulan dosyaları (`.gitignore` ve `.git/info/exclude` içinde listelenenler) sil:

`git clean {{[-f|--force]}} -x`
