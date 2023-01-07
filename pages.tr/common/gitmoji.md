# gitmoji

> Commit'lerde emoji kullanmak içni interaktif bir komut satırı aracı.
> Daha fazla bilgi için: <https://github.com/carloscuesta/gitmoji-cli>.

- Commit sihirbazını çalıştır:

`gitmoji --commit`

- Git hook'u başlat (bu sayede `git commit` çalıştırıldığı zaman `gitmoji` otomatik olarak çalıştırılabilir):

`gitmoji --init`

- Git hook'u sil:

`gitmoji --remove`

- Tüm kullanılabilir emojileri ve açıklamalarını sırala:

`gitmoji --list`

- Belirtilen kelime sırası için emoji sırası ara:

`gitmoji --search {{kelime1}} {{kelime2}}`

- Ana depodan emojileri güncelle:

`gitmoji --update`

- Genel tercihleri düzenle:

`gitmoji --config`
