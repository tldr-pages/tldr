# case

> Costrutto builtin di Bash per creare istruzioni condizionali a scelta multipla.
> Maggiori informazioni: <https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- Confronta una variabile con stringhe letterali per decidere quale comando eseguire:

`case {{$COUNTRULE}} in {{words}}) {{wc --words README}} ;; {{lines}}) {{wc --lines README}} ;; esac`

- Combina pattern con |, usando * come pattern di fallback:

`case {{$COUNTRULE}} in {{[wW]|words}}) {{wc --words README}} ;; {{[lL]|lines}}) {{wc --lines README}} ;; *) {{echo "cosa?"}} ;; esac`

- Consente di confrontare più pattern:

`case {{$ANIMAL}} in {{cat}}) {{echo "È un gatto"}} ;;& {{cat|dog}}) {{echo "È un gatto o un cane"}} ;;& *) {{echo "Fallback"}} ;; esac`

- Continua con i comandi del pattern successivo senza ricontrollare il pattern:

`case {{$ANIMAL}} in {{cat}}) {{echo "È un gatto"}} ;& {{dog}}) {{echo "È un gatto o un cane passato al ramo successivo"}} ;& *) {{echo "Fallback"}} ;; esac`

- Mostra l'aiuto:

`help case`
