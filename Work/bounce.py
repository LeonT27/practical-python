# bounce.py
#
# Exercise 1.5
current_height = 100
bounces = 3/5
total_bounces = 10
current_bounce = 0

while current_bounce < total_bounces:
    current_height *= bounces
    current_bounce += 1
    print(current_bounce, round(current_height,4))