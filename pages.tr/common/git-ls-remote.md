# git ls-remote

> Çevrimiçi depolardaki isim ve URL bazlı referansları sıralamaya yarayan Git komutu.
> İsim veya URL girilmemişse, varsayılan dal veya çevrimiçi dalın kökeni kullanılır.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-ls-remote>.

- Varsayılan çevrimiçi depodaki tüm referansları göster:

`git ls-remote`

- Varsayılan çevrimiçi depodaki yalnızca baş referanslarını göster:

`git ls-remote --heads`

- Varsayılan çevrimiçi depodaki yalnızca etiket referanslarını göster:

`git ls-remote --tags`

- Girilen isim veya URL'de bulunan çevrimiçi depodaki tüm referansları göster:

`git ls-remote {{depo_adresi}}`

- Bir çevrimiçi depodaki referansları belirtilen desene göre göster:

`git ls-remote {{depo_ismi}} "{{desen}}"`
