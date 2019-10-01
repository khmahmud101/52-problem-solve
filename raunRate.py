t = int(input())
for i in range(t):
    r1 = int(input())
    r2 = int(input())
    B = int(input())
    ball_played = 300 - B
    current_rr = (r2/ball_played)*6
    asking_rr = ((r1 - r2+1) / B)*6
    print("Total run",r2, ",current Run Rate",current_rr,",asking Run Rate",asking_rr)




