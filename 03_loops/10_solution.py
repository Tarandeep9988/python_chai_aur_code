# Exponential Backoff
# Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries

import time

wait_time = 1
max_retreis = 5

attempts = 1

print("You are given", max_retreis, "attempts")
while attempts <= max_retreis:
    print("Attempt: ", attempts, "- wait time: ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1