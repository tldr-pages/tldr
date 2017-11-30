# qsub

> Submits a script to the queue management system TORQUE.

- Submit a script with default settings (depends on TORQUE settings):

`qsub {{script.sh}}`

- Submit a script with a specified wallclock runtime limit of X hours, Y minutes and Z seconds:

`qsub -l walltime={{X}}:{{Y}}:{{Z}} {{script.sh}}`

- Submit a script that is executed on X nodes using Y cores per node:

`qsub -l nodes={{X}}:ppn={{Y}} {{script.sh}}`

- Submit a script to a specific queue. Note that different queues can have different maximum and minimum runtime limits:

`qsub -q {{queuename}} {{script.sh}}`
