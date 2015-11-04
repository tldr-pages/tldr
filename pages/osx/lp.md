# lp

> print files

- print a file to a named printer (found in Printers & Scanners --> Options and Supplies)

'lp -d {{device_name}} {{path/to/filename}}

- print N copies to default printer (example used is 2)

'lp -n 2 {{path/to/filename}}'

- print only certain pages to the default printer (print pages 1, 3-5, and 16)

'lp -n -P 1,3-5,16'
