#ազուրիտ

> Azure Storage API-ի համատեղելի սերվեր (էմուլատոր) տեղական միջավայրում:.
> Լրացուցիչ տեղեկություններ. <https://www.npmjs.com/package/azurite>:.

- Օգտագործեք գոյություն ունեցող գտնվելու վայրը որպես աշխատանքային տարածքի ուղի.:

`azurite {{[-l|--location]}} {{path/to/directory}}`

- Անջատել մուտքի մատյանը, որը ցուցադրվում է վահանակում.:

`azurite {{[-s|--silent]}}`

- Միացնել վրիպազերծման մատյանը՝ որպես տեղեկամատյան նպատակակետ տրամադրելով ֆայլի ուղին՝:

`azurite {{[-d|--debug]}} {{path/to/debug.log}}`

- Անհատականացրեք Blob/Queue/Table ծառայության լսման հասցեն.:

`azurite {{--blobHost|--queueHost|--tableHost}} {{0.0.0.0}}`

- Անհատականացրեք Blob/Queue/Table ծառայության լսման նավահանգիստը.:

`azurite {{--blobPort|--queuePort|--tablePort}} {{8888}}`
