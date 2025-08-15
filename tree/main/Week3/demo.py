def main():
    data = open('demo.txt')
    lines = data.readlines()

    with open('demo.txt', 'w') as file:
        file.write('hello world! line 1 ')

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()

