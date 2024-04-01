def binary_to_hex(binary):
    # Convert binary to decimal first
    decimal = int(binary, 2)
    # Convert decimal to hexadecimal
    hexadecimal = hex(decimal)
    # Remove the '0x' prefix from the hexadecimal representation
    return hexadecimal[2:]

def convert_file(input_file, output_file):
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w') as f_out:
            for line in f_in:
                binary_number = line.strip()
                hexadecimal_number = binary_to_hex(binary_number)
                f_out.write(hexadecimal_number.upper() + '\n')

input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")

convert_file(input_file_path, output_file_path)
print("Conversion completed.")
