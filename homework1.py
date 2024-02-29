# import random
#
# def up_down_game():
#     attempts = 0
#     best_score = float('inf')  # 플레이어의 최고 시도 횟수를 저장하는 변수
#
#     while True:
#         # 새로운 게임을 시작하거나 재시작할 때마다 숫자를 새로 생성합니다.
#         secret_number = random.randint(1, 100) # 1부터 100까지의 숫자 중 랜덤으로 번호를 생성합니다
#         print("새로운 게임을 시작합니다. 1부터 100 사이의 숫자를 맞춰보세요!")
#
#         while True:
#             try:
#                 guess = int(input("숫자를 입력하세요: "))
#             except ValueError:
#                 print("숫자를 입력하세요.")
#                 continue
#
#             attempts += 1 # 정답 ?번 시도하여 맞추었다는 변수 선언
#
#             if guess < 1 or guess > 100:
#                 print("1부터 100 사이의 숫자를 입력하세요.")
#                 continue
#
#             if guess < secret_number:
#                 print("업up! 더 큰 숫자를 입력하시오.")
#             elif guess > secret_number:
#                 print("다운down! 더 작은 숫자를 입력하시오.")
#             else:
#                 print(f"축하합니다! {attempts}번 시도해서 맞추셨습니다.")
#                 if attempts < best_score:
#                     best_score = attempts
#                     print(f"최고 기록 달성! 최고 시도 횟수: {best_score}")
#                 break




import random

        # 게임 재시작 여부를 묻고, 입력이 'yes'가 아니면 게임을 종료합니다.
play_again = input("게임을 다시 하시겠습니까? (Y/N): ").lower() #
if play_again != 'yes':
    print("게임을 종료합니다.")
    
def newgame():
        while True:
            yn= input("당신은 게임을 다시 시작하시겠습니까 ?: (Y/N)")
            if yn.lower() == "y":
                updown() # 게임을 재시작 여부를 묻고 있습니다 ^^
            elif yn.lower() == "n":
                print("Game EXit")
                break
            else:
                print("경고! 잘못 입력하셨습니다. 다시 입력해 주세요.")

        # 게임을 종료할시  시도한 횟수를 초기화합니다.
        attempts = 0

def updown():
    random_number = random.randint(1,100) # 랜덤으로 번호생성
    count = 1
    while True:
        try:
            answer = print("숫자를 입력")
            if answer == random_number :
                print("정답! 축하드립니다!")
                print(f'시도한 횟수 {count}번')
                newgame()
                break
            elif answer > random_number:
                print("down")
            else:
                print("up")
            count += 1
        except ValueError:
            print("숫자만 입력이 가능합니다.")

newgame()

# 업다운 게임 실행
# up_down_game()
