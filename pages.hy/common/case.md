# դեպք

> Bash-ի ներկառուցված կոնստրուկցիա՝ բազմակի ընտրության պայմանական հայտարարություններ ստեղծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-case>:.

- Համապատասխանեցրեք փոփոխականը տողերի տառերի հետ՝ որոշելու համար, թե որ հրամանը պետք է գործարկվի.:

`case {{$COUNTRULE}} in {{words}}) {{wc --words README}} ;; {{lines}}) {{wc --lines README}} ;; esac`

- Միավորել օրինաչափությունները |-ի հետ, օգտագործել * որպես հետադարձ օրինակ.:

`case {{$COUNTRULE}} in {{[wW]|words}}) {{wc --words README}} ;; {{[lL]|lines}}) {{wc --lines README}} ;; *) {{echo "what?"}} ;; esac`

- Թույլատրել համընկնող բազմաթիվ նախշեր.:

`case {{$ANIMAL}} in {{cat}}) {{echo "It's a cat"}} ;;& {{cat|dog}}) {{echo "It's a cat or a dog"}} ;;& *) {{echo "Fallback"}} ;; esac`

- Շարունակեք հաջորդ օրինակի հրամաններին՝ առանց նախշը ստուգելու.:

`case {{$ANIMAL}} in {{cat}}) {{echo "It's a cat"}} ;& {{dog}}) {{echo "It's either a dog or cat fell through"}} ;& *) {{echo "Fallback"}} ;; esac`

- Ցուցադրել օգնությունը.:

`help case`
