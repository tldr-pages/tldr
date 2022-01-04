# gitlab-runner

> GitLab koşucuları için CLI aracı.
> Daha fazla bilgi: <https://docs.gitlab.com/runner/>.

- Bir koşucuyu kayıt ettir:

`sudo gitlab-runner register --url {{https://gitlab.ornek.com}} --registration-token {{token}} --name {{isim}}`

- Bir koşucuyu Docker çalıştırıcısıyla kayı ettir:

`sudo gitlab-runner register --url {{https://gitlab.ornek.com}} --registration-token {{token}} --name {{isim}} --executor {{docker}}`

- Bir koşucunun kaydını geri al:

`sudo gitlab-runner unregister --name {{isim}}`

- Koşucu servisinin durumunu görüntüle:

`sudo gitlab-runner status`

- Koşucu servisini yeniden başlat:

`sudo gitlab-runner restart`

- Kayıt edilen koşucuların GitLab'e bağlanabilme durumlarını kontrol et:

`sudo gitlab-runner verify`
