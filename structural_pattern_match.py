# def execute_commad(command):
#     if command == 'ls':
#         print('$ listing files')
#     elif command == 'cd':
#         print('$ changing directory')
#     else:
#         print('$ command not implemented')

#     print('...rest of the code')

# execute_commad('ls')

# def execute_commad(command):
#     match command:
#         case 'ls':
#             print('$ listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _:
#             print('$ command not implemented')

# execute_commad('lss')


# def execute_commad(command):
#     match command.split():
#         case ['ls', *directories, '--force']:
#             for directory in directories:
#                 print('$ listing files FORCED', directory)
#         case ['ls', *directories]:
#             for directory in directories:
#                 print('$ listing files', directory)
#         case ['cd', path]:
#             print('$ changing directory', path)
#         case _:
#             print('$ command not implemented')        


# execute_commad('ls /Users /Documents --force')
# execute_commad('ls /Users /Documents')

# def execute_commad(command):
#     match command.split():
#         case ['ls' | 'list', *directories]:
#             for directory in directories:
#                 print('$ listing files from', directory)
#         case ['cd' | 'change', path]:
#             print('$ changing directory', path)
#         case _:
#             print('$ command not implemented')

#     print('...rest of the code')        


# execute_commad('ls /Users /Documents')
# execute_commad('list /Users /Documents')
# execute_commad('change /Users' )

# def execute_commad(command):
#     match command.split():
#         case ['ls' | 'list', *directories] if len((directories)) > 1:
#             for directory in directories:
#                 print('$ listing ALL directories from', directory)
#         case ['ls' | 'list', *directories] if len((directories)) <= 1:
#             for directory in directories:
#                 print('$ listing ONE directories from', directories[0])
#         case ['cd' | 'change', path]:
#             print('$ changing directory', path)
#         case _:
#             print('$ command not implemented')

#     print('...rest of the code')        


# execute_commad('ls /Users /Documents /Test')
# execute_commad('ls /Users')

# def execute_commad(command):
#     match command.split():
#         case ['ls' | 'list' as the_command, *directories] as the_list if len((directories)) > 1:
#             for directory in directories:
#                 print('$ listing ALL directories from', directory)
#             print(f'{the_command}{the_list}')
#         case ['ls' | 'list', *directories] if len((directories)) <= 1:
#             for directory in directories:
#                 print('$ listing ONE directories from', directories[0])
#         case ['cd' | 'change', path]:
#             print('$ changing directory', path)
#         case _:
#             print('$ command not implemented')

#     print('...rest of the code')        


# execute_commad('ls /Users /Documents /Test')
# execute_commad('ls /Users')


