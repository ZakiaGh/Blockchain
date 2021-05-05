from hashlib import sha256
from datetime import datetime 

def hashFunction(block):
    bloc = (str(block.index) + 
    str(block.timeStamp) + 
    str(block.data) + 
    str(block.previousHash) + 
    str(block.signature))

    return(sha256(bloc.encode('utf-8')).hexdigest())

class Block(object):
    def __init__(self, index, timeStamp,previousHash, data):
        self.index = index
        self.timeStamp = timeStamp
        self.previousHash = previousHash
        self.data = data
        self.signature = 0
        self.hash = hashFunction(self)

    def proofWork(self, difficulty):
        nbr_zeros = "0" * difficulty

        while self.hash[0:difficulty] != nbr_zeros:
            self.signature += 1
            self.hash = hashFunction(self)

class Blockchain(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.chains = []
        
        firstBlock = Block(0,  datetime.now(), None, [])
        firstBlock.proofWork(self.difficulty)
        self.chains.append(firstBlock)

    @property
    
    def lastBlock(self):
        return self.chains[-1]
    
    def newBlock(self, data):
        return(Block(self.lastBlock.index + 1, datetime.now(), self.lastBlock.hash, data))

    def addBlock(self, block):
        block.proofWork(self.difficulty)
        pre_hash = self.lastBlock.hash
        if pre_hash != block.previousHash:
            return False
        self.chains.append(block)

    def expose(self):
        for block in self.chains:
            chain = ("Block  "+
            str(block.index)+
            " {"+"\tindex: "+str(block.index)+
            "\t\ttimestamp: "+str(block.timeStamp)+
            "\n\tprevious hash: "+str(block.previousHash) + 
            "\t\tdata: "+str(block.data)+"\n\thash: "+str(block.hash)+
            "\t\t\tsignature: "+str(block.signature)+"\n}\t")
            print(str(chain))

    
if __name__ == '__main__':
    bitcoin = Blockchain(3)

    blocknbr1 = bitcoin.newBlock("Oumaima sent to Zakia 10 BTC")

    bitcoin.addBlock(blocknbr1)

    blocknbr2 = bitcoin.newBlock("Kevin sent to Jean 2 BTC")

    bitcoin.addBlock(blocknbr2)

    blocknbr3 = bitcoin.newBlock("Alexia sent to Guillaume 6 BTC")

    bitcoin.addBlock(blocknbr3)

    blocknbr4 = bitcoin.newBlock("Yanis sent to Adam 7 BTC")

    bitcoin.addBlock(blocknbr4)


    bitcoin.expose()