# mkdir

> Dizinleri oluştur ve izinlerini ayarla.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Belirtilen dizinleri oluştur:

`mkdir {{yol/dizin1 yol/dizin2 ...}}`

- Belirtilen dizinleri ve gerekiyorsa üst dizinlerini oluştur:

`mkdir {{[-p|--parents]}} {{yol/dizin1 yol/dizin2 ...}}`

- Belirtilen izinlerle dizinleri oluştur:

`mkdir {{[-m|--mode]}} {{u=rwx,g=rw,o=r}} {{yol/dizin1 yol/dizin2 ...}}`

- Birden fazla iç içe dizini özyinelemeli olarak oluştur:

`mkdir {{[-p|--parents]}} {{yol/{a,b}/{x,y,z}/{h,i,j}}}`
