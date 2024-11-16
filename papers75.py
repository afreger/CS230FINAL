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
    authors = authors.replace('&', ',').split(',')
    i = 0
    while i < len(authors) - 1:
        name_last = authors[i].strip().capitalize()
        name_first = authors[i + 1].strip()
        if len(name_first.split()) == 1 and '.' in name_first:
            initial_first = name_first
        else:
            initial_first = initial(name_first)
        result += f"{initial_first} {name_last}; "
        i += 2

    if result.endswith("; "):
        result = result[:-2]
    return result + "}"


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
    numsent = abstract.count('.') + abstract.count('!') + abstract.count('?')  # Count number of sentences
    words = abstract.split()  # Split abstract into separate words
    numwords = len(words)  # Count the total number of words
    numchars = sum(len(removepunc(word)) for word in words)  # Count the number of characters excluding punctuation
    numstopwords = sum(1 for word in words if removepunc(word).lower() in STOPWORDS)  # Count stopwords

    avg_words_per_sent = round(numwords / numsent, 2)  # Calculate average words per sentence
    avg_chars_per_word = round(numchars / numwords, 2)  # Calculate average characters per word

    return numsent, numwords, numstopwords, avg_words_per_sent, avg_chars_per_word


def removepunc(word):
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join(char for char in word if char not in punctuations)


def printlongtext(text, attribute="Abstract"):
    # Create the initial line with the attribute name aligned to the right
    prefix = " " * (25 - len(attribute) - 1) + attribute + ": "

    # Determine the maximum text width based on screen length and line prefix
    width = SCREENLEN - len(prefix)

    # Split the text into words
    words = text.split()
    realline = ""
    linefirst = True

    # Loop through each word to form lines of appropriate width
    for word in words:
        # Check if adding the next word would exceed the maximum width
        if len(realline + word) + (1 if realline else 0) > width:
            if linefirst:
                # Print the first line with the attribute label
                print(prefix + realline)
                linefirst = False
            else:
                # Indent and print subsequent lines
                print(" " * 26 + realline)
            # Start a new line with the current word
            realline = word
        else:
            # Add the word to the current line, with a space if it's not the first word
            realline += (" " if realline else "") + word

    # Print any remaining words in the current line
    if realline:
        if linefirst:
            print(prefix + realline)
        else:
            print(" " * 26 + realline)


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