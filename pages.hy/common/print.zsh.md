#տպել

> Z Shell (`zsh`) ներկառուցված: Տպել արգումենտներ, որոնք նման են `echo`-ին:.
> Տես նաև՝ `echo`, `printf`, `zsh`:.
> Լրացուցիչ տեղեկություններ. <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>:.

- Տպել մուտքագրում.:

`print "Hello" "World"`

- Տպել՝ առանձնացված նոր տողով.:

`print -l "Line1" "Line 2" "Line3"`

- Տպել առանց նոր տողի:

`print -n "Hello"; print "World"`

- Միացնել հետշեղի փախուստները.:

`print -e "Line 1\nLine2"`

- Տպեք արգումենտներ, ինչպես նկարագրված է `printf`-ով (կեղևների միջև ավելի մեծ շարժունակության համար, փոխարենը օգտագործեք `printf` հրամանը):

`print -f "%s is %d years old.\n" "Alice" 30`
