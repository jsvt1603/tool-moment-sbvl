import streamlit as st
import numpy
import pandas
import math
from PIL import Image
from docx import Document
import io
import base64


#Tạo file hướng dẫn làm
def create_word_document(content):
    doc = Document()
    doc.add_paragraph(content)
    return doc

def get_binary_file_downloader_html(bin_file, file_label='File'):
    data = bin_file.getvalue()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,{bin_str}" download="{file_label}">Tải xuống file Word</a>'
    return href


#Đây là phần hearder
st.title("Công cụ tính mô men quán tính")
st.text("Đây là công cụ giúp các bạn tính moment một cách nhanh chóng với hình dạng phổ biến")
st.caption("Developer by Phan Văn Thành")

#Đây là phần sidebar
hinh_dang = ["Chữ I","Chữ T","Chữ U", "Chữ C"]
st.sidebar.header("Chọn hình dạng cấu kiện")
cau_kien = st.sidebar.radio("Chọn hình dạng cấu kiện",hinh_dang)


#Đây là phần thân
cot1,cot2,cot3 = st.columns(3)
with cot1:
    if cau_kien == "Chữ I":
        st.write("Đây là hình ảnh cấu kiện bạn đã chọn")
        image = Image.open('I.jpg')
        st.image(image)
    elif cau_kien == "Chữ T":
        st.write("Đây là hình ảnh cấu kiện bạn đã chọn")
        image = Image.open('T.jpg')
        st.image(image)
    elif cau_kien == "Chữ U":
        st.write("Đây là hình ảnh cấu kiện bạn đã chọn")
        image = Image.open('U.jpg')
        st.image(image)
    elif cau_kien == "Chữ C":
        st.write("Đây là hình ảnh cấu kiện bạn đã chọn")
        image = Image.open('C.jpg')
        st.image(image)

with cot2 :
    h_input = st.text_input("Nhập chiều cao h của cấu kiện (cm)")
    b_input = st.text_input("Nhập chiều rộng b của cấu kiện (cm)")
    c_input = st.text_input("Nhập chiều dày c của cấu kiện (cm)")
    f_input = st.text_input("Nhập chiều dày f của cấu kiện (cm)")

    
with cot3:
    try:
        h = float(h_input)
        b = float(b_input)
        c = float(c_input)
        f = float(f_input)
        
        if cau_kien == "Chữ I":
            Ix = 2 * ((b * (c ** 3)) / 12) + ((f * ((h-2*c) ** 3)) / 12)+(b*c)*2*(c/2+(h-2*c)/2)**2
            Iy = 2 * ((c * (b ** 3)) / 12) + (((h-2*c) * (f ** 3)) / 12)
            Ix = round(Ix,2)
            Iy = round(Iy,2)
            st.write(f"moment quán tính Ix là {Ix} (cm^4)")
            st.write(f"moment quán tính Iy là {Iy} (cm^4)")
            if st.button('Tải xuống bài hướng dẫn'):
                doc = create_word_document(f"Do là hình đối xứng theo phương x và phương y nên không cần tìm trọng tâm\n Ta chia hình thành ba khối hình chữ nhật để sử dụng công thức moment đối với hình chữ nhật\n Ở đây anh đã chia ba hình như hình minh họa\n {image}\n anh áp dụng công thức Ix=b*h^3/12")
                buf = io.BytesIO()
                doc.save(buf)
                buf.seek(0)
                st.markdown(get_binary_file_downloader_html(buf, 'Word_Document.docx'), unsafe_allow_html=True)

        elif cau_kien == "Chữ T":
            y = (b*c*(c/2+(h-c))+f*(h-c)*(h-c)/2)/(b*c+f*(h-c))
            Ix = 1/12*f*(h-c)**3+f*(h-c)*((h-c)/2-y)**2+(b*c**3)/12+b*c*((h-c)+c/2-y)**2
            Iy = ((h-c)*f**3)/12+b**3*c/12
            Ix = round(Ix,2)
            Iy = round(Iy,2)
            st.write(f"moment quán tính Ix là {Ix} (cm^4)")
            st.write(f"moment quán tính Iy là {Iy} (cm^4)")
        elif cau_kien == "Chữ U":
            y = (b*c*c/2+2*f*(h-c)*((h-c)/2+c))/(b*c+2*f*(h-c))
            Ix = 1/12*b*c**3+b*c*(y-c/2)**2+2*(1/12*f*(h-c)**3+f*(h-c)*((h-c)/2+c-y)**2)
            Iy = 1/12*c*b**3+2*(1/12*h*f**3+(h-c)*f*(b/2-f/2)**2)
            Ix = round(Ix,2)
            Iy = round(Iy,2)
            st.write(f"moment quán tính Ix là {Ix} (cm^4)")
            st.write(f"moment quán tính Iy là {Iy} (cm^4)")

        elif cau_kien == "Chữ C":
            y = (2*b*c*b/2+(h-2*c)*f*(h-2*c)/2)/(2*b*c+(h-2*c)*f)
            Ix = 1/12*f*(h-2*c)**3+2*(1/12*b*c**3+b*c*(c/2+(h-2*c)/2)**2)
            Iy = 1/12*(h-2*c)*f**3+(h-2*c)*f*((h-2*c)/2-y)+2*(1/12*c*b**3+c*b*(b/2-y)**2)
            Ix = round(Ix,2)
            Iy = round(Iy,2)
            st.write(f"moment quán tính Ix là {Ix} (cm^4)")
            st.write(f"moment quán tính Iy là {Iy} (cm^4)")
    except ValueError:
        st.warning("Vui lòng nhập các thông số hợp lệ.")
    
