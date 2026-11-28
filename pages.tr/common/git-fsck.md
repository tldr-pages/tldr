# git fsck

> Git depo indeksindeki düğümlerin geçerliliğini ve bağlantılarını doğrula.
> Not: Herhangi bir değişiklik yapmaz.
> Ayrıca bakınız: `git gc`.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-fsck>.

- Mevcut depoyu kontrol et:

`git fsck`

- Bulunan tüm etiketleri sırala:

`git fsck --tags`

- Bulunan tüm kök düğümleri sırala:

`git fsck --root`

- Erişilemeyen ve sarkan (dangling) tüm nesneleri göster, reflog'ları yok say ve tam bütünlük denetimi yap:

`git fsck --dangling --no-reflogs --unreachable --full`

- Yalnızca bağlantıları kontrol et (nesne bütünlüğü doğrulamasını atla):

`git fsck --connectivity-only`
