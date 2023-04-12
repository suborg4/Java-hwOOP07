from HW.model.vending_machine.VendingMachine import VendingMachine
from HW.model.products.BottleOfWater import BottleOfWater
from HW.model.products.HotDrinks import HotDrinks
from HW.UI.UIConsole import UIConsole

class Service:

    def start(self):
        console = UIConsole()
        list_hot_drinks = [HotDrinks('Кофе', 300, 0.4, 80),
                           HotDrinks('Чай', 150, 0.44, 85),
                           HotDrinks('Руссиано', 200, 0.6, 70)]
        list_bottle_of_water = [BottleOfWater('Cola', 400, 0.4),
                                BottleOfWater('Sprite', 250, 0.5),
                                BottleOfWater('Fanta', 180, 0.5)]
        vending_machine1 = VendingMachine()
        vending_machine2 = VendingMachine()
        console.print_message('Добавление горячих напитков')
        vending_machine1.list_products = list_hot_drinks
        console.print_list_product(vending_machine1.list_products)
        console.print_message('Добавление холодных напитков')
        vending_machine2.list_products = list_bottle_of_water
        console.print_list_product(vending_machine2.list_products)
        console.print_message('Добавление Глинтвейна')
        vending_machine1.add_at_list(HotDrinks('Глинтвейн', 300, 0.8, 65))
        console.print_list_product(vending_machine1.list_products)
        console.print_message('Добавление Лимонада')
        vending_machine2.add_at_list(BottleOfWater('Лимонад', 150, 0.8))
        console.print_list_product(vending_machine2.list_products)
        console.print_message('Выдача чая')
        console.print_message(vending_machine1.get_product('Чай'))
        console.print_message('Выдача Sprite')
        console.print_message(vending_machine2.get_product('Sprite'))