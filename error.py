try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No errors occurred")
finally:
    print("This will always run")

    class MyError(Exception):
        pass

    try:
        raise MyError("An error occurred")
    except MyError as e:
        print(e)