from game import *
def init():
    global s
    s = My_Secret_number()

def new_game(request):
    try:
        boundary = int(request.get('boundary',None))
        if boundary <=0:
            raise Exception
    except:
        return {'code':'error','msg':'유효한 범위가 아닙니다.'}

    global s
    s.New_Game(boundary)

    return {'code':'success'}

def guess(request):
    try:
        guess = int(request.get('guess',None))

    except:
        return {'code':'error','msg':'유효한 값이 아닙니다.'}

    global s
    result = s.Guess(guess)

    if result == 0:
        return {'code':'clear','msg':'GAME CLEAR '+s.Get_Trials()}
    elif result < 0:
        return {'code':'success','msg':'GREATER!'}
    elif result > 0:
        return {'code':'success','msg':'SMALLER!'}
    else:
        return {'code':'error','msg':'벗어난 범위의 값을 입력했습니다'}

    
