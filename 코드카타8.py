# 리스트 안에 있는 숫자들 중, 과반수 이상에 해당하는 숫자면 그 숫자 반환하기
def more_than_half(nums):
    half_len = len(nums) // 2
    new = []
    new_dic = {}
  
    for i in nums:
        if i not in new:
            new.append(i)
    
    for k in new:
      num = nums.count(k)
      new_dic[k] = num
      if new_dic[k] > half_len:
          return new_dic[k]
