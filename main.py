#숫자야구 이정환
import random
data = 0
x = 0
ans = []
cnt = 0

# 랜덤을 이용, 겹치지 않게 뽑는거 
for i in range(3):
  num = random.randrange(0, 10)
  if num in ans:
    num = random.randrange(0, 10)
  ans.append(num)
print(ans)


# 게임을 실행
# 정답 생성
# (9번)플레이어 입력
  # 비교 => 맞으면 승리
# 패배

while(cnt <= 9):



# 플레이어 입력
while(cnt != 9):
  for i in range(3):
    x = input()

  s = 0
  b = 0
  for i in range(3):
    x = input()
    if(i == 0):
      if(x==num_h):
        s+=1
      elif(x==num_o | x==num_t):
        b+=1
    if(i == 1):
      if(x==num_t):
        s+=1
      elif(x==num_o | x==num_h):
        b+=1
    if(i == 2):
      if(x==num_o):
        s+=1
      elif(x==num_t | x==num_h):
        b+=1
  if(s == 3):
    print('성공')
  else:
    cnt+=1
    print('다시')
  if(cnt==8):
    print('종료')
    break