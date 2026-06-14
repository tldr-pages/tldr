# virsh կապ

> Միացեք վիրտուալ մեքենայի հիպերվիզորին:.
> Տես նաև՝ `virsh`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/virsh>:.

- Միացեք լռելյայն հիպերվիզորին.:

`virsh connect`

- Միացեք որպես արմատ տեղական QEMU/KVM հիպերվիզորին.:

`virsh connect qemu:///system`

- Գործարկեք հիպերվիզորի նոր օրինակ և միացեք դրան որպես տեղական օգտագործող.:

`virsh connect qemu:///session`

- Միացեք որպես արմատ հեռավոր հիպերվիզորին՝ օգտագործելով SSH:

`virsh connect qemu+ssh://{{user_name@host_name}}/system`
