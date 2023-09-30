

import streamlit as st


st.set_page_config(layout='wide')


def main():
    st.title('测试')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('上传图片')
        img_file = st.file_uploader('QQ截图20230715165057.png')
    with col2:
        if img_file:
            st.image(img_file)


if __name__ == '__main__':
    main()
