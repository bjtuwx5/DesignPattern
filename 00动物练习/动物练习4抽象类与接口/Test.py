import MachineCat
import StoneMonkey

if __name__ == "__main__":
    arrayAnimal = {
        MachineCat.MachineCat("叮当"),
        StoneMonkey.StoneMonkey("孙悟空")
    }

    for animal in arrayAnimal:
        print(animal.changeThing("各种各样的东西！"))