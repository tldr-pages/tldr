# git fsck

> Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula.
> Düzenleme yapılması tavsiye edilmez. Geçersiz düğümleri çözmek için `git gc` komutu önerilir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-fsck>.

- Mevcut depoyu kontrol et:

`git fsck`

- Bulunan tüm etiketleri sırala:

`git fsck --tags`

- Bulunan tüm kök düğümleri sırala:

`git fsck --root`
