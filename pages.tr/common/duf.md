# duf

> Disk Kullanımı/Boş Alan Aracı (Disk Usage/Free Utility).
> Ayrıca bakınız: `ncdu`, `df`.
> Daha fazla bilgi: <https://github.com/muesli/duf#usage>.

- Erişilebilir aygıtları listele:

`duf`

- Her şeyi listele (sözde, yinelenen veya erişilemeyen dosya sistemleri gibi):

`duf --all`

- Yalnızca belirtilen aygıtları veya bağlama noktalarını göster:

`duf {{dizin1/yolu dizin2/yolu ...}}`

- Çıktıyı belirtilen bir ölçüte göre sırala:

`duf --sort {{size|used|avail|usage}}`

- Belirli dosya sistemlerini göster veya gizle:

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- Çıktıyı anahtara göre sırala:

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- Temayı değiştir (`duf` doğru temayı algılayamazsa):

`duf --theme {{dark|light}}`
