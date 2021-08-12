# rpm

> Manager de pachete RPM.

- Arată versiunea pachetului httpd:

`rpm -q {{httpd}}`

- Lista versiunilor tuturor pachetelor de potrivire:

`rpm -qa '{{mariadb*}}'`

- Instalați forțat un pachet, indiferent de versiunile instalate în prezent:

`rpm -U {{package_name.rpm}} --force`

- Identificarea proprietarului unui fișier și arată versiunea pachetului:

`rpm -qf {{/etc/postfix/main.cf}}`

- Lista fișierelor deținute de pachete:

`rpm -ql {{kernel}}`

- Arată scriptlete dintr-un fișier RPM:

`rpm -qp --scripts {{package_name.rpm}}`

- Afișează fișierele modificate, lipsă și/sau incorect instalate ale pachetelor potrivite:

`rpm -Va '{{php-*}}'`
