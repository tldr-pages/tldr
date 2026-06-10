# gitlint

> Git commit հաղորդագրության linter-ը ստուգում է ձեր commit հաղորդագրությունների ոճը:.
> Լրացուցիչ տեղեկություններ. <https://jorisroovers.com/gitlint/>:.

- Ստուգեք վերջին հանձնման հաղորդագրությունը.:

`gitlint`

- Լինտի պարտավորությունների շրջանակը.:

`gitlint --commits {{single_refspec_argument}}`

- Ուղ դեպի գրացուցակ կամ Python մոդուլ՝ օգտագործողի կողմից սահմանված լրացուցիչ կանոններով.:

`gitlint --extra-path {{path/to/directory}}`

- Սկսեք կոնկրետ CI աշխատանք.:

`gitlint --target {{path/to/target_directory}}`

- Ճանապարհ դեպի ֆայլ, որը պարունակում է commit-msg.:

`gitlint --msg-filename {{path/to/file}}`

- Կարդացեք փուլային կատարման մետա-տեղեկատվությունը տեղական պահոցից.:

`gitlint --staged`
