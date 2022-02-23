# xfce4-terminal

> XFCE4 terminal öykünücüsü.
> Daha fazla bilgi: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- Yeni bir terminal penceresi aç:

`xfce4-terminal`

- Başlangıç başlığı belirle:

`xfce4-terminal --initial-title "{{başlangıç_başlığı}}"`

- Mevcut terminal penceresinde yeni bir sekme aç:

`xfce4-terminal --tab`

- Yeni bir terminal penceresini belirlenen bir komutu çalıştırarak aç:

`xfce4-terminal --command "{{argümanlı_komut}}"`

- Çalıştırılan komutun çalışmayı kesme durumunda dahi terminali kapama:

`xfce4-terminal --command "{{argümanlı_komut}}" --hold`

- Her birinde farklı komut çalışacak birçok yeni sekme aç:

`xfce4-terminal --tab --command "{{komut_a}}" --tab --command "{{komut_b}}"`
