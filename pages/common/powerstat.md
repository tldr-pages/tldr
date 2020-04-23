# powerstat

> Measures the power consumption of a computer that has a battery power source or supports the RAPL interface.
> More information: <http://manpages.ubuntu.com/manpages/bionic/man8/powerstat.8.html>.

- Measure power with the default of 10 samples with an interval of 10 seconds:

`powerstat`

- Measure power with custom number of samples and interval duration:

`powerstat {{interval}} {{number_of_samples}}`

- Measure power using Intel's RAPL interface:

`powerstat -R {{interval}} {{number_of_samples}}`

- Show an histogram of the power measurements:

`powerstat -H {{interval}} {{number_of_samples}}`

- Enable all statistics gathering options:

`powerstat -a {{interval}} {{number_of_samples}}`
