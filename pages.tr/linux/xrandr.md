# xrandr

> Bir ekran için boyut, yön ve/veya çıkış yansımasını ayarla.
> Daha fazla bilgi için: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Sistemin mevcut durumunu göster (bilinen ekranlar, çözünürlükler, ...):

`xrandr --query`

- Bağlantısı kesilmiş çıkışları devre dışı bırak ve bağlanmış olanları varsayılan ayarlar ile devreye sok:

`xrandr --auto`

- DisplayPort 1'in çözünürlük ve yenileme hızını 1920x1080, 60Hz olarak değiştir:

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- HDMI2'nin çözünürlüğünü 1280x1024'e değiştirip, DP1'in sağına koy:

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- VGA1 çıkışını devre dışı bırak:

`xrandr --output {{VGA1}} --off`

- LVDS1 için parlaklığı 50% yap:

`xrandr --output {{LVDS1}} --brightness {{0.5}}`
