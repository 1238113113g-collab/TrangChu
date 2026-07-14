import streamlit as st

# =========================================================================
# 1. CẤU HÌNH TRANG WEB
# =========================================================================
st.set_page_config(
    page_title="Hệ sinh thái Trợ lý AI - Tư vấn Chuyên nghiệp", 
    page_icon="💼", 
    layout="centered"
)

# Thêm một chút CSS để giao diện trông đẹp mắt và chuyên nghiệp hơn
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 18px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 30px;
    }
    .app-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E5E7EB;
        background-color: #F9FAFB;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# 2. KHU VỰC TIÊU ĐỀ CHÍNH
# =========================================================================
st.markdown('<div class="main-title">💼 HỆ THỐNG TRỢ LÝ AI CHUYÊN BIỆT</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Giải pháp tự động hóa báo cáo, phân tích tài chính và hỗ trợ pháp lý doanh nghiệp</div>', unsafe_allow_html=True)

st.markdown("---")

# =========================================================================
# 3. DANH MỤC CÁC WEB PHỤ (CÁC CÔNG CỤ CHUYÊN BIỆT)
# =========================================================================
st.subheader("🚀 Chọn công cụ trợ lý bạn cần sử dụng:")

# --- Công cụ 1: Phân tích Đầu tư ---
with st.container():
    st.markdown("""
    <div class="app-card">
        <h3>📊 Trợ lý Lập Báo cáo Đầu tư</h3>
        <p>Hỗ trợ đọc file tài liệu dự án, PDF, trích xuất số liệu doanh thu, lợi nhuận và tự động soạn thảo báo cáo phân tích đầu tư.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bạn hãy thay đường dẫn web phụ thực tế của bạn vào đây
    st.link_button(
        "Truy cập Trợ lý Đầu tư →", 
        "https://truongthanhgiang.streamlit.app/", 
        use_container_width=True
    )

st.write("") # Tạo khoảng cách

# --- Công cụ 2: Phân tích & Kiểm tra Ngân hàng ---
with st.container():
    st.markdown("""
    <div class="app-card">
        <h3>🏦 Trợ lý Phân tích Báo cáo Ngân hàng</h3>
        <p>Tự động hóa việc phân tích sao kê, đối chiếu số liệu tài khoản và kiểm tra tính tuân thủ pháp lý của các giao dịch ngân hàng.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Link này sau này khi bạn tạo web phụ thứ 2 thì dán vào đây
    st.link_button(
        "Truy cập Trợ lý Ngân hàng →", 
        "https://share.streamlit.io/", # Link tạm thời
        use_container_width=True
    )

st.markdown("---")

# =========================================================================
# 4. KHU VỰC LIÊN HỆ & HỖ TRỢ
# =========================================================================
st.subheader("📞 Đăng ký nhận tư vấn chuyên sâu")
st.write("Nếu bạn cần hỗ trợ về các nghiệp vụ Tài chính - Pháp lý - Thuế, vui lòng để lại thông tin:")

with st.form("contact_form"):
    name = st.text_input("Họ và tên của bạn:")
    email = st.text_input("Địa chỉ Email:")
    phone = st.text_input("Số điện thoại:")
    message = st.text_area("Yêu cầu cụ thể:")
    
    submit_button = st.form_submit_button("Gửi thông tin liên hệ")
    
    if submit_button:
        if name and (email or phone):
            st.success(f"Cảm ơn {name}! Chúng tôi đã nhận được thông tin và sẽ phản hồi sớm nhất.")
        else:
            st.error("Vui lòng điền đầy đủ Họ tên và cách thức liên lạc (Email/SĐT).")
