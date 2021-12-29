# git checkout

> Bulunulan dalı değiştir veya çalışma ağaçlarını onar.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-checkout>.

- Yeni bir dal oluştur ve bu dala geç:

`git checkout -b {{dal_ismi}}`

- Belirtilen bir referansa (dal, uzak/dal, etiket gibi) dayanacak şekilde yeni bir dal oluştur ve bu dala geç:

`git checkout -b {{dal_ismi}} {{referans}}`

- Varolan yerel bir dala geç:

`git checkout {{dal_ismi}}`

- En son kontrol edilmiş olan dala geç:

`git checkout -`

- Uzak bağlantıdaki varolan bir dala geç:

`git checkout --track {{uzak_bağlantı_adresi}}/{{dal_ismi}}`

- Mevcut dizindeki sahnelenmemiş tüm değişiklikleri ayır (geri alma benzeri bir komut için `git reset` komutu önerilir):

`git checkout .`

- Sahnelenmemiş değişiklikleri belirtilen dosyaya ayır:

`git checkout {{dosya_ismi}}`

- Mevcut dizindeki bir dosyayı, belirtilen dalda commit edilmiş sürümü ile değiştirin:

`git checkout {{dal_ismi}} -- {{dosya_ismi}}`
