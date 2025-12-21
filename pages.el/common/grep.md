# grep

> Εύρεση μοτίβων σε αρχεία χρησιμοποιώντας κανονικές εκφράσεις (`regex`).
> Περισσότερες πληροφορίες: <https://www.gnu.org/software/grep/manual/grep.html>.

- Αναζήτηση για ένα μοτίβο μέσα σε ένα αρχείο:

`grep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- Αναζήτηση για μια ακριβή συμβολοσειρά (απενεργοποιεί τα `regex`) (fixed strings/-[F]):

`grep {{[-F|--fixed-strings]}} "{{exact_string}}" {{path/to/file}}`

- Αναζήτηση μοτίβου σε όλα τα αρχεία αναδρομικά ([r]ecursive) σε έναν κατάλογο, εμφανίζοντας αριθμούς γραμμών ([n]umber) ταιριάσματος, αγνοώντας τα δυαδικά αρχεία ([I]gnore binary):

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{search_pattern}}" {{path/to/directory}}`

- Χρήση εκτεταμένων ([E]xtended) κανονικών εκφράσεων `regex` (υποστηρίζει `?`, `+`, `{}`, `()`, και `|`), σε λειτουργία αδιαφορίας πεζών-κεφαλαίων ([i]gnore case):

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{search_pattern}}" {{path/to/file}}`

- Εκτύπωση 3 γραμμών πλαισίου ([C]ontext) γύρω, πριν ([B]efore), ή μετά ([A]fter) από κάθε ταίριασμα:

`grep {{--context|--before-context|--after-context}} 3 "{{search_pattern}}" {{path/to/file}}`

- Εκτύπωση ονόματος αρχείου (with filename/-[H]) και αριθμού γραμμής ([n]umber) για κάθε ταίριασμα με έγχρωμη έξοδο:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{search_pattern}}" {{path/to/file}}`

- Αναζήτηση γραμμών που ταιριάζουν με ένα μοτίβο, εκτυπώνοντας μόνο ([o]nly) το ταιριαστό κείμενο:

`grep {{[-o|--only-matching]}} "{{search_pattern}}" {{path/to/file}}`

- Ανάγνωση δεδομένων από το `stdin` και μη εκτύπωση γραμμών που ταιριάζουν με το μοτίβο (αντιστροφή/in[v]ert match):

`cat {{path/to/file}} | grep {{[-v|--invert-match]}} "{{search_pattern}}"`
