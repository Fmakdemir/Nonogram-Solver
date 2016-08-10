#!/usr/bin/env python3
import numpy as np

class NonogramGenerator(object):
	"""docstring for NonogramGenerator"""
	def __init__(self):
		super(NonogramGenerator, self).__init__()

	@staticmethod
	def array_to_nonogram(ar):
		rows = []
		cols = []
		ar = np.array(ar)
		if len(ar.shape) != 2:
			raise ValueError('Must receive an array of 2 dimensions')
		ar = ar != 0 # convert to a bool array
		print(ar)
		pass

NonogramGenerator.array_to_nonogram([[2, 3], [1, 0]])