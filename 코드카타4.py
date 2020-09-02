# 사전 스터디 당시 구현했던 팰린드롬
def palindrome(n):
    for i in range(0,len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True


n = input('단어를 입력하세요:')
print(palindrome(n))

# 코드카타 당시 팰린드롬 > int 형식이라 위의 코드로 구현 안됨. list로 변환 후 구현
def same_reverse(num):
    list_num = [num]
    for i in list_num:
      if i < 0:
        return False
      if i > 0:
        for i in range(0, len(list_num)//2):
          if list_num[i] == list_num[-i-1]:
            continue
          else:
            return False
        return True