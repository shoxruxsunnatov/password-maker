from random import choice

l = 'abcdefghijklmnopqrstuvwxyz'
l += l.upper()+'0123456789'
l += '~!@#$%^&*()_+'

print('  By Shoxrux Sunnatov (Telegram: @Alexander_king).\n')
while True:
	input('\nClick ENTER for new password')
	password = ''
	for i in range(16):
		password += choice(list(l))

	print(' '+password)