import hashlib
import json
from time import time 

class blokchain(object):
	
	# constructor will create empty list to store blockchain and another to store transactions
	def __init_(self):
		
		self.chain = []
		self.current_transaction = []

		# Create the block with no predecessors AKA genesir block 
		self.new_block(previous_hash = 1, proof = 100)

	def new_block(self,proof, previous_hash = None):
	
		
		block = {
			# length of chain
			'index': len(self.chain) + 1 ,
			'timestamp': time(),
			'transactions': self.current_transaction,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]), # allocation previous hash 

		}
		# Reset currect transcation
		self.current_transaction =[]

		self.chain.append(block) 

		return block 

	def new_transaction(self, sender, recipient, amount):
		# Adds new transation to the list of transactions


		self.current_transaction.append({

			'sender': sender,
			'recipient': recipient,
			'amount': amount,


			})
		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		# hashes a block
		pass

	@property 
	def last_block(self):
		# returns last block in chain 
		pass

