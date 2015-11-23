# -*- coding: utf-8 -*-
def reverse(byte):
	s = format(byte,'08b')
	s = s[::-1] # reverse
	return int(s, 2)

def bmp2bytes(s):
	s = s.replace('\n','')
	assert(len(s) == 7*5)
	d = 0
	for y in range(7):
		for x in range(5):
			q = 1 << (37 - (y*5 + x))
			c = s[y*5 + x]
			if c == 'x':
				d |= q
			elif c != '.':
				print y, x
				raise Exception('Unknow symbol %s' % c)

	b = []
	for i in reversed(range(5)):
		x = d & (0xff << i*8)
		x = reverse(x >> i*8)
		b.append(format(x, '#04x'))
	return b

def bytes2bmp(byte):
	d = 0
	for i in range(5):
		b = reverse(byte[i])
		d |= b << (4 - i)*8
	
	s = ''
	for y in range(7):
		for x in range(5):
			q = 1 << (37 - (y*5 + x))
			if d & q:
				s += 'x'
			else:
				s += '.'
		s += '\n'
	return s

s = {}
s['А'] = """
.xxx.
x...x
x...x
x...x
xxxxx
x...x
x...x
"""

s['Б'] = """
xxxxx
x...x
x....
xxxx.
x...x
x...x
xxxx.
"""
s['В'] = """
xxxx.
x...x
x...x
xxxx.
x...x
x...x
xxxx.
"""

s['Г'] = """
xxxxx
x...x
x....
x....
x....
x....
x....
"""

s['Д'] = """
.xxxx
..x.x
..x.x
.x..x
x...x
xxxxx
x...x
"""

s['Е'] = """
xxxxx
x....
x....
xxxxx
x....
x....
xxxxx
"""

s['Ж'] = """
x.x.x
x.x.x
x.x.x
.xxx.
x.x.x
x.x.x
x.x.x
"""

s['З'] = """
xxxx.
....x
....x
..xx.
....x
....x
xxxx.
"""
s['И'] = """
x...x
x...x
x..xx
x.x.x
xx..x
x...x
x...x
"""
s['Й'] = """
.x.x.
..x..
x...x
x..xx
x.x.x
xx..x
x...x
"""

s['К'] = """
x...x
x..x.
x.x..
xx...
x.x..
x..x.
x...x
"""

s['Л'] = """
.xxxx
..x.x
..x.x
..x.x
..x.x
x.x.x
.x..x
"""
s['М'] = """
x...x
xx.xx
x.x.x
x...x
x...x
x...x
x...x
"""
s['Н'] = """
x...x
x...x
x...x
xxxxx
x...x
x...x
x...x
"""
s['О'] = """
.xxx.
x...x
x...x
x...x
x...x
x...x
.xxx.
"""
s['П'] = """
xxxxx
x...x
x...x
x...x
x...x
x...x
x...x
"""
s['Р'] = """
xxxx.
x...x
x...x
xxxx.
x....
x....
x....
"""
s['С'] = """
.xxx.
x...x
x....
x....
x....
x...x
.xxx.
"""
s['Т'] = """
xxxxx
..x..
..x..
..x..
..x..
..x..
..x..
"""
s['У'] = """
x...x
x...x
x...x
.x.x.
..x..
.x...
x....
"""
s['Ф'] = """
..x..
.xxx.
x.x.x
x.x.x
x.x.x
.xxx.
..x..
"""
s['Х'] = """
x...x
x...x
.x.x.
..x..
.x.x.
x...x
x...x
"""
s['Ц'] = """
x...x
x...x
x...x
x...x
x...x
xxxxx
....x
"""
s['Ч'] = """
x...x
x...x
x...x
.xxxx
....x
....x
....x
"""
s['Щ'] = """
x.x.x
x.x.x
x.x.x
x.x.x
x.x.x
xxxxx
....x
"""
s['Ш'] = """
x.x.x
x.x.x
x.x.x
x.x.x
x.x.x
x.x.x
xxxxx
"""
s['Ъ'] = """
xx...
.x...
.x...
.xxx.
.x..x
.x..x
.xxx.
"""
s['Ы'] = """
x...x
x...x
x...x
xx..x
x.x.x
x.x.x
xx..x
"""

s['ьБ'] = """
x....
x....
x....
xxxx.
x...x
x...x
xxxx.
"""
s['Э'] = """
.xxx.
x...x
..x.x
.x.xx
....x
x...x
.xxx.
"""
s['Ю'] = """
x..x.
x.x.x
x.x.x
xxx.x
x.x.x
x.x.x
x..x.
"""
s['Я'] = """
.xxxx
x...x
x...x
.xxxx
..x.x
.x..x
x...x
"""
s['а'] = """
.....
.....
.xxx.
....x
.xxxx
x...x
.xxxx
"""
s['б'] = """
..xxx
.x...
x....
xxxx.
x...x
x...x
.xxx.
"""
s['в'] = """
.....
.....
xxxx.
x...x
xxxx.
x...x
xxxx.
"""
s['г'] = """
.....
.....
xxxxx
x....
x....
x....
x....
"""
s['д'] = """
.....
.....
..xxx
.x..x
.x..x
xxxxx
x...x
"""
s['е'] = """
.....
.....
.xxx.
x...x
xxxxx
x....
.xxx.
"""
s['ё'] = """
.x.x.
.....
.xxx.
x...x
xxxxx
x....
.xxx.
"""

s['ж'] = """
.....
.....
x.x.x
x.x.x
.xxx.
x.x.x
x.x.x
"""
s['з'] = """
.....
.....
xxxx.
....x
.xxx.
....x
xxxx.
"""
s['и'] = """
.....
.....
x...x
x..xx
x.x.x
xx..x
x...x
"""
s['й'] = """
.x.x.
..x..
x...x
x..xx
x.x.x
xx..x
x...x
"""
s['к'] = """
.....
.....
x...x
x.x..
xx...
x.x..
x...x
"""
s['л'] = """
.....
.....
.xxxx
.x..x
.x..x
.x..x
x...x
"""
s['м'] = """
.....
.....
x...x
xx.xx
x.x.x
x...x
x...x
"""

s['н'] = """
.....
.....
x...x
x...x
xxxxx
x...x
x...x
"""
s['о'] = """
.....
.....
.xxx.
x...x
x...x
x...x
.xxx.
"""
s['п'] = """
.....
.....
xxxxx
x...x
x...x
x...x
x...x
"""
s['р'] = """
.....
.....
xxxx.
x...x
xxxx.
x....
x....
"""

s['с'] = """
.....
.....
.xxx.
x....
x....
x...x
.xxx.
"""
s['т'] = """
.....
.....
xxxxx
..x..
..x..
..x..
..x..
"""
s['у'] = """
.....
.....
x...x
.x.x.
..x..
.x...
x....
"""
s['ф'] = """
..x..
..x..
.xxx.
x.x.x
.xxx.
..x..
..x..
"""
s['х'] = """
.....
.....
x...x
.x.x.
..x..
.x.x.
x...x
"""
s['ц'] = """
.....
.....
x...x
x...x
x...x
xxxxx
....x
"""
s['ч'] = """
.....
.....
x...x
x...x
.xxxx
....x
....x
"""
s['ш'] = """
.....
.....
x.x.x
x.x.x
x.x.x
x.x.x
xxxxx
"""
s['щ'] = """
.....
.....
x.x.x
x.x.x
x.x.x
xxxxx
....x
"""
s['ъ'] = """
.....
.....
xx...
.x...
.xxx.
.x..x
.xxx.
"""
s['ы'] = """
.....
.....
x...x
x...x
xx..x
x.x.x
xx..x
"""
s['ь'] = """
.....
.....
x....
x....
xxxx.
x...x
xxxx.
"""
s['э'] = """
.....
.....
xxxx.
....x
.xxxx
....x
xxxx.
"""
s['ю'] = """
.....
.....
x..x.
x.x.x
xxx.x
x.x.x
x..x.
"""
s['я'] = """
.....
.....
.xxxx
x...x
.xxxx
.x..x
x...x
"""

s['ß'] = """
..xx.
.x..x
.x..x
.xxx.
.x..x
.x..x
x.xx.
"""

s['Ö'] = """
.x.x.
.xxx.
x...x
x...x
x...x
x...x
.xxx.
"""

s['ö'] = """
.....
.x.x.
.xxx.
x...x
x...x
x...x
.xxx.
"""

s['Ä'] = """
.x.x.
.xxx.
x...x
x...x
xxxxx
x...x
x...x
"""

s['ä'] = """
.....
.x.x.
.xxx.
....x
.xxxx
x...x
.xxxx
"""

s['Ü'] = """
.x.x.
x...x
x...x
x...x
x...x
x...x
.xxx.
"""

s['ü'] = """
.....
.x.x.
.....
x...x
x...x
x...x
.xxx.
"""

if __name__ == "__main__":
	for k in s.keys():
		print '{%s}, //"%s"' % (', '.join( bmp2bytes(s[k]) ), k)
		#	print bytes2bmp([0xf8, 0x10, 0x42, 0x8e, 0x1e])
