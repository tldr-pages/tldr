#սոքս

> Sound eXchange. նվագարկել, ձայնագրել և վերափոխել աուդիո ֆայլեր:.
> Աուդիո ձևաչափերը նույնականացվում են ընդլայնման միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sox>:.

- Միավորել երկու աուդիո ֆայլ մեկի մեջ.:

`sox {{[-m|--combine mix]}} {{path/to/input_audio1}} {{path/to/input_audio2}} {{path/to/output_audio}}`

- Կտրեք աուդիո ֆայլը նշված ժամանակներում.:

`sox {{path/to/input_audio}} {{path/to/output_audio}} trim {{start}} {{duration}}`

- Նորմալացրեք աուդիո ֆայլը (ձայնը կարգավորեք առավելագույն գագաթնակետին, առանց կտրելու).:

`sox --norm {{path/to/input_audio}} {{path/to/output_audio}}`

- Հետադարձեք և պահպանեք աուդիո ֆայլը.:

`sox {{path/to/input_audio}} {{path/to/output_audio}} reverse`

- Տպել աուդիո ֆայլի վիճակագրական տվյալները.:

`sox {{path/to/input_audio}} {{[-n|--null]}} stat`

- Բարձրացրեք աուդիո ֆայլի ծավալը 2x-ով.:

`sox {{[-v|--volume]}} 2.0 {{path/to/input_audio}} {{path/to/output_audio}}`
