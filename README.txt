Usage: python burnRateCalc.py timesFile.txt pressuresFile.txt config.txt output.txt
Files MUST be in the directory you're executing the command from.
This is only for a BATES propellant grain, and operates under the assumption that the throat area does not erode.

Inputs and corresponding units are as follows:

#  - Number of propellant segments (N)
#  - Segment outside diameter (D, mm)
#  - Throat area (Ato, mm^2)
#  - Density (g/cm^3)
#  - Initial web thickness (wo, mm)
#  - Inner diameter (do, mm)
#  - Segment initial length (Lo, mm)
#  - Characteristic velocity (c*, m/s)
#  - Initial burn distance guess (s, mm)