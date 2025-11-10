class Printer:
    def printAyan(self, n):
        print(" ".join(["Ayan"] * n))

class Printer:
    def printAyan(self, n):
        print(("Ayan\n" * n).strip())
      
class Student:
    def __init__(self, name):
        self.name = name    # 'self' refers to the current object

    def greet(self):
        print("Hello,", self.name)


class Printer:
    def printAyan(self, n):
        print(("Ayan\n" * n).strip())
      
class Printer:
    def printAyan(self, n):
        if n == 0:
            return
        print("Ayan")
        self.printAyan(n - 1)

class Printer:
    def printAyan(self, n):
        # Print "Ayan" n times without using loop
        print(("Ayan\n" * n).strip())

#include <iostream>
#include <string>
using namespace std;

int main() {
    int n = 5;
    string name = "Ayan\n";
    cout << string().insert(0, n, '\n').replace(0, 0, n * 5, ' '); // Not elegant — so recursion preferred.
}
