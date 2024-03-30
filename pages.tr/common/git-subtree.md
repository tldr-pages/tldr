# git subtree

> Proje bağımlılıklarını alt proje olarak yönetmeye yarayan bir araç.
> Daha fazla bilgi için: <https://manpages.debian.org/latest/git-man/git-subtree.1.html>.

- Bir Git deposunu alt ağaç olarak ekle:

`git subtree add --prefix={{dizin/konumu}} --squash {{depo_url'si}} {{dal_ismi}}`

- Alt ağaç deposunu son commit'ine güncelle:

`git subtree pull --prefix={{dizin/konumu}} {{depo_url'si}} {{dal_ismi}}`

- Son alt ağaca kadar olan değişiklikleri alt ağaca commit'le:

`git subtree merge --prefix={{dizin/konumu}} --squash {{depo_url'si}} {{dal_ismi}}`

- Commit'leri bir alt ağaç deposuna yolla:

`git subtree push --prefix={{dizin/konumu}} {{depo_url'si}} {{dal_ismi}}`

- Bir alt ağacın geçmişinden yeni bir proje geçmişi dışa aktar:

`git subtree split --prefix={{dizin/konumu}} {{depo_url'si}} -b {{dal_ismi}}`
