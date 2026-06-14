# tgpt

> Խոսեք AI չաթբոտի հետ՝ առանց API ստեղների անհրաժեշտության:.
> Հասանելի մատակարարներ՝ `openai`, `opengpts`, `koboldai`, `phind`, `llama2`, `blackboxai`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/aandrew-me/tgpt>:.

- Զրուցեք լռելյայն մատակարարի հետ (GPT-3.5-turbo):

`tgpt "{{prompt}}"`

- Սկսեք բազմաշերտ ինտերակտիվ ռեժիմ.:

`tgpt {{[-m|--multiline]}}`

- Ստեղծեք պատկերներ և պահեք դրանք ընթացիկ գրացուցակում.:

`tgpt {{[-img|--image]}} "{{prompt}}"`

- Ստեղծեք կոդը լռելյայն մատակարարի հետ (GPT-3.5-turbo).:

`tgpt {{[-c|--code]}} "{{prompt}}"`

- Հանգիստ զրուցեք կոնկրետ մատակարարի հետ (առանց անիմացիաների).:

`tgpt --provider {{openai|opengpts|koboldai|phind|llama2|blackboxai}} {{[-q|--quiet]}} {{[-w|--whole]}} "{{prompt}}"`

- Ստեղծեք և կատարեք կեղևի հրամաններ՝ օգտագործելով հատուկ մատակարար (հաստատման հուշումով).:

`tgpt --provider {{llama2}} {{[-s|--shell]}} "{{prompt}}"`

- API բանալի, մոդել, պատասխանի առավելագույն երկարություն, ջերմաստիճան և `top_p` հուշում (պահանջվում է `openai` մատակարարից օգտվելիս):

`tgpt --provider openai --key "{{api_key}}" --model "{{gpt-3.5-turbo}}" --max-length {{10}} --temperature {{0.7}} --top_p {{0.9}} "{{prompt}}"`

- Սնուցեք ֆայլը որպես լրացուցիչ նախնական հուշում մուտքագրում.:

`tgpt < {{path/to/file}} --provider {{blackboxai}} "{{prompt}}"`
