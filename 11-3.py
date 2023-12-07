import d11_2 as mod

#다른 모듈에서 만든 데이터프레임 가져오기
print(mod.df1)

print("데이터 크기:" , mod.df1.shape)

#이름만 추출하여 리스트로 변경하여 출력
once_list=mod.df1['이름'].tolist()
print("특정 열만 다시 리스트로 변경 후 출력: ", once_list)

#코난의 정보만 추출하여 출력
print("특정 열의 특정 경우만 리스트 출력")
column_info=mod.df1[mod.df1['이름']=='코난'].set_index('이름')
print(column_info)

