
import random

print("🎯 به بازی حدس عدد خوش اومدی!")
print("من یه عدد بین 1 تا 100 انتخاب کردم، حدس بزن چی هست 😎")

# عدد تصادفی
number = random.randint(1, 100)
guess = None
tries = 0

while guess != number:
    try:
        guess = int(input("عددتو وارد کن: "))
        tries += 1

        if guess < number:
            print("برو بالاتر ⬆️")
        elif guess > number:
            print("برو پایین‌تر ⬇️")
        else:
            print(f"آفرین 🎉 درست حدس زدی! عدد {number} بود.")
            print(f"تعداد تلاش‌هات: {tries}")
    except ValueError:
        print("فقط عدد وارد کن!")

print("پایان بازی 👋")