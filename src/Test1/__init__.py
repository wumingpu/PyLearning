from pip._vendor.distlib.compat import raw_input
name = raw_input('What is your name?')
if name.endswith('tank'):
    print ('Hello tank')
elif name.endswith('xiao'):
    print ('Hello xiao')
else:
    print ('Hello Strange111')