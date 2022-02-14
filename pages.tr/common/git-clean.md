# git clean

> Takip edilmeyen dosyaları çalışma ağacından sil.
> Daha fazla bilgi: <https://git-scm.com/docs/git-clean>.

- Git tarafından takip edilmeyen dosyaları sil:

`git clean`

- Git tarafından takip edilmeyen dosyaları etkileşimli bir nizamda sil:

`git clean -i`

- Hangi dosyaların silinmeye aday olduğunu onları silmeden göster:

`git clean --dry-run`

- Git tarafından takip edilmeyen dosyaları zorla zil:

`git clean -f`

- Git tarafından takip edilmeyen dizinleri zorla zil:

`git clean -fd`

- `.gitignore` ve `.git/info/exclude`'deki yoksayılan dosyalar dahiş olmak üzere takip edilmeyen dosyaları sil:

`git clean -x`
