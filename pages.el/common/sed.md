# sed

> Επεξεργασία κειμένου με χρήση scripts.
> Δείτε επίσης: `awk`, `ed`.
> Περισσότερες πληροφορίες: <https://manned.org/sed.1posix>.

- Αντικατάσταση όλων των εμφανίσεων του `apple` (βασικό `regex`) με `mango` (βασικό `regex`) σε όλες τις γραμμές εισόδου και εκτύπωση του αποτελέσματος στο `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Εκτέλεση ενός συγκεκριμένου script ([f]ile) και εκτύπωση του αποτελέσματος στο `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Εκτύπωση μόνο της πρώτης γραμμής στο `stdout`:

`{{command}} | sed -n '1p'`
