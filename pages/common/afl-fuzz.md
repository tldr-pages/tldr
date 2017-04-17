# afl-fuzz

> American fuzzy lop is a fuzzer that uses instrumentation and genetic algorithms.
> After fuzzing, have a look at the "crashes" directory in {{output_directory}}.

- Compile and instrument a "hello world" that crashes if you write "1".

`echo {{"main(){ if (getchar() == '1') abort(); }"}} > {{hello.c}} ; afl-gcc {{hello.c}} -o {{executable}}`

- Create a directory with a sample test case - one byte saying "2".

`mkdir {{input_cases}} && echo -n 2 >> {{input_cases}}/{{example}}`

- Perform fuzzing of the "hello world" from first step using the sample test case.

`AFL_EXIT_WHEN_DONE=1 afl-fuzz -i {{input_cases}} -o {{output_directory}} -- {{./executable}}`
