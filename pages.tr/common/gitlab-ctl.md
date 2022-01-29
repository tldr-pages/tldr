# gitlab-ctl

> Çok amaçlı GitLab yönetim CLI aracı.
> Daha fazla bilgi: <https://docs.gitlab.com/omnibus/maintenance/>.

- Tüm servislerin durumunu görüntüle:

`sudo gitlab-ctl status`

- Belirtilen servisin durumunu görüntüle:

`sudo gitlab-ctl status {{nginx}}`

- Tüm servisleri yeniden başlat:

`sudo gitlab-ctl restart`

- Belirtilen servisi yeniden başlat:

`sudo gitlab-ctl restart {{nginx}}`

- Tüm servislerin kaydını görüntüle ve `Ctrl + C` basılana kadar okumaya devam et:

`sudo gitlab-ctl tail`

- Belirtilen servisin kaydını görüntüle:

`sudo gitlab-ctl tail {{nginx}}`
