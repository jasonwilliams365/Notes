from datetime import datetime, timedelta

now = datetime.now()
print("Current time:", now)

tomorrow = now + timedelta(days=1)
print("Tomorrow:", tomorrow)