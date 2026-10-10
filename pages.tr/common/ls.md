# ls

> Dizin içeriğini listele.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Dosyaları satır başına bir tane olacak şekilde listele:

`ls -1`

- Gizli dosyalar dahil tüm dosyaları listele:

`ls {{[-a|--all]}}`

- Dosyaları, türünü belirten bir son ek simgesiyle listele (dizin/, sembolik_bağlantı@, çalıştırılabilir*, ...):

`ls {{[-F|--classify]}}`

- Tüm dosyaları uzun biçimde listele (izinler, sahiplik, boyut ve değiştirilme tarihi):

`ls {{[-la|-l --all]}}`

- Dosyaları uzun biçimde, boyutları okunabilir birimlerle (KiB, MiB, GiB) göstererek listele:

`ls {{[-lh|-l --human-readable]}}`

- Dosyaları uzun biçimde, boyuta göre (azalan) sıralayarak özyinelemeli olarak listele:

`ls {{[-lSR|-lS --recursive]}}`

- Dosyaları uzun biçimde, değiştirilme zamanına göre ve ters sırada (en eski önce) listele:

`ls {{[-ltr|-lt --reverse]}}`

- Yalnızca dizinleri listele:

`ls {{[-d|--directory]}} */`
