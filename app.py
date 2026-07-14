import streamlit as st

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")

# 2. 完美的 CSS 注入：強制橫向滾動、美化卡片、並將原生的 Streamlit button 改造成整張可點擊的卡片
st.markdown("""
<style>
/* 1. 強制讓特定橫向區塊變成左右滑動，並加上柔和的滾動效果 */
div[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    padding: 20px 5px !important;
    gap: 20px !important;
    scroll-behavior: smooth;
}

/* 2. 限制每一個欄位 (卡片) 的寬度與卡片外觀 */
div[data-testid="stHorizontalBlock"] > div {
    min-width: 220px !important;
    max-width: 220px !important;
    flex-shrink: 0 !important;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 20px 15px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s, box-shadow 0.2s;
    text-align: center;
}

/* 3. 當滑鼠懸停在整張卡片上時的動態效果 */
div[data-testid="stHorizontalBlock"] > div:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

/* 4. 將原生按鈕改造成「透明滿版按鈕」，覆蓋在卡片內部，實現點擊頭像/文字皆能觸發 */
div[data-testid="stHorizontalBlock"] button {
    background-color: transparent !important;
    border: none !important;
    color: inherit !important;
    padding: 0 !important;
    width: 100% !important;
    height: auto !important;
    box-shadow: none !important;
    transition: none !important;
}

div[data-testid="stHorizontalBlock"] button:hover {
    background-color: transparent !important;
    color: #007bff !important; /* 懸停時名字變藍色提示可點擊 */
}

/* 5. 幹部頭像美化 */
.member-avatar {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    object-fit: cover;
    margin: 0 auto 12px;
    display: block;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    pointer-events: none; /* 讓點擊事件穿透到按鈕上 */
}

/* 6. 幹部職稱標籤樣式 */
.role-badge {
    background-color: #eef5ff;
    color: #007bff;
    font-size: 13px;
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 8px;
    pointer-events: none;
}

/* 7. 提示點擊的覆蓋小字 */
.click-hint {
    font-size: 11px;
    color: #a0aec0;
    margin-top: 5px;
    pointer-events: none;
}

/* 8. 滾動條美化 */
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

# 合併重複後的幹部資料（使用更穩定的 GitHub Avatars 作為頭像來源，解決無法顯示的問題）
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

    # 如果有被點擊的成員，進入「詳細頁面」
    if st.session_state.selected_member is not None:
        member = st.session_state.selected_member
        
        # 返回按鈕
        if st.button("← 返回成員列表"):
            st.session_state.selected_member = None
            st.rerun()
        
        st.markdown("---")
        
        # 個人詳細資訊頁面
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f'<img src="{member["img"]}" class="member-avatar" style="width:200px; height:200px; margin:0;">', unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"## {member['name']}")
            st.markdown(f'<span class="role-badge" style="font-size: 15px;">{member["role"]}</span>', unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(f"**📧 Email：** {member['email']}")
            st.markdown(f"**🎯 專長：** {member['specialty']}")
            st.markdown(f"**📝 簡介：** {member['intro']}")
            
    else:
        # 顯示成員列表（滑動狀態）
        st.write("💡 **左右滑動** 瀏覽幹部，**點擊任何一張幹部頭像/卡片**即可查看個人詳細資訊！")
        
        # 建立與成員數量相同的 columns (利用 CSS 保持在同一行並產生滾動條)
        cols = st.columns(len(members))
        
        for idx, member in enumerate(members):
            with cols[idx]:
                # 利用 HTML 設計卡片的內容結構
                card_content = f"""
                <img class="member-avatar" src="{member["img"]}" />
                <div><span class="role-badge">{member["role"]}</span></div>
                <div style="font-size: 18px; font-weight: bold; margin-bottom: 2px;">{member["name"]}</div>
                <div class="click-hint">🔍 點擊查看個人頁面</div>
                """
                
                # 將整段美化的 HTML 當成「按鈕文字」丟給 st.button 渲染！
                # 這樣一來，整張卡片（包含頭像與文字）就成為一個大按鈕，點擊任何地方都會觸發 Python 事件！
                if st.button(card_content, key=f"btn_{member['id']}", use_container_width=True):
                    st.session_state.selected_member = member
                    st.rerun()

elif page == "聯絡我們":
    st.title("📬 聯絡社團幹部")
    st.
