import random

ans1='You can do it!'
ans2='Keep going'
ans3="Don't smoking!"
ans4='shut up'
ans5='Working now'
ans6='한글이 가로로 쳐져!!!!'
ans7='가즈아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ'
ans8='gazuaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

print('MyMagic8ball에 오신 것을 환영합니다.')

question=input('조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n')

print('고민 중...\n'*4)

choice=random.randint(1,8)
if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
elif choice==6:
    answer=ans6
elif choice==7:
    answer=ans7
else :
    answer=ans8

print(answer)

input('\n\n마치려면 엔터 키를 누르세요.')
