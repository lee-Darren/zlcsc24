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
    padding: 20px 15px 45px 15px !important; /* 增加底部 padding (45px)，為「個人頁面」文字留出空間 */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important; 
    justify-content: flex-start !important;
    position: relative !important; /* 作為絕對定位按鈕的基準 */
    overflow: hidden !important; 
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
    pointer-events: none !important; /* 確保滑鼠事件穿透 */
}

/* 5. 圓形頭像樣式 */
.custom-circle-avatar {
    width: 110px !important;
    height: 110px !important;
    border-radius: 50% !important;
    object-fit: cover !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    display: block !important;
    pointer-events: none !important;
}

/* 6. 職稱標籤樣式 */
.role-badge-container {
    width: 100%;
    text-align: center;
    margin-top: 5px;
    margin-bottom: 5px;
    pointer-events: none !important;
}
.role-badge {
    background-color: #eef5ff;
    color: #007bff;
    font-size: 13px;
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 20px;
    display: inline-block;
    pointer-events: none !important;
}

/* 7. 名字樣式 */
.member-name-text {
    font-size: 16px;
    font-weight: bold;
    color: #334155;
    margin-top: 10px;
    text-align: center;
    pointer-events: none !important;
}

/* 8. 【終極完美覆蓋】精準定位只包覆 stButton 的容器，將按鈕 100% 展開並覆蓋整張卡片 */
div[data-testid="stHorizontalBlock"] div[data-testid="element-container"]:has(div.stButton) {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    z-index: 9999 !important; /* 超高層級，絕對覆蓋在照片、職稱、名字的最上方 */
}

div[data-testid="stHorizontalBlock"] div.stButton,
div[data-testid="stHorizontalBlock"] div.stButton > button {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    background-color: transparent !important; /* 平時背景完全透明 */
    border: none !important;
    box-shadow: none !important;
    cursor: pointer !important;
    border-radius: 16px !important; /* 圓角貼合卡片外框 */
    
    /* 核心排版：利用 Flexbox 將按鈕文字推至卡片最底部 */
    display: flex !important;
    align-items: flex-end !important;
    justify-content: center !important;
    padding-bottom: 15px !important; /* 控制「個人頁面」字樣與底部的距離 */
    
    /* 文字樣式設定 */
    color: #007bff !important; 
    font-size: 14px !important;
    font-weight: bold !important;
    transition: background-color 0.2s, color 0.2s !important;
}

/* 當滑鼠移入卡片時，整張卡片微幅變暗，且文字顏色加深 */
div[data-testid="stHorizontalBlock"] > div:hover button {
    background-color: rgba(0, 123, 255, 0.03) !important; 
    color: #0056b3 !important;
    text-decoration: underline !important; /* 滑鼠懸停時加上底線，增加提示感 */
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
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "1", 
        "role": "副社 兼 教學", 
        "name": "李尚瑾", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=leeshangjin", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "2", 
        "role": "公關", 
        "name": "魏敘百", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=weisubai", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "3", 
        "role": "活動", 
        "name": "張承緒", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=zhangchengxu", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "4", 
        "role": "活動 兼 總務", 
        "name": "曾開元", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=zengkaiyuan", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "5", 
        "role": "美宣", 
        "name": "倪宇廷", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=niyuting", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "6", 
        "role": "設備", 
        "name": "陳庭弘", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=chentinghong", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "7", 
        "role": "文書", 
        "name": "黃于恩", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=huangyuen", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    },
    {
        "id": "8", 
        "role": "教學", 
        "name": "蘇奕全", 
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=suyichuan", 
        "email": "************@email.com", 
        "specialty": "**********", 
        "intro": "*****************"
    }
]

# 3. 根據使用者點選的頁面，顯示不同的內容
if page == "首頁介紹":
    st.title("歡迎來到中崙資研")
    st.subheader("這裡是最適合你的資訊研究社")
    
    st.image("https://raw.githubusercontent.com/lee-Darren/zlcsc24/main/1784017363261.jpg", width=700)
    
    st.markdown("""
    ### 🌟 關於我們
    我們是看似業餘，實則超級專業的資研社，這裡歡迎不論是資訊新手或者超級厲害的你
    * **學習內容**：Python基礎、C++語法、AI應用、升學管道、學長姐經驗談。
    * **社團活動**：交流茶會、聯合迎新、聖誕交換禮物、社內程式競賽與成發。
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
        st.write("💡 點擊幹部介紹下方按鈕即可查看個人詳細資訊！")
        
        # 建立與成員數量相同的 columns
        cols = st.columns(len(members))
        
        for idx, member in enumerate(members):
            with cols[idx]:
                # A. 顯示頭像、職稱與名字在同一個 markdown 中
                st.markdown(
                    f"""
                    <div class="avatar-container">
                        <img src="{member["img"]}" class="custom-circle-avatar" />
                    </div>
                    <div class="role-badge-container">
                        <span class="role-badge">{member["role"]}</span>
                    </div>
                    <div class="member-name-text">{member["name"]}</div>
                    """, 
                    unsafe_allow_html=True
                )
                
                # B. 透明按鈕（在按鈕上加入標註 "個人頁面 →"，並利用 CSS 將其完美的定位與延伸）
                if st.button("個人頁面 →", key=f"btn_{member['id']}", use_container_width=True):
                    st.session_state.selected_member = member
                    st.rerun()

elif page == "聯絡我們":
    st.title("📬 聯絡社團幹部")
    st.write("有任何加入社團、合作 or 課程問題，請填寫下方表單，送出後幹部將會在 `zlcsc24@gmail.com` 信箱收到您的訊息：")
    
    # 已為 zlcsc24@gmail.com 啟用並綁定完畢的專用 Key
    WEB3FORMS_KEY = "fae75878-ba6b-47e2-8231-9a7442eb9bc3"

    # 使用原生 HTML/CSS 建立與 Streamlit 風格完美融合的表單
    # 這能確保 100% 傳送成功，不需要使用者額外開啟任何郵件軟體
    st.markdown(
        f"""
        <div style="background-color: #f8fafc; padding: 30px; border-radius: 16px; border: 1px solid #e2e8f0; max-width: 600px; margin: 0 auto;">
            <form action="https://api.web3forms.com/submit" method="POST">
                <!-- 隱藏的金鑰與設定（Web3Forms 專用） -->
                <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
                <input type="hidden" name="subject" value="【中崙資研官網新提問】有人在官網留言囉！">
                <input type="hidden" name="from_name" value="中崙資研官網表單">
                
                <!-- 如果成功送出，自動返回原來的 Streamlit 頁面（請替換為你的 Streamlit 部署網址，目前預設為感謝頁面） -->
                <input type="hidden" name="redirect" value="https://web3forms.com/success">

                <!-- 1. 稱呼欄位 -->
                <div style="margin-bottom: 20px;">
                    <label style="display: block; font-weight: bold; margin-bottom: 8px; color: #334155;">你的稱呼： <span style="color: red;">*</span></label>
                    <input type="text" name="name" required placeholder="例如：王小明" style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 15px;">
                </div>

                <!-- 2. Email 欄位（對手點擊回信時，系統會自動帶入此 Email） -->
                <div style="margin-bottom: 20px;">
                    <label style="display: block; font-weight: bold; margin-bottom: 8px; color: #334155;">聯絡 Email： <span style="color: red;">*</span></label>
                    <input type="email" name="email" required placeholder="例如：your-email@gmail.com" style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 15px;">
                </div>

                <!-- 3. 班級/學號欄位 -->
                <div style="margin-bottom: 20px;">
                    <label style="display: block; font-weight: bold; margin-bottom: 8px; color: #334155;">班級 / 學號（選填）：</label>
                    <input type="text" name="class_number" placeholder="例如：101 / 99999" style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 15px;">
                </div>

                <!-- 4. 提問內容 -->
                <div style="margin-bottom: 25px;">
                    <label style="display: block; font-weight: bold; margin-bottom: 8px; color: #334155;">你想問的問題或回饋： <span style="color: red;">*</span></label>
                    <textarea name="message" required rows="5" placeholder="請輸入您想詢問的詳細內容..." style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 15px; resize: vertical;"></textarea>
                </div>

                <!-- 5. 提交按鈕 -->
                <button type="submit" style="
                    width: 100%;
                    background-color: #007bff;
                    color: white;
                    padding: 12px;
                    border: none;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 16px;
                    cursor: pointer;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
                    transition: background-color 0.2s;
                ">
                    🚀 點我一次完成送出
                </button>
            </form>
        </div>
        """,
        unsafe_allow_html=True
    )
