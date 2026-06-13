# dnf config-manager

> Fedora tabanlı sistemlerde DNF yapılandırma seçeneklerini ve depoları yönetmek için kullanılır.
> Varsayılan olarak `dnf` ile gelmez, `dnf-plugins-core` ile desteklenir.
> Ayrıca bakınız: `dnf`.
> Daha fazla bilgi için: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>.

- Bir URL'den depo ekle (ve etkinleştir):

`dnf config-manager --add-repo={{repository_url}}`

- Mevcut yapılandırma değerlerini yazdır:

`dnf config-manager --dump`

- Belirli bir depoyu etkinleştir:

`dnf config-manager {{[--enable|--set-enabled]}} {{repository_id}}`

- Belirtilen depoları devre dışı bırak:

`dnf config-manager {{[--disable|--set-disabled]}} {{repository_id1 repository_id2 ...}}`

- Bir depo için yapılandırma seçeneği ayarla:

`dnf config-manager --setopt={{option}}={{value}}`

- Yardımı görüntüle:

`dnf config-manager --help-cmd`
