from customer import Customer
from item import Item
from seller import Seller
from wallet import __init__

seller = Seller("DICストア")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Tarjeta Madre", 28980, seller)
    Item("Unidad de fuente de alimentación", 8980, seller)
    Item("Caja de la computadora", 8727, seller)
    Item("Disco duro de 3.5'", 10980, seller)
    Item("SSD de 2,5 pulgadas", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("Cooler de CPU", 13400, seller)
    Item("Tablero Gráfico", 23800, seller)

print("🤖 Porfavor dime tu nombre")
customer = Customer(input())

print("🏧 Por favor ingrese el monto a cargar en la billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Empieza a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de Productos")
    seller.show_items()

    print("️️⛏ Por favor, ingrese el número del producto")
    number = int(input())

    print("⛏ Por favor, ingrese la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Cantidad Total: {customer.cart.total_amount()}")

    print("😭 Terminar de comprar?(yes/no)")
    end_shopping = input() == "yes"

print("💸 Confirmar la compra?(yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ Propuedad de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo en la cartera de {customer.name}: {customer.wallet.balance}")

print(f"📦Disponible de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo en la cartera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Cantidad Total: {customer.cart.total_amount()}")

print("🎉 Fin")