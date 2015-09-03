Custom Topology created using Mininet
- Currently, can create X switches and Y hosts per switch (parameters taken as command line args)
- The even nodes ping only even nodes and odd nodes ping only odd nodes
- The bandwidth has been throttled to 1mbps for odd and 2mbps for even hosts.
- All the features have been fully implemented.

In order to run the code: sudo python2.7 customTopology.py <number_of_switches> <number_of_hosts_per_switch>
