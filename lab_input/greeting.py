from datetime import date
def main():
    name = input("Name: ")
    today = date.today()
    print(f"Hello, {name}. Happy {today.strftime('%A')}!")
main()
