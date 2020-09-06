#공통된 시작단어 반환
def get_prefix(strs):
     if len(strs) == 0:
   return ''
 
 res = ''
 strs = sorted(strs)

   for i in strs[0]:
       if strs[-1].startswith(res+i):
           res += i
       else:
           break
   return res