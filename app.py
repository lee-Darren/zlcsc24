import streamlit as st

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")

# 2. 注入極致置中與卡片全域點擊的 CSS 樣式
st.markdown("""
<style>
/* 1. 強制讓 columns 橫向排列不換行，並產生滾動條 */
div[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    padding: 15px 5px !important;
    gap: 15px !important;
    scroll-behavior: smooth;
    align-items: stretch !important;
}

/* 2. 定義每一張卡片的寬度與外觀，並設為相對定位 */
div[data-testid="stHorizontalBlock"] > div {
    min-width: 210px !important;
    max-width: 210px !important;
    flex-shrink: 0 !important;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px 15px 25px 15px !important; /* 增加底部 padding，防止名字被擠壓切掉 */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important; 
    justify-content: flex-start !important;
    position: relative !important;
    overflow: hidden !important; /* 確保子元件與圓角對齊 */
}

/* 3. 滑鼠懸停卡片時的陰影與上浮效果 */
div[data-testid="stHorizontalBlock"] > div:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

/* 4. 自訂頭像外層包裝容器 */
.avatar-container {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
    margin: 0 auto 10px auto !important;
    pointer-events: none !important; /* 防止干擾點擊 */
}

/* 5. 圓形頭像樣式 */
.custom-circle-avatar {
    width: 110px !important;
    height: 110px !important;
    border-radius: 50% !important;
    object-fit: cover !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    display: block !important;
    pointer-events: none !important; /* 防止干擾點擊 */
}

/* 6. 職稱標籤樣式 */
.role-badge-container {
    width: 100%;
    text-align: center;
    margin-top: 5px;
    margin-bottom: 5px;
    pointer-events: none !important; /* 防止干擾點擊 */
}
.role-badge {
    background-color: #eef5ff;
    color: #007bff;
    font-size: 13px;
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 20px;
    display: inline-block;
    pointer-events: none !important; /* 防止干擾點擊 */
}

/* 7. 名字樣式 */
.member-name-text {
    font-size: 16px;
    font-weight: bold;
    color: #334155;
    margin-top: 10px;
    text-align: center;
    pointer-events: none !important; /* 防止干擾點擊 */
}

/* 8. 【終極放大點擊範圍】將 Streamlit 的按鈕與其父容器全部強制「絕對定位」並鋪滿整張卡片 */
div[data-testid="stHorizontalBlock"] div[data-testid="element-container"],
div[data-testid="stHorizontalBlock"] div.stButton {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}

div[data-testid="stHorizontalBlock"] button {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    background-color: transparent !important; /* 完全透明 */
    border: none !important;
    color: transparent !important; /* 隱藏按鈕文字 */
    box-shadow: none !important;
    cursor: pointer !important;
    z-index: 9999 !important; /* 頂天層級，絕對覆蓋在照片、職稱和名字之上 */
    border-radius: 16px !important; /* 圓角與外框卡片貼合 */
    margin: 0 !important;
}

/* 滑鼠移入卡片時，按鈕底色呈現極微透的藍色做點擊回饋 */
div[data-testid="stHorizontalBlock"] > div:hover button {
    background-color: rgba(0, 123, 255, 0.02) !important; 
}

/* 9. 滾動條美化 */
div[data-testid="stHorizontalBlock"]::-webkit-scrollbar {
    height: 8px;
}
div[data-testid="stHorizontalBlock"]::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 10px;
}
div[data-testid="stHorizontalBlock"]::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 10px;
}
div[data-testid="stHorizontalBlock"]::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# 3. 建立側邊欄導覽選單
st.sidebar.title("🧭 網站導覽")
page = st.sidebar.radio("請選擇頁面：", ["首頁介紹", "成員介紹", "聯絡我們"])

# 成員資料
members = [
    {
        "id": "0", 
        "role": "社長 兼 教學", 
        "name": "陳平安", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=chenpingan", 
        "email": "chenpingan@email.com", 
        "specialty": "程式架構、系統設計、網路爬蟲、資料處理", 
        "intro": "熱愛開源專案，擅長 Python 和 Web 開發，帶領大家進入數據的世界。"
    },
    {
        "id": "1", 
        "role": "副社 兼 教學", 
        "name": "李尚瑾", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=leeshangjin", 
        "email": "leeshangjin@email.com", 
        "specialty": "AI 應用、數據分析、專案實戰", 
        "intro": "對機器學習充滿熱情，喜歡用程式解決實際問題，用實際案例展示 AI 的力量。"
    },
    {
        "id": "2", 
        "role": "公關", 
        "name": "魏敘百", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=weisubai", 
        "email": "weisubai@email.com", 
        "specialty": "溝通協調、活動策劃", 
        "intro": "負責社團對外關係，是社團最溫暖的橋樑。"
    },
    {
        "id": "3", 
        "role": "活動", 
        "name": "張承緒", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=zhangchengxu", 
        "email": "zhangchengxu@email.com", 
        "specialty": "活動企劃、時間管理", 
        "intro": "確保每場活動順暢進行，細心負責是我的代名詞。"
    },
    {
        "id": "4", 
        "role": "活動 兼 總務", 
        "name": "曾開元", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=zengkaiyuan", 
        "email": "zengkaiyuan@email.com", 
        "specialty": "活動執行、現場管理、財務管理、資源規劃", 
        "intro": "活動現場的靈魂人物，並確保社團資源能得到最合理、最完美的分配。"
    },
    {
        "id": "5", 
        "role": "美宣", 
        "name": "倪宇廷", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=niyuting", 
        "email": "niyuting@email.com", 
        "specialty": "平面設計、視覺創意", 
        "intro": "用創意與美感設計，傳遞中崙資研最鮮明的品牌形象。"
    },
    {
        "id": "6", 
        "role": "設備", 
        "name": "陳庭弘", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=chentinghong", 
        "email": "chentinghong@email.com", 
        "specialty": "硬體維護、技術支援", 
        "intro": "默默守護大後方的設備狂熱者，負責社團所有的硬體與技術基礎建設。"
    },
    {
        "id": "7", 
        "role": "文書", 
        "name": "黃于恩", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=huangyuen", 
        "email": "huangyuen@email.com", 
        "specialty": "文檔整理、紀錄管理", 
        "intro": "細心記錄社團的發展歷程，保管所有珍貴的活動回憶與重要文檔。"
    },
    {
        "id": "8", 
        "role": "教學", 
        "name": "蘇奕全", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=suyichuan", 
        "email": "suyichuan@email.com", 
        "specialty": "Python 基礎、演算法", 
        "intro": "教學風格幽默風趣，擅長用最簡單好懂的概念講解複雜的演算法。"
    }
]

# 3. 根據使用者點選的頁面，顯示不同的內容
if page == "首頁介紹":
    st.title("歡迎來到中崙資研")
    st.subheader("這裡是最適合你的資訊研究社")
    
    st.image("https://raw.githubusercontent.com/lee-Darren/zlcsc24/main/1784017363261.jpg", width=700)
    
    st.markdown("""
    ### 🌟 關於我們
    我們是熱愛技術、喜歡動手實作的科技社團。無論你是程式小白還是大神的轉世，這裡都有你的舞台！
    * **學習內容**：Python 基礎、網路爬蟲、AI 應用、基礎演算法。
    * **社團活動**：技術交流會、專題黑客松、學長姐經驗傳承。
    """)

elif page == "成員介紹":
    st.title("🧑‍🤝‍🧑 成員介紹")

    # 初始化追蹤變數
    if "selected_member" not in st.session_state:
        st.session_state.selected_member = None

    # 1. 顯示「個人詳細頁面」
    if st.session_state.selected_member is not None:
        member = st.session_state.selected_member
        
        # 返回按鈕
        if st.button("← 返回成員列表"):
            st.session_state.selected_member = None
            st.rerun()
        
        st.markdown("---")
        
        # 個人詳細資訊卡片
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(member['img'], width=200)
        
        with col2:
            st.markdown(f"## {member['name']}")
            st.markdown(f'<span class="role-badge" style="font-size: 15px;">{member["role"]}</span>', unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(f"**📧 Email：** {member['email']}")
            st.markdown(f"**🎯 專長：** {member['specialty']}")
            st.markdown(f"**📝 簡介：** {member['intro']}")
            
    # 2. 顯示「左右滾動卡片列表」
    else:
        st.write("💡 點擊卡片內**任何地方**（包含照片、名字、背景）即可查看個人詳細資訊！")
        
        # 建立與成員數量相同的 columns
        cols = st.columns(len(members))
        
        for idx, member in enumerate(members):
            with cols[idx]:
                # A. 顯示頭像（透過 CSS 完美、強制左右置中）
                st.markdown(
                    f'<div class="avatar-container">'
                    f'<img src="{member["img"]}" class="custom-circle-avatar" />'
                    f'</div>', 
                    unsafe_allow_html=True
                )
                
                # B. 顯示職稱
                st.markdown(f'<div class="role-badge-container"><span class="role-badge">{member["role"]}</span></div>', unsafe_allow_html=True)
                
                # C. 顯示名字
                st.markdown(f'<div class="member-name-text">{member["name"]}</div>', unsafe_allow_html=True)
                
                # D. 終極全覆蓋透明按鈕
                if st.button("", key=f"btn_{member['id']}", use_container_width=True):
                    st.session_state.selected_member = member
                    st.rerun()

elif page == "聯絡我們":
    st.title("📬 聯絡社團幹部")
    st.write("有任何加入社團、合作或課程問題，請填寫表單：")
    
    with st.form("my_form"):
        name = st.text_input("你的稱呼：")
        class_num = st.text_input("班級 / 學號：")
        msg = st.text_area("你想問的問題或回饋：")
        
        submit_button = st.form_submit_button(label="送出表單")
        
        if submit_button:
            st.success(f"🎉 收到！謝謝 {name} 的留言，教學或網管學長會盡快回覆你！")
