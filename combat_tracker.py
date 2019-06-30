"""

   python combat_tracker

"""

#enter character name
handle = input('Who are you, even? ') #with attitude
print(handle)

#enter max hp
max_hp = input('How tough are you on a good day? Like number-wise:')
max_hp = int(max_hp)
print(handle, '-- HP:', '/', max_hp)
print(type(max_hp))


#enter starting combat hp
starting_hp = input('How tough do you feel now? '
	                'Also, like a number.....:')
starting_hp = int(starting_hp)
print(handle, '-- HP:', starting_hp, '/', max_hp)

#enter hp change in current turn
cur_turn = input('What happened this turn, ? Use +x or -x: ')
cur_turn = int(cur_turn)

#calculate new current hp

cur_hp = starting_hp + cur_turn
print(type(cur_hp))
if cur_hp > max_hp:
    cur_hp = max_hp

elif cur_hp < 1 and cur_hp > -3 * max_hp:
    print('You are down, get ready for some saving throws!')

elif cur_hp < -3 * max_hp + 1:
    print('You dead!')




#display new current hp
print(handle, '-- HP:', cur_hp, '/',max_hp)

#following turns
