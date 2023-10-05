import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", "-a", type=float, default=0.5)
parser.add_argument("--l1_ratio", "-l1", type=float, default=0.5)

# Parse the command-line arguments
parsed_args = parser.parse_args()

# Access the parsed arguments
alpha_value = parsed_args.alpha
l1_ratio_value = parsed_args.l1_ratio

print("Alpha:", alpha_value)
print("L1 Ratio:", l1_ratio_value)
