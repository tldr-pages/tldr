# bindkey

> Ավելացնել թեժ ստեղներ Z shell-ում:.
> Տես նաև՝ `zle`:.
> Լրացուցիչ տեղեկություններ. <https://zsh.sourceforge.io/Doc/Release/Zsh-Line-Editor.html#Zle-Builtins>:.

- Թվարկեք բոլոր առկա թեժ ստեղները.:

`bindkey`

- Կցեք թեժ ստեղնը կոնկրետ հրամանին.:

`bindkey "{{^k}}" {{kill-line}}`

- Կցեք թեժ ստեղնը կոնկրետ բանալի [s] հաջորդականությանը.:

`bindkey -s '^o' 'cd ..\n'`

- [l]ist keycars:

`bindkey -l`

- Թվարկեք բոլոր թեժ ստեղները ստեղնով[M]ap:

`bindkey -M {{main}}`

- Միացնել [v]i ռեժիմը.:

`bindkey -v`

- Միացնել [e]macs ռեժիմը (կանխադրված ռեժիմ).:

`bindkey -e`

- Ստուգեք, թե որ ռեժիմն է ակտիվ (vi կամ emacs):

`bindkey -lL main | grep -Eo 'viins|emacs'`
