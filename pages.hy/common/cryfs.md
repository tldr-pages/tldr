# cryfs

> Կրիպտոգրաֆիկ ֆայլային համակարգ ամպի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/cryfs>:.

- Տեղադրեք կոդավորված ֆայլային համակարգ: Նախաստորագրման մոգը կսկսվի առաջին կատարման ժամանակ.:

`cryfs {{path/to/cipher_directory}} {{path/to/mount_point}}`

- Ապամոնտաժել կոդավորված ֆայլային համակարգը.:

`cryfs-unmount {{path/to/mount_point}}`

- Ավտոմատ ապամոնտաժել տասը րոպե անգործությունից հետո.:

`cryfs --unmount-idle {{10}} {{path/to/cipher_directory}} {{path/to/mount_point}}`

- Ցուցակեք աջակցվող ծածկագրերը.:

`cryfs --show-ciphers`
