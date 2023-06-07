file_path = "/Users/christelvanharen/Documents/StageRadboud/isatools/TWOCdemonstrator/data/ISA_test/feature-matrices-general.csv"

with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()
    replace_interpunction = file_contents.replace(';', ',')
    replace_interpunction = replace_interpunction.split('\n')
    output_lines = []

    for line in replace_interpunction:
        line = line.split(',')
        if line[0]:

            if not output_lines:
                # Enclose the first row in quotation marks
                quotation_marks = ['"' + item + '"' for item in line]
                output_lines.append(','.join(quotation_marks))
            else:
                quotation_marks = ['"' + item + '"' for item in line]
                bacteria = '"' + line[0] + '"'
                output_lines.append(bacteria + ',' + ','.join(line[1:]))
                # print(output_lines)

# Join the lines with newlines
    output_content = '\n'.join(output_lines)
    print(output_content)

# Rewrite the file with the modified content
with open(file_path, 'w') as file:
    file.write(replace_interpunction)

    print("File rewritten succesfully!")


