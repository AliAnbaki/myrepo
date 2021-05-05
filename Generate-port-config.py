#! /usr/bin/env python
"""
Script to create network config by using CSV files with Jinja templates.
"""
# importing modules
import csv
from jinja2 import Template


# Assign var to CSV file and J2 file
source_file = "switch-ports.csv"
interface_template_file = "switchport-interface-template.j2"

# place holder for full configuration
interface_configs = ""

# Open  the J2 file  and create a J2 Object
with open(interface_template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline= True)

# Open the CSV file
with open(source_file) as f:
# Use DictReader to access data from CSV
    reader = csv.DictReader(f)
# For each row in the CSV, generate an interface configuration using the jinja template
    for row in reader:
        interface_config = interface_template.render(
            interface = row["Interface"],
            vlan = row["VLAN"],
            server = row["Server"],
            link = row["Link"],
            purpose = row["Purpose"]
        )
#Switch, Interface, Server, Link, Purpose, VLAN
#sbx-n9kv-ao,Ethernet1/13,esxi-01,nic 0,Virtualization Host,trunk
# Append interface configuration to the full configuration
        interface_configs += interface_config

# Save the final configuraiton to interface_configs
with open("interface_configs.txt", "w") as f:
    f.write(interface_configs)
