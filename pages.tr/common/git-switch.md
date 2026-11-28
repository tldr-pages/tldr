# git switch

> Git dalları arasında geçiş yap. Git sürümü 2.23+ olmalıdır.
> Ayrıca bakınız: `git checkout`.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-switch>.

- Varolan bir dala geç:

`git switch {{dal_ismi}}`

- Yeni bir dal yarat ve ona geç:

`git switch {{[-c|--create]}} {{dal_ismi}}`

- Varolan commit üzerine yeni bir dal yarat ve ona geç:

`git switch {{[-c|--create]}} {{dal_ismi}} {{commit}}`

- Önceki dala geç:

`git switch -`

- Bir dala geç ve tüm alt modülleri uyum için güncelle:

`git switch --recurse-submodules {{dal_ismi}}`

- Bir dala geç ve mevcut dal ile commit'lenmeyen değişiklikleri bu dal ile birleştir:

`git switch {{[-m|--merge]}} {{dal_ismi}}`

- Bir etikete veya commit'e geç:

`git switch {{[-d|--detach]}} {{etiket|commit}}`

- Başka bir uzak bağlantıdaki dala geç:

`git switch {{[-t|--track]}} {{uzak_bağlantı}}/{{dal_ismi}}`
