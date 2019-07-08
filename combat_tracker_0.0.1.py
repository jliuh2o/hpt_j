#Establishing player stats categories.

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


    print('Oh, handle almost sound dirty when you say it like that.\n'
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
