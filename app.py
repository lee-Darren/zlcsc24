import base64
import os
import requests
import streamlit as st

# 1. 網頁頂端標題與圖示設定
st.set_page_config(page_title="資訊研究社社團官網", page_icon="💻", layout="wide")


# 💡 輔助函式：將圖片（無論是本地檔案還是網路網址）轉換為 Base64，確保 HTML img 標籤能正確顯示
def get_image_base64(img_path):
  if img_path.startswith("http://") or img_path.startswith("https://"):
    return img_path  # 網路網址直接返回
  if os.path.exists(img_path):
    with open(img_path, "rb") as img_file:
      encoded = base64.b64encode(img_file.read()).decode()
      # 根據副檔名判斷 mime type
      ext = img_path.split(".")[-1].lower()
      mime = "image/png" if ext == "png" else "image/jpeg"
      return f"data:{mime};base64,{encoded}"
  return img_path  # 若檔案不存在則返回原路徑


# 2. 注入 CSS 樣式
st.markdown(
    """
<style>
/* 1. 幹部卡片區域：改為 wrap 允許自動換行，並設為居中對齊 */
div[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: center !important;
    padding: 15px 5px !important;
    gap: 20px !important;
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

/* 3. 滑鼠懸停卡片時的效果 */
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

/* 8. LINE 按鈕樣式 */
.line-anchor-btn {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    background-color: #06C755 !important;
    color: white !important;
    font-weight: bold !important;
    font-size: 16px !important;
    padding: 14px 28px !important;
    border-radius: 30px !important;
    box-shadow: 0 4px 12px rgba(6, 199, 85, 0.3) !important;
    text-decoration: none !important;
    transition: all 0.2s !important;
    margin: 12px 0 !important;
}
.line-anchor-btn:hover {
    background-color: #05B34C !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 16px rgba(6, 199, 85, 0.4) !important;
    color: white !important;
}

/* 9. 自動換行 */
div[data-testid="stMarkdownContainer"] {
    word-break: break-word !important;
    overflow-wrap: break-word !important;
    white-space: pre-line !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# 3. 建立側邊欄導覽選單
st.sidebar.title("🧭 網站導覽")
page = st.sidebar.radio("請選擇頁面：", ["首頁介紹", "成員介紹", "聯絡我們"])

# LINE 社群網址變數
LINE_COMMUNITY_URL = "https://line.me/ti/g2/UqZ3ywFePcVOcm7rqVRzBfLMXFSFaEMhRLS_rA?utm_source=invitation&utm_medium=link_copy&utm_campaign=default"

# 幹部資料
members = [
    {
        "id": "0",
        "role": "社長 兼 教學",
        "name": "陳平安",
        "img": (
            "https://api.dicebear.com/7.x/adventurer/svg?seed=chenpingan"
        ),
        "email": "************@email.com",
        "specialty": "python",
        "intro": (
            "平安的「平」，平安的「安」\nc++自學ing\n會教html\n鐵道迷\n(never"
            " gonna give you up 🎶 )"
        ),
        "ig": "zlcsc24_fean",
    },
    {
        "id": "1",
        "role": "副社 兼 教學",
        "name": "李尚瑾",
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=leeshangjin",
        "email": "s11430264@zlsh.tp.edu.tw",
        "specialty": "**********",
        "intro": "*****************",
        "ig": "",
    },
    {
        "id": "2",
        "role": "公關",
        "name": "魏敘百",
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=weisubai",
        "email": "************@email.com",
        "specialty": "**********",
        "intro": "*****************",
        "ig": "",
    },
    {
        "id": "3",
        "role": "活動",
        "name": "張承緒",
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=zhangchengxu",
        "email": "************@email.com",
        "specialty": "**********",
        "intro": "*****************",
        "ig": "",
    },
    {
        "id": "4",
        "role": "活動 兼 總務",
        "name": "曾開元",
        "img": "螢幕擷取畫面 2026-08-07 202010 - 20830曾開元.png",
        "email": "s11430172@zlsh.tp.edu.tw",
        "specialty": "大提琴、鋼琴",
        "intro": "教數學英文 興趣是音樂 不會寫程式",
        "ig": "zlcsc24._.kaiyuan0401",
    },
    {
        "id": "5",
        "role": "美宣",
        "name": "倪宇廷",
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=niyuting",
        "email": "************@email.com",
        "specialty": "**********",
        "intro": "*****************",
        "ig": "",
    },
    {
        "id": "6",
        "role": "設備",
        "name": "陳庭弘",
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=chentinghong",
        "email": "lemon69365625@gmail.com",
        "specialty": "太多了",
        "intro": "我很懶 （真的 \n有馬加奈♥️  Wonhee♥️\nIAN🫪 Moka🫪",
        "ig": "zlcsc24_starrynight",
    },
    {
        "id": "7",
        "role": "文書",
        "name": "黃于恩",
        "img": "IMG_3495 - 20832黃于恩.jpeg",
        "email": "s11430275@zlsh.tp.edu.tw",
        "specialty": "我會彈鋼琴、我愛打羽毛球、玩Pokémon go",
        "intro": (
            "哈嘍～我是文書20832黃于恩，平常最喜歡玩Pokémon"
            " go，有問題都歡迎問我ㄛ～（副社長也太帥～這句不用加）"
        ),
        "ig": "zlcsc24_penguin",
    },
    {
        "id": "8",
        "role": "教學",
        "name": "蘇奕全",
        "img": "https://api.dicebear.com/7.x/adventurer/svg?seed=suyichuan",
        "email": "andysuyichuan@gmail.com",
        "specialty": "c++, arduino在學",
        "intro": (
            "嗨我是教學長蘇奕全,不要看我是教學長實際上費柴一個,我也會打一些槍戰只不過都很菜\n)歡迎學弟妹加資研喔."
        ),
        "ig": "zlscsc_chuan",
    },
]

if page == "首頁介紹":
  st.title("歡迎來到中崙資研")
  st.subheader("這裡是最適合你的資訊研究社")

  st.image(
      "https://raw.githubusercontent.com/lee-Darren/zlcsc24/main/1784017363261.jpg",
      width=700,
  )

  st.markdown("""
    ### 🌟 關於我們
    我們是看似業餘，實則超級專業的資研社，這裡歡迎不論是資訊新手或者超級厲害的你
    * **學習內容**：Python基礎、C++語法、AI應用、升學管道、學長姐經驗談。
    * **社團活動**：交流茶會、聯合迎新、聖誕交換禮物、社內程式競賽與成發。
    """)

  st.markdown("---")
  st.markdown("### 💬 有問題想直接問學長姐？")

  html_link_1 = f"""
    <a class="line-anchor-btn" href="{LINE_COMMUNITY_URL}" target="_blank">
        🟢 點我加入【中崙資研新生提問群】
    </a>
    """
  st.markdown(html_link_1, unsafe_allow_html=True)
  st.caption(
      "💡 **手機版操作提示：** 若直接點選按鈕無反應，請**長按按鈕**並選擇"
      " **「在新分頁開啟」** 或 **「在瀏覽器開啟」** 即可順利加入群組喔！"
  )

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
      st.image(member["img"], width=200)

    with col2:
      st.markdown("## " + member["name"])
      st.markdown(
          '<span class="role-badge" style="font-size: 15px;">'
          + member["role"]
          + "</span>",
          unsafe_allow_html=True,
      )
      st.markdown("---")
      st.markdown("**📧 Email：** " + member["email"])
      st.markdown("**＠ IG：** " + member["ig"])
      st.markdown("**🎯 專長：** " + member["specialty"])
      st.markdown("**📝 簡介：**\n" + member["intro"])

  else:
    st.write("💡 點擊幹部介紹下方按鈕即可查看個人詳細資訊！")

    cols = st.columns(len(members))

    for idx, member in enumerate(members):
      with cols[idx]:
        # 💡 這邊呼叫 get_image_base64() 將檔名轉為 HTML 可讀取的編碼
        img_src = get_image_base64(member["img"])

        html_code = (
            '<div class="avatar-container">'
            f'    <img src="{img_src}" class="custom-circle-avatar" />'
            "</div>"
            '<div class="role-badge-container">'
            '    <span class="role-badge">' + member["role"] + "</span>"
            "</div>"
            '<div class="member-name-text">' + member["name"] + "</div>"
        )
        st.markdown(html_code, unsafe_allow_html=True)

        st.write("")
        if st.button(
            "個人頁面 →", key="btn_" + str(member["id"]), use_container_width=True
        ):
          st.session_state.selected_member = member
          st.rerun()

elif page == "聯絡我們":
  st.title("📬 聯絡社團幹部")

  st.info(
      "💡 溫馨提示：如果想要獲得最即時、最快速的回答，建議直接加入我們的 LINE"
      " 新生群發問喔！"
  )

  html_link_2 = f"""
    <a class="line-anchor-btn" href="{LINE_COMMUNITY_URL}" target="_blank">
        🟢 點我秒入【新生 LINE 提問群】
    </a>
    """
  st.markdown(html_link_2, unsafe_allow_html=True)
  st.caption(
      "💡 **手機版操作提示：** 若直接點選按鈕無反應，請**長按按鈕**並選擇"
      " **「在新分頁開啟」** 即可！"
  )
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
          post_url = (
              "https://docs.google.com/forms/d/e/" + FORM_ID + "/formResponse"
          )

          payload = {
              ENTRY_NAME: name,
              ENTRY_EMAIL: email,
              ENTRY_CLASS: class_num,
              ENTRY_MSG: msg,
          }

          try:
            response = requests.post(post_url, data=payload, timeout=10)

            if response.status_code == 200:
              st.success(
                  "🎉 傳送成功！謝謝 "
                  + name
                  + " 的留言，學長姐會盡快回覆到您的信箱："
                  + email
                  + "！"
              )
            else:
              st.error("😭 傳送失敗，請稍後再試，或直接聯絡幹部！")
          except Exception as e:
            st.error("⚠️ 連線超時，請檢查您的網路狀態！")
