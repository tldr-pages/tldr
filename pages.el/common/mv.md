# mv

> Μετακίνηση ή μετονομασία αρχείων και καταλόγων.
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Μετονομασία ενός αρχείου ή καταλόγου όταν ο προορισμός δεν υπάρχει:

`mv {{path/to/source}} {{path/to/target}}`

- Μετακίνσηη ενός αρχείου ή καταλόγου σε έναν άλλο ήδη υπάρχον κατάλογο:

`mv {{path/to/source}} {{path/to/existing_directory}}`

- Μετακίνηση πολλαπλών αρχείων σε έναν ήδη υπάρχον κατάλογο, κρατώντας τα ονόματα των αρχείων ίδια:

`mv {{path/to/source1 path/to/source2 ...}} {{path/to/existing_directory}}`

- Να μην γίνει ερώτηση για επιβεβαίωση πριν την αντικατάσταση υπάρχοντων αρχείων:

`mv {{[-f|--force]}} {{path/to/source}} {{path/to/target}}`

- Να γίνει ερώτηση για επιβεβαίωση διαδραστικά πριν την αντικατάσταση υπάρχοντων αρχείων, ανεξαρτήτως δικαιωμάτων αρχείου:

`mv {{[-i|--interactive]}} {{path/to/source}} {{path/to/target}}`

- Να μην γίνει αντικατάσταση υπάρχοντων αρχείων στο προορισμό:

`mv {{[-n|--no-clobber]}} {{path/to/source}} {{path/to/target}}`

- Μετακίνηση αρχείων σε αναλυτική λειτουργία, με εμφάνιση μετά την μετακίνηση:

`mv {{[-v|--verbose]}} {{path/to/source}} {{path/to/target}}`

- Καθορισμός καταλόγου προορισμού για την χρήση εξωτερικών εργαλείων για την συλλογή αρχείων προς μετακίνηση:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{path/to/target_directory}}`
