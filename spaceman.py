import random

# 화면 크기 설정
WIDTH = 400
HEIGHT = 400

# 게임 오브젝트 생성
player = Actor('alien')
player.pos = (200, 200)
question_mark = Actor('question')
question_mark.pos = (random.randint(50, 350), random.randint(50, 350))

# 게임 루프
def update():
    global question_mark
    
    # 키보드 입력 처리
    if keyboard.left:
        player.x -= 5
    elif keyboard.right:
        player.x += 5
    elif keyboard.up:
        player.y -= 5
    elif keyboard.down:
        player.y += 5
    
    # 충돌 체크
    if player.colliderect(question_mark):
        # 물음표와 충돌 시 물음표의 위치 재설정
        question_mark.pos = (random.randint(50, 350), random.randint(50, 350))
    
    # 화면 그리기
    screen.clear()
    player.draw()
    question_mark.draw()
