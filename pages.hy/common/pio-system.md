# pio համակարգ

> Համակարգի տարբեր հրամաններ PlatformIO-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/system/>:.

- Տեղադրեք կեղևի ավարտը ընթացիկ կեղևի համար (աջակցում է Bash, fish, Zsh և PowerShell):

`pio system completion install`

- Տեղահանել կեղևի ավարտը ընթացիկ կեղևի համար.:

`pio system completion uninstall`

- Ցուցադրել ամբողջ համակարգի PlatformIO տեղեկատվությունը.:

`pio system info`

- Հեռացրեք չօգտագործված PlatformIO տվյալները.:

`pio system prune`

- Հեռացրեք միայն քեշավորված տվյալները.:

`pio system prune --cache`

- Թվարկեք չօգտագործված PlatformIO տվյալները, որոնք կհեռացվեն, բայց իրականում չեն ջնջվում դրանք.:

`pio system prune --dry-run`
