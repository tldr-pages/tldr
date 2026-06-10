# sui հաճախորդ ptb

> Ստեղծեք, ստորագրեք և կատարեք ծրագրավորվող գործարքների բլոկներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.sui.io/references/cli/ptb>:.

- Փաթեթից և մոդուլից կանչեք «Տեղափոխել» գործառույթը.:

`sui client ptb --move-call p::m::f "<{{type}}>" args`

- Կատարեք Move վեկտոր u64 տիպի երկու տարրերով.:

`sui client ptb --make-move-vec "<u64>" "[1000,2000]"`

- Կտրեք գազի մետաղադրամը և փոխանցեք այն հետևյալ հասցեով.:

`sui client ptb --split-coins gas "[1000]" --assign new_coins --transfer-objects "[new_coins]" @{{address}}`

- Փոխանցել օբյեկտը հասցեին.:

`sui client ptb --transfer-objects "[{{object_id}}]" @{{address}}`

- Հրապարակեք Move փաթեթը և փոխանցեք արդիականացման հնարավորությունը ուղարկողին.:

`sui client ptb --move-call sui::tx_context::sender --assign sender --publish "." --assign upgrade_cap --transfer-objects "[upgrade_cap]" sender`
