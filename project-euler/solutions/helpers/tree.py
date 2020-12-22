#!/usr/bin/env python

class BinNode():
	''' '''
	def __init__(self, data, parent):
		self.data = data
		self.parent = parent
		self.left = None
		self.right = None

	def left(self, data):
		self.left = BinNode(data, self)
		return self.left

	def right(self, data):
		self.right = BinNode(data, self)
		return self.right


