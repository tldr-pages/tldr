# pio հաշիվ

> Կառավարեք ձեր PlatformIO հաշիվը:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/account/>:.

- Գրանցեք նոր PlatformIO հաշիվ.:

`pio account register {{[-u|--username]}} {{username}} {{[-e|--email]}} {{email}} {{[-p|--password]}} {{password}} --firstname {{firstname}} --lastname {{lastname}}`

- Ընդմիշտ ջնջեք ձեր PlatformIO հաշիվը և հարակից տվյալները.:

`pio account destroy`

- Մուտք գործեք ձեր PlatformIO հաշիվ.:

`pio account login {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Դուրս եկեք ձեր PlatformIO հաշվից.:

`pio account logout`

- Թարմացրեք ձեր PlatformIO պրոֆիլը.:

`pio account update {{[-u|--username]}} {{username}} {{[-e|--email]}} {{email}} --firstname {{firstname}} --lastname {{lastname}} --current-password {{password}}`

- Ցույց տալ մանրամասն տեղեկատվություն ձեր PlatformIO հաշվի մասին.:

`pio account show`

- Վերականգնել ձեր գաղտնաբառը՝ օգտագործելով ձեր օգտանունը կամ էլ.:

`pio account forgot {{[-u|--username]}} {{username_or_email}}`
