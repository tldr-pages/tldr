# case

> Esegui branch diversi in base al valore di un'espressione.

- Esegui il match di una variabile su diverse stringhe per decidere che comando eseguire:

`case {{$metrica}} in {{parole}}) {{wc -w README}}; ;; {{linee}}) {{wc -l README}}; ;; esac`

- Combina pattern con |, utilizzando * come pattern di fallback:

`case {{$metrica}} in {{[pP]|parole}}) {{wc -w README}}; ;; {{[lL]|linee}}) {{wc -l README}}; ;; *) {{echo "cosa?"}}; ;; esac`
