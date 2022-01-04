# dirs

> Dizin yığını görüntüler veya üzerinde oynama yapar.
> Dizin yığını, `pushd` ve `popd` komutlarıyla üzerinde oynama yapılabilen, son ziyaret edilen dizinleri gösteren bir listedir.
> Daha fazla bilgi: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Dizin yığınını her madde arasında boşluk olacak şekilde görüntüle:

`dirs`

- Dizin yığınını her satır başı tek madde olacak şekilde görüntüle:

`dirs -p`

- Dizin yığınında 0'dan başlamak üzere yalnızca nth girişini göster:

`dirs +{{N}}`

- Dizin yığınını temizle:

`dirs -c`
