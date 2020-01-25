#!/usr/bin/python3

import random

# 당첨 확률: 30%
WIN_RATE = 0.3
# 뽑기 횟수: 10개
NUMBER_OF_DRAWS = 10

# 뽑기 컨테이너와 승/패 개수
draws = []
win_draws = int(NUMBER_OF_DRAWS * WIN_RATE)
loss_draws = NUMBER_OF_DRAWS - win_draws
print("win={0} / loss={1}".format(win_draws, loss_draws))

# 당첨 제비를 넣습니다.
for i in range(0, win_draws):
    draws.append(1)

# 그 다음 꽝 제비를 넣습니다.
for i in range(0, loss_draws):
    draws.append(0)

# 제비를 섞습니다.
random.seed()
random.shuffle(draws)

# 제비 출력
print(draws)
