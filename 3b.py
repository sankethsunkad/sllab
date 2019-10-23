class reverser:
    sent=""
    revsent=""
    def __init__(self,sent):
        self.sent=sent
        self.reverseWordSentence()
    def reverseWordSentence(self):
        self.revsent = " ".join(reversed(self.sent.split()))
sent=input("enter a phrase or a sentence : ")
rev = reverser(sent.strip())
print(rev.revsent)
