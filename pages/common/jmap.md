# jmap

> Java memory map tool.
> More information: <https://docs.oracle.com/javase/7/docs/technotes/tools/share/jmap.html>.

- Print shared object mappings for a Java process (output like pmap):

`jmap {{java_pid}}`

- Print heap summary information:

`jmap -heap {{filename.jar}} {{java_pid}}`

- Print histogram of heap usage by type:

`jmap -histo {{java_pid}}`

- Dump contents of the heap into a binary file for analysis with jhat:

`jmap -dump:format=b,file={{path/to/file}} {{java_pid}}`
