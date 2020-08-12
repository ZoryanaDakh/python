s = str(input('Shutdown?'))

n = str(input('NShutdown?'))

def shut_down(answer):
    if answer == ('yes'):
        print('Shutting down')
    elif answer == ('no'):
        print('Shutdown aborted')
    else:
        print('Sorry')

shut_down(s)

shut_down(n)