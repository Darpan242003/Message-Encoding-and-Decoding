msg = input("Enter your message: ")
words = msg.split()

coding = input("Enter 1 if you want to encode a message and 0 to decode it:")

if (coding == "1"):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            s1 = ("qwe" + word[1:] + word[0] + "iop")
            nwords.append(s1)
        else:
            nwords.append(word[::-1])

    final_message = " ".join(nwords)
    print(final_message)

elif (coding == "0"):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            s1 = word[3:-3]
            s1 = s1[-1] + s1[:-1]
            nwords.append(s1)
        else:
            nwords.append(word[::-1])
final_message = " ".join(nwords)
print(final_message)       
    

















