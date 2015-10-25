def reverse(byte):
	s = format(byte,'08b')
	s = s[::-1] # reverse
	return int(s, 2)

def bmp2bytes(s):
	s = s.replace('\n','')
	d = 0
	for y in range(7):
		for x in range(5):
			q = 1 << (37 - (y*5 + x))
			if s[y*5 + x] == 'x':
				d |= q
	
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
s['_'] = """
.....
.....
.....
.....
.....
xxxxx
.....
"""
s[':'] = """
.....
..xx.
..x..
.....
..x..
..xx.
.....
"""
s['.'] = """
.....
.....
.....
.....
..x..
..xx.
.....
"""

s['0'] = """
.xxx.
x...x
x...x
x...x
x...x
x...x
.xxx.
"""

s['8'] = """
.xxx.
x...x
x...x
.xxx.
x...x
x...x
.xxx.
"""

s['@'] = """
.xxx.
x...x
x..xx
x.x.x
x..xx
x....
.xxxx
"""

if __name__ == "__main__":
	print ', '.join( bmp2bytes(s['0']) )
	print bytes2bmp([0xf8, 0x10, 0x42, 0x8e, 0x1e])
