# echo

> Εκτύπωση των δοθέντων ορισμάτων.
> Δείτε επίσης: `printf`.
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Εκτύπωση ενός μηνύματος κειμένου. Σημείωση: Τα εισαγωγικά είναι προαιρετικά:

`echo "{{Hello World}}"`

- Εκτύπωση ενός μηνύματος με μεταβλητές περιβάλλοντος:

`echo "{{My path is $PATH}}"`

- Εκτύπωση μηνύματος χωρίς τον χαρακτήρα νέας γραμμής στο τέλος (no newline/-[n]):

`echo -n "{{Hello World}}"`

- Προσάρτηση ενός μηνύματος στο αρχείο:

`echo "{{Hello World}}" >> {{file.txt}}`

- Ενεργοποίηση των ειδικών χαρακτήρων διαφυγής με backslash (enable escapes/-[e]):

`echo -e "{{Column 1\tColumn 2}}"`

- Εκτύπωση της κατάστασης εξόδου της τελευταίας εκτελεσθείσας εντολής (Σημείωση: Στο Windows Command Prompt και PowerShell οι αντίστοιχες εντολές είναι `echo %errorlevel%` και `$lastexitcode`):

`echo $?`

- Πέρασμα κειμένου σε άλλο πρόγραμμα μέσω `stdin`:

`echo "{{Hello World}}" | {{program}}`
