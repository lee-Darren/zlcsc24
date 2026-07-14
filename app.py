import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")

# CSS 樣式（包含全域樣式與滾動條美化）
st.markdown("""
<style>
/* 隱藏預設 Streamlit 按鈕的某些邊框，讓自訂介面更乾淨 */
.stButton>button {
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

# 2. 建立側邊欄導覽選單
st.sidebar.title("🧭 網站導覽")
page = st.sidebar.radio("請選擇頁面：", ["首頁介紹", "成員介紹", "聯絡我們"])

# 成員資料
members = [
    {"id": "0", "role": "社長", "name": "陳平安", "img": "https://i.pravatar.cc/220?u=chenpingan", "email": "chenpingan@email.com", "specialty": "程式架構、系統設計", "intro": "熱愛開源專案，擅長 Python 和 Web 開發。"},
    {"id": "1", "role": "副社", "name": "李尚瑾", "img": "https://i.pravatar.cc/220?u=leeshangjin", "email": "leeshangjin@email.com", "specialty": "AI 應用、數據分析", "intro": "對機器學習充滿熱情，喜歡用程式解決實際問題。"},
    {"id": "2", "role": "公關", "name": "魏敘百", "img": "https://i.pravatar.cc/220?u=weisubai", "email": "weisubai@email.com", "specialty": "溝通協調、活動策劃", "intro": "負責社團對外關係，是社團的橋樑。"},
    {"id": "3", "role": "活動", "name": "張承緒", "img": "https://i.pravatar.cc/220?u=zhangchengxu", "email": "zhangchengxu@email.com", "specialty": "活動企劃、時間管理", "intro": "確保每場活動順暢進行，細心負責。"},
    {"id": "4", "role": "活動", "name": "曾開元", "img": "https://i.pravatar.cc/220?u=zengkaiyuan", "email": "zengkaiyuan@email.com", "specialty": "活動執行、現場管理", "intro": "活動現場的靈魂人物，確保一切完美。"},
    {"id": "5", "role": "美宣", "name": "倪宇廷", "img": "https://i.pravatar.cc/220?u=niyuting", "email": "niyuting@email.com", "specialty": "平面設計、視覺創意", "intro": "用創意設計傳遞社團的品牌形象。"},
    {"id": "6", "role": "設備", "name": "陳庭弘", "img": "https://i.pravatar.cc/220?u=chentinghong", "email": "chentinghong@email.com", "specialty": "硬體維護、技術支援", "intro": "負責社團設備和技術基礎設施。"},
    {"id": "7", "role": "文書", "name": "黃于恩", "img": "https://i.pravatar.cc/220?u=huangyuen", "email": "huangyuen@email.com", "specialty": "文檔整理、紀錄管理", "intro": "記錄社團發展歷程，保管重要文檔。"},
    {"id": "8", "role": "教學", "name": "蘇奕全", "img": "https://i.pravatar.cc/220?u=suyichuan", "email": "suyichuan@email.com", "specialty": "Python 基礎、演算法", "intro": "擅長用簡單方式講解複雜概念。"},
    {"id": "9", "role": "教學", "name": "陳平安二", "img": "https://i.pravatar.cc/220?u=chenpingan2", "email": "chenpingan2@email.com", "specialty": "網路爬蟲、資料處理", "intro": "帶領大家進入數據的世界。"},
    {"id": "10", "role": "教學", "name": "李尚瑾二", "img": "https://i.pravatar.cc/220?u=leeshangjin2", "email": "leeshangjin2@email.com", "specialty": "AI 應用、專案實戰", "intro": "用實際案例展示 AI 的力量。"},
    {"id": "11", "role": "總務", "name": "曾開元二", "img": "https://i.pravatar.cc/220?u=zengkaiyuan2", "email": "zengkaiyuan2@email.com", "specialty": "財務管理、資源規劃", "intro": "確保社團資源合理分配 and 運用。"},
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

    # 讀取網址 Query Parameter 來判斷是否有點擊特定成員
    query_params = st.query_params
    selected_member_id = query_params.get("member_id", None)

    # 如果有選中特定成員
    if selected_member_id is not None:
        # 找出對應的成員資料
        member = next((m for m in members if m["id"] == selected_member_id), None)
        
        if member:
            # 返回按鈕（清空 query parameter）
            if st.button("← 返回成員列表"):
                st.query_params.clear()
                st.rerun()
            
            st.markdown("---")
            
            # 個人詳細資訊頁面
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(member['img'], width=220)
            
            with col2:
                st.markdown(f"## {member['name']}")
                st.markdown(f"### {member['role']}")
                st.markdown("---")
                st.markdown(f"**📧 Email：** {member['email']}")
                st.markdown(f"**🎯 專長：** {member['specialty']}")
                st.markdown(f"**📝 簡介：** {member['intro']}")
        else:
            st.warning("找不到該成員資訊。")
            st.query_params.clear()
            
    else:
        # 顯示成員列表
        st.write("💡 左右滑動瀏覽幹部，**點擊頭像**可查看詳細個人資訊！")
        
        # 建立 HTML 的橫向滾動元件
        card_html_templates = []
        for member in members:
            # 建立點擊頭像會重新導向並帶上 query_param 的連結
            # target="_parent" 確保能在 Streamlit 主視窗中跳轉，而不是在 iframe 內
            detail_link = f"?member_id={member['id']}"
            
            card_html = f"""
            <div class="member-card">
                <a href="{detail_link}" target="_parent" style="text-decoration: none; color: inherit;">
                    <div class="img-container">
                        <img src="{member['img']}" alt="{member['name']}">
                        <div class="hover-overlay">點擊查看</div>
                    </div>
                    <h4>{member['name']}</h4>
                    <p class="role">{member['role']}</p>
                </a>
            </div>
            """
            card_html_templates.append(card_html)
            
        all_cards_html = "\n".join(card_html_templates)

        # 完整的 HTML + CSS 元件
        scroll_component_html = f"""
        <style>
        .member-scroll {{
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding: 20px 10px;
            scroll-behavior: smooth;
            -webkit-overflow-scrolling: touch;
        }}
        .member-card {{
            min-width: 200px;
            max-width: 200px;
            background: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            padding: 20px;
            text-align: center;
            flex-shrink: 0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .member-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
        }}
        .img-container {{
            position: relative;
            width: 120px;
            height: 120px;
            margin: 0 auto 12px;
            border-radius: 50%;
            overflow: hidden;
            cursor: pointer;
        }}
        .img-container img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: scale 0.3s ease;
        }}
        .hover-overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: bold;
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        .img-container:hover .hover-overlay {{
            opacity: 1;
        }}
        .img-container:hover img {{
            scale: 1.1;
        }}
        .member-card h4 {{
            margin: 10px 0 5px;
            font-size: 18px;
            font-family: sans-serif;
            color: #333;
        }}
        .member-card p.role {{
            margin: 0;
            font-size: 14px;
            color: #007bff;
            font-weight: bold;
            background: #eef5ff;
            padding: 4px 12px;
            border-radius: 20px;
            display: inline-block;
        }}
        /* 滾動條美化 */
        .member-scroll::-webkit-scrollbar {{
            height: 8px;
        }}
        .member-scroll::-webkit-scrollbar-track {{
            background: #f1f1f1;
            border-radius: 10px;
        }}
        .member-scroll::-webkit-scrollbar-thumb {{
            background: #c1c1c1;
            border-radius: 10px;
        }}
        .member-scroll::-webkit-scrollbar-thumb:hover {{
            background: #a8a8a8;
        }}
        </style>

        <div class="member-scroll">
            {all_cards_html}
        </div>
        """
        
        # 渲染滾動元件（高度設為 350px 確保卡片與陰影完整顯示）
        components.html(scroll_component_html, height=350, scrolling=False)

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
