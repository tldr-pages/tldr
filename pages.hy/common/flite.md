#ֆլիտ

> Խոսքի սինթեզի շարժիչ:.
> Լրացուցիչ տեղեկություններ. <http://www.festvox.org/flite/doc/>:.

- Թվարկեք բոլոր հասանելի ձայները.:

`flite -lv`

- Տեքստի տողը խոսքի վերածել.:

`flite -t "{{string}}"`

- Փոխակերպեք ֆայլի բովանդակությունը խոսքի.:

`flite -f {{path/to/file.txt}}`

- Օգտագործեք նշված ձայնը.:

`flite -voice {{file://path/to/filename.flitevox|url}}`

- Պահպանեք արտադրանքը wav ֆայլի մեջ.:

`flite -voice {{file://path/to/filename.flitevox|url}} -f {{path/to/file.txt}} -o {{output.wav}}`

- Ցուցադրման տարբերակը:

`flite --version`
