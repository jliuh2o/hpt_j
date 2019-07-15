#Dis Thang contains my fxns

#This function collects character data and stores them in a file.
#It should be run as soon as the library is imported to establish base 
#conditions.

def stats():


    handle = None
    max_hp = None
    cur_hp = None

    exist = input('Hello, welcom to combat tracker Django3000!\n'
                  'It looks like shit is about to go down so,\n'
                  'let\'s get a few things straight.\n'
                  'Do I know you?  (y/n)')

    if exist == 'y':
        handle = input('So what is your handle?\n')
        #check for handle.stats.text
        with open(handle + '.stats.txt', 'r') as f:
            # handle = some line in file
            f.readline()
        
            # max_hp = some other line in file
            
            max_hp = int(f.readline())
            # cur_hp = some other, other line in file
            
            cur_hp = int(f.readline())

        print(handle, '---  HP: ', cur_hp, ' / ', max_hp)
        
        correct = input('Does this look right? (y/n)')
        if correct == 'y':
            print('Oh, goodie.  Let\'s go!')
            # begin combat tracking with combat menu.

        elif correct == 'n':
            print('Oh shit, gender-neutral offspring! Let\'s'
                  ' edit.')

            # edit = True
            # while edit:
            #     action = input('Change handle(h) -- Change'
            #                    ' max HP(m) -- Change current'
            #                    ' HP(c) -- Exit(e)')
            #     if action == 'h':
            #         # midify handle
            #     elif action == 'm':
            #         #midify max hp
            #     elif action == 'c':
            #         #modify current hp
            #     elif action == 'e':
            #         break
            #     else:
            #         print('Ummmm.... You don\'t have that'
            #                   ' option.')


    elif exist == 'n':
        handle = input('Yay, fresh meat for Cthulhu! \nWhat\'s your'
                       ' handle, sacrifice?\n')
        char_stats = handle + ('.stats.txt')
        with open(char_stats, 'w') as f:
            f.write(handle + '\n')


        print('Oh,', handle, 'sound almost dirty when you say it like that.\n'
              'Lets\'s get intimate.')
        max_hp = input ('What is your maximum HP?')
        max_hp = int(max_hp)

        cur_hp = input (' What is your current HP?')
        cur_hp = int(cur_hp)

        with open(char_stats, 'a') as f:
            f.write(str(max_hp) + '\n' + str(cur_hp) +'\n')

        
        print('Now we can begin, muahahahahha.')
        # Begin combat tracking with combat menu


    else:
        print('Wait, what?  That does not commute.')

    return {
            'character_name': handle,
            'maximum_hp': max_hp,
            'current_hp': cur_hp,
            }


#           HP Calculator here

def hp_calc(cstats):

    handle = cstats['character_name']
    max_hp = cstats['maximum_hp']
    cur_hp = cstats['current_hp']



    com_status = True

    while com_status:
        action = input('Heal(g) -- Damage(l) -- End Combat(f)' + '\n'*5)

        if action == 'g':
            g_var = input('How many points do you gain?')
            g_var = int(g_var)
            cur_hp = cur_hp + g_var
            if cur_hp > max_hp:
                cur_hp = max_hp
            print(handle, '-- HP:', cur_hp, '/', max_hp)
            print('Ok, next again...')

        elif action == 'l':
            l_var = input('How many points did you loose?')
            l_var = int(l_var)
            # print(l_var, cur_hp)
            cur_hp = cur_hp - l_var
            # print(cur_hp, type(max_hp))
            # print('type of cur_hp: ', type(cur_hp))
            # input('Press enter to continue...')
            if cur_hp < 1 and cur_hp > -3 * max_hp:
                print('You are down, get ready for some saving throws!')

            elif cur_hp < -3 * max_hp + 1:
                print('You dead!')
                break
            print(handle, '-- HP:', cur_hp, '/', max_hp)
            print('Ok, next again...')

        elif action == 'f':
            com_status = False
            print(handle, '-- HP:', cur_hp, '/', max_hp)

        else:
            print('That is an invalid input!'
                    'Try again...')

    cstats['current_hp'] = cur_hp


def combat_mop_up(cstats):

    handle = cstats['character_name']
    max_hp = cstats['maximum_hp']
    cur_hp = cstats['current_hp']

    with open(handle + '.stats.txt', 'w') as f:

        f.write(handle + '\n' + str(max_hp) + '\n' + str(cur_hp) 
                + '\n')


