# su

> Kabuk ortamında başka bir kullanıcıya geçiş yapın.

- Süper kullanıcıya geçin (kök şifresi gerektirir):

`su`

- Belirli bir kullanıcıya geçin (kullanıcının şifresini gerektirir):

`su {{kullanıcıadı}}`

- Belirli bir kullanıcıya geçin ve tam oturum açma kabuğunu simüle edin:

`su - {{kullanıcıadı}}`

- Başka bir kullanıcı olarak bir komut çalıştırın:

`su - {{kullanıcıadı}} -c "{{komut}}"`
