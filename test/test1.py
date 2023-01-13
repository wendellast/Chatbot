import time

logs = [
        "Loading.",
        "Loading..",
        "Loading...",
        "Loading....",
        "Loading....."
]

for l in logs:
  time.sleep(1)
  print(l)