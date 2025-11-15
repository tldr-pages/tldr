# dirname

> Belirtilen dosya veya yolun ana dizinini hesaplar.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Belirtilen yolun ana dizinini hesapla:

`dirname {{dosya_veya_dizine/giden/yol}}`

- Birden çok yolun ana dizinini hesapla:

`dirname {{dosya_veya_dizine/giden/yol_1}} {{dosya_veya_dizine/giden/yol_2}}`

- Komut çıktısını yeni satır yerine NUL karakteri ile sınırlandırma (`xargs` yazılımı ile kullanırken işe yarar):

`dirname {{[-z|--zero]}} {{dosya_veya_dizine/giden/yol_1}} {{dosya_veya_dizine/giden/yol_2}}`
