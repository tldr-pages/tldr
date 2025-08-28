# adduser

> Kullanıcı ekleme yardımcısı
> Detaylı bilgi için bkz: <https://manned.org/man.tr/adduser.8>.

- Varsayılan ev diziniyle yeni bir kullanıcı oluşturun ve kullanıcının bir parola belirlemesini isteyin:

`adduser {{kullanıcı_adı}}`

- Ev dizini oluşturmadan yeni bir kullanıcı oluşturun:

`adduser --no-create-home {{kullanıcı_adı}}`

- Özel ev dizini yolunuzu kullanarak bir kullanıcı oluşturun:

`adduser --home {{ev/dizini/yolu}} {{kullanıcı_adı}}`

- Özel bir kabuğu giriş kabuğu olarak ayarlayarak bir kullanıcı oluşturun:

`adduser --shell {{kabuk/yolu}} {{kullanıcı_adı}}`

- Belirtilen gruba dahil olacak şekilde bir kullanıcı oluşturun:

`adduser --ingroup {{grup}} {{kullanıcı_adı}}`
