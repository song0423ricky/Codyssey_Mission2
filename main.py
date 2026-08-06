def print_menu():
    print("=" * 40)
    print("       🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def get_menu_choice():
    while True:
        try:
            raw = input("선택: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램을 종료합니다.")
            exit()

        if raw == "":
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력하세요.")
            continue

        if not raw.isdigit():
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        choice = int(raw)
        if choice < 1 or choice > 5:
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        return choice


def main():
    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == 1:
            print("퀴즈 풀기 (아직 구현 전)")
        elif choice == 2:
            print("퀴즈 추가 (아직 구현 전)")
        elif choice == 3:
            print("퀴즈 목록 (아직 구현 전)")
        elif choice == 4:
            print("점수 확인 (아직 구현 전)")
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()