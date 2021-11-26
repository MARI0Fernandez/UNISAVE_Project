import cv2
import numpy as np
import qrcode
import csv
import pandas as pd
import matplotlib.pyplot as plt


col_list = ["NIF", "Name", "Surname", "Degree", "Budget", "qrcode_image", "University_Budget", "Restaurant&Bars_Budget", "Supermarket_Budget", "Leisure_Budget"]

def creating_qr_code(NIF, name, surname, degree, monthlybudget):
        data = "{Name}\n{Surname}\n{Degree}\n{NIF}\n{Monthlybudget}".format(Name=name, Surname=surname, Degree=degree, NIF=NIF, Monthlybudget= monthlybudget)
        features = qrcode.QRCode(version=1, box_size=7, border=3)
        features.add_data(data)
        features.make(fit=True)
        generate_image = features.make_image(fill_color="black", back_color="White")
        generate_image.save("./Images_QRcode/{nif}.png".format(nif=NIF))


class OldUser:
    def __init__(self, NIF):
        self.nif = NIF

    def registered(self, filename="infousers.csv"):
        self.file = open(filename, "r")
        df = pd.read_csv(self.file, usecols=col_list)
        df2 = list(df["NIF"])
        self.file.close()
        if self.nif in df2:
            return True
        else:
            return False


class NewUser:
    def __init__(self, NIF, Name, Surname, Degree, Monthlybudget):
        self.NIF = NIF
        self.Name = Name
        self.Surname = Surname
        self.Degree = Degree
        self.Monthlybudget = Monthlybudget

    def register(self, filename="infousers.csv"):
        with open(filename, "a+", newline="\n") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=["NIF", "Name", "Surname", "Degree", "Budget", "qrcode_image", "University_Budget", "Restaurant&Bars_Budget", "Supermarket_Budget", "Leisure_Budget"]
            )
            writer.writerow({"NIF": self.NIF, "Name": self.Name, "Surname": self.Surname, "Degree": self.Degree, "Budget": self.Monthlybudget, "qrcode_image": self.NIF + ".png",
                         "University_Budget": [self.Monthlybudget * 0.2], "Restaurant&Bars_Budget": [self.Monthlybudget * 0.3], "Supermarket_Budget": [self.Monthlybudget * 0.4], "Leisure_Budget": [self.Monthlybudget * 0.1]})
            csvfile.close()
            print("\nLET'S GO. Now, you are in our system.")
            print("\n-----------------------------------------")


class Features:
    def __init__(self, NIF, name, surname, degree, budget, qrcode_image, universitybudget, restaurantbudget, supermarketbudget, leisurebudget):
        self.nif = NIF
        self.name = name
        self.surname = surname
        self.degree = degree
        self.budget = budget
        self.qrcode_image = qrcode_image
        self.universitybudget = universitybudget
        self.restaurantbudget = restaurantbudget
        self.supermarketbudget = supermarketbudget
        self.leisurebudget = leisurebudget

    def qrcode_window(self):
        img = cv2.imread("./Images_QRcode/{ans}.png".format(ans=self.nif), 1)
        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])
        plt.title("Hello {} {}".format(self.name, self.surname))
        plt.xlabel("Once you have finished, click the close button.\nPlease, go back to the console.", horizontalalignment="center")
        plt.show()
        plt.close()


    def getexpenses(self, filename="infousers.csv"):
        df = pd.read_csv(filename, usecols=col_list)
        i = list(df["NIF"]).index(self.nif)
        expense = input("How much have you spent? (<Enter> to quit)")
        while expense != "":
            expense = eval(expense)
            category = int(input("Where would you put this expense?"
                "\n1. University"
                "\n2. Restaurants and bars"
                "\n3. Supermarket"
                "\n4. Leisure"
                "\n "))

            if category == 1:
                output = "University"
                x2 = df["University_Budget"][i].strip('][."').split(',')
                if expense < eval(x2[0]):
                    x2[0] = eval(x2[0])-expense
                    x2.append(float(expense))
                    newlist = list(map(float, x2))
                    df.loc[i, "University_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                    print("\nYou have spent", str(expense) + "€", "in", output)
                elif expense <= eval(x2[0]):
                    x2[0] = eval(x2[0])-expense
                    x2.append(float(expense))
                    newlist = list(map(float, x2))
                    df.loc[i, "University_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                    print("\nWARNING!, you have no more  money in University.")
                    print("You have spent", str(expense) + "€", "in", output)
                else:
                    print("You do not have enough money to pay.")

            elif category == 2:
                output = "Restaurant and Bars"
                y2 = df["Restaurant&Bars_Budget"][i].strip('][."').split(',')
                if expense < eval(y2[0]):
                    y2[0] = eval(y2[0])-expense
                    y2.append(float(expense))
                    newlist = list(map(float, y2))
                    df.loc[i, "Restaurant&Bars_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                elif expense <= eval(y2[0]):
                    y2[0] = eval(y2[0])-expense
                    y2.append(float(expense))
                    newlist = list(map(float, y2))
                    df.loc[i, "Restaurant&Bars_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                    print("\nWARNING!, you have no more  money in Restaurant and Bars.")
                    print("You have spent", str(expense) + "€", "in", output)
                else:
                    print("You do not have enough money to pay.")

            elif category == 3:
                output = "Supermarket"
                z2 = df["Supermarket_Budget"][i].strip('][."').split(',')
                if expense < eval(z2[0]):
                    z2[0] = eval(z2[0])-expense
                    z2.append(float(expense))
                    newlist = list(map(float, z2))
                    df.loc[i, "Supermarket_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                elif expense <= eval(z2[0]):
                    z2[0] = eval(y2[0])-expense
                    z2.append(float(expense))
                    newlist = list(map(float, z2))
                    df.loc[i, "Supermarket_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                    print("\nWARNING!, you have no more  money in Supermarket.")
                    print("You have spent", str(expense) + "€", "in", output)
                else:
                    print("You do not have enough money to pay.")

            elif category == 4:
                output = "Leisure"
                w2 = df["Leisure_Budget"][i].strip('][."').split(',')
                if expense < eval(w2[0]):
                    w2[0] = eval(w2[0])-expense
                    w2.append(float(expense))
                    newlist = list(map(float, w2))
                    df.loc[i, "Leisure_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                elif expense <= eval(w2[0]):
                    w2[0] = eval(w2[0])-expense
                    w2.append(float(expense))
                    newlist = list(map(float, w2))
                    df.loc[i, "Leisure_Budget"] = "{}".format(newlist)
                    df.to_csv("infousers.csv", index=False)
                    print("\nWARNING!, you have no more  money in Leisure.")
                    print("You have spent", str(expense) + "€", "in", output)
                else:
                     print("You do not have enough money to pay.")

            else:
                print("You need to enter a number between 1 and 4.")

            expense = input("\nHave you paid anything else? How much have you spent? (<Enter> to quit) ")



    def Showmoney(self, filename = "infousers.csv"):
        df = pd.read_csv(filename, usecols=col_list)
        i = list(df["NIF"]).index(self.nif)
        print("\nThese are your budgets")
        print("University_Budget", "Restaurant&Bars_Budget", "Supermarket_Budget", "Leisure_Budget", sep="|")
        uni = df["University_Budget"][i].strip('][."').split(',')
        rest = df["Restaurant&Bars_Budget"][i].strip('][."').split(',')
        supm = df["Supermarket_Budget"][i].strip('][."').split(',')
        leis = df["Leisure_Budget"][i].strip('][."').split(',')
        print(round(eval(uni[0]), 2), round(eval(rest[0]),2), round(eval(supm[0]),2), round(eval(leis[0]),2),  sep="\t\t\t|\t\t")


    def Entermoney(self, filename = "infousers.csv"):
        df = pd.read_csv(filename, usecols=col_list)
        i = list(df["NIF"]).index(self.nif)

        self.Showmoney()
        money = input("\nHow much money do you want to enter? (<Enter> to quit) ")
        while money != "":
            money = eval(money)
            category = eval(input("In which category do you can to put the money?"
            "\n1. University"
            "\n2. Restaurants and bars"
            "\n3. Supermarket"
            "\n4. Leisure"
            "\n"))
            if category == 1:
                output = "University"
                x2 = df["University_Budget"][i].strip('][."').split(',')
                x2[0] = eval(x2[0])+money
                newlist = list(map(float, x2))
                df.loc[i, "University_Budget"] = "{}".format(newlist)
                df.to_csv("infousers.csv", index=False)
            elif category == 2:
                output = "Restaurants and Bars"
                y2 = df["Restaurant&Bars_Budget"][i].strip('][."').split(',')
                y2[0] = eval(y2[0])+money
                newlist = list(map(float, y2))
                df.loc[i, "Restaurant&Bars_Budget"] = "{}".format(newlist)
                df.to_csv("infousers.csv", index=False)
            elif category == 3:
                output = "Supermarket"
                z2 = df["Supermarket_Budget"][i].strip('][."').split(',')
                z2[0] = eval(z2[0])+money
                newlist = list(map(float, z2))
                df.loc[i, "Supermarket_Budget"] = "{}".format(newlist)
                df.to_csv("infousers.csv", index=False)
            elif category == 4:
                output = "Leisure"
                w2 = df["Leisure_Budget"][i].strip('][."').split(',')
                w2[0] = eval(w2[0])+money
                newlist = list(map(float, w2))
                df.loc[i, "Leisure_Budget"] = "{}".format(newlist)
                df.to_csv("infousers.csv", index=False)
            else:
                print("You entered a wrong value.")

            print("\nYou have entered", str(money) + "€", "into", output)
            money = input("Do you want to enter more money, how much? (<Enter> to quit) ")


    def Showexpenses(self, filename="infousers.csv"):
        df = pd.read_csv(filename, usecols=col_list)
        i = list(df["NIF"]).index(self.nif)

        uni = [float(x) for x in df["University_Budget"][i].strip('][."').split(",")]
        rest = [float(x) for x in df["Restaurant&Bars_Budget"][i].strip('][."').split(",")]
        supr = [float(x) for x in df["Supermarket_Budget"][i].strip('][."').split(",")]
        leis = [float(x) for x in df["Leisure_Budget"][i].strip('][."').split(",")]
        total_List = [uni, rest, supr, leis]
        for x in total_List:
            x.pop(0)

        print("University_budget:", total_List[0], "->", "-"+str(sum(total_List[0])))
        print("Restaurant&Bars_budget:", total_List[1], "->", "-"+str(sum(total_List[1])))
        print("Supermarket_budget:", total_List[2], "->", "-"+str(sum(total_List[2])))
        print("Leisure_budget:", total_List[3], "->", "-"+str(sum(total_List[3])))

        ans = input("\nDo you want to observe the graph expense of any category? (Yes or No) ").lower()
        while True:
            if ans == "yes":
                ans2 = eval(input("What graph do you want to watch?"
                                  "\n1. Line graph with all expenses"
                                    "\n2. Bar chart with total expenses"
                                    "\n"))
                if ans2 == 1:
                    graph1 = total_List[0]
                    l1 = len(total_List[0])
                    graph2 = total_List[1]
                    l2 = len(total_List[1])
                    graph3 = total_List[2]
                    l3 = len(total_List[2])
                    graph4 = total_List[3]
                    l4 = len(total_List[3])
                    plt.plot(range(1, l1+1), graph1, "o-", color ="blue")
                    plt.plot(range(1, l2+1), graph2, "o-", color="green")
                    plt.plot(range(1, l3+1), graph3, "o-", color="yellow")
                    plt.plot(range(1, l4+1), graph4, "o-", color="grey")
                    plt.xlabel("Number of expense")
                    plt.ylabel("Money spent")
                    plt.legend(["University", "Restaurants & Bars", "Supermarket", "Leisure"], loc=0)
                    plt.title("EXPENSES IN CATEGORIES")
                    plt.show()

                elif ans2 == 2:
                    values1 = sum(total_List[0])
                    values2 = sum(total_List[1])
                    values3 = sum(total_List[2])
                    values4 = sum(total_List[3])
                    labels = ["University", "Restaurants & Bars", "Supermarket", "Leisure"]
                    y_pos = np.arange(len(labels))
                    list2 = [values1, values2, values3, values4]

                    plt.bar(y_pos, list2, align="center", alpha=0.5, edgecolor= ["blue", "green", "yellow", "grey"])
                    plt.xticks(y_pos, labels, rotation=45)
                    plt.ylabel("Euros")

                    plt.show()

                ans = input("\nDo you want to observe the graph of expenses of the categories? (Yes or No) ").lower()
            else:

                break



def main():
    print("WELCOME TO UNISAVE! The program that will help you to control your budget.")
    print("In order to know if you are already in the system could you type your NIF.")
    NIF = input("NIF: ").strip()
    user = OldUser(NIF)
    if not user.registered():
        print("\n-----------------------------------------")
        print("\nAs you are not in our system, we are going to ask you for some information\nin order to save you in the system. Could you please answer the following?\n")
        while True:
            name = input("Your name: ").strip().title()
            surname = input("Your surname: ").title()
            degree = input("Your degree (Abbreviation, such as: BBADBA): ").strip().upper().replace("&", "")
            monthlybudget = eval(input("Your monthly budget: "))
            try:
                if name.isalpha() == False or degree.isalpha() == False:
                    print("\nYou entered wrong values (Numbers or symbols).\nTry to enter again your info, paying special attention to name, surname and degree.\n")
                else:
                    break
            except:
                break
        user2 = NewUser(NIF, name, surname, degree, monthlybudget)
        user2.register()
        creating_qr_code(NIF, name, surname, degree, monthlybudget)
    else:
        print("\n-----------------------------------------\n")

    print("MAIN PAGE")
    df = pd.read_csv("infousers.csv", usecols=col_list)
    i = list(df["NIF"]).index(NIF)
    name = df["Name"][i]
    surname = df["Surname"][i]
    degree = df["Degree"][i]
    budget = df["Budget"][i]
    qrcode_image = df["qrcode_image"][i]
    university = df["University_Budget"][i]
    restaurant = df["Restaurant&Bars_Budget"][i]
    supermarket = df["Supermarket_Budget"][i]
    leisure = df["Leisure_Budget"][i]
    print("Hello,", name, surname)
    answer = input("What would you like to do? (<Enter> to quit)"
        "\n1. QRcode to pay."
        "\n2. Visualize my budget for my categories."
        "\n3. Enter some money into a category."
        "\n4. Observe my expenses in a category"
        "\n")
    features = Features(NIF, name, surname, degree,  budget, qrcode_image, university, restaurant, supermarket, leisure)
    while answer != "":
        answer = int(answer)
        if answer == 1:
            print("\n-----------------------------------------")
            print("PAY PAGE")
            features.qrcode_window()
            features.getexpenses()
        if answer == 2:
            print("\n-----------------------------------------")
            print("SUMMARY PAGE")
            features.Showmoney()
        if answer == 3:
            print("\n-----------------------------------------")
            print("INCOME PAGE")
            features.Entermoney()
            features.Showmoney()
        if answer == 4:
            print("\n-----------------------------------------")
            print("EXPENSES PAGE")
            features.Showexpenses()
        print("\n-----------------------------------------")
        print("MAIN PAGE")
        print("\nWhat else do you want to do? (<Enter> to quit)")
        answer = input("1. QRcode to pay."
        "\n2. Visualize my budget for my categories."
        "\n3. Enter some money into a category."
        "\n4. Observe my expenses in a category"
        "\n")

    print("THANK YOU FOR USING UNISAVE!")


if __name__ == "__main__":
    main()
