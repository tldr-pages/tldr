# git credential

> Kullanıcı kimlik bilgilerini kurtar ve sakla.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-credential>.

- Kimlik bilgilerini, kullanıcı ismi ve parolayı konfigürasyon dosyası aracılığıyla kurtararak göster:

`echo "{{url=http://örnek.com}}" | git credential fill`

- Kimlik bilgilerini sonra kullanma amacıyla saklamak için bütün yapılandırılmış kimlik yardımcılarına gönder:

`echo "{{url=http://örnek.com}}" | git credential approve`

- Belirtilen kimlik bilgisini bütün yapılandırılmış kimlik yardımcılarından temizle:

`echo "{{url=http://örnek.com}}" | git credential reject`
