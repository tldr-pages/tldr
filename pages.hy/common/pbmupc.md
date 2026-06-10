# pbmupc

> Ստեղծեք ապրանքի համընդհանուր կոդի (UPC) PBM պատկեր:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmupc.html>:.

- Ստեղծեք UPC պատկեր նշված ապրանքի տեսակի, արտադրողի ծածկագրի և ապրանքի կոդի համար.:

`pbmupc {{product_type}} {{manufacturer_code}} {{product_code}} > {{path/to/output.pbm}}`

- Օգտագործեք այլընտրանքային ոճ, որը չի ցուցադրում ստուգման գումարը.:

`pbmupc -s2 {{product_type}} {{manufacturer_code}} {{product_code}} > {{path/to/output.pbm}}`
