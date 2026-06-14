# f3fix

> Խմբագրել կեղծ ֆլեշ կրիչի բաժանման աղյուսակը:.
> Տես նաև՝ `f3probe`, `f3write`, `f3read`:.
> Լրացուցիչ տեղեկություններ. <https://oss.digirati.com.br/f3/>:.

- Լրացրեք կեղծ ֆլեշ կրիչը մեկ բաժանմամբ, որը համապատասխանում է իր իրական հզորությանը.:

`sudo f3fix {{/dev/device_name}}`

- Նշեք բաժանումը որպես bootable:

`sudo f3fix --boot {{/dev/device_name}}`

- Նշեք ֆայլային համակարգը.:

`sudo f3fix --fs-type={{filesystem_type}} {{/dev/device_name}}`
