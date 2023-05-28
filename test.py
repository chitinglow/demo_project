import streamlit as st
import random

def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return result

code = '''
def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return result
'''


st.set_page_config(page_title="The Law of Large Number",
                   page_icon="game_die",
                   layout="centered")

url = "https://easylang.dev/apps/tutorial_mcarlo.html"
st.title("The Law of Large Numbers")
st.write("This web app is replication of from [this link](%s) to practice the Monte Carlo Methods and Python skills" % url)

st.header("Coin flip")
codeCol, resultCol = st.columns([2,1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run", key="btn1"):
        result = coin_flip()
        bg_color = "#ccffcc"
        st.markdown(
            f"""
            <style>
            .result {{
                background-color: {bg_color};
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="result">{result}</div>',
            unsafe_allow_html=True
        )


def count_flips(n):
    heads = 0
    tails = 0

    for _ in range(n):
        flip = random.randint(0, 1)
        if flip == 1:
            heads += 1
        else:
            tails += 1

    heads_percentage = 100.0 * heads / n
    tails_percentage = 100.0 * tails / n

    return heads, tails, heads_percentage, tails_percentage

code2 = """
        def count_flips(n):
            heads = 0
            tails = 0

            for _ in range(n):
                flip = random.randint(0, 1)
                if flip == 1:
                    heads += 1
                else:
                    tails += 1

            heads_percentage = 100.0 * heads / n
            tails_percentage = 100.0 * tails / n

            return heads, tails, heads_percentage, tails_percentage

        n = 1000
        heads_count, tails_count, heads_percentage, tails_percentage = count_flips(n)
"""
codeCol2, resultCol2 = st.columns([2,1])
with codeCol2:
    st.code(code2, language='Python')


with resultCol2:
    if st.button("Run",key="btn2"):
        n = 1000
        heads_count, tails_count, heads_percentage, tails_percentage = count_flips(n)
        bg_color = "#ccffcc"
        st.markdown(
            f"""
            <style>
            .result {{
                background-color: {bg_color};
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="result">Heads count: {heads_count}</div>'
            f'<div class="result">Tails count: {tails_count}</div>'
            f'<div class="result">Heads percentage: {heads_percentage} %</div>'
            f'<div class="result">Tails percentage: {tails_percentage} %</div>',
            unsafe_allow_html=True
        )