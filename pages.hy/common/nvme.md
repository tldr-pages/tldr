# nvme

> NVMe պահեստավորման օգտագործողի տարածքի օգտակար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/nvme>:.

- Թվարկեք բոլոր NVMe սարքերը.:

`sudo nvme list`

- Ցույց տալ սարքի տեղեկատվությունը.:

`sudo nvme smart-log {{device}}`

- Անվտանգ ջնջել օգտվողի տվյալները NVMe սարքի վրա.:

`sudo nvme format {{[-s|--ses]}} 1 {{[-r|--reset]}} {{device}}`
