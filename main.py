class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question   # 문제 문자열
        self.choices = choices     # 선택지 4개가 담긴 리스트
        self.answer = answer       # 정답 번호 (1~4)

    def show(self, index):
        print(f"\n[문제 {index}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

def play_quiz(quizzes):
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다.")
        return None

    print(f"\n📝 퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    correct_count = 0

    for index, quiz in enumerate(quizzes, start=1):
        quiz.show(index)
        answer = get_answer_input()
        if quiz.is_correct(answer):
            print("✅ 정답입니다!")
            correct_count += 1
        else:
            print(f"❌ 오답입니다. (정답: {quiz.answer}번)")

    score = int(correct_count / len(quizzes) * 100)
    print("\n" + "=" * 40)
    print(f"🏆 결과: {len(quizzes)}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40)
    return score

def add_quiz(quizzes):
    print("\n📌 새로운 퀴즈를 추가합니다.")

    question = get_text_input("문제를 입력하세요: ")

    choices = []
    for i in range(1, 5):
        choice = get_text_input(f"선택지 {i}: ")
        choices.append(choice)

    answer = get_answer_input()

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)

    print("\n✅ 퀴즈가 추가되었습니다!")


def get_text_input(prompt):
    while True:
        try:
            raw = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램을 종료합니다.")
            exit()

        if raw == "":
            print("⚠️ 입력이 비어 있습니다. 다시 입력하세요.")
            continue

        return raw

def get_answer_input():
    while True:
        try:
            raw = input("정답 입력: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램을 종료합니다.")
            exit()

        if raw == "":
            print("⚠️ 입력이 비어 있습니다. 숫자를 입력하세요.")
            continue

        if not raw.isdigit():
            print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        answer = int(raw)
        if answer < 1 or answer > 4:
            print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
            continue

        return answer

def get_default_quizzes():
    return [
        Quiz(
            "마블 시네마틱 유니버스에서 타노스가 모은 인피니티 스톤의 개수는?",
            ["4개", "5개", "6개", "7개"],
            3
        ),
        Quiz(
            "영화 '기생충'의 감독은?",
            ["박찬욱", "봉준호", "김기덕", "이창동"],
            2
        ),
        Quiz(
            "영화 '인터스텔라'의 감독은?",
            ["크리스토퍼 놀란", "제임스 카메론", "스티븐 스필버그", "리들리 스콧"],
            1
        ),
        Quiz(
            "아카데미 작품상을 최초로 수상한 비영어권 영화는?",
            ["기생충", "로마", "아무르", "화양연화"],
            1
        ),
        Quiz(
            "영화 '타이타닉'을 감독한 사람은?",
            ["제임스 카메론", "스티븐 스필버그", "리들리 스콧", "크리스토퍼 놀란"],
            1
        ),
    ]

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
    quizzes = get_default_quizzes()

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == 1:
            play_quiz(quizzes)    
        elif choice == 2:
            add_quiz(quizzes)
        elif choice == 3:
            print("퀴즈 목록 (아직 구현 전)")
        elif choice == 4:
            print("점수 확인 (아직 구현 전)")
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()