"""
Homework #3
Description: Strings and functions
"""
import constants
WIDTH = 25
SCREENLEN = constants.SCREENLEN
STOPWORDS = constants.STOPWORDS


def processcitation(citation):
    # Determine the type based on the outlet (journal or conference)
    if "Proceedings" in citation:
        type = "Conference Article"
    else:
        type = "Journal Paper"

    year = citation.split('(')[1][:4]
    authors = citation.split('.')[0].strip()
    title = citation.split('.')[1].strip()
    outlet = citation.split(',')[1].strip()
    vol_issue = citation.split(',')[2].split()[0]
    issue = citation.split(',')[2].split()[1] if len(citation.split(',')[2].split()) > 1 else ""
    pp = citation.split(',')[3].strip() if len(citation.split(',')) > 3 else ""
    article = citation.split(',')[4].strip() if len(citation.split(',')) > 4 else ""

    # Process the authors to format them correctly
    authors = processauthors(authors)

    return type, year, authors, title, outlet, vol_issue, issue, pp, article


def processauthors(authors):
    result = "{"
    author_list = authors.replace("&", "").split(",")  # Split by comma and remove &
    processed_authors = []

    for author in author_list:
        author = author.strip()
        # Check if there is a space for first and last name
        if " " in author:
            # Extract the first initial and last name
            names = author.split()
            first_initial = names[1][0].upper() + "."
            last_name = names[0].capitalize()
            processed_authors.append(f"{first_initial} {last_name}")

    # Join authors with "; "
    result += "; ".join(processed_authors)
    result += "}"
    return result


def initial(firstname):
    '''
    This is a supporting function to extract the first name initial
    '''
    return firstname[0].upper()  # Return the uppercase initial

def processtitle(title):
    title = title.capitalize()

    # Find punctuation marks and capitalize the next character after them
    result = []
    capitalize_next = False

    for char in title:
        if capitalize_next and char.isalpha():  # Capitalize the next letter after punctuation
            result.append(char.upper())
            capitalize_next = False
        else:
            result.append(char)

        if char in ':.!?':  # Set flag after punctuation
            capitalize_next = True

    return ''.join(result)

    # return title.capitalize()

def abstractstats(abstract):
    numsent = len(abstract.split('. '))  # Count sentences by splitting at periods followed by a space
    numwords = removepunc(abstract).count(" ") + 1  # Count words by splitting at spaces
    numchars = sum(len(word) for word in abstract)  # Total number of characters
    numstopwords = 0

    for word in abstract.split():
        clean_word = removepunc(word.lower())  # Remove punctuation from each word
        if clean_word in STOPWORDS:
            numstopwords += 1

    avg_sent_len = round(numwords / numsent, 2)
    avg_word_len = (len(removepunc(abstract)) - removepunc(abstract).count(" ")) / numwords

    return numsent, numwords, numstopwords, avg_sent_len, avg_word_len

def removepunc(word):
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join(char for char in word if char not in punctuations)


def printlongtext(text, attribute="Abstract"):
    print(f"{attribute + ':':>{WIDTH}}", end=" ")  # Print the attribute label
    text = text.replace("\n", " \n ").split(" ")  # Split the text into words, accounting for newlines
    current_line = ""

    first_line = True
    for word in text:
        if word == "\n":  # Handle explicit newline
            print(current_line.rstrip())  # Print the current line and start a new one
            current_line = ""
            first_line = False
        elif len(current_line) + len(word) + 1 <= SCREENLEN:  # Check if word fits in the current line
            current_line += word + " "  # Add word to current line
        else:
            if first_line:
                print(current_line.rstrip())  # Print the first line with the attribute label
                first_line = False
            else:
                print(" " * (WIDTH + 1) + current_line.rstrip())  # Indent subsequent lines
            current_line = word + " "  # Start new line with the word

    # Print the last line
    if current_line:
        if first_line:
            print(current_line.rstrip())  # Print the first line
        else:
            print(" " * (WIDTH + 1) + current_line.rstrip())  # Indent last line


# Helping functions
def printcitation(type, year, authors, title, outlet, vol, issue, pp, article):
    print(f"{'Publication Type:':>{WIDTH}} {type}")
    print(f"{'Publication Year:':>{WIDTH}} {year}")
    printlongtext(authors, "Authors")
    printlongtext(title, "Title")
    printlongtext(outlet, "Publication Venue")
    print(f"{'Volume:':>{WIDTH}} {vol}")
    print(f"{'Issue:':>{WIDTH}} {issue}")
    print(f"{'Pages:':>{WIDTH}} {pp}")
    print(f"{'Article No.:':>{WIDTH}} {article}")

def printabstract(abstract, numsent, numwords, numstopwords, avgsentlen, avgwordlen):
    printlongtext(abstract, "Abstract")
    print(f"{'# sentences:':>{WIDTH}} {numsent}")
    print(f"{'# words:':>{WIDTH}} {numwords}")
    print(f"{'# stop words:':>{WIDTH}} {numstopwords}")
    print(f"{'Average sentence length:':>{WIDTH}} {avgsentlen}")
    print(f"{'Average word length:':>{WIDTH}} {avgwordlen}")
    print()

# Main function
def main():
    count = 0
    f = open("input.txt", 'r')
    lines = f.read().split('\n')

    for line in lines:
        line = line.strip()
        if len(line) != 0:
            count += 1

            if count % 2 == 1:
                print("=" * ((SCREENLEN-8)//2) + "Paper #" + str(count//2+1) + "=" * ((SCREENLEN-8)//2))

            if line.startswith("Citation"):
                type, year, authors, title, outlet, vol, issue, pp, article = processcitation(line[10:])
                printcitation(type, year, authors, title, outlet, vol, issue, pp, article)  # [10:] strips off "Citation:"
            else:
                numsent, numwords, numstopwords, avgsentlen, avgwordlen = abstractstats(line[10:])
                printabstract(line[10:], numsent, numwords, numstopwords, avgsentlen, avgwordlen)  # [10:] strips off "Abstract:"

def test():
    print("\nremovepunc tests")
    word1 = removepunc("Prediction:")  # check for punctuation at end of word
    word2 = removepunc("hello,")  # another test
    word3 = removepunc("world!")  # another test
    print(word1, word2, word3, sep="\n")

    print("\nprocessauthors tests")
    authors1 = processauthors("Messeri, L. & Crockett, M.J.")  # two authors
    authors2 = processauthors("Smith, J. & Doe, J.")  # two authors
    authors3 = processauthors("Brown, A. & Taylor, B.")  # two authors
    print(authors1, authors2, authors3, "\n", sep="\n")

    print("\nprocesstitle tests")
    title1 = processtitle("Harnessing Python: Transforming Business Analytics in Education")
    title2 = processtitle("a simple test case for title processing")
    title3 = processtitle("sample title case")
    print(title1, title2, title3, "\n", sep="\n")

    print("\nprintlongtext tests")
    outlet = "International Journal of Innovative Practices in Business Education and Technology Integration"
    printlongtext(authors1, "Authors")
    printlongtext(title1, "Title")
    printlongtext(outlet, "Publication Venue")

    print("\nprocesscitation tests")
    type, year, authors, title, outlet, vol, issue, pp, article = \
        processcitation(
            "Messeri, L. & Crockett, M.J. (2024). Artificial intelligence and illusions of understanding in scientific research, Nature, 627, 49-58.")
    printcitation(type, year, authors, title, outlet, vol, issue, pp, article)

    print("\nabstract test")
    abstract = "This is a very long sentence. It could be the abstract of an article. It describes a summary of the article."
    numsent, numwords, numstopwords, avgsentlen, avgwordlen = abstractstats(abstract)
    printabstract(abstract, numsent, numwords, numstopwords, avgsentlen, avgwordlen)

# test()
main()
