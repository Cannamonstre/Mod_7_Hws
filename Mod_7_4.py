team_1, team_2 = 'The Code Masters', 'The Data Wizards'

#  % using
team1_num = 7
print('There are %s members in "The Code Masters" team!' % team1_num)

team1_num = 7
team2_num = 9
print("Today, each team has %s and %s members respectively!" % (team1_num, team2_num))

#  format() using
score_2 = 44
print("The Data Wizards team completed {} tasks!".format(score_2))

team1_time = 1337.4
team2_time = 1442.4
print("The Data Wizards team completed tasks for {} seconds!".format(team2_time))

#  f-strings using
score_1 = 69  # the 12th line for score_2
print(f"The teams completed {score_1} and {score_2} tasks respectively.")

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'The winner is "{team_1}"!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'The winner is "{team_2}"!'
else:
    challenge_result = "The match ended in a draw!"

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print(challenge_result)
print(f"It was {tasks_total} tasks completed today, "
      f"average time of completing one task is {time_avg} seconds!")
