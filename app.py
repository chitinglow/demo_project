import streamlit as st
import matplotlib.pyplot as plt
import random
import time

def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return result

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

def check_win_or_lose():
    numb = random.randint(1, 37)
    if numb >= 19:
        return "You win $10"
    else:
        return "You lose $10"

def calculate_cash(n):
    cash = 0
    for i in range(1, n+1):
        cash -= 10
        numb = random.randint(1, 37)
        if numb >= 19:
            cash += 20
    return cash


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

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run", key="btn1"):
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

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run", key="btn2"):
        heads, tails, heads_percentage, tails_percentage = count_flips(n)
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
            f'<div class="result">Heads count: {heads}</div>'
            f'<div class="result">Tails count: {tails}</div>'
            f'<div class="result">Heads percentage: {heads_percentage:.2f}%</div>'
            f'<div class="result">Tails percentage: {tails_percentage:.2f}%</div>',
            unsafe_allow_html=True
        )


st.header("Roulette")
code = """
def check_win_or_lose():
    numb = random.randint(1, 37)
    if numb >= 19:
        return "You win $10"
    else:
        return "You lose $10"
"""

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run", key="btn3"):
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


code1 = """
def calculate_cash(n):
    cash = 0
    for i in range(1, n+1):
        cash -= 10
        numb = random.randint(1, 37)
        if numb >= 19:
            cash += 20
    return cash
"""

st.header("Roulette Simulation")
n = st.number_input("Enter the number of plays", value=1000, min_value=1, step=1)

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code1, language='Python')

with resultCol:
    if st.button("Run", key="btn4"):
        result1 = calculate_cash(n)
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
            f'<div class="result">Cash after playing: ${result1}</div>',
            unsafe_allow_html=True
        )

st.write("Now we lose nearly every time - That's the Law of large numbers")
st.write("The simulation already comes close to the calculated value.")

code = """10 * 10000 * ((18/37) - (19/37))"""
st.code(code, language='Python')
run_col, result_col = st.columns([2,15], gap="small")
if run_col.button("Run", key="btn5"):
    with result_col:
        result1 = 10 * 10000 * ((18/37) - (19/37))
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
            f'<div class="result">${result1:.2f}</div>',
            unsafe_allow_html=True
        )


def simulate_game():
    cash = 1000
    day = 1
    game = 0

    while cash < 2000 and cash >= 10:
        game += 1
        cash -= 10
        numb = random.randint(1, 37)
        if numb >= 19:
            cash += 20

        if game == 500:
            st.markdown(
                f"""
                <style>
                .day_{day} {{
                    background-color: #ffcccc;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True
            )
            day += 1
            game = 0
            time.sleep(1.5)

    st.markdown(
        f"""
        <style>
        .final {{
            background-color: #ccffcc;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="final">Day {day}: ${cash}</div>',
        unsafe_allow_html=True
    )

# Streamlit UI
st.header("Gambling simulation")
st.write("Gambling with $1000 Simulation")
code = """
def simulate_game():
    cash = 1000
    day = 1
    game = 0

    while cash < 2000 and cash >= 10:
        game += 1
        cash -= 10
        numb = random.randint(1, 37)
        if numb >= 19:
            cash += 20

        if game == 500:
            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True
            )
            day += 1
            game = 0
            time.sleep(1.5)

    st.markdown(
        f'<div class="final">Day {day}: ${cash}</div>',
        unsafe_allow_html=True
    )
"""

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run", key="btn6"):
        result = simulate_game()


def simulate_game2():
    cash = 1000
    day = 1
    game = 0

    while cash < 2000 and cash >= 10:
        game += 1

        if random.randint(1, 37) < 19:
            set_high = 1
        else:
            set_high = 0

        cash -= 10
        numb = random.randint(1, 37)

        if set_high == 1 and numb >= 19:
            cash += 20
        elif set_high == 0 and 1 <= numb <= 18:
            cash += 20

        if game == 500:
            st.markdown(
                f"""
                <style>
                .day_{day} {{
                    background-color: #ffcccc;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True
            )
            day += 1
            game = 0
            time.sleep(1.5)

    st.markdown(
        f"""
        <style>
        .final {{
            background-color: #ccffcc;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="final">Day {day}: ${cash}</div>',
        unsafe_allow_html=True
    )


code = """
def simulate_game():
    cash = 1000
    day = 1
    game = 0

    while cash < 2000 and cash >= 10:
        game += 1

        if random.randint(1, 37) < 19:
            set_high = 1
        else:
            set_high = 0

        cash -= 10
        numb = random.randint(1, 37)

        if set_high == 1 and numb >= 19:
            cash += 20
        elif set_high == 0 and 1 <= numb <= 18:
            cash += 20

        if game == 500:
            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True
            )
            day += 1
            game = 0
            time.sleep(1.5)

    st.markdown(
        f'<div class="final">Day {day}: ${cash}</div>',
        unsafe_allow_html=True
    )
"""
codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run", key="btn7"):
        result = simulate_game2()


def simulate_game3():
    cash = 10000
    day = 1
    bet = 10
    game = 0

    while cash < 20000 and cash >= 10:
        game += 1
        cash -= bet
        numb = random.randint(1, 37)

        if numb >= 19:
            cash += 2 * bet
            bet = 10
        else:
            bet *= 2
            if bet > 1000:
                bet = 1000
            if bet > cash:
                bet = cash

        if game == 500:
            st.markdown(
                f"""
                <style>
                .day_{day} {{
                    background-color: #ffcccc;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True
            )
            day += 1
            game = 0
            time.sleep(1.5)

    st.markdown(
        f"""
        <style>
        .final {{
            background-color: #ccffcc;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="final">Day {day}: ${cash}</div>',
        unsafe_allow_html=True
    )

st.write("Increase bet")

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run", key="btn8"):
        result = simulate_game3()



def simulate_sessions(num_sessions):
    n_win = 0

    for _ in range(num_sessions):
        cash = 10000
        bet = 10

        while cash < 20000 and cash >= 10:
            cash -= bet
            numb = random.randint(1, 37) - 1

            if numb >= 19:
                cash += 2 * bet
                bet = 10
            else:
                bet *= 2
                if bet > 1000:
                    bet = 1000
                if bet > cash:
                    bet = cash

        if cash >= 20000:
            n_win += 1

    return n_win

st.header("Gambling Simulation")
num_sessions = st.number_input("Enter the number of sessions:", min_value=1, value=100)

code = """
def simulate_sessions(num_sessions):
    n_win = 0

    for _ in range(num_sessions):
        cash = 10000
        bet = 10

        while cash < 20000 and cash >= 10:
            cash -= bet
            numb = random.randint(1, 37) - 1

            if numb >= 19:
                cash += 2 * bet
                bet = 10
            else:
                bet *= 2
                if bet > 1000:
                    bet = 1000
                if bet > cash:
                    bet = cash

        if cash >= 20000:
            n_win += 1

    return n_win
"""

codeCol, resultCol = st.columns([2, 1.5])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run Simulation", key='btn9'):
        wins = simulate_sessions(num_sessions)
        result_text = f"Number of Wins: {wins}"
        result_html = f'<div style="background-color: #ccffcc; padding: 10px;">{result_text}</div>'
        st.markdown(result_html, unsafe_allow_html=True)

box = list(range(1, 51))

def drawing():
    for i in range(6):
        h = random.randint(i, 49)
        box[i], box[h] = box[h], box[i]

def check(my_numbers):
    n_match = 0
    for i in range(6):
        for j in range(6):
            if my_numbers[i] == box[j]:
                n_match += 1
    return n_match

def simulate_lottery(my_numbers):
    week = 0
    n_match = 0

    while n_match < 6:
        drawing()
        n_match = check(my_numbers)

        if n_match == 5:
            st.markdown(
                f"""
                <style>
                .week_{week} {{
                    background-color: #ffcccc;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="week_{week}">5 correct after {week // 52} years</div>',
                unsafe_allow_html=True
            )

        week += 1

    st.markdown(
        f"""
        <style>
        .final {{
            background-color: #ccffcc;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="final">6 correct after {week // 52} years</div>',
        unsafe_allow_html=True
    )

# Streamlit UI
st.header("Lottery Number Matching Simulation")
st.write("Enter Your Numbers:")
my_numbers = st.text_input("Enter 6 numbers separated by commas")

code = '''

box = list(range(1, 51))

def drawing():
    for i in range(6):
        h = random.randint(i, 49)
        box[i], box[h] = box[h], box[i]

def check(my_numbers):
    n_match = 0
    for i in range(6):
        for j in range(6):
            if my_numbers[i] == box[j]:
                n_match += 1
    return n_match

def simulate_lottery(my_numbers):
    week = 0
    n_match = 0

    while n_match < 6:
        drawing()
        n_match = check(my_numbers)

        if n_match == 5:
            st.markdown(
                f"""
                <style>
                .week_{week} {{
                    background-color: #ffcccc;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="week_{week}">5 correct after {week // 52} years</div>',
                unsafe_allow_html=True
            )

        week += 1

    st.markdown(
        f"""
        <style>
        .final {{
            background-color: #ccffcc;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="final">6 correct after {week // 52} years</div>',
        unsafe_allow_html=True
    )
'''

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Run Simulation", key='btn909'):
        my_numbers = [int(num.strip()) for num in my_numbers.split(',')]
        simulate_lottery(my_numbers)


def estimate_pi(n):
    hit = 0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y < 1:
            hit += 1

    pi_estimate = 4 * hit / n

    return pi_estimate

# Streamlit UI
st.header("Monte Carlo Pi Estimation")
st.write("Number of Samples")
n = st.number_input("Enter the number of samples:", min_value=1, value=100000, step=1)

code = """
def estimate_pi(n):
    hit = 0

    for _ in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y < 1:
            hit += 1

    pi_estimate = 4 * hit / n

    return pi_estimate
"""

codeCol, resultCol = st.columns([2, 1.5])

with codeCol:
    st.code(code, language='Python')

with resultCol:
    if st.button("Estimate Pi", key='btn919'):
        pi_approx = estimate_pi(n)
        result_text = f"Approximation of Pi: {pi_approx:.4f}"
        result_html = f'<div style="background-color: #ccffcc; padding: 10px;">{result_text}</div>'
        st.markdown(result_html, unsafe_allow_html=True)



def estimate_pi_draw(n):
    hit = 0
    points = []

    for i in range(n):
        x = random.random()
        y = random.random()

        if x * x + y * y < 1:
            hit += 1
            color = '#990000'  # Red
        else:
            color = '#000000'  # Black

        points.append((x * 100, y * 100, color))

    xs, ys, colors = zip(*points)
    plt.scatter(xs, ys, color=colors, s=5)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Iteration: {n}")

    # Display the final plot
    st.pyplot(plt.gcf())

    pi_approx = 4 * hit / n
    return pi_approx

# Streamlit UI
st.header("Monte Carlo Pi Estimation with Visualization")
st.write("Number of Iterations")
n = st.number_input("Enter the number of iterations:", min_value=1, value=50000, step=1)

if st.button("Estimate Pi"):
    pi_approx = estimate_pi_draw(n)
    st.write(f"Approximation of Pi: {pi_approx}")