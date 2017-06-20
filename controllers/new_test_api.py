
def test():
	x,y,z = tuple(request.args)
	id = request.vars['id']
	gid = request.vars['gid']
	return 'test successful. args:{}, vars:{}'.format(request.args, (request.vars.keys(),request.vars.values()))