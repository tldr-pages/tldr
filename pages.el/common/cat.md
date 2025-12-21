# cat

> Εμφάνιση και συνένωση αρχείων.
> Περισσότερες πληροφορίες: <https://manned.org/cat.1posix>.

- Εμφάνιση του περιεχομένου ενός αρχείου στο `stdout`:

`cat {{path/to/file}}`

- Συνένωση πολλαπλών αρχείων σε ένα αρχείο εξόδου:

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- Προσάρτηση πολλαπλών αρχείων σε ένα αρχείο εξόδου:

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- Αντιγραφή των περιεχομένων ενός αρχείου σε ένα αρχείο εξόδου χωρίς buffering:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Εγγραφή του περιεχομένου του `stdin` σε ένα αρχείο:

`cat - > {{path/to/file}}`
