# GREP : Global Regular Expression print

> xzegrep - Search compressed files for regular expression.

>More information: (https://manpages.ubuntu.com/manpages/xenial/man1/xzgrep.1.html#description)

## Synopsis:
```
       xzgrep [grep_option][-e] pattern file...
       xzegrep ...
       xzfgrep ...
       lzgrep ...
       lzegrep ...
       lzfgrep ...

```
```
xzgrep [grep_options] [-e] pattern file...
```
* -e: Allows to use a ‘-‘ sign in the beginning of the pattern.
  
## Example:
```
grep -e -goodMorning greet.csv
```

* xzgrep invokes grep(1) on files which may be either uncompressed or compressed with xz(1),
       lzma(1), gzip(1), bzip2(1), or lzop(1).  All options  specified  are  passed  directly  to
       grep(1).

* If  xzgrep  is  invoked as xzegrep or xzfgrep then egrep(1) or fgrep(1) is used instead of
       grep(1).  The same applies to names lzgrep, lzegrep, and lzfgrep, which are  ***provided  for
       backward compatibility with LZMA Utils.***

