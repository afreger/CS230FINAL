def count_words(file_name):
    # List of words to track
    words_of_interest = ['excellent', 'great', 'good', 'ok']

    # Create an empty dictionary to store word counts
    word_counts = {}

    # Open the file and read its content
    file = open(file_name, 'r')
    content = file.read().lower()  # Read the file content and convert to lowercase
    file.close()  # Close the file after reading

    # Split the content into words
    words_in_file = content.split()

    # Iterate through each word in the file
    for word in words_in_file:
        # Check if the word is in the list of words of interest
        if word in words_of_interest:
            # If the word is found, increment its count in the dictionary
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts


# Example usage
file_name = 'words.txt'
print(count_words(file_name))
