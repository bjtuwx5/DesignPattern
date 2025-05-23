import Animal
import Cat
import Dog

if __name__ == "__main__":
    arrayAnimal = {
        Cat.Cat("小花"),
        Dog.Dog("小汪")
    }

    for animal in arrayAnimal:
        print(animal.shout())