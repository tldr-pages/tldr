# git rebase

> Bir daldan başka bir dalın üstüne commit'leri tekrar temeller.
> Sıklıkla bir dalı commit'leriyle beraber başka bir tabana "taşımak" için kullanılır.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-rebase>.

- Mevcut dalı belirtilen öbür dal üzerine temelle:

`git rebase {{yeni_taban_dal}}`

- Commit'lerin sıralanması, çıkartılması, birleştirilmesi veya modifiye edilmesine izin vermek için tekrar temellemeyi etkileşimli olacak şekilde başlat:

`git rebase -i {{hedef_taban_dalı_veya_commit_değeri}}`

- Bir birleştirme hatası tarafından durdurulan tekrar temelleme işlemini çekişen dosyaları düzenledikten sonra devam ettir:

`git rebase --continue`

- Birleştirme çatışmasından ötürü durdurulan tekrar temelleme işlemini çekişen commit'leri atlayarak devam ettir:

`git rebase --skip`

- Devam eden tekrar temelleme işlemini iptal et (örneğin birleştirmede çatışma yaşandığında):

`git rebase --abort`

- Mevcut dalın bir parçasını belirtilen eski tabandan yeni tabana taşı:

`git rebase --onto {{yeni_taban}} {{eski_taban}}`

- Son 3 commit'i etkileşimli olmayacak şekilde yeniden uygula:

`git rebase -i {{HEAD~5}}`

- Herhangi bir çatışmayı çalışan dal sürümünü kurtarmak üzere otomatik olarak çöz (`theirs` argümanı burada ters anlama sahip):

`git rebase -X theirs {{dal_ismi}}`
