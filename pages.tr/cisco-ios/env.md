# env

> Ortamı göster veya bir programı değiştirilmiş bir ortamda çalıştır.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Ortamı göster:

`env`

- Bir program çalıştır. Programın yolunu bulmak için betiklerde shebang (#!) sonrasında sıkça kullanılır:

`env {{program}}`

- Ortamı temizle ve bir program çalıştır:

`env {{[-i|--ignore-environment]}} {{program}}`

- Bir değişkeni ortamdan kaldır ve bir program çalıştır:

`env {{[-u|--unset]}} {{değişken}} {{program}}`

- Bir değişken ayarla ve bir program çalıştır:

`env {{değişken}}={{değer}} {{program}}`

- Bir veya daha fazla değişken ayarla ve bir program çalıştır:

`env {{değişken1=değer değişken2=değer değişken3=değer ...}} {{program}}`

- Bir programı farklı bir adla çalıştır:

`env {{[-a|--argv0]}} {{özel_ad}} {{program}}`
