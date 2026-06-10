# ավտոմատ բեռնում

> Նշել գործառույթները ծույլ բեռնման համար Zsh-ում:.
> Գործառույթները չեն բեռնվում հիշողության մեջ մինչև առաջին անգամ կանչելը, ինչը բարելավում է shell-ի գործարկման ժամանակը:.
> Լրացուցիչ տեղեկություններ. <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>:.

- Ավտոմատ բեռնել գործառույթը անունով.:

`autoload {{function_name}}`

- Ավտոմատ բեռնեք գործառույթը և անմիջապես լուծեք դրա սահմանումը.:

`autoload +X {{function_name}}`

- Ավտոմատ բեռնել գործառույթ՝ օգտագործելով Zsh ոճի ավտոմատ բեռնումը (խորհուրդ է տրվում).:

`autoload -Uz {{function_name}}`

- Գործառույթները հասանելի դարձրեք գրացուցակից՝ ավելացնելով այն `fpath`-ին:

`fpath=({{path/to/functions_dir}} $fpath) && autoload -Uz {{function_name}}`

- Zsh ավարտման համակարգը ավտոմատ բեռնել.:

`autoload -Uz compinit && compinit`

- Ավտոմատ բեռնեք և օգտագործեք `add-zsh-hook` կոմունալ ծրագիրը.:

`autoload -Uz add-zsh-hook`
