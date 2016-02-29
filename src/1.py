sum = 0
for num in xrange(1000):
	if num % 3 is 0 or num % 5 is 0:
		sum += num

print 'Answer: %s' % sum