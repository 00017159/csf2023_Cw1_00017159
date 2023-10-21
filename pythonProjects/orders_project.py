print("Buyurtma qabul qiling!!!")
print("Bizdan nima xarid qilmoqcisiz? ")
b_o = []
n = 1

while True:
    buyurtma = f"{n}-xarid qilmoqchi bo'lgan narsangiz?: "
    buyurtma = f"Xarid qilmoqchi bo'lgan narsangiz?: "
    b = input(buyurtma)
    b_o.append(b)

    javob = input("Yana biror narsa xarid qilishni xohlaysizmi (ha/yoq)? ")
    n += 1
    if javob == "yoq":
        break

print("Buyurtma qilingan ovqatlar:")
for i in b_o:
   print(i.title())