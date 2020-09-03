#String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.

def get_len_of_str(s):
    	dct = {}
	max_so_far = curr_max = start = 0
	for index, i in enumerate(s):
		if i in dct and dct[i] >= start:
			max_so_far = max(max_so_far, curr_max)
			curr_max = index - dct[i]
			start = dct[i] + 1
		else:
			curr_max += 1
		dct[i] = index
	return max(max_so_far, curr_max)