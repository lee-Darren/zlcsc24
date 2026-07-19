import streamlit as st

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")

# 2. 注入 CSS 樣式
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

/* 2. 定義每一張卡片的寬度與外觀 */
div[data-testid="stHorizontalBlock"] > div {
    min-width: 210px !important;
    max-width: 210px !important;
    flex-shrink: 0 !important;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px 15px 20px 15px !important; 
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important; 
    justify-content: flex-start !important;
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
}

/* 5. 圓形頭像樣式 */
.custom-circle-avatar {
    width: 110px !important;
    height: 110px !important;
    border-radius: 50% !important;
    object-fit: cover !important;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    display: block !important;
}

/* 6. 職稱標籤樣式 */
.role-badge-container {
    width: 100%;
    text-align: center;
    margin-top: 5px;
    margin-bottom: 5px;
}
.role-badge {
    background-color: #eef5ff;
    color: #007bff;
    font-size: 13px;
    font-weight: bold;
    padding: 4px 12px;
    border-radius: 20px;
    display: inline-block;
}

/* 7. 名字樣式 */
.member-name-text {
    font-size: 16px;
    font-weight: bold;
    color: #334155;
    margin-top: 10px;
    text-align: center;
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

/* 9. LINE 社群專屬按鈕美化 (全新升級突破版) */
.line-btn-js {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background-color: #06C755;
    color: white !important;
    font-weight: bold;
    font-size: 16px;
    padding: 12px 24px;
    border-radius: 30px;
    border: none;
    box-shadow: 0 4px 12px rgba(6, 199, 85, 0.3);
    cursor: pointer;
    transition: all 0.2s;
    margin: 10px 0;
    text-decoration: none;
}
.line-btn-js:hover {
    background-color: #05B34C;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(6, 199, 85, 0.4);
}
</style>
""", unsafe_allow_html=True)

# 3. 建立側邊欄導覽選單
st.sidebar.title("🧭 網站導覽")
page = st.sidebar.radio("請選擇頁面：", ["首頁介紹", "成員介紹", "聯絡我們"])

# LINE 社群網址變數
LINE_COMMUNITY_URL = "https://line.me/ti/g2/UqZ3ywFePcVOcm7rqVRzBfLMXFSFaEMhRLS_rA?utm_source=invitation&utm_medium=link_copy&utm_campaign=default"

# 幹部資料
members = [
    {"id": "0", "role": "社長 兼 教學", "name": "陳平安", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=chenpingan", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "1", "role": "副社 兼 教學", "name": "李尚瑾", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=leeshangjin", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "2", "role": "公關", "name": "魏敘百", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=weisubai", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "3", "role": "活動", "name": "張承緒", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=zhangchengxu", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "4", "role": "活動 兼 總務", "name": "曾開元", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=zengkaiyuan", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "5", "role": "美宣", "name": "倪宇廷", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=niyuting", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "6", "role": "設備", "name": "陳庭弘", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=chentinghong", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "7", "role": "文書", "name": "黃于恩", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=huangyuen", "email": "************@email.com", "specialty": "**********", "intro": "*****************"},
    {"id": "8", "role": "教學", "name": "蘇奕全", "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=suyichuan", "email": "************@email.com", "specialty": "**********", "intro": "*****************"}
]

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
    
    # ─── 突破限制：首頁 LINE 按鈕 ───
    st.markdown("---")
    st.markdown("### 💬 有問題想直接問學長姐？")
    
    # 核心黑科技：利用 window.open(..., '_blank') 或是 window.top.location 繞過 iframe 限制
    # 這裡使用 window.open 配合頂層調用，可以完美在手機瀏覽器開新分頁跳轉至 LINE 社群，同時維持超美綠色按鈕外觀！
    js_button_1 = f'''
    <button class="line-community-btn" onclick="window.open('{LINE_COMMUNITY_URL}', '_blank')">
        🟢 點我加入【中崙資研新生提問群】
    </button>
    '''
    st.markdown(js_button_1, unsafe_allow_html=True)
    st.write("點擊上方按鈕將自動為您開啟 LINE 社群，課程、社團疑惑一秒替你解答！")

elif page == "成員介紹":
    st.title("🧑‍🤝‍🧑 成員介紹")

    if "selected_member" not in st.session_state:
        st.session_state.selected_member = None

    if st.session_state.selected_member is not None:
        member = st.session_state.selected_member
        
        if st.button("← 返回成員列表"):
            st.session_state.selected_member = None
            st.rerun()
        
        st.markdown("---")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(member['img'], width=200)
        
        with col2:
            st.markdown("## " + member['name'])
            st.markdown('<span class="role-badge" style="font-size: 15px;">' + member["role"] + '</span>', unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("**📧 Email：** " + member['email'])
            st.markdown("**🎯 專長：** " + member['specialty'])
            st.markdown("**📝 簡介：** " + member['intro'])
            
    else:
        st.write("💡 點擊幹部介紹下方按鈕即可查看個人詳細資訊！")
        
        cols = st.columns(len(members))
        
        for idx, member in enumerate(members):
            with cols[idx]:
                html_code = (
                    '<div class="avatar-container">'
                    '    <img src="' + member["img"] + '" class="custom-circle-avatar" />'
                    '</div>'
                    '<div class="role-badge-container">'
                    '    <span class="role-badge">' + member["role"] + '</span>'
                    '</div>'
                    '<div class="member-name-text">' + member["name"] + '</div>'
                )
                st.markdown(html_code, unsafe_allow_html=True)
                
                st.write("")
                if st.button("個人頁面 →", key="btn_" + str(member['id']), use_container_width=True):
                    st.session_state.selected_member = member
                    st.rerun()

elif page == "聯絡我們":
    import requests

    st.title("📬 聯絡社團幹部")
    
    st.info("💡 溫馨提示：如果想要獲得最即時、最快速的回答，建議直接點擊下方按鈕加入我們的 LINE 新生群發問喔！")
    
    # ─── 突破限制：聯絡我們頁面 LINE 按鈕 ───
    js_button_2 = f'''
    <button class="line-community-btn" onclick="window.open('{LINE_COMMUNITY_URL}', '_blank')">
        🟢 點我秒入【新生 LINE 提問群】
    </button>
    '''
    st.markdown(js_button_2, unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("若您不方便使用 LINE，也可以填寫以下電子提問單，我們會以 Email 回覆您：")
    
    FORM_ID = "1FAIpQLScvl7BmxZ4CyLnzJSofEyvlF1KP6Vxdg35hp7UGmM8bBUSXHQ"
    
    ENTRY_NAME = "entry.91137281"     
    ENTRY_EMAIL = "entry.72815929"    
    ENTRY_CLASS = "entry.1337932870"  
    ENTRY_MSG = "entry.2008744679"    

    with st.form("my_form"):
        name = st.text_input("你的稱呼：")
        email = st.text_input("聯絡 Email：")
        class_num = st.text_input("班級 / 學號（選填）：")
        msg = st.text_area("你想問的問題或回饋：")
        
        submit_button = st.form_submit_button(label="🚀 送出表單")
        
        if submit_button:
            if not name.strip():
                st.warning("請填寫您的稱呼唷！")
            elif not email.strip() or "@" not in email:
                st.warning("請輸入正確的聯絡 Email！")
            elif not msg.strip():
                st.warning("請輸入您想問的問題或回饋！")
            else:
                with st.spinner("正在為您傳送訊息給學長姐..."):
                    post_url = "https://docs.google.com/forms/d/e/" + FORM_ID + "/formResponse"
                    
                    payload = {
                        ENTRY_NAME: name,
                        ENTRY_EMAIL: email,
                        ENTRY_CLASS: class_num,
                        ENTRY_MSG: msg
                    }
                    
                    try:
                        response = requests.post(post_url, data=payload, timeout=10)
                        
                        if response.status_code == 200:
                            st.success("🎉 傳送成功！謝謝 " + name + " 的留言，學長姐會盡快回覆到您的信箱：" + email + "！")
                        else:
                            st.error("😭 傳送失敗，請稍後再試，或直接聯絡幹部！")
                    except Exception as e:
                        st.error("⚠️ 連線超時，請檢查您的網路狀態！")
