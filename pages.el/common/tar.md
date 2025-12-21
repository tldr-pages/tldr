# tar

> Εργαλείο αρχειοθέτησης.
> Συχνά συνδυάζεται με μεθόδους συμπίεσης, όπως `gzip` ή `bzip2`.
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/tar/manual/tar.html>.

- Δημιουργία ([c]reate) μιας αρχειοθέτησης και εγγραφή της σε ένα αρχείο ([f]ile):

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- Δημιουργία ([c]reate) ενός συμπιεσμένου αρχείου g[z]ip και εγγραφή του σε ένα αρχείο ([f]ile):

`tar czf {{path/to/target.tar.gz}} {{path/to/file1 path/to/file2 ...}}`

- Δημιουργία ([c]reate) ενός συμπιεσμένου αρχείου g[z]ip από έναν κατάλογο χρησιμοποιώντας σχετικές διαδρομές:

`tar czf {{path/to/target.tar.gz}} {{[-C|--directory]}} {{path/to/directory}} .`

- Εξαγωγή (e[x]tract) ενός (συμπιεσμένου) αρχείου στον τρέχοντα κατάλογο αναλυτικά ([v]erbosely) από ένα αρχείο ([f]ile):

`tar xvf {{path/to/source.tar[.gz|.bz2|.xz]}}`

- Εξαγωγή (e[x]tract) ενός (συμπιεσμένου) αρχείου σε συγκεκριμένο κατάλογο:

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}} {{[-C|--directory]}} {{path/to/directory}}`

- Δημιουργία ([c]reate) ενός συμπιεσμένου αρχείου χρησιμοποιώντας την επέκταση αρχείου για τον αυτόματο ([a]utomatically) καθορισμό του προγράμματος συμπίεσης:

`tar caf {{path/to/target.tar.xz}} {{path/to/file1 path/to/file2 ...}}`

- Λίστα (lis[t]) περιεχομένων ενός αρχείου tar αναλυτικά ([v]erbosely):

`tar tvf {{path/to/source.tar}}`

- Εξαγωγή (e[x]tract) αρχείων που ταιριάζουν με ένα μοτίβο (pattern) από ένα αρχείο tar:

`tar xf {{path/to/source.tar}} --wildcards "{{*.html}}"`
