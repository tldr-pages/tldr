# ecl

> Run Embeddable Common Lisp (ECL).  
> More information: <https://ecl.common-lisp.dev/static/files/manual/ecl-23.9.9/Invoking-ECL.html> :contentReference[oaicite:3]{index=3}

- Start the REPL:  
  `ecl`
- Load and evaluate a Lisp file:  
  `ecl --load {{file.lisp}}`
- Compile a Lisp file to an executable:  
  `ecl --compile {{file.lisp}} -o {{executable}}`

#### History/substitution examples in sh/Bash/Zsh:

- Substitute with the previous command and run it with sudo:  
  `sudo !!`
- Substitute with a command based on its line number found with history:  
  `!{{number}}`ggit
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
