"""
@file Node.py
@author Marcin Kretkowski, Adrianna Łukaszuk
"""

class Node:
	def __init__(self, isLeaf, attribute, attributeValue):
		self.attribute = attribute
		self.attributeValue = attributeValue
		self.isLeaf = isLeaf
		self.children = []