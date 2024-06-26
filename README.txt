Usage: python burnRateCalc.py timesFile.txt pressuresFile.txt config.txt output.txt from cd of proper folder in command prompt
- timesFile and pressuresFile require matching time and pressure entries. goes line by line for each value. time should be in seconds and pressures should be in pascals
- config file contains the rest of the relevant data for the propellant grain used for the calculations (see below)
- sample input, output, and config files included in the folder, but you make your own for the grain

Files MUST be in the directory you're executing the command from.
This is only for a BATES propellant grain, and operates under the assumption that the throat area does not erode.

The output file will compare your entered initial web thickness (difference between the outer and inner diameter of the grain) to the total accounted burn distance. These should be near each other to ensure a good approximation. If they aren't, input a different initial burn distance.

Inputs and corresponding units for config file are as follows:

#  - Number of propellant segments (N)
#  - Segment outside diameter (D, mm)
#  - Throat area (Ato, mm^2)
#  - Density (g/cm^3)
#  - Initial web thickness (wo, mm)
#  - Inner diameter (do, mm)
#  - Segment initial length (Lo, mm)
#  - Characteristic velocity (c*, m/s)
#  - Initial burn distance guess (s, mm)
