# git subtree

> Proje bağımlılıklarını alt proje olarak yönetmeye yarayan bir araç.
> Daha fazla bilgi için: <https://manned.org/git-subtree>.

- Bir Git deposunu alt ağaç olarak ekle:

`git subtree add {{[-P|--prefix]}} {{dizin/konumu}} --squash {{depo_url'si}} {{dal_ismi}}`

- Alt ağaç deposunu son commit'ine güncelle:

`git subtree pull {{[-P|--prefix]}} {{dizin/konumu}} {{depo_url'si}} {{dal_ismi}}`

- Son alt ağaca kadar olan değişiklikleri alt ağaca commit'le:

`git subtree merge {{[-P|--prefix]}} {{dizin/konumu}} --squash {{depo_url'si}} {{dal_ismi}}`

- Commit'leri bir alt ağaç deposuna yolla:

`git subtree push {{[-P|--prefix]}} {{dizin/konumu}} {{depo_url'si}} {{dal_ismi}}`

- Bir alt ağacın geçmişinden yeni bir proje geçmişi dışa aktar:

`git subtree split {{[-P|--prefix]}} {{dizin/konumu}} {{depo_url'si}} {{[-b|--branch]}} {{dal_ismi}}`
