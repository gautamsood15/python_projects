import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a, a+b
    return a


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', help='print the fib number with a statement', action='store_true')
    group.add_argument('-q', '--quiet', help="print the fib(num) result directly", action='store_true')
    parser.add_argument("num", help="Enter the Fibonacci number you wish to calculate", type=int)
    parser.add_argument('-o', '--output', help="Output result to a file", action="store_true")
    args = parser.parse_args()
    result = fib(args.num)

    if args.verbose:
        print("The "+str(args.num)+"th fib number is "+str(result))
    elif args.quiet:
        print(result)

    elif args.output:
        f = open("fibonacci.txt", "a")
        f.write(str(result) + "\n")

    else:
        print("Fib("+str(args.num)+") = "+str(result))


if __name__ == "__main__":
    main()
