# clisp

> Run GNU CLISP — an ANSI Common Lisp interpreter and compiler.  
> More information: <https://www.gnu.org/software/clisp/clisp.html> :contentReference[oaicite:5]{index=5}

- Start the REPL:  
  `clisp`
- Compile a Lisp file to bytecode and execute:  
  `clisp -c {{file.lisp}}`
- Execute a Lisp expression directly:  
  `clisp -x "{{expression}}"`

#### History/substitution examples in sh/Bash/Zsh:

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
