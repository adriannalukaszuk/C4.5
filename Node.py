class Node:
	def __init__(self,isLeaf, label):
		self.label = label
		self.isLeaf = isLeaf
		self.children = []