#!/usr/bin/env python3
import numpy as np
import json

class NonogramGenerator(object):
	"""docstring for NonogramGenerator"""
	def __init__(self):
		super(NonogramGenerator, self).__init__()

	@staticmethod
	def count_rows(ar):
		res = []
		for row in ar:
			row_res = []
			cnt = 0
			for v in row:
				if v == True:
					cnt += 1
				elif cnt != 0:
					row_res.append(cnt)
					cnt = 0
			if cnt != 0:
				row_res.append(cnt)
			res.append(row_res)
		return res

	@staticmethod
	def array_to_nonogram(ar):
		rows = []
		cols = []
		# make sure we get numpy array for shape and all
		ar = np.array(ar)
		if len(ar.shape) == 1 and type(ar[0]) == np.str_:
			ar = np.array([list(s.lower()) for s in ar]) == 'x'
		if len(ar.shape) != 2:
			raise ValueError('Must receive an array of 2 dimensions')
		ar = ar != 0 # convert to a bool array
		print(json.dumps({
				'r': NonogramGenerator.count_rows(ar),
				'c': NonogramGenerator.count_rows(np.transpose(ar))
				}))
		pass

ar = [
'...xxxxx.xxx..',
'...xxxxx.xxx..',
'...xx....xxxx.',
'...xx....xx.xx',
'...xxxx..xx..x',
'...xxxx..xx...',
'...xx....xx...',
'...xx....xx...',
'...xx....xx...',
'...xx....xx...',
]
NonogramGenerator.array_to_nonogram(ar)
