# Author: Littl
# CreatedDate : 8th July 2021
# Example file for working with conditional statements
#


def main():
    x, y = 1000, 100

    # conditional flow uses if, elif, else
    if (x<y):
        st = "x is less than y"
    elif (x==y):
        st = "x equals y"
    else:
        st = "x greater than y"
    
    print(st)
    # conditional statements let you use "a if C else b"
    st = "x greater than y" if (x>y) else  "x not greater than y"
    print(st)

if __name__ == "__main__":
    main()
