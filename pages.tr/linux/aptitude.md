# aptitude

> Debian ve Ubuntu paket yönetim aracı.
> Daha fazla bilgi için: <https://manned.org/aptitude>.

- Kullanılabilir paket ve sürüm listesini senkronize et. Bu, herhangi bir aptitude komutunu uygulamadan önce çalıştırılmalıdır:

`sudo aptitude update`

- Yeni bir paket ve onun bağımlılıklarını kur:

`sudo aptitude install {{paket}}`

- Paket ara:

`aptitude search {{paket}}`

- İndirilmiş bir paket ara: (`?installed` bir aptitude arama ifadesidir):

`aptitude search '?installed({{paket}})'`

- Bir paket ve onun bağımlılıklarını kaldır:

`sudo aptitude remove {{paket}}`

- Yüklü paketleri son kullanılabilir sürümlerine yükselt:

`sudo aptitude upgrade`

- Yüklü paketleri yükle (`aptitude upgrade` gibi), gereksizleri sil ve yeni bağımlılıkları karşılamak üzere ek paketler kur:

`sudo aptitude full-upgrade`

- Bir paketin otomatik yükseltilmesini engellemek için onu beklemede tut:

`sudo aptitude hold '?installed({{paket}})'`
