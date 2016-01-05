# xargs

> read list of strings and pass each to another function as the arguments

- find all zip files and extract with unzip function

`find . -type f -name "*.zip" | xargs unzip`

- find all text files containing the string 'foo'

`find . -name '*.txt' | xargs grep 'foo'`


