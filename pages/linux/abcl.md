# abcl

> Run Armed Bear Common Lisp (ABCL) on the JVM.  
> More information: <https://abcl.org/>.

- Start the REPL under JVM:  
  `abcl`

- Load a Lisp file:  
  `abcl --load {{file.lisp}}`

- Run a Lisp expression from the command line:  
  `abcl --eval "{{expression}}"`

## History / substitution examples in sh/Bash/Zsh:

- Substitute with the previous command and run it with sudo:  
  `sudo !!`

- Substitute with a command based on its line number found with history:  
  `!{{number}}`

- Substitute with a command that was used a specified number of lines back:  
  `!-{{number}}`

- Substitute with the most recent command that starts with a string:  
  `!{{string}}`

- Substitute with the arguments of the latest command:  
  `{{command}} !*`

- Substitute with the last argument of the latest command:  
  `{{command}} !$`

- Print last command that starts with a string without executing it:  
  `!{{string}}:p`
