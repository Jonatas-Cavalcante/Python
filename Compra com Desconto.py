val_uso = float(input("Digite o valor da compra: "))



if val_uso < 100:
    val_desconto = val_uso * 0.05
    val_total = val_uso - val_desconto
    print(f"Desconto de: {val_desconto}")
    print(f"Valor da compra com desconto: {val_total}")

elif val_uso >= 100 <= 199:
        val_desconto = val_uso * 0.1
        val_total = val_uso - val_desconto
        print(f"Desconto de: {val_desconto}")
        print(f"Valor da compra com desconto: {val_total}")

elif val_uso >= 200:
        val_desconto = val_uso * 0.2
        val_total = val_uso - val_desconto
        print(f"Desconto de: {val_desconto}")
        print(f"Valor da compra com desconto: {val_total}")