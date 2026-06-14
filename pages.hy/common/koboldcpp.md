# koboldcpp

> AI տեքստի ստեղծման ծրագիր GGML և GGUF մոդելների համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/LostRuins/koboldcpp/wiki#command-line-arguments-reference>:.

- Բեռնել մեկ կամ մի քանի մոդելային ֆայլեր.:

`koboldcpp {{[-m|--model]}} {{path/to/model_file}}`

- Սահմանեք միացքը լսելու համար (կանխադրված է 5001):

`koboldcpp --port {{port}}`

- Սահմանեք օգտագործվող թելերի քանակը.:

`koboldcpp {{[-t|--threads]}} {{amount_of_threads}}`

- Գործարկեք վեբ զննարկիչը, երբ բեռնումն ավարտված է.:

`koboldcpp --launch`

- Սկսեք առանց GUI գործարկիչի.:

`koboldcpp --skiplauncher`
