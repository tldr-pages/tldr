# tail

> A file content viewer that allows you to inspect the end of a file

- The base syntax is this:

`tail {{OPTION}} {{FILE}}`

- Without any option it shows you the last 10 rows of the file
- If there are less than 10 rows it just shows the remaining ones

- The simplest option is __-n__ num
  - It allows you to specify how many rows visualize  
  - `tail -n 5 {{FILE}}` shows only the last 5 rows
  - Write -n num is the same as writing -num
  
- The + option indicates from which line start the output
  - `tail +6 {{FILE}}` shows you all the lines between the 6th and the last one included
  
- The option __-c__ prints the last ‘num’ bytes from the file specified
  - You can use also -c +num, and it displays all the data after skipping num bytes
  
- The option __-q__: It is used if more than 1 file is given
  - `tail -q {{FILE_1}} {{FILE_2}}`
  
- The option __-f__ is used for change dynamically the output as soon as new lines are added to the file

- You can check the version of the __tail__ program with tail `tail --version`
