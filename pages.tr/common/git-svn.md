# git svn

> Bir alt sürüm deposu ve Git arasında çift yönlü operasyon.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-svn>.

- Bit SVN deposunu klonla:

`git svn clone {{https://ornek.com/altsürüm_deposu}} {{yerel_dizin}}`

- Bir SVN deposunu belirtilen düzenleme numarasından başlayarak klonla:

`git svn clone -r{{1234}}:HEAD {{https://svn.ornek.net/altsürüm/depo}} {{yerel_dizin}}`

- Uzak SVN deposundan yerel klonu güncelle:

`git svn rebase`

- Git HEAD'i değiştirmeden uzak SVN deposundan güncellemeleri çek:

`git svn fetch`

- SVN deposuna geri commit'le:

`git svn dcommit`
