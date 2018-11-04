from sys import stdout

# Setup for problem #1 - Chinese Phone Numbers
program_name = "Phone"

root_output_location = r"C:\DKC3\{0}Out.txt".format(program_name)
root_input_location = r"C:\DKC3\{0}In.txt".format(program_name)

# Uncomment when prepared to submit
# with open(root_output_location, "w") as output:
with open(root_input_location) as input_file:
    # Comment out and uncomment line 9 when ready to submit
    output = stdout
    for line in input_file:
        output.write(line)

