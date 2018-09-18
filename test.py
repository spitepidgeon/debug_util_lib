

import args_util_lib
import debug_util_lib

#GLOBAL VARS
#debug=True



# args=args_util_lib.buildArgs()

# print "Num args: %s" % len(args)

# debug_util_lib.setup(debug)

#test_module.test1()
#print test_module.flag


print("\n\nBeginning script")

debug=debug_util_lib.debugger(2)
debug.setLevel(3)

print("Done\n\n")