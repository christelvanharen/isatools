""" 
Adjusted by Christel van Haren
Last modification made on 27/6/2023

This Python scripts rewrote the feature data and the feature metadata, so it can be used for examples.ipynb
"""


def read_file(file_path):
    """
    Reads the contents of the file at the given file path.

    Args:
        file_path: The path to the input file.

    Returns:
        str: The contents of the input file.
    """
    with open(file_path, 'r') as file:
        file_contents = file.read()
    return file_contents


def process_file_content(file_content):
    """
    Processes the content of the file by replacing punctuation, splitting lines, and modifying the data.

    Args:
        file_content: The content of the input file.

    Returns:
        str: The processed content of the input file.
    """
    replace_interpunction = file_content.replace(';', ',')
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

    output_content = '\n'.join(output_lines)
    return output_content


def write_file(file_path, output_content):
    """
    Writes the given content to the file at the specified file path.

    Args:
        file_path: The path to the file.
        content: The content to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(output_content)


def main():
    file_path = "/Users/christelvanharen/Documents/StageRadboud/isatools/TWOCdemonstrator/data/ISA_test/feature-matrices-general.csv"
    file_contents = read_file(file_path)
    output_content = process_file_content(file_contents)
    write_file(file_path, output_content)
    print("File rewritten successfully!")


main()

