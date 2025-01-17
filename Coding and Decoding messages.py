import random 
import string
# import random and string module to add random letters in the message

length = 3      # no. of random letters to be added in each word

message = input("Enter your message: ")
words = message.split()  #saperate each word in a message

coding = input("Enter 1 if you want to encode a message and 0 to decode it:")

if (coding == "1"):    # coding block
    new_words = []
    for word in words:
        if (len(word) >= 3):
            sequence_start = "".join(random.choices(string.ascii_letters, k=length))
            # adds 3 random letters at the start of message
            sequence_end = "".join(random.choices(string.ascii_letters, k=length))
            # adds 3 random letters at the end of message
            msg = (sequence_start + word[1:] + word[0] + sequence_end)  # indexing to remove the first letter and append it to the end of each word
            new_words.append(msg)
        else:
            new_words.append(word[::-1]) # reverse the word if contains less than 3 letters

    final_message = " ".join(new_words)
    print(final_message)

elif (coding == "0"):      # decoding block
    new_words = []
    for word in words:
        if (len(word) >= 3):
            msg = word[3:-3] # removes the first and last three random letters of a word
            msg = msg[-1] + msg[:-1]  # rearrange the last letter at the start of each word
            new_words.append(msg)
        else:
            new_words.append(word[::-1])
    final_message = " ".join(new_words)
    print(final_message)       
    

















