# mkdir

> Δημιουργία καταλόγων και ορισμός των δικαιωμάτων τους.
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Δημιουργία συγκεκριμένων καταλόγων:

`mkdir {{path/to/directory1 path/to/directory2 ...}}`

- Δημιουργία συγκεκριμένων καταλόγων, και αν χρειάζεται, των γονέων τους:

`mkdir {{[-p|--parents]}} {{path/to/directory1 path/to/directory2 ...}}`

- Δημιουργία καταλόγων με συγκεκριμένα δικαιώματα:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{path/to/directory1 path/to/directory2 ...}}`

- Δημιουργία πολλαπλών ένθετων καταλόγων αναδρομικά:

`mkdir {{[-p|--parents]}} {{path/to/{a,b}/{x,y,z}/{h,i,j}}}`
