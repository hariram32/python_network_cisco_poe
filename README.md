PoE Status Report
===================

Hello all, this is a simple script to produce a report of PoE usage and current enabled interfaces on a Cisco switch

----------

Process
-------------

 - Netmiko logs into a device listed within the all_devices dictionary (in `device_credientials.py`) 
 - Netmiko sends the following command to the device: `show power inline | exclude Interface|Watt|----` 
	 - the idea here is to exclude all unnecessary output
- first line of output will highlight the switch's current utilization 
- split up the output by line
- iterate through each line within for loop
- split up columns by white space
- store columns into variables
- if the power column is over 0.0 watts, produce output detailing the interface specifics

#### Notes
> - a try/except mechanism is included to provide feedback on any device that doesn't support PoE.
> - does not support Juniper (future release)

----------

Future Ideas
-------------

> - either email or create a .csv file local on the user's machine. 
> - running a CDP/LLDP neighbor on each interface pulling power.
