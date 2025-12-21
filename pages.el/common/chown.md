# chown

> Αλλαγή του χρήστη και της ομάδας ιδιοκτησίας αρχείων και καταλόγων.
> Δείτε επίσης: `chgrp`.
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Αλλαγή του χρήστη-ιδιοκτήτη ενός αρχείου/καταλόγου:

`sudo chown {{user}} {{path/to/file_or_directory}}`

- Αλλαγή του χρήστη-ιδιοκτήτη και της ομάδας (group) ενός αρχείου/καταλόγου:

`sudo chown {{user}}:{{group}} {{path/to/file_or_directory}}`

- Αλλαγή του χρήστη-ιδιοκτήτη και της ομάδας ώστε και τα δύο να έχουν το όνομα `user`:

`sudo chown {{user}}: {{path/to/file_or_directory}}`

- Αλλαγή της ομάδας (group) ενός αρχείου σε μια ομάδα στην οποία ανήκει ο τρέχων χρήστης:

`chown :{{group}} {{path/to/file_or_directory}}`

- Αναδρομική ([R]ecursive) αλλαγή του ιδιοκτήτη ενός καταλόγου και των περιεχομένων του:

`sudo chown {{[-R|--recursive]}} {{user}} {{path/to/directory}}`

- Αλλαγή του ιδιοκτήτη ενός συμβολικού συνδέσμου (χωρίς να ακολουθηθεί ο σύνδεσμος --no-dereference/-[h]):

`sudo chown {{[-h|--no-dereference]}} {{user}} {{path/to/symlink}}`

- Αλλαγή του ιδιοκτήτη ενός αρχείου/καταλόγου ώστε να ταιριάζει με ένα αρχείο αναφοράς (reference):

`sudo chown --reference {{path/to/reference_file}} {{path/to/file_or_directory}}`
