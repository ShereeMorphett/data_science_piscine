# You must take in *args a quantity of unknown number and make the Mean, Median,
# Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
# ask.
# You have to manage the errors.


# *args and **kwargs are special keyword which allows function to take variable length argument.

# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# -----
# std : 17982.70124086944
# var : 323377543.9183673


def ft_statistics(*args: any, **kwargs: any) -> None:
    for key, value in kwargs.items():
        if len(args) == 0:
            print(f"ERROR")
        else:
            match value:
                case "mean":
                    print(f"mean : {sum(args)/len(args)}")
                case "median":
                    index = round(len(args) / 2)
                    print(f"median : {list(sorted(args))[index]}")
                case "quartile":
                    sorted(args)
                    print(f"quartile : ")
                case "std":
                    print(f"std : ")
                case "var":
                    print(f"var : ")

def main():
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
    except Exception as e:
        print(f"ERROR")



if __name__ == "__main__":
    main()