# git instaweb

> gitweb sunucusu başlatmak için yardımcı araç.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-instaweb>.

- Mevcut Git deposu için bir gitweb sunucusu başlat:

`git instaweb --start`

- Yalnızca yerel ağda başlat:

`git instaweb --start --local`

- Belirtilmiş bir port'da başlat:

`git instaweb --start --port {{1234}}`

- Belirtilmiş bir HTTP daemon'u kullan:

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Ayrıca bir ağ tarayıcısını otomatik olarak başlat:

`git instaweb --start --browser`

- Çalışan mevcut gitweb sunucusunu durdur:

`git instaweb --stop`

- Çalışan mevcut gitweb sunucusunu yeniden başlat:

`git instaweb --restart`
