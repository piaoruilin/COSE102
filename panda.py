import pandas as pd

df_dict = dict()

df_dict['상호명'] = ['예예 치킨', '스타북스', '미세스 피자', '어디야 커피']
df_dict['시'] = ['서울특별시', '서울특별시', '서울특별시', '서울특별시']
df_dict['구'] = ['관악구', '종로구', '중랑구', '은평구']
df_dict['동'] = ['대학동', '창신동', '면목동', '구파발동']

df = pd.DataFrame(df_dict)

print(df)