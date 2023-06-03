import streamlit as st
import random


def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return result

def check_win_or_lose():
    numb = random.randint(1, 37)
    if numb >= 19:
        return "You win $10"
    else:
        return "You lose $10"

def calculate_cash():
    cash = 0
    for i in range(1, 1001):
        cash -= 10
        numb = random.randint(1, 37)
        if numb >= 19:
            cash += 20
    return f"Cash after playing: ${cash}"

def run_section(title, code, button_text, n=None, button_key=None):
    codeCol, resultCol = st.columns([2, 1])

    with codeCol:
        st.code(code, language='Python')

    with resultCol:
        if st.button(button_text, button_key):
            if n is not None:
                result = count_flips(n)
                st.markdown(
                    f"""
                    <style>
                    .result {{
                        background-color: #ccffcc;
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="result">{result}</div>',
                    unsafe_allow_html=True
                )
            else:
                result = coin_flip()
                st.markdown(
                    f"""
                    <style>
                    .result {{
                        background-color: #ccffcc;
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="result">{result}</div>',
                    unsafe_allow_html=True
                )

def run_roulette(title, code, button_text, n=None, button_key=None):
    codeCol, resultCol = st.columns([2, 1])

    with codeCol:
        st.code(code, language='Python')

    with resultCol:
        if st.button(button_text, button_key):
            if n is not None:
                result = count_flips(n)
                st.markdown(
                    f"""
                    <style>
                    .result {{
                        background-color: #ccffcc;
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    f'<div class="result">{result}</div>',
                    unsafe_allow_html=True
                )
            else:
                result = check_win_or_lose()
                st.markdown(
                    f"""
                    <style>
                    .result {{
                        background-color: #ccffcc;
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


st.set_page_config(
    page_title="The Law of Large Number",
    page_icon="game_die",
    layout="centered"
)

url = "https://easylang.dev/apps/tutorial_mcarlo.html"
st.title("The Law of Large Numbers")
st.write(
    "This web app is a replication from [this link](%s) to practice the Monte Carlo Methods and Python skills" % url)

st.header("Coin flip")
code = '''
def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return result
'''
run_section("Coin flip", code, "Run", button_key="btn1")

st.header("Count flips")
code = """
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
"""
n = st.number_input("Enter the value of n", value=1000, min_value=1, step=1)

code_col, input_col = st.columns([2, 1])

with code_col:
    st.code(code, language='Python')

with input_col:
    if st.button("Run", key="btn2"):
        heads, tails, heads_percentage, tails_percentage = count_flips(n)
        st.markdown(
            f'''
            <style>
            .result {{
                background-color: #ccffcc;
            }}
            </style>
            ''',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="result">Heads count: {heads}</div>'
            f'<div class="result">Tails count: {tails}</div>'
            f'<div class="result">Heads percentage: {heads_percentage:.2f}%</div>'
            f'<div class="result">Tails percentage: {tails_percentage:.2f}%</div>',
            unsafe_allow_html=True
        )

code = """
def check_win_or_lose():
    numb = random.randint(1, 37)
    if numb >= 19:
        return "You win $10"
    else:
        return "You lose $10"
"""

st.header("Roulette")

run_roulette("Roulette", code, "Run", button_key="btn3")


code1 = """
def calculate_cash():
    cash = 0
    for i in range(1, 1001):
        cash -= 10
        numb = random.randint(1, 37)
        if numb >= 19:
            cash += 20
    return f"Cash after playing: ${cash}"
"""

code_col1, input_col1 = st.columns([2, 1])

with code_col:
    st.code(code1, language='Python')

with input_col:
    if st.button("Run", key="btn4"):
        result1 = calculate_cash()
        st.markdown(
            f'''
            <style>
            .result {{
                background-color: #ccffcc;
            }}
            </style>
            ''',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="result">{result1}</div>',
            unsafe_allow_html=True
        )