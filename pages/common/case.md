# case

> Branch based on the value of an expression.
> More information: <https://manned.org/case>.

- Match a variable against string literals to decide which command to run:

`case {{$tocount}} in {{words}}) {{wc -w README}}; ;; {{lines}}) {{wc -l README}}; ;; esac`

- Combine patterns with |, use * as a fallback pattern:

`case {{$tocount}} in {{[wW]|words}}) {{wc -w README}}; ;; {{[lL]|lines}}) {{wc -l README}}; ;; *) {{echo "what?"}}; ;; esac`
