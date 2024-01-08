# git stash

> Yerel Git düzenlemelerini geçici bir alanda sakla.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-stash>.

- Yeni (izlenmeyen) dosyalar hariç mevcut değişiklikleri sakla:

`git stash push -m {{keyfi_saklama_mesajı}}`

- Yeni (izlenmeyen) dosyalar dahil mevcut değişiklikleri sakla:

`git stash -u`

- Değiştirilen dosyaların parçalarını etkileşimli şekilde seçip sakla:

`git stash -p`

- Tüm saklananları göster (saklanan ismi, bağlı olduğu dal ve mesaj gösterilir):

`git stash list`

- Bir saklananı uygula (varsayılan son saklanandır ve stash@{0} olarak belirtilir):

`git stash apply {{keyfi_saklanan_veya_commit_ismi}}`

- Bir saklananı uygula (varsayılan stash@{0}), ve eğer uygulanması sıkıntı çıkarmıyorsa onu saklanan listesinden kaldır:

`git stash pop {{keyfi_saklanan_ismi}}`

- Tüm saklananları bırak:

`git stash clear`
