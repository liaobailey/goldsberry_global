import streamlit as st
import pandas as pd
import numpy as np
import simplejson as json
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc


player_dict = players.get_players()

st.title("Shot Chart Visualization")

st.subheader("Shot charts for all All Stars for the 2019-2020 season plus the top 3 draft picks")

@st.cache(persist = True)
def load_data(csv, nrows):
    data = pd.read_csv(csv, nrows = nrows)
    return data

raw = load_data('raw_new.csv', 200000)

@st.cache
def fill(df, player, make_or_all, time_remaining, win_or_lose, up_or_down):
    fill = df[(df['PLAYER_NAME'] == player) & (df['clutch'] == time_remaining) & (df['win'] == win_or_lose) & (df['status'] == up_or_down)]
    if make_or_all == 'FGA':
        return fill
    else:
        fill2 = fill[fill['SHOT_MADE_FLAG'] == 1]
        return fill2

player = st.sidebar.selectbox(
    "What Player would you like to look at?",
    ("LeBron James", "Giannis Antetokounmpo", "James Harden", "Devin Booker", "Donovan Mitchell", "Russell Westbrook", "Damian Lillard", "Luka Doncic", "Nikola Jokic", "Anthony Davis", "Trae Young", "Jayson Tatum", "Kawhi Leonard", "Brandon Ingram", "Pascal Siakam", "Khris Middleton", "Domantas Sabonis", "Bam Adebayo", "Ja Morant", "Chris Paul", "Rudy Gobert", "Joel Embiid", "Ben Simmons", "Kemba Walker", "Jimmy Butler", "Kyle Lowry", "RJ Barrett", "Zion Williamson")
)

make = st.sidebar.selectbox(
    "Do you want to see all shots or just makes?",
    ("All", "Just Makes")
)

time = st.sidebar.selectbox(
    "Do you want to see how your player shoots in the clutch?",
    ("No", "Last 5 Minutes", "Last 3 Minutes")
)

win = st.sidebar.selectbox(
    "Do you want to see all how your player shot in a win?",
    ("All", "W", "L")
)

up = st.sidebar.selectbox(
    "Do you want to see how your player shot ahead or trailing?",
    ("All", "Ahead", "Trailing")
)

if make == 'All':
    make = 'FGA'
else:
    make = 'PTS'

if time == 'No':
    time = 'none'
else:
    time = time

if win == 'All':
    win = 'none'
else:
    win = win

if up == 'All':
    up = 'none'
elif up == 'Ahead':
    up = 'Ahead or Tied'
else:
    up = 'Behind or Tied'

viz = st.button('Create Visualization Now!')
if viz:
    with st.spinner('Creating Visualization...'):
        df = fill(raw, player, make, time, win, up)
        joint_shot_chart = sns.jointplot(df.LOC_X, df.LOC_Y, stat_func=None,
                                     kind='scatter', space=0, alpha=0.5)
        joint_shot_chart.fig.set_size_inches(11,11)
        ax = joint_shot_chart.ax_joint

        hoop = Circle((0, 0), radius=7.5, linewidth=2, color='black', fill=False)

        # Create backboard
        backboard = Rectangle((-30, -7.5), 60, -1, linewidth=2, color='black')

        # The paint
        # Create the outer box 0f the paint, width=16ft, height=19ft
        outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=2, color='black',
                              fill=False)
        # Create the inner box of the paint, widt=12ft, height=19ft
        inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=2, color='black',
                              fill=False)

        # Create free throw top arc
        top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                             linewidth=2, color='black', fill=False)
        # Create free throw bottom arc
        bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                                linewidth=2, color='black', linestyle='dashed')
        # Restricted Zone, it is an arc with 4ft radius from center of the hoop
        restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=2,
                         color='black')

        # Three point line
        # Create the side 3pt lines, they are 14ft long before they begin to arc
        corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=2,
                                   color='black')
        corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=2, color='black')
        # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
        # I just played around with the theta values until they lined up with the
        # threes
        three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=2,
                        color='black')

        # Center Court
        center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                               linewidth=2, color='black')
        center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                               linewidth=2, color='black')

        court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                  bottom_free_throw, restricted, corner_three_a,
                  corner_three_b, three_arc, center_outer_arc,
                  center_inner_arc]

        for element in court_elements:
            ax.add_patch(element)

        ax.set_xlim(-250,250)
        ax.set_ylim(422.5, -47.5)

        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(labelbottom=False, labelleft=False)
        st.pyplot()
