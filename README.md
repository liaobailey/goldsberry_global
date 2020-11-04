# goldsberry_global

I created this repository to try to replicate some of the visualizations Kirk Goldsberry has. This project is one that maps shot selection amongst top NBA Players.

In this project, I wanted to implement my data analysis in a webapp and stumbled onto StreamLit. Picking up StreamLit syntax was not too difficult and I was able to deploy a webapp to the ip address below:

http://54.197.143.241:8501

# Getting Started

I played around with the NBA Api end point and was able to successfully make api calls. However, once I integrated with AWS, the endpoint stopped working, which seems to be something that the NBA actively blocks. I ended up downloading the data to my remote computer and uploading it onto AWS as a static CSV.

From there I added filters for top players, makes/misses, crunch time, and wins/losses. I then plotted the location of each shot onto a shot map.

Here are some of my favorite conclusions:

# Insights
Lebron James:

Filter for Last 5 Minutes when the Lakers won their game.
We see that in the last 5 minutes of wins, Lebron took 36.79% of his shots from 3 and 63.21% of his shots from 2. But let's break it down by when the Lakers were trailing vs when they were ahead.

Last 5 Minutes Trailing Percentage of 3's taken in Wins: 14.29%

Last 5 Minutes Ahead Percentage of 3's taken in Wins: 39.58%

When Lebron is ahead in games, he feels more confident taking 3's. It is possible that intuitively Lebron knows his highest expected value comes from getting a close range shot vs a 3 which is why when his team needs points to come from behind, he'll attack the rim more. 

Some issues here could be his team has a vast lead and scoring is not as critical, but I'm assuming if Lebron is in the game with 5 minutes remaining, it is a fairly close game.

James Harden: 

Filter for Wins and when Houston is ahead. 

For this filter, James Harden is shooting a staggering 60.57% of his shots from 3. The next closest is Damien Lillard with the same filters shooting 51.37% of his shots from 3. Harden's running mate, Russell Westbrook shoots only 13.62% of his shots from 3 with the same filters.

Gobert, Simmons, Bam, 3 Point Woes:

These 3 are the only all stars to take less than 2% of their shots from 3. Gobert is the only one at 0%. Should be noted that none of these players were starters on their all star teams which aligns with the entire analytics movement of the NBA moving towards the 3 point line. 

Along these lines, Zion Williamson only took 3.89% of his shots from 3. If Zion wants to enter a super star conversation it looks incredibly more likely that he'll need to develop a 3 point shot...if he can stay healthy first.
