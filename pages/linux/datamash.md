# datamash

> Perform basic numeric, textual and statistical operations on input textual data files.
> More information: <http://www.gnu.org/software/datamash/>.

- Get max, min, mean and median of a single column of numbers:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- Get the mean of a single column of float numbers (floats must use "," and not "."):

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- Get the mean of a single column of numbers with a given decimal precision:

`echo -e '1\n2\n3\n4\n5\n5' | datamash -R {{number_of_decimals_wanted}} mean 1`

- Get the mean of a single column of numbers ignoring "Na" and "NaN" (literal) strings:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
