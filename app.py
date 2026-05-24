import streamlit as st
from datetime import datetime

# পেজ কনফিগারেশন
st.set_page_config(page_title="সার্বজনীন লিচু আড়ত মেমো", page_icon="🍓", layout="centered")

st.title("🍓 লিচু বাজার সার্বজনীন মেমো জেনারেটর")
st.markdown("---")

# ইনপুট সেকশন (ওয়েবসাইট ফরম্যাট)
st.header("🏪 আড়ত ও চালানের তথ্য দিন")
arot_name = st.text_input("আপনার আড়ত বা প্রতিষ্ঠানের নাম লিখুন", placeholder="উদা: মেসার্স সততা আড়ত")

col1, col2 = st.columns(2)
with col1:
    farmer_name = st.text_input("👤 চাষী বা বিক্রেতার নাম")
    farmer_mobile = st.text_input("📱 চাষীর মোবাইল নম্বর")
with col2:
    leichi_quantity = st.number_input("🔢 মোট কত পিস লিচু?", min_value=0, step=1000, value=5000)
    rate_per_thousand = st.number_input("💰 প্রতি হাজার লিচুর দাম (টাকা)", min_value=0.0, value=2500.0)

# গাণিতিক হিসাব (১০% কমিশন, লেবার ছাড়া)
total_price = (leichi_quantity / 1000) * rate_per_thousand
commission_amount = total_price * 0.10
net_payable = total_price - commission_amount

date_str = datetime.now().strftime('%d/%m/%Y')
time_str = datetime.now().strftime('%I:%M %p')

# ডিজিটাল মেমো ডিজাইন (HTML + CSS)
html_content = f"""
<div style="border: 2px solid #27ae60; padding: 25px; font-family: 'Arial', sans-serif; border-radius: 12px; background-color: #ffffff; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-top: 20px;">
    <div style="text-align: center; border-bottom: 2px dashed #27ae60; padding-bottom: 10px; margin-bottom: 15px;">
        <h2 style="color: #27ae60; margin: 0; font-size: 24px;">{arot_name if arot_name else 'ডিজিটাল আড়ত'}</h2>
        <p style="margin: 5px 0; color: #7f8c8d; font-size: 14px;">বড় বাজার লিচু মহাল | ডিজিটাল রসিদ</p>
    </div>
    <div style="font-size: 14px; color: #2c3e50; line-height: 1.6; margin-bottom: 15px;">
        <b>তারিখ:</b> {date_str} | <b>সময়:</b> {time_str}<br>
        <b>চাষীর নাম:</b> {farmer_name if farmer_name else '---'}<br>
        <b>মোবাইল:</b> {farmer_mobile if farmer_mobile else '---'}
    </div>
    <table style="width: 100%; border-collapse: collapse; font-size: 14px; margin-bottom: 15px;">
        <thead>
            <tr style="background-color: #27ae60; color: white;">
                <th style="padding: 8px; text-align: left;">বিবরণ</th>
                <th style="padding: 8px; text-align: right;">টাকা (BDT)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #eee;">লিচু ({leichi_quantity:,} পিস)</td>
                <td style="padding: 8px; border-bottom: 1px solid #eee; text-align: right;">{total_price:,.2f}</td>
            </tr>
            <tr>
                <td style="padding: 8px; border-bottom: 1px solid #eee; color: #c0392b;">আড়ত খরচ (১০%)</td>
                <td style="padding: 8px; border-bottom: 1px solid #eee; text-align: right; color: #c0392b;">-{commission_amount:,.2f}</td>
            </tr>
            <tr style="font-weight: bold; background-color: #f9f9f9; border-top: 2px solid #27ae60;">
                <td style="padding: 8px;">কৃষক পাবেন (Net)</td>
                <td style="padding: 8px; text-align: right; color: #27ae60; font-size: 16px;">{net_payable:,.2f}</td>
            </tr>
        </tbody>
    </table>
    <div style="text-align: center; font-size: 12px; color: #95a5a6; border-top: 1px solid #eee; padding-top: 10px; margin-bottom: 15px;">
        নিখুঁত ডিজিটাল হিসাবের জন্য ধন্যবাদ।<br>
        <small>Powered by Atikur's Math Lab</small>
    </div>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# প্রিন্ট বা পিডিএফ ডাউনলোডের বাটন
if st.button("🖨️ মেমো প্রিন্ট / PDF ডাউনলোড করুন", use_container_width=True):
    st.components.v1.html("<script>window.print();</script>", height=0)
