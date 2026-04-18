# winword

> Microsoft Office's word processor application.
> More information: <https://support.microsoft.com/office/command-line-switches-for-microsoft-office-products-079164cd-4ef5-4178-b235-441737deb3a6#category=word>.

- Launch the word processor application:

`winword`

- Launch Word with [n]o open documents:

`winword /n`

- [w]rite a new blank document:

`winword /w`

- Create a new document, [f]ollowing the contents of an existing file:

`winword /f {{path\to\file}}`

- Open one or more files for edi[t]ing:

`winword /t {{path\to\file1 path\to\file2 ...}}`

- Open a file with all AutoExec [m]acros disabled:

`winword /m {{path\to\file}}`

- Open a file with all AutoExec [m]acros disabled, then run a specific macro:

`winword /m{{MacroName}} {{path\to\file}}`

- Start Microsoft Word in Safe Mode:

`winword /safe`
