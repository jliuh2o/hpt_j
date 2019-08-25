handle = 'Django'
max_hp = 200
cur_hp = 100

# def combat_tracker(cstats):

#     handle = cstats['character_name']
#     max_hp = cstats['maximum_hp']
#     cur_hp = cstats['current_hp']
turn_ct = 1
turn_ct = int(turn_ct)

print('Let\'s kick they dumb asses!!!\n\n\n')


com_status = True

while com_status:

    print('It is turn {}, {}!\n'
          'You are at {} / {} HP\n'
          'So what are you gonna do?\n'.format(turn_ct, handle,
           cur_hp, max_hp))
    action = input ('(1) Take damage\n'
                    '(2) Heal\n'
                    '(3) Cast spell\n'
                    '(4) Status affect\n'
                    '(5) End turn\n'
                    '(6) Finish Combat\n'
                    )

    if action == '1':
        l_var = input('How much damage did you take?')
        l_var = int(l_var)
        
        print('You have lost {} points out of your {} points of '
              'HP.\n'.format(l_var, cur_hp))

        cur_hp = cur_hp - l_var

        print('This puts you at {} points out of {} max points'.format(cur_hp, max_hp))

        if cur_hp < 1 and cur_hp > -2 * max_hp:
            print('You are down!\n'
                  'Oh shit, oh shit, oh shit!\n'
                  'Man, are you gonna make it???\n'
                  'Get ready for some DEATH saving throws.\n'
                  'Starting on your next turn tho.')
            
            d_suc = 0
            d_fail = 0
            
            while d_suc < 3 and d_fail < 3:

                cling = input('Are you ready for death saving throw? (y/n)')

                if cling == 'y':
                    turn_ct = turn_ct + 1
                    d_try = input('It is now turn {}.\nOk, go!\n'
                                  'Did you succeed(1) or did you FAIL'
                                  '(2)?'.format(turn_ct))
                    
                    if d_try == '1':
                        d_suc = d_suc + 1
                        print('Let\'s keep going!')


                        if d_suc > 2:
                            cur_hp = 1
                            print('Phew, ok.  You made it!\n'
                                  '...for now.....')

                    elif d_try == '2':
                        d_fail = d_fail + 1
                        print('Fluck a buck!')

                        if d_fail > 2:
                            print('Yeah, you are DED dead.\n'
                                  'Hmmmm, maybe close casket...')
                            # How do I make this end the combat?
                            break
                elif cling == 'n':
                    print('Ok, I guess we\'ll make death wait...')
    
    elif action == '2':
        g_var = input('How many HP did you gain?')
        g_var = int(g_var)
        cur_hp = cur_hp + g_var
        if cur_hp > max_hp:
            cur_hp = max_hp
            print('You gained {} points of HP.\n'
                  'So you are at {} point out of {}pt max'.format(g_var, cur_hp, max_hp))

    elif action == '3':

        spell_lvl = input('What level spell slot do you burn?(0-9)')
        spell_lvl = int(spell_lvl)

        if spell_lvl < 1:
            print('Oh, it\'s just a Cantripppppffff.  Whateves.')

        elif spell_lvl > 0:
            

        spell_dur = input('How many turns does you spell last?\n'
                          'Just put in 0 for instantaneous, smarty pants!')