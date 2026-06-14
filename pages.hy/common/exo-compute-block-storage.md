# exo հաշվարկի բլոկ-պահեստավորում

> Կառավարեք Exoscale Block Storage ծառայությունը:.
> Լրացուցիչ տեղեկություններ. <https://community.exoscale.com/product/storage/block-storage/>:.

- Ստեղծեք 20 ԳԲ բլոկի պահեստային ծավալ.:

`exo compute block-storage create {{volume_name}} --size 20 {{[-z|--zone]}} {{zone}}`

- Ցուցակ բլոկների պահպանման ծավալները.:

`exo compute block-storage list`

- Կցեք Block Storage Volume հաշվարկային օրինակին.:

`exo compute block-storage attach {{volume_name|id}} {{instance_name|id}} {{[-z|--zone]}} {{zone}}`

- Ստիպողաբար անջատեք Block Storage Volume-ը (հաստատում չի պահանջում).:

`exo compute block-storage detach {{volume_name|id}} {{[-z|--zone]}} {{zone}} {{[-f|--force]}}`

- Ստեղծեք Block Storage Volume-ի լուսանկար.:

`exo compute block-storage snapshot create {{volume_name|id}} --name {{snapshot_name}} {{[-z|--zone]}} {{zone}}`

- Ստեղծեք Block Storage Volume snapshot-ից.:

`exo compute block-storage create {{volume_name}} --snapshot {{snapshot_name|id}} {{[-z|--zone]}} {{zone}}`

- Թարմացրեք գոյություն ունեցող Block Storage Volume-ը նոր անունով և 30 ԳԲ նոր ծավալով:

`exo compute block-storage update {{volume_name|id}} --size 30 --name {{new_name}}`
