from LoanCalc import LoanCalc

def main():
    lc = LoanCalc()
    for i in range(4):
        lc.getInput(i)

    input()
    lc.calculateOutput()
    print(lc.returnJSON())

if __name__ == "__main__":
    main()