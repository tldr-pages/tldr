# git stash

> Yerel Git düzenlemelerini geçici bir alanda sakla.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-stash>.

- Mevcut commit'lenmemiş değişiklikleri sakla:

`git stash`

- Yeni (izlenmeyen) dosyalar dahil mevcut değişiklikleri sakla:

`git stash {{[-u|--include-untracked]}}`

- Değiştirilen dosyaların parçalarını etkileşimli şekilde seçip sakla:

`git stash {{[-p|--patch]}}`

- Tüm saklananları listele:

`git stash list`

- Saklananın, oluşturulduğu andaki commit'e göre farkını yama (patch) olarak göster:

`git stash show {{[-p|--patch]}}`

- Bir saklananı uygula ve uygulanması çakışmaya yol açmıyorsa onu saklananlar listesinden kaldır:

`git stash pop`

- En son saklananı sil:

`git stash drop`

- Tüm saklananları sil:

`git stash clear`
