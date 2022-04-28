# minetestserver

> Çok oyunculu sınırsız dünyalı bloklu sanbox sunucusu.
> Ayrıca `minetest` sayfasına bakılması önerilir.
> Daha fazla bilgi: <https://wiki.minetest.net/Setting_up_a_server>.

- Sunucuyu başlar:

`minetestserver`

- Müsait dünyaları sırala:

`minetestserver --world list`

- Yüklenecek dünya ismini belirt:

`minetestserver --world {{dunya_ismi}}`

- Müsait oyun ID'lerini sırala:

`minetestserver --gameid list`

- Kullanılacak oyunu belirt:

`minetestserver --gameid {{oyun_id'si}}`

- Belirtilmiş bir port'u dinle:

`minetestserver --port {{34567}}`

- Başka bir veritabanı yazılımına göç et:

`minetestserver --migrate {{sqlite3|leveldb|redis}}`

- Sunucuyu başlattıktan sonra interaktif bir terminal aç:

`minetestserver --terminal`
