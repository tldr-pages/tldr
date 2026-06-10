#յարա

> Նախշերի համապատասխանող գործիք՝ չարամիտ ծրագրերը հայտնաբերելու և դասակարգելու համար:.
> Տես նաև՝ `yarac`:.
> Լրացուցիչ տեղեկություններ. <https://yara.readthedocs.io/en/stable/commandline.html>:.

- Սկանավորեք որոշակի ֆայլ կանոնների ֆայլով.:

`yara {{path/to/rule.yar}} {{path/to/file}}`

- Ռեկուրսիվորեն սկանավորեք հնարավոր սպառնալիքներ պարունակող գրացուցակ և ենթագրքեր.:

`yara {{path/to/rule.yar}} {{[-r|--recursive]}} {{path/to/directory}}`

- Սկանավորեք գործող գործընթացն իր PID-ով՝ օգտագործելով բազմաթիվ կանոններ.:

`yara {{path/to/rule1.yar path/to/rule2.yar ...}} {{pid}}`

- Տպել մետատվյալները՝ կապված համապատասխան կանոնների հետ.:

`yara {{[-m|--print-meta]}} {{path/to/rule.yar}} {{path/to/file}}`

- Տպեք այն տողերը, որոնց պատճառով կանոնը համընկավ.:

`yara {{[-s|--print-strings]}} {{path/to/rule.yar}} {{path/to/file}}`

- Զուգահեռ սկանավորման համար օգտագործեք որոշակի քանակությամբ թելեր.:

`yara {{[-p|--threads]}} {{number_of_threads}} {{path/to/rule.yar}} {{path/to/directory}}`

- Օգտագործեք կազմված YARA կանոնների ֆայլը՝ գրացուցակը ռեկուրսիվ կերպով սկանավորելու համար.:

`yara {{[-C|--compiled-rules]}} {{path/to/rules.bin}} {{[-r|--recursive]}} {{path/to/directory}}`
