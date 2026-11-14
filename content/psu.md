---
title: PSU
date: 02/11/2026
---
Input to the PSU - 220V / 50Hz OR 110V / 60HZ AC power.
Output from the PSU - 12V and 5V DC power.

#### Summary
The PSU's stages look like below, step 1-2 are on the dangerous side, having direct wire connection to the high power wall outlet, steps 4 and below are on the safe side, low power, low voltage. Step 3 is the separator between them.
These 2 circuits are galvanically isolated (means there is no direct path between them for the current to travel). Transformers are used to transmit power across these two sides, and opto-couplers are used for signalling, neither requires a wire connection.

1. AC power gets converted into 400V DC power.
	1. Components used - EMI filter, bridge rectifier, Active Power Factor Correction (PFC) circuit - <https://www.youtube.com/watch?v=MS5vd3LomWg>
2. 400V DC power is chopped into "fake" AC power. Detailed reasoning below.
3. The choppy 400V power is sent as input to two different transformers with different power ratios (input/output ratio which is fixed for a transformer). Transformers provide the galvanic isolation safety net. And the two power lines - 12V, 5VSB are totally separate power lines with different circuits and transformers. Only their input source is the same - 400V source.
	1. The bigger transformer steps down the 400V to 12V (this is also choppy aka "Fake AC" electric wave). This only gets turned on when you press the power button on your computer.
	2. The smaller transformer steps down the 400V to 5V (also called 5VSB, 5V stand-by), this one is always available, and keeps a few critical pieces on - clock, power on detection circuit, USB ports etc. Purple wire on the 24-pin connector. Keeping this always on uses very little idle power compared to the bigger converter circuit.
4. Smoothening out the 12V/5V choppy output from transformer to provide a flat stable DC power line.
#### Detailed dive
TBD
