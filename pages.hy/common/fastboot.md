# fastboot

> Շփվեք միացված Android սարքերի հետ bootloader ռեժիմում (մի տեղ ԱԶԲ-ն չի աշխատում):.
> Լրացուցիչ տեղեկություններ. <https://cs.android.com/android/platform/superproject/+/main:system/core/fastboot>:.

- Բացեք bootloader-ը.:

`fastboot oem unlock`

- Վերակողպեք բեռնիչը.:

`fastboot oem lock`

- Վերագործարկեք սարքը «fastboot» ռեժիմից նորից «fastboot» ռեժիմի մեջ.:

`fastboot reboot bootloader`

- Ցույց տալ տվյալ պատկերը.:

`fastboot flash {{path/to/file.img}}`

- Ֆլեշ մաքսային վերականգնման պատկեր.:

`fastboot flash recovery {{path/to/file.img}}`

- Ցուցակել միացված սարքերը.:

`fastboot devices`

- Ցուցադրել սարքի բոլոր տեղեկությունները.:

`fastboot getvar all`
