# datamash

> Instrument pentru a efectua operații numerice, textuale și statistice de bază pe fișierele de date textuale introduse.
> Mai multe informaţii: <http://www.gnu.org/software/datamash/>

- Obțineți max, min, medie și mediană a unei singure coloane de numere:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- Obțineți media unei singure coloane de numere plutitoare (flotoare trebuie să utilizeze „,” și nu” . „):

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- Obțineți media unei singure coloane de numere cu o precizie zecimală dată:

`echo -e '1\n2\n3\n4\n5\n5' | datamash -R {{number_of_decimals_wanted}} mean 1`

- Obțineți media unei singure coloane de numere ignorând „Na” și „NaN” (literal) șiruri:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
