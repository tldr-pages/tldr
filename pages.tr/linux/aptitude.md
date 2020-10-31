# aptitude

> Debian ve Ubuntu paket yönetim aracı.

- Kullanılabilir paket ve sürüm listesini senkronize et. Bu, herhangi bir aptitude komutunu uygulamadan önce çalıştırılmalıdır:

`aptitude update`

- Yeni bir paket ve onun bağımlılıklarını kur:

`aptitude install {{package}}`

- Paket ara:

`aptitude search {{package}}`

- İndirilmiş bir paket ara: (`?installed` bir aptitude arama ifadesidir):

`aptitude search '?installed({{package}})'`

- Bir paket ve onun bağımlılıklarını kaldır:

`aptitude remove {{package}}`

- Yüklü paketleri son kullanılabilir sürümlerine yükselt:

`aptitude upgrade`

- Yüklü paketleri yükle (`aptitude upgrade` gibi), gereksizleri sil ve yeni bağımlılıkları karşılamak üzere ek paketler kur:

`aptitude full-upgrade`

- Bir paketin otomatik yükseltilmesini engellemek için onu beklemede tut:

`aptitude hold '?installed({{package}})'`
