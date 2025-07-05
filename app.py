import streamlit as st

st.set_page_config(page_title="درصد دودی شیشه", layout="centered")

st.title("🔍 بررسی درصد دودی شیشه ماشین")
st.write("درصد دودی شیشه رو وارد کن تا ببینی وضعیت قانونیش چطوره 👇")

percent = st.slider("درصد دودی شیشه", 0, 100, 30)

if percent < 20:
    st.success("✅ خیلی روشنه – مشکلی نداره")
elif percent < 50:
    st.info("✅ نرماله – احتمالاً قانونی")
elif percent < 70:
    st.warning("⚠️ نسبتاً دودی – ممکنه ایراد بگیرن")
else:
    st.error("❌ خیلی دودی – احتمال جریمه")
