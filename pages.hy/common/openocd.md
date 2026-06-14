# openocd

> Վրիպազերծել և ծրագրավորել ներկառուցված համակարգերը OpenOCD-ով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/openocd>:.

- Կցեք OpenOCD նիստը կազմաձևման ֆայլով տախտակին.:

`openocd {{[-f|--file]}} {{config_file.cfg}}`

- Կցեք OpenOCD նիստը բազմաթիվ կազմաձևման ֆայլերով տախտակին.:

`openocd {{[-f|--file]}} {{config_file1.cfg}} {{[-f|--file]}} {{config_file2.cfg}}`

- Կցեք OpenOCD նիստը տախտակին՝ կազմաձևման ֆայլերով և սերվերի գործարկման ժամանակ կատարվող հրամանների ցանկով.:

`openocd {{[-f|--file]}} {{config_file.cfg}} {{[-c|--command]}} "{{command}}"`

- Օգտագործեք կազմաձևման ֆայլերը նշված ճանապարհով.:

`openocd {{[-s|--search]}} {{path/to/search}} {{[-f|--file]}} {{config_file.cfg}}`

- [Ինտերակտիվ] OpenOCD-ի գործարկումից հետո միացրեք GDB-ն OpenOCD լռելյայն 3333 պորտին:

`target extended-remote localhost`

- Ցուցակեք կայքի ամբողջ սկրիպտային գրադարանը.:

`ls /usr/local/share/openocd/scripts`
