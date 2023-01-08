# svccfg

> Servis yapılandırmalarını içe aktar, dışa aktar ve düzenle.
> Daha fazla bilgi için: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Yapılandırma dosyasını değerlendir:

`svccfg validate {{smf.xml}}`

- Servis yapılandırma dosyalarını belirtilen dosyaya yazılacak şekilde dışa aktar:

`svccfg export {{servisismi}} > {{smf.xml}}`

- Dosyadan servis yapılandırmalarını içe aktar/güncelle:

`svccfg import {{smf.xml}}`
