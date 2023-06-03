import streamlit as st
import matplotlib.pyplot as plt
import random
import time


def coin_flip():
    # randomly flip the coin for head and tail
    result = random.choice(["Heads", "Tails"])
    return result


def count_flips(n):
    """
    Randomly flips the coin for head and tail base on number of input
    :param n: number of input
    :return: count of head, tail, head percentage and tail percentage
    """
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
    # Based on random number generator, if number greater or equal to 19 then win $10 else lose $10
    numb = random.randint(1, 37)
    if numb >= 19:
        return "You win $10"
    else:
        return "You lose $10"


def calculate_cash(n):
    # base on number of input calculated the total amount of cash win
    cash = 0
    for i in range(1, n + 1):
        cash -= 10
        numb = random.randint(1, 37) - 1
        if numb >= 19:
            cash += 20
    return cash


# set the page configuration
st.set_page_config(
    page_title="The Law of Large Number", page_icon="game_die", layout="centered"
)


url = "https://easylang.dev/apps/tutorial_mcarlo.html"
st.title("The Law of Large Numbers")

st.subheader("What is the Large Number?")
st.write("The law of large numbers is a fundamental concept in statistics and probability theory. It states that as the number of observations or samples increases, the average or mean of those observations will converge to the expected or true value.")
st.write('In simpler terms, if you repeat an experiment or observation many times, the average result will become more and more stable and closer to the expected outcome. This law is based on the principle that as the sample size increases, the random variations or "noise" in the data tend to cancel each other out, leading to more reliable and predictable results.')

st.subheader("Coin flip")
st.write("For example, flipping a fair coin. The expected probability was 50/50")
code = """
def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return result
"""

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language="Python")

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
            unsafe_allow_html=True,
        )
        st.markdown(f'<div class="result">{result}</div>', unsafe_allow_html=True)
st.write("")

st.write("However, if you flip the coin a large number of times, like a thousand or a million, you will see that the proportion of heads and tails will get closer to 0.5, reflecting the expected probability.")

st.write("")
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
    st.code(code, language="Python")

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
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="result">Heads count: {heads}</div>'
            f'<div class="result">Tails count: {tails}</div>'
            f'<div class="result">Heads percentage: {heads_percentage:.2f}%</div>'
            f'<div class="result">Tails percentage: {tails_percentage:.2f}%</div>',
            unsafe_allow_html=True,
        )


st.title("Roulette")
st.write("The same concept can be applied to Roulette games.")
st.write("In roulette, there is a wheel with numbered pockets ranging from 0 to 36 (in European roulette) or 00 to 36 (in American roulette), with alternating red and black colors. The objective is to predict which pocket the ball will land in after the wheel is spun.")
st.write("In below example, if the ball is landed on the number you win $$10, if not then you lose $10")

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
    st.code(code, language="Python")

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
            unsafe_allow_html=True,
        )
        st.markdown(f'<div class="result">{result}</div>', unsafe_allow_html=True)

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
st.write("Let's play a thousand times:")
n = st.number_input("Enter the number of plays", value=1000, min_value=1, step=1)

codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code1, language="Python")

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
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="result">Cash after playing: ${result1}</div>',
            unsafe_allow_html=True,
        )

st.write("Most of the time we lose. Why do we actually lose?")
st.write('When you place a bet on a specific number, the payout for a win is usually 35 to 1. However, the odds of winning are not exactly 1 in 37, respectively, because of the presence of the 0 pocket, which are considered as "house" pockets.')


st.write("The simulation already comes close to the calculated value.")
code = """10 * 10000 * ((18/37) - (19/37))"""

st.code(code, language="Python")

run_col, result_col = st.columns([2, 15], gap="small")
if run_col.button("Run", key="btn5"):
    with result_col:
        result1 = 10 * 10000 * ((18 / 37) - (19 / 37))
        st.markdown(
            f"""
            <style>
            .result {{
                background-color: #ccffcc;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(f'<div class="result">${result1:.2f}</div>', unsafe_allow_html=True)


def simulate_game():
    cash = 1000
    day = 1
    game = 0

    while cash < 2000 and cash >= 10:
        game += 1
        cash -= 10
        numb = random.randint(1, 37) - 1
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
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True,
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
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="final">Day {day}: ${cash}</div>', unsafe_allow_html=True)


# Streamlit UI
st.subheader("Gambling simulation")
st.write("Let say we put $1000 into gambling for simulation")
st.write("We always bet 10 dollar on the high numbers. When the 1000 dollor is gone or becomes 2000 dollar, we stop playing. When the casino day is over (after 500 games), we go home and continue playing the next day.")
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
    st.code(code, language="Python")

with resultCol:
    if st.button("Run", key="btn6"):
        result = simulate_game()

st.write("We lose the game all the time")


def simulate_game2():
    cash = 1000
    day = 1
    game = 0

    while cash < 2000 and cash >= 10:
        game += 1

        if random.randint(1, 37) -1 < 19:
            set_high = 1
        else:
            set_high = 0

        cash -= 10
        numb = random.randint(1, 37) -1

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
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True,
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
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="final">Day {day}: ${cash}</div>', unsafe_allow_html=True)

st.write("To win the game, we adjust the strategy.  The chance that a high number will come after a low one could be higher. So we bet on the high numbers if there was a low number before, otherwise we bet on the low numbers")
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
    st.code(code, language="Python")

with resultCol:
    if st.button("Run", key="btn7"):
        result = simulate_game2()
st.write("But this does not work.")

def simulate_game3():
    cash = 10000
    day = 1
    bet = 10
    game = 0

    while cash < 20000 and cash >= 10:
        game += 1
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

        if game == 500:
            st.markdown(
                f"""
                <style>
                .day_{day} {{
                    background-color: #ffcccc;
                }}
                </style>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="day_{day}">Day {day}: ${cash}</div>',
                unsafe_allow_html=True,
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
        unsafe_allow_html=True,
    )
    st.markdown(f'<div class="final">Day {day}: ${cash}</div>', unsafe_allow_html=True)


st.write("How about we increase the bet")
st.write("We double the bet after each loss so that the first win resumes all previous losses and makes a profit equal to the original bet. But we are limited by our capital and the table limit of 1000 dollar. Starting capital is 10000 dollar.")


codeCol, resultCol = st.columns([2, 1])

with codeCol:
    st.code(code, language="Python")

with resultCol:
    if st.button("Run", key="btn8"):
        result = simulate_game3()


st.write("Sadly, that didn't work.")

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

st.write("Most of the time we lose. But with this strategy we seem to be able to win more often. We'll just try this n times in a row and see how often it works out.")
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
    st.code(code, language="Python")

with resultCol:
    if st.button("Run Simulation", key="btn9"):
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
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<div class="week_{week}">5 correct after {week // 52} years</div>',
                unsafe_allow_html=True,
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
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="final">6 correct after {week // 52} years</div>',
        unsafe_allow_html=True,
    )


# Streamlit UI
st.subheader("Lottery Number Matching Simulation")
st.write("Let's apply it on Lottery")
st.write("How many years does it take to have a Lotto six (6 out of 49) if you give a tip every week? For a Lotto five, the years are also printed out.")

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
    st.code(code, language="Python")

with resultCol:
    if st.button("Run Simulation", key="btn909"):
        my_numbers = [int(num.strip()) for num in my_numbers.split(",")]
        simulate_lottery(my_numbers)

st.write("Your 6 numbers will come - sooner or later, more likely later.")

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
st.subheader("Monte Carlo Pi Estimation")
st.write("There are other things you can do with Monte Carlo methods. For example, you can approximate the value of PI.")
st.write("Fire random points at a square with side length 1 and count the number of points inside the quarter circle. This can be easily determined by the theorem of Pythagoras. This number times four is close to PI.")
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
    st.code(code, language="Python")

with resultCol:
    if st.button("Estimate Pi", key="btn919"):
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
            color = "#990000"  # Red
        else:
            color = "#000000"  # Black

        points.append((x * 100, y * 100, color))

    xs, ys, colors = zip(*points)
    plt.scatter(xs, ys, color=colors, s=5)
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title(f"Iteration: {n}")

    # Display the final plot
    st.pyplot(plt.gcf())

    pi_approx = 4 * hit / n
    return pi_approx


# Streamlit UI
st.subheader("Monte Carlo Pi Estimation with Visualization")
st.write("Let's visualize it")
n = st.number_input("Enter the number of iterations:", min_value=1, value=50000, step=1)

if st.button("Estimate Pi"):
    pi_approx = estimate_pi_draw(n)
    st.write(f"Approximation of Pi: {pi_approx}")