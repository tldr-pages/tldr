# llvm-dis

> Convertește fișierele de cod bitcode LLVM în LLVM Intermediate Reprezentare (IR) care poate fi citită de om.
> Mai multe informaţii: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>

- Convertiți un fișier de cod bitcode ca LLVM IR și scrieți rezultatul la stdout:

`llvm-dis {{path/to/input.bc}} -o -`

- Conversia unui fișier de cod bitcode într-un fișier LLVM IR cu același nume de fișier:

`llvm-dis {{path/to/file.bc}}`

- Convertiți un fișier de cod bitcode în LLVM IR, scriind rezultatul în fișierul specificat:

`llvm-dis {{path/to/input.bc}} -o {{path/to/output.ll}}`
