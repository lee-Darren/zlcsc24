import streamlit as st

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")

# 2. 建立側邊欄導覽選單
st.sidebar.title("🧭 網站導覽")
page = st.sidebar.radio("請選擇頁面：", ["首頁介紹", "社課講義", "聯絡我們"])

# 3. 根據使用者點選的頁面，顯示不同的內容
if page == "首頁介紹":
    st.title("🚀 歡迎來到資訊研究社！")
    st.subheader("用程式碼敲開未來的門，用熱血寫下我們的青春")
    
    # 放一張示範科技圖（使用 Unsplash 的可直接顯示圖片連結）
    st.image("https://images.unsplash.com/photo-1518779578993-ec3579fee39f?auto=format&fit=crop&w=1200&q=80", width=700)
    
    st.markdown("""
    ### 🌟 關於我們
    我們是熱愛技術、喜歡動手實作的科技社團。無論你是程式小白還是大神的轉世，這裡都有你的舞台！
    * **學習內容**：Python 基礎、網路爬蟲、AI 應用、基礎演算法。
    * **社團活動**：技術交流會、專題黑客松、學長姐經驗傳承。
    """)

elif page == "社課講義":
    st.title("📚 歷屆社課資源庫")
    st.write("這裡是我們上課的精華筆記，歡迎社員自主複習：")
    
    # 使用摺疊選單（Expander）功能
    with st.expander("第一週：認識 Python 與環境架設"):
        st.write("學習如何在電腦安裝 Python，並印出人生第一行程式碼！")
        st.code("print('Hello, Python!')", language="python")
        
    with st.expander("第二週：網路爬蟲入門"):
        st.write("利用 Python 抓取網路上的公開資料。")
        st.code("import requests\nresponse = requests.get('https://example.com')", language="python")

elif page == "聯絡我們":
    st.title("📬 聯絡社團幹部")
    st.write("有任何加入社團、合作或課程問題，請填寫表單：")
    
    # 建立互動式表單
    with st.form("my_form"):
        name = st.text_input("你的稱呼：")
        class_num = st.text_input("班級 / 學號：")
        msg = st.text_area("你想問的問題或回饋：")
        
        # 點擊按鈕的反應
        submit_button = st.form_submit_button(label="送出表單")
        
        if submit_button:
            st.success(f"🎉 收到！謝謝 {name} 的留言，教學或網管學長會盡快回覆你！")
