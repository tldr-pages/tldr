# git switch

> Git dalları arasında geçiş yap. Gir sürümü 2.23+ olmalıdır.
> Ayrıca benzer işlev gören `git checkout` komutuna bakılması önerilir.
> Daha fazla bilgi: <https://git-scm.com/docs/git-switch>.

- Varolan bir dala geç:

`git switch {{dal_ismi}}`

- Yeni bir dal yarat ve ona geç:

`git switch --create {{dal_ismi}}`

- Varolan commit üzerine yeni bir dal yarat ve ona geç:

`git switch --create {{dal_ismi}} {{commit}}`

- Önceki dala geç:

`git switch -`

- Bir dala geç ve tüm alt modülleri uyum için güncelle:

`git switch --recurse-submodules {{dal_ismi}}`

- Bir dala geç ve mevcut dal ile commit'lenmeyen değişiklikleri bu dal ile birleştir:

`git switch --merge {{dal_ismi}}`
