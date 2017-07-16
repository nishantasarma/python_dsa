class Node:

	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.number = None
		self.left = left
		self.right = right


class Tree:

	def __init__(self, data):
		self.data = data
		



	def number(tree, count=0):

		if tree.left is not None:
			count = number(tree.left, count)

		if tree.right is not None:		
			count = number(tree.right, count)
		
		tree.number = count
		return count+1
