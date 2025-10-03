from Task_1 import grams_to_ounces, sphere_volume, filter_prime # type: ignore
from Task_3 import Account # type: ignore

print(grams_to_ounces(100))   # проверка
print(sphere_volume(5))       # проверка
print(filter_prime([1,2,3,4,5,11,15]))

acc = Account("KBTU", 1000)
acc.deposit(200)
acc.withdraw(1500)
