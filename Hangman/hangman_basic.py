# 1. "Computer 단어 선택(변수1)" -> "빈칸보여주기(변수3)"
# 2. 사용자 알파벳 입력
# 3. 게임 상태 업데이트
# 4. 다 맞췄으면 사용자 Win
# 5. 7번이 틀렸으면 사용자 Loose


# ㄱ. 알파벳이 단어에 있으면 채우고 없으면 오류 횟수 증가
# ㄴ. 있으면 정답이라고 알려주고 "알파벳이 있는 칸을 채워서 출력(변수3)"
# ㄷ. 없으면 오답이라고 알려주고 "시도횟수(변수2)" 증가

# TEST
# 1.Man
# 2.APPLE
# 3.BANANA

import random
# 1.자료구조

limit_error = 7

def select_word():
    word_list = ["MAN","APPLE","BANANA","WOMAN","TOMATO","CAT"]
    return random.choice(word_list)

# 게임 로직
# 1. "Computer 단어 선택(변수1)" -> "빈칸보여주기(변수3)"
target_word = select_word()
# print("컴퓨터가 생각한 단어:", target_word)
blank_char = "_"
word_screen = blank_char * len(target_word)


num_error = 0
while num_error < limit_error:

    # 2. 사용자 알파벳 입력
    user_input = input("알파벳 입력: ").upper()
    if user_input in word_screen:
        print(f"{user_input}은 이미 맞춘 단어야 바보야")
        continue

    # 3. 게임 상태 업데이트
    # ㄱ. 알파벳이 단어에 있으면 채우고 없으면 오류 횟수 증가

    # 없으면 오류 횟수 증가
    if target_word.find(user_input) == -1:
        num_error += 1
        print(f"오답: {num_error}회")
    # 알파벳이 단어에 있으면 채우기
    else:
        for i in range(len(target_word)):
            if target_word[i] == user_input:
                word_screen = word_screen[:i] + user_input + word_screen[i+1:]
        print("정답:", word_screen)

    # 4. 다 맞췄으면 (word_screen에 _가 없으면) 사용자 Win
    if word_screen.count(blank_char) == 0:
        print("You Win")
        break

# 5. 7번이 틀렸으면 You Loose
if num_error >= limit_error:
    print("You Loose", target_word)