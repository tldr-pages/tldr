# mount

> Tek bir dizindeki tüm dosya sistemlerine erişin.
> Daha fazla bilgi için: <https://manned.org/mount.8>.

- Bağlı olan tüm dosya sistemlerini görüntüleyin:

`mount`

- Bir aygıtı bir dizine bağlayın:

`mount {{aygıt_dosyası/yolu}} {{hedef_dizin/yolu}}`

- Bir aygıtı dizine eğer o dizin yoksa oluşturarak bağlayın:

`mount {{[-m|--mkdir]}} {{aygıt_dosyası/yolu}} {{hedef_dizin/yolu}}`

- Bir aygıtı bir dizine özel kullanıcı için bağlayın:

`mount {{[-o|--options]}} uid={{kullanıcı_id}},gid={{grup_id}} {{aygıt_dosyası/yolu}} {{hedef_dizin/yolu}}`

- Bir CD-ROM aygıtını (dosya tipi ISO9660) `/cdrom`'a bağlayın (salt okunur):

`mount {{[-t|--types]}} {{iso9660}} {{[-o|--options]}} ro {{/dev/cdrom}} {{/cdrom}}`

- `/etc/fstab`'da tanımlanmış olan tüm dosya sistemlerini bağlayın:

`mount {{[-a|--all]}}`

- `/etc/fstab`'da bahsedilen özel bir dosya sistemini bağlayın (örneğin `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount {{/my_drive}}`

- Bir dizini başka bir dizine bağlayın:

`mount {{[-B|--bind]}} {{eski_dizin/yolu}} {{yeni_dizin/yolu}}`
