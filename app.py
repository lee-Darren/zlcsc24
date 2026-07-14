import streamlit as st
import streamlit.components.v1 as components

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")

st.markdown("""
<style>
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
    st.subheader("這裡是最適合你的資訊研究社")
    
    # 放一張示範科技圖（使用 Unsplash 的可直接顯示圖片連結）
    st.image("https://raw.githubusercontent.com/lee-Darren/zlcsc24/main/1784017363261.jpg", width=700)
    
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
        {"role": "社長", "name": "陳平安", "img": "https://i.pravatar.cc/220?u=chenpingan", "email": "chenpingan@email.com", "specialty": "程式架構、系統設計", "intro": "熱愛開源專案，擅長 Python 和 Web 開發。"},
        {"role": "副社", "name": "李尚瑾", "img": "https://i.pravatar.cc/220?u=leeshangjin", "email": "leeshangjin@email.com", "specialty": "AI 應用、數據分析", "intro": "對機器學習充滿熱情，喜歡用程式解決實際問題。"},
        {"role": "公關", "name": "魏敘百", "img": "https://i.pravatar.cc/220?u=weisubai", "email": "weisubai@email.com", "specialty": "溝通協調、活動策劃", "intro": "負責社團對外關係，是社團的橋樑。"},
        {"role": "活動", "name": "張承緒", "img": "https://i.pravatar.cc/220?u=zhangchengxu", "email": "zhangchengxu@email.com", "specialty": "活動企劃、時間管理", "intro": "確保每場活動順暢進行，細心負責。"},
        {"role": "活動", "name": "曾開元", "img": "https://i.pravatar.cc/220?u=zengkaiyuan", "email": "zengkaiyuan@email.com", "specialty": "活動執行、現場管理", "intro": "活動現場的靈魂人物，確保一切完美。"},
        {"role": "美宣", "name": "倪宇廷", "img": "https://i.pravatar.cc/220?u=niyuting", "email": "niyuting@email.com", "specialty": "平面設計、視覺創意", "intro": "用創意設計傳遞社團的品牌形象。"},
        {"role": "設備", "name": "陳庭弘", "img": "https://i.pravatar.cc/220?u=chentinghong", "email": "chentinghong@email.com", "specialty": "硬體維護、技術支援", "intro": "負責社團設備和技術基礎設施。"},
        {"role": "文書", "name": "黃于恩", "img": "https://i.pravatar.cc/220?u=huangyuen", "email": "huangyuen@email.com", "specialty": "文檔整理、紀錄管理", "intro": "記錄社團發展歷程，保管重要文檔。"},
        {"role": "教學", "name": "蘇奕全", "img": "https://i.pravatar.cc/220?u=suyichuan", "email": "suyichuan@email.com", "specialty": "Python 基礎、演算法", "intro": "擅長用簡單方式講解複雜概念。"},
        {"role": "教學", "name": "陳平安", "img": "https://i.pravatar.cc/220?u=chenpingan2", "email": "chenpingan2@email.com", "specialty": "網路爬蟲、資料處理", "intro": "帶領大家進入數據的世界。"},
        {"role": "教學", "name": "李尚瑾", "img": "https://i.pravatar.cc/220?u=leeshangjin2", "email": "leeshangjin2@email.com", "specialty": "AI 應用、專案實戰", "intro": "用實際案例展示 AI 的力量。"},
        {"role": "總務", "name": "曾開元", "img": "https://i.pravatar.cc/220?u=zengkaiyuan2", "email": "zengkaiyuan2@email.com", "specialty": "財務管理、資源規劃", "intro": "確保社團資源合理分配和運用。"},
    ]

    # 初始化 Session State 用於模態視窗
    if "selected_member" not in st.session_state:
        st.session_state.selected_member = None

    # 建立可點擊的成員卡片 HTML
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
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .member-card:hover {
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
    }
    .member-card img {
        width: 120px;
        height: 120px;
        object-fit: cover;
        border-radius: 50%;
        margin-bottom: 12px;
        cursor: pointer;
    }
    .member-card h4 {
        margin: 8px 0 4px;
        font-size: 18px;
    }
    .member-card p {
        margin: 4px 0;
        color: #333333;
        font-size: 14px;
    }
    .member-scroll::-webkit-scrollbar {
        height: 10px;
    }
    .member-scroll::-webkit-scrollbar-thumb {
        background: rgba(0,0,0,0.2);
        border-radius: 999px;
    }
    </style>

    <div style='display:flex; justify-content:center;'>
    <div class='member-scroll'>
    """
    
    for idx, member in enumerate(members):
        cards_html += f"""
        <div class='member-card' onclick="document.getElementById('member-{idx}').click()">
            <img src='{member['img']}' alt='{member['name']}'>
            <h4>{member['name']}</h4>
            <p><strong>{member['role']}</strong></p>
        </div>
        <input type='hidden' id='member-{idx}'>
        """
    
    cards_html += "</div></div>"
    components.html(cards_html, height=360, scrolling=True)

    # 建立詳細資訊檢視
    st.write("---")
    st.write("💡 點擊頭像查看更多幹部資訊")
    
    # 建立欄位選擇器
    st.subheader("🔍 選擇幹部查看詳情")
    cols = st.columns(3)
    
    for idx, member in enumerate(members):
        col = cols[idx % 3]
        with col:
            if st.button(f"👤 {member['name']} ({member['role']})", key=f"btn-{idx}"):
                st.session_state.selected_member = idx
    
    # 顯示選中幹部的詳細資訊
    if st.session_state.selected_member is not None:
        member = members[st.session_state.selected_member]
        
        with st.container():
            st.markdown(f"### {member['name']} - {member['role']}")
            
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(member['img'], width=150, use_column_width=False)
            
            with col2:
                st.markdown(f"**📧 Email:** {member['email']}")
                st.markdown(f"**🎯 專長:** {member['specialty']}")
                st.markdown(f"**📝 簡介:** {member['intro']}")
            
            if st.button("❌ 關閉", key="close-modal"):
                st.session_state.selected_member = None
                st.rerun()

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
