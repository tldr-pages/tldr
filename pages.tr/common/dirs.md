# dirs

> Dizin yığını görüntüler veya üzerinde oynama yapar.
> Dizin yığını, `pushd` ve `popd` komutlarıyla üzerinde oynama yapılabilen, son ziyaret edilen dizinleri gösteren bir listedir.
> Ayrıca bakınız: `pushd`, `popd`.
> Daha fazla bilgi için: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Dizin yığınını her madde arasında boşluk olacak şekilde görüntüle:

`dirs`

- Dizin yığınını her satır başı tek madde olacak şekilde görüntüle:

`dirs -p`

- Dizin yığınını numaralı bir liste olarak görüntüle:

`dirs -v`

- Dizin yığınını tilde (`~`) öneki olmadan görüntüle:

`dirs -l`

- Dizin yığınında 0'dan başlamak üzere yalnızca `n`. girişi göster (yalnızca Bash):

`dirs +{{n}}`

- Dizin yığınında sondan itibaren 0'dan başlamak üzere yalnızca `n`. girişi göster (yalnızca Bash):

`dirs -{{n}}`

- Dizin yığınını temizle:

`dirs -c`
