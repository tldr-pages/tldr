# opt

> Un instrument care preia fișierele sursă LVM și execută optimizări și/sau analize specificate pe ele.
> Mai multe informaţii: <https://llvm.org/docs/CommandGuide/opt.html>

- Rulați o optimizare sau analiză pe un fișier de cod bitcode:

`opt -{{passname}} {{path/to/file.bc}} -S -o {{file_opt.bc}}`

- Ieșiți graficul fluxului de control al unei funcții într-un fișier `.dot`:

`opt {{-dot-cfg}} -S {{path/to/file.bc}} -disable-output`

- Optimizați programul la nivelul 2 și ieșiți rezultatul într-un alt fișier:

`opt -O2 {{path/to/file.bc}} -S -o {{path/to/output_file.bc}}`
