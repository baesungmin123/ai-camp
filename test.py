from PIL import Image
import streamlit as st

img = Image.open('images/김치찌개.jpg')
video_file = open('images/조리과정.mp4', 'rb')
st.title('내 짜바리 블로그 :smiley:')
st.header('하하하하하하하', divider='rainbow')
st.header('_아직 제대로 된 블로그는 :rainbow[아니다] :sunglasses:')
st.subheader("_사실 블로그라는 이름만 가지고 있지 사실상 :red[낙서장]임 ㅇㅇ")
st.header("1.:red[김치찌개]")
st.image(img)
img = Image.open('images/재료.png')
st.subheader(":rainbow[재료]")
st.image(img)
st.subheader("자세한 조리과정")
st.video(video_file)

st.header("2.자 이제 퀴즈 시간")
password1 = "김치찌개"
answer1 = "참치" and "돼지고기"
quiz1_password = st.text_input("퀴즈를 풀고싶다면, [지금까지 나온 메뉴 이름]을 적어주세요",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("이 두 재료중 내가 김치찌개에 더 많이 넣어먹는것은? 1.돼지고기,2.참치(배성민 기준)?")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1 == answer1:
            st.balloons()
            st.success("정답입니다!")
            st.write("난 돼지고기가 좋아 ╰(*°▽°*)╯")

