s1 = "poranna"
s2 = "kawa"
mid_id = len(s1)//2
prev_id = mid_id
next_id = mid_id
s3 = s1[:prev_id] + s2 + s1[next_id:]
print(s3)
