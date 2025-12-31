# echo

> Verilen argümanları yazdır.
> Ayrıca bakınız: `printf`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Bir metin mesajı yazdır. Not: Tırnak işaretleri isteğe bağlı:

`echo "{{Merhaba Dünya}}"`

- Ortam değişkenlerini kullanarak mesaj yazdır:

`echo "{{Path değişkenim $PATH}}"`

- Satır sonu karakteri olmadan mesaj yazdır:

`echo -n "{{Merhaba Dünya}}"`

- Dosyaya mesaj ekle:

`echo "{{Merhaba Dünya}}" >> {{dosya.txt}}`

- Ters eğik çizgi kaçış karakterlerinin (özel karakterlerin) yorumlanmasını etkinleştir:

`echo -e "{{Sütun 1\tSütun 2}}"`

- En son çalıştırılan komutun çıkış durumunu yazdır (Not: Windows Komut İstemi ve PowerShell’de eşdeğer komutlar sırasıyla `echo %errorlevel%` ve `$lastexitcode`'dur):

`echo $?`
