# docker images

> Docker imgelerini yönet.
> Daha fazla bilgi için: <https://docs.docker.com/engine/reference/commandline/images/>.

- Tüm Docker imgelerini listele:

`docker images`

- Orta düzeyler de dahil olmak üzere tüm Docker imgelerini sırala:

`docker images --all`

- Çıktıyı sessiz modda (yalnızca sayısal ID'ler olarak) sırala:

`docker images --quiet`

- Herhangi bir konteyner tarafından kullanılmayan tüm Docker imgelerini sırala:

`docker images --filter dangling=true`

- İsminde belirtilen dizeleri taşıyan imgeleri sırala:

`docker images "{{*isim*}}"`
