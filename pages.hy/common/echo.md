#արձագանք

> Տպել տրված փաստարկները:.
> Տես նաև՝ `printf`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>:.

- Տպել տեքստային հաղորդագրություն: Նշում. Մեջբերումները կամընտիր են.:

`echo "{{Hello World}}"`

- Տպել հաղորդագրություն շրջակա միջավայրի փոփոխականներով.:

`echo "{{My path is $PATH}}"`

- Տպեք հաղորդագրություն առանց նոր տողի.:

`echo -n "{{Hello World}}"`

- Կցեք հաղորդագրություն ֆայլին.:

`echo "{{Hello World}}" >> {{file.txt}}`

- Միացնել ետ կտրվածքով փախուստների մեկնաբանումը (հատուկ նիշ).:

`echo -e "{{Column 1\tColumn 2}}"`

- Տպեք վերջին կատարված հրամանի ելքի կարգավիճակը (Նշում. Windows Command Prompt-ում և PowerShell-ում համարժեք հրամաններն են՝ համապատասխանաբար `echo %errorlevel%` և `$lastexitcode`).:

`echo $?`

- Տեքստ փոխանցեք մեկ այլ ծրագրի `stdin`-ի միջոցով.:

`echo "{{Hello World}}" | {{program}}`
