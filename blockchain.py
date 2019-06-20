import hashlib
import json
from time import time 
from uuid import uuid4

class blokchain(object):
	
	def proof_of_work(self, last_proof):

		# proof of work algorithm
		# 	find a number p' in such way that hash(p p') contains leading 4 zero
		#  here p is previous proof and p' is the new proof 

		proof = 0

		while self.valid_proof(last_proof, proof) is False:
			proof+=1

		return proof

	def valid_proof(last_proof, proof):

		guess = f'{last_proof}{proof}'.encode()
		guess_hash = hashlib.sha256(guess).hexdigest()

		# return boolean if its leading 4 zero than True else false 
		return guess_hash[:4]== "0000"	



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
		# Creates as SHA-256 hash of a block
		block_string = json.dumps(block, sort_keys=True).encode()

		return hashlib.sha256(block_string).hexdigest()

	@property 
	def last_block(self):
		# returns last block in chain 
		return self.chain[-1]
