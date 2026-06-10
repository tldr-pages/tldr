# jmap

> Java հիշողության քարտեզի գործիք:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/jmap.html>:.

- Տպել ընդհանուր օբյեկտների քարտեզագրումները Java գործընթացի համար (ելք, ինչպես pmap):

`jmap {{java_pid}}`

- Տպել կույտի ամփոփ տեղեկատվություն.:

`jmap -heap {{filename.jar}} {{java_pid}}`

- Տպել կույտի օգտագործման հիստոգրամը ըստ տեսակի.:

`jmap -histo {{java_pid}}`

- Կույտի պարունակությունը թափեք երկուական ֆայլի մեջ՝ jhat-ով վերլուծելու համար.:

`jmap -dump:format=b,file={{path/to/file}} {{java_pid}}`

- Թափել կույտի կենդանի օբյեկտները երկուական ֆայլի մեջ՝ jhat-ով վերլուծելու համար.:

`jmap -dump:live,format=b,file={{path/to/file}} {{java_pid}}`
