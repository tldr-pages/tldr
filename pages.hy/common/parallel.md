#զուգահեռ

> Գործարկել հրամանները մի քանի պրոցեսորի միջուկների վրա:.
> Տես նաև՝ `xargs`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/parallel/man.html>:.

- Gzip մի քանի ֆայլ միանգամից՝ օգտագործելով բոլոր միջուկները.:

`parallel gzip ::: {{path/to/file1 path/to/file2 ...}}`

- Կարդացեք փաստարկները `stdin`-ից, գործարկեք միանգամից 4 աշխատանք.:

`ls *.txt | parallel {{[-j|--jobs]}} 4 gzip`

- Փոխակերպեք JPEG պատկերները PNG-ի, օգտագործելով փոխարինող տողերը.:

`parallel convert {} {.}.png ::: *.jpg`

- Զուգահեռ xargs, խցկեք որքան հնարավոր է շատ args մեկ հրամանի վրա.:

`{{args}} | parallel -X {{command}}`

- Բաժանեք `stdin`-ը ~1M բլոկների, յուրաքանչյուր բլոկ կերակրեք նոր հրամանի `stdin`-ին.:

`cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}`

- Գործարկեք բազմաթիվ մեքենաների վրա SSH-ի միջոցով.:

`parallel {{[-S|--sshlogin]}} {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`

- Ներբեռնեք 4 ֆայլ միաժամանակ տեքստային ֆայլից, որը պարունակում է հղումներ, որոնք ցույց են տալիս առաջընթացը.:

`parallel {{[-j|--jobs]}} 4 --bar --eta curl {{[-sO|--silent --remote-name]}} {} :::: {{path/to/links.txt}}`

- Տպեք այն աշխատանքները, որոնք `parallel`-ն աշխատում է `stderr`-ում:

`parallel {{[-t|--verbose]}} {{command}} ::: {{args}}`
