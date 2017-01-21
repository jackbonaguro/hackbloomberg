import sys
import client


def main():
    try:
        client.run("rcb", "pass1", "MY_CASH")
    except:
        print("lose")


if __name__ == '__main__':
  main()
