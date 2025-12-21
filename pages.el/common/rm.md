# rm

> Διαγραφή αρχείων ή καταλόγων.
> Δείτε επίσης: `rmdir`, `trash`.
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html>.

- Διαγραφή συγκεκριμένων αρχείων:

`rm {{path/to/file1 path/to/file2 ...}}`

- Διαγραφή συγκεκριμένων αρχείων, αγνοώντας τα αν δεν υπάρχουν:

`rm {{[-f|--force]}} {{path/to/file1 path/to/file2 ...}}`

- Διαγραφή συγκεκριμένων αρχείων διαδραστικά, ρωτώντας πριν απο κάθε διαγραφή:

`rm {{[-i|--interactive]}} {{path/to/file1 path/to/file2 ...}}`

- Διαγραφή συγκεκριμένων αρχείων, εμφανίζοντας πληροφορίες για κάθε διαγραφή:

`rm {{[-v|--verbose]}} {{path/to/file1 path/to/file2 ...}}`

- Διαγραφή συγκεκριμένων αρχείων και καταλόγων, αναδρομικά:

`rm {{[-r|--recursive]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Διαγραφή άδειων καταλόγων (αυτή θεωρείται η ασφαλής τακτική):

`rm {{[-d|--dir]}} {{path/to/directory}}`
