# grub2-mkpasswd-pbkdf2

> GRUB için hashlenmiş parola oluşturun.
> Daha fazla bilgi için: <https://manned.org/grub2-mkpasswd-pbkdf2>.

- GRUB2 için PBKDF2 kullanarak parola hash'i oluşturun ve çıktıya yazdırın:

`sudo grub2-mkpasswd-pbkdf2 {{[-c|--iteration-count]}} {{pbkdf2_yenileme_sayısı}} {{[-s|--salt]}} {{salt_uzunluğu}}`
