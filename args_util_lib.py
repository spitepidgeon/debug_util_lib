def buildArgs():
	args=[]
	print 'Creating arg list (\'done\' to end)'
	args.append(raw_input('args[0]: ').strip())
	while args[-1] != 'done':
		args.append(raw_input('args[%s]: ' % len(args)).strip())
	args.pop(-1)
	print 'Done building list; %s items saved.' % len(args)
	return args
	  	
def printArgs(args):
	for index, arg in enumerate(args):
	  	print 'args[%s]: %s' % (index, arg)
