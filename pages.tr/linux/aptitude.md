# aptitude

> Debian ve Ubuntu paket yönetim aracı.
> Daha fazla bilgi için: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Kullanılabilir paket ve sürüm listesini senkronize et. Bu, herhangi bir aptitude komutunu uygulamadan önce çalıştırılmalıdır:

`aptitude update`

- Yeni bir paket ve onun bağımlılıklarını kur:

`aptitude install {{paket}}`

- Paket ara:

`aptitude search {{paket}}`

- İndirilmiş bir paket ara: (`?installed` bir aptitude arama ifadesidir):

`aptitude search '?installed({{paket}})'`

- Bir paket ve onun bağımlılıklarını kaldır:

`aptitude remove {{paket}}`

- Yüklü paketleri son kullanılabilir sürümlerine yükselt:

`aptitude upgrade`

- Yüklü paketleri yükle (`aptitude upgrade` gibi), gereksizleri sil ve yeni bağımlılıkları karşılamak üzere ek paketler kur:

`aptitude full-upgrade`

- Bir paketin otomatik yükseltilmesini engellemek için onu beklemede tut:

`aptitude hold '?installed({{paket}})'`
