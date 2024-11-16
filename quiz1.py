import string

# Step 1: Set the sentence variable
sentence = "This is a simple example of how to handle a sentence with some punctuation."

# Step 2: Remove punctuation manually by iterating through the characters
sentence_no_punctuation = ""
for char in sentence:
    if char not in string.punctuation:
        sentence_no_punctuation += char

# Step 3: Initialize variables to store the reformatted sentence and average word length calculations
formatted_sentence = ""
total_word_length = 0
word_count = 0
current_word = ""

# Step 4: Iterate through the sentence character by character
for char in sentence_no_punctuation + " ":  # Add space at the end to capture the last word
    if char != " ":  # If the character is not a space, build the current word
        current_word += char
    else:  # If a space is encountered, process the current word
        if current_word:  # Ensure the word is not empty
            # Replace 'a' with '@' using format strings
            current_word = current_word.replace('a', '@').replace('s', '$')

            # Surround words with 3 or 4 letters in brackets using format strings
            if 3 <= len(current_word) <= 4:
                formatted_sentence += f"[{current_word}] "
            else:
                formatted_sentence += f"{current_word} "

            # Update total word length and word count for average calculation
            total_word_length += len(current_word)
            word_count += 1

            # Reset current_word for the next word
            current_word = ""

# Step 5: Calculate the average word length
if word_count > 0:
    average_word_length = total_word_length / word_count
else:
    average_word_length = 0

# Step 6: Print the formatted sentence and average word length
print("Formatted Sentence:", formatted_sentence.strip())
print("Average Word Length:", average_word_length)
