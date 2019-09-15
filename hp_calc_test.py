

def hp_calc(hp_stats):

	max_hp = int(hp_stats['max_hp'])
	cur_hp = int(hp_stats['cur_hp'])

	comb_status = True

	while comb_status:

		action = hp_menu()

		if action == '1':
			cur_hp = hp_gain(cur_hp, max_hp)

		elif action == '2':
			cur_hp = hp_loss(cur_hp)

		elif action == '3':
			print('Final HP is: ', cur_hp)
			return hp_stats
	

def hp_menu():

	action = input('(1). Gain\n'
				   '(2). Loose\n'
				   '(3). End\n'
					   			)
	return action

def hp_gain(cur_hp, max_hp):
	
	g_var = input('Enter HP gain:')
	g_var = int(g_var)
	cur_hp += g_var
	if cur_hp > max_hp:
		cur_hp = max_hp
	print('Current HP is: ', cur_hp)
	return cur_hp

def hp_loss(cur_hp):

	l_var = input('Enter HP loss:')
	l_var = int(l_var)
	cur_hp -= l_var
	if cur_hp < 1:
		print('Toast!!!  You is.')
	print('Current HP is: ', cur_hp)
	return cur_hp

if __name__ == '__main__':

	hp_stats = {
			    'max_hp': '100',
			    'cur_hp': '50',
			    }

	hp_calc(hp_stats)