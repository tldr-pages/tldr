# f3 զոնդ

> Զննեք արգելափակված սարքը (օրինակ՝ ֆլեշ կրիչը կամ microSD քարտը) կեղծ ֆլեշ հիշողության համար:.
> Տես նաև՝ `f3read`, `f3write`, `f3fix`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/AltraMayor/f3>:.

- Հետազոտել բլոկ սարքը.:

`sudo f3probe {{path/to/block_device}}`

- Օգտագործեք հնարավոր նվազագույն RAM-ը.:

`sudo f3probe --min-memory {{path/to/block_device}}`

- Ժամանակային սկավառակի գործառնություններ.:

`sudo f3probe --time-ops {{path/to/block_device}}`
