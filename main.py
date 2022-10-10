import activities
import os


def init():
    if not os.path.isfile('routines_generated.md'):
        with open('routines_generated.md', 'w+') as f:
            f.write('# Rutin generated')


init()


def show_routines():
    for key in routine_dict:
        print(key, '-->', routine_dict[key])


def flush_file():
    with open('routines_generated.md', 'w+') as f:
        f.write('')


def show_file():
    with open('routines_generated.md', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            print("    " + line.strip('\n'))


routine_dict = {}


def menu():
    for key in routine_dict:
        print(key)


stall = '30 sec: Mellantid'
routine_dict.update(activities.chores_routine)
routine_dict.update(activities.coding_routine)
routine_dict.update(activities.unsorted)
routine_dict.update(activities.lektions_rutin)
routine_dict.update(activities.nightly_routine)
routine_dict.update(activities.lunch_distans_rutin)
routine_dict.update(activities.random)
routine_dict.update(activities.iordning_sig)
routine_dict.update(activities.common_new_2022)


def append_to_first_line():
    for key in routine_dict:
        if routine_input == key:
            try:
                open("temp.txt", "w").write(f"{routine_dict[key]}" + open("routines_generated.md").read())

            except:
                print('Err: Write to file')


def dict_sort():
    sorted(routine_dict)
    for key in routine_dict:
        print(key)


state = 'run'

while state != 'quit':
    menu()
    print('Show, flush, quit, menu, sort, append')
    routine_input = input('Routine input: ')
    if routine_input == 'quit':
        state = 'quit'
    if routine_input == 'show':
        show_file()
    elif routine_input == 'flush':
        flush_file()
        show_file()
    elif routine_input == 'menu':
        menu()
    elif routine_input == 'sort':
        dict_sort()
        show_routines()
    elif routine_input == 'append':
        append_to_first_line()

    for key in routine_dict:
        if routine_input == key:
            print(key, '-->', routine_dict[key])
            try:
                with open('routines_generated.md', 'a+') as f:
                    f.write(stall)
                    f.write('\n')
                    f.write(routine_dict[key])
                    f.write('\n')
            except:
                print('Err: Write to file')
