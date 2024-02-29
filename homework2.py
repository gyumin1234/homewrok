import random

def determine_winner(player, computer):
    # 가위바위보 승패를 판정하는 함수
    if player == computer:
        return "비겼습니다!"
    elif (player == "가위" and computer == "보") or \
        (player == "바위" and computer == "가위") or \
        (player == "보" and computer == "바위"):
        return "플레이어가 이겼습니다!"
    else:
        return "컴퓨터가 이겼습니다!"

def rock_paper_scissors():
    choices = ["가위", "바위", "보"]

    while True:
        # 플레이어의 선택을 입력받습니다.
        player_choice = input("가위, 바위, 보 중 하나를 선택하세요 (종료하려면 '종료' 입력): ").strip().lower()

        # 입력이 유효한지 확인합니다.
        if player_choice not in choices and player_choice != '종료':
            print("유효하지 않은 선택입니다. 다시 선택하세요.")
            continue
        
        if player_choice == '종료':
            print("게임을 종료합니다.")
            break

        # 컴퓨터의 선택을 무작위로 결정합니다.
        computer_choice = random.choice(choices)

        # 플레이어와 컴퓨터의 선택을 출력합니다.
        print(f"플레이어: {player_choice}, 컴퓨터: {computer_choice}")

        # 승패를 판정하고 결과를 출력합니다.
        winner = determine_winner(player_choice, computer_choice)
        print(winner)

# 가위바위보 게임을 실행합니다.
rock_paper_scissors()
