# exo հաշվարկային օրինակ

> Կառավարեք Exoscale Compute օրինակները:.
> Լրացուցիչ տեղեկություններ. <https://community.exoscale.com/product/compute/instances/>:.

- Ստեղծեք Debian-ի վրա հիմնված Compute օրինակ՝ 10 ԳԲ սկավառակի չափով.:

`exo compute instance create --disk-size 10 {{instance_name}} {{[-z|--zone]}} {{zone}} --template '{{Linux Debian 12 (Bookworm) 64-bit}}'`

- Մուտք գործեք հաշվարկային օրինակ SSH-ի միջոցով.:

`exo compute instance ssh {{instance_name|id}}`

- Թվարկեք բոլոր Հաշվարկային դեպքերը.:

`exo compute instance list`

- Ավելացրեք օրինակ Անվտանգության խմբին.:

`exo compute instance security-group add {{instance_name|id}} {{security_group_name|id}}`

- Սանդղակավորեք Հաշվարկային օրինակի չափը.:

`exo compute instance scale {{instance_name|id}} {{instance_type}}`

- Ստեղծեք Հաշվարկային օրինակի պատկեր.:

`exo compute instance snapshot create {{instance_name|id}}`

- Վերադարձեք Compute օրինակը snapshot-ի (պատկերի ստեղծումից հետո գրված տվյալները կկորչեն).:

`exo compute instance snapshot revert {{snapshot_id}} {{instance_name|id}}`

- Հաշվարկային օրինակի սկավառակի չափը դարձրեք 20 ԳԲ.:

`exo compute instance resize-disk {{instance_name|id}} 20`
