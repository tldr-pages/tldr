# mosquitto_passwd

> Կառավարեք գաղտնաբառի ֆայլերը մոծակների համար:.
> Տես նաև՝ `mosquitto`:.
> Լրացուցիչ տեղեկություններ. <https://mosquitto.org/man/mosquitto_passwd-1.html>:.

- Նոր օգտատեր ավելացրեք գաղտնաբառի ֆայլին (կպահանջվի մուտքագրել գաղտնաբառը).:

`mosquitto_passwd {{path/to/password_file}} {{username}}`

- Ստեղծեք գաղտնաբառի ֆայլը, եթե այն արդեն գոյություն չունի.:

`mosquitto_passwd -c {{path/to/password_file}} {{username}}`

- Փոխարենը ջնջեք նշված օգտվողի անունը.:

`mosquitto_passwd -D {{path/to/password_file}} {{username}}`

- Թարմացրեք հին պարզ տեքստային գաղտնաբառի ֆայլը հաշված գաղտնաբառի ֆայլի.:

`mosquitto_passwd -U {{path/to/password_file}}`
