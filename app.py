import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")

st.markdown("""
<style>
.block-container {
    padding: 1rem 3rem;
    text-align: center;
}
.member-scroll {
    display: flex;
    justify-content: center;
    gap: 16px;
    overflow-x: auto;
    padding: 16px 0;
}
.member-card {
    min-width: 240px;
    max-width: 240px;
    background: #ffffff;
    border: 1px solid #e6e6e6;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    padding: 18px;
    text-align: center;
    flex-shrink: 0;
}
.member-card img {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 50%;
    margin-bottom: 12px;
}
.member-card h4 {
    margin: 8px 0 4px;
    font-size: 18px;
}
.member-card p {
    margin: 4px 0;
    color: #333333;
}
.member-scroll::-webkit-scrollbar {
    height: 10px;
}
.member-scroll::-webkit-scrollbar-thumb {
    background: rgba(0,0,0,0.2);
    border-radius: 999px;
}
</style>
""", unsafe_allow_html=True)

# 2. 建立側邊欄導覽選單
st.sidebar.title("🧭 網站導覽")
page = st.sidebar.radio("請選擇頁面：", ["首頁介紹", "成員介紹", "社課講義", "聯絡我們"])

# 3. 根據使用者點選的頁面，顯示不同的內容
if page == "首頁介紹":
    st.title("歡迎來到中崙資研")
    st.subheader("用程式碼敲開未來的門，用熱血寫下我們的青春")
    
    # 放一張示範科技圖（使用 Unsplash 的可直接顯示圖片連結）
    st.image("images/1784017363261.jpg", width=700)
    
    st.markdown("""
    ### 🌟 關於我們
    我們是熱愛技術、喜歡動手實作的科技社團。無論你是程式小白還是大神的轉世，這裡都有你的舞台！
    * **學習內容**：Python 基礎、網路爬蟲、AI 應用、基礎演算法。
    * **社團活動**：技術交流會、專題黑客松、學長姐經驗傳承。
    """)

elif page == "成員介紹":
    st.title("🧑‍🤝‍🧑 成員介紹")
    st.write("認識我們的核心社員與幹部，歡迎加入中崙資研社團！")

    members = [
        {"role": "社長", "name": "陳平安", "img": "https://i.pravatar.cc/220?u=chenpingan"},
        {"role": "副社", "name": "李尚瑾", "img": "https://i.pravatar.cc/220?u=leeshangjin"},
        {"role": "公關", "name": "魏敘百", "img": "https://i.pravatar.cc/220?u=weisubai"},
        {"role": "活動", "name": "張承緒", "img": "https://i.pravatar.cc/220?u=zhangchengxu"},
        {"role": "活動", "name": "曾開元", "img": "https://i.pravatar.cc/220?u=zengkaiyuan"},
        {"role": "美宣", "name": "倪宇廷", "img": "https://i.pravatar.cc/220?u=niyuting"},
        {"role": "設備", "name": "陳庭弘", "img": "https://i.pravatar.cc/220?u=chentinghong"},
        {"role": "文書", "name": "黃于恩", "img": "https://i.pravatar.cc/220?u=huangyuen"},
        {"role": "教學", "name": "蘇奕全", "img": "https://i.pravatar.cc/220?u=suyichuan"},
        {"role": "教學", "name": "陳平安", "img": "https://i.pravatar.cc/220?u=chenpingan2"},
        {"role": "教學", "name": "李尚瑾", "img": "https://i.pravatar.cc/220?u=leeshangjin2"},
        {"role": "總務", "name": "曾開元", "img": "https://i.pravatar.cc/220?u=zengkaiyuan2"},
    ]

    cards_html = """
    <style>
    html, body { margin: 0; padding: 0; }
    .member-scroll {
        display: flex;
        justify-content: flex-start;
        gap: 16px;
        overflow-x: auto;
        padding: 16px 48px;
        scroll-snap-type: x mandatory;
    }
    .member-card {
        min-width: 240px;
        max-width: 240px;
        background: #ffffff;
        border: 1px solid #e6e6e6;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
        padding: 16px;
        text-align: center;
        flex-shrink: 0;
        scroll-snap-align: start;
        margin-right: 8px;
    }
    .member-card img {
        width: 120px;
        height: 120px;
        object-fit: cover;
        border-radius: 50%;
        margin-bottom: 12px;
    }
    .member-card h4 {
        margin: 8px 0 4px;
        font-size: 18px;
    }
    .member-card p {
        margin: 4px 0;
        color: #333333;
    }
    .member-scroll::-webkit-scrollbar {
        height: 10px;
    }
    .member-scroll::-webkit-scrollbar-thumb {
        background: rgba(0,0,0,0.2);
        border-radius: 999px;
    }
    </style>

    </style>

    <div style='display:flex; justify-content:center;'>
    <div class='member-scroll'>
    """
    for member in members:
        cards_html += f"""
        <div class='member-card'>
            <img src='{member['img']}' alt='{member['name']}'>
            <h4>{member['name']}</h4>
            <p><strong>{member['role']}</strong></p>
        </div>
        """
    cards_html += "</div></div>"

    components.html(cards_html, height=360, scrolling=True)
    st.write("---")
    st.write("如果你想要，我也可以幫你把每位社員的專長和聯絡方式補上。")

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
