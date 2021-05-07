from hashlib import sha256
from datetime import datetime

def updatehash(*args):
    hashing_text = ""; h = sha256()

    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block():

    def __init__(self,index=0, previous_hash="0"*64, data=None, signature=0,dateStamp=0):
        self.data = data
        self.index = index
        self.previous_hash = previous_hash
        self.signature = signature
        self.dateStamp= datetime.now()

    def hash(self):
        return updatehash(
            self.index,
            self.previous_hash,
            self.data,
            self.signature,
            self.dateStamp
        )

    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious_Hash: %s\nData: %s\nsignature: %s\nsignature: %s\n" %(
            self.index,
            self.hash(),
            self.previous_hash,
            self.data,
            self.signature,
            self.dateStamp
            )
        )


class Blockchain():
    difficulty = 4
    def __init__(self):
        self.chain = []

    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    def proofofwork(self, block):
       
        try: block.previous_hash = self.chain[-1].hash()
        except IndexError: pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.signature += 1

    def isValid(self):
        for i in range(1,len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
                return False

        return True

