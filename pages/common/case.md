# case

> Bash builtin construct for creating multi-choice conditional statements.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- Match a variable against string literals to decide which command to run:

`case {{$COUNTRULE}} in {{words}}) {{wc -w README}} ;; {{lines}}) {{wc -l README}} ;; esac`

- Combine patterns with |, use * as a fallback pattern:

`case {{$COUNTRULE}} in {{[wW]|words}}) {{wc -w README}} ;; {{[lL]|lines}}) {{wc -l README}} ;; *) {{echo "what?"}} ;; esac`

- Allow matching multiple patterns:

`case {{$ANIMAL}} in {{cat}}) echo "It's a cat" ;;& {{cat|dog}}) echo "It's a cat or a dog" ;;& *) echo "Fallback" ;; esac`

- Continue to the next pattern's commands without checking the pattern:

`case {{$ANIMAL}} in {{cat}}) echo "It's a cat" ;& {{dog}}) echo "It's either a dog or cat fell through" ;& *) echo "Fallback" ;; esac`
