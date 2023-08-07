def count_words_in_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())

        with open(output_filename, 'w') as file:
            file.write("Number of words: " + str(word_count))
        
        print("Number of words: ", word_count)

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")

# Test case
input_filename = "input.txt"
output_filename = "output.txt"
count_words_in_file(input_filename, output_filename)
