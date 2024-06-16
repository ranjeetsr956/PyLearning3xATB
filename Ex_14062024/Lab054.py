# match case

browser = input("Enter a browser = ")
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code is executed")
    case "firefox":
        print("Firefox code is executed")
    case "edge":
        print("Edge code is executed")
    case _:
        print("Enter a valid browser")