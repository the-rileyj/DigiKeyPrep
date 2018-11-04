# Digi-Key Annual Collegiate Programming Competition Prep

## About

Gives a basic overview of the skills nessesary (in python 3) to be prepared for the [Annual Digi-Key Programming Competition](https://www.digikey.com/en/resources/edu/dkc3-computing-competition#Tabs1)

## Resources

* The problems for this year are available in ```./problems```

* Last years problems are available on the [Digi-Key website about the competition](https://www.digikey.com/en/resources/edu/dkc3-computing-competition#Tabs1)

## Getting Started

### Change the Boilerplate to conform to your system

The input and output paths are filled in with how they would be during the competition; clearly you will not have the same paths setup, change those and any other discrepancies to conform to your environment

```python

# Lines 6 and 7 in the original unchanged file
root_output_location = r"./{0}Out.txt".format(program_name)
root_input_location = r"./{0}In.txt".format(program_name)

```

### Copy the Boilerplate and Change it for the Problem You Pick

```python

# Line 4 in the original unchanged file
program_name = "Phone" # This sets it up for problem 1 where the input file is in the format {ProblemName}In.txt

```

### Run the Code and Check Your Output Against What is in the PDFs

Running your code (as you most likely know):

```bash

rj@fbi-spyvan:/DigiKeyPrep $ python {file name}

```

Then check the output you got with the given input against the predicted output for your problem (PDFs at ```./problems```).