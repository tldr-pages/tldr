# cp

> Αντιγραφή αρχείων και καταλόγων.
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Αντιγραφή ενός αρχείου σε άλλη τοποθεσία:

`cp {{path/to/source_file.ext}} {{path/to/target_file.ext}}`

- Αντιγραφή ενός αρχείου σε άλλο κατάλογο, διατηρώντας το όνομα του αρχείου:

`cp {{path/to/source_file.ext}} {{path/to/target_parent_directory}}`

- Αναδρομική αντιγραφή των περιεχομένων ενός καταλόγου σε άλλη τοποθεσία (αν ο προορισμός υπάρχει, ο κατάλογος αντιγράφεται μέσα σε αυτόν):

`cp {{[-r|--recursive]}} {{path/to/source_directory}} {{path/to/target_directory}}`

- Αντιγραφή ενός καταλόγου αναδρομικά, σε αναλυτική λειτουργία (εμφάνιση αρχείων καθώς αντιγράφονται):

`cp {{[-vr|--verbose --recursive]}} {{path/to/source_directory}} {{path/to/target_directory}}`

- Αντιγραφή πολλών αρχείων ταυτόχρονα σε έναν κατάλογο:

`cp {{[-t|--target-directory]}} {{path/to/destination_directory}} {{path/to/file1 path/to/file2 ...}}`

- Αντιγραφή όλων των αρχείων με την συγκεκριμένη επέκταση σε άλλη τοποθεσία, σε διαδραστική λειτουργία (ζητά επιβεβαίωση πριν την αντικατάσταση):

`cp {{[-i|--interactive]}} {{*.ext}} {{path/to/target_directory}}`

- Ακολούθηση συμβολικών συνδέσμων πριν την αντιγραφή:

`cp {{[-L|--dereference]}} {{link}} {{path/to/target_directory}}`

- Χρήση της πλήρους διαδρομής των πηγαίων αρχείων, δημιουργώντας ενδιάμεσους καταλόγους που λείπουν κατά την αντιγραφή:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
