import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Tracker App", layout="centered")

st.title("💸 Expense Tracker App")
st.write("Add expenses one by one. Click Finish to see summary 📊")

# Session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

if "finished" not in st.session_state:
    st.session_state.finished = False

# INPUT SECTION
if not st.session_state.finished:

    with st.form("expense_form", clear_on_submit=True):
        expense_name = st.text_input("📝 Expense Name")
        amount = st.number_input("💰 Amount", min_value=0.0, step=10.0)
        category = st.selectbox(
            "📂 Category",
            ["Food", "Travel", "Rent", "Shopping", "Others"]
        )

        add_more = st.form_submit_button("➕ Add More")

        if add_more:
            if expense_name and amount > 0:
                st.session_state.expenses.append({
                    "Expense": expense_name,
                    "Amount": amount,
                    "Category": category
                })
                st.success("Expense added! Add another one 👇")
            else:
                st.warning("Please enter valid expense details")

    if st.button("✅ Finish"):
        if st.session_state.expenses:
            st.session_state.finished = True
        else:
            st.warning("Please add at least one expense")

# RESULT SECTION
if st.session_state.finished:
    df = pd.DataFrame(st.session_state.expenses)

    st.subheader("📋 Expense List")
    st.dataframe(df, use_container_width=True)

    total = df["Amount"].sum()
    st.metric("💰 Total Expense", f"₹ {total:.2f}")

    st.subheader("📊 Expense Distribution")

    category_sum = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(
        category_sum,
        labels=category_sum.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")

    st.pyplot(fig)
