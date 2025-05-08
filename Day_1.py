# Day 2: While Loops - Countdown timer
import time

countdown = 5
while countdown > 0:
    print(f"⏳ {countdown} second ...")
    time.sleep(1)
    countdown -= 1

print("🕒 Time's up!")