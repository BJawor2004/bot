import math
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Zalogowano jako {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!hej":
        await message.channel.send("Hej! Jak mogę pomóc?")

    if message.content.startswith("!usun"):
        try:
            liczba = int(message.content.split()[1])
            deleted = await message.channel.purge(limit=liczba + 1)
            await message.channel.send(f"Usunięto {len(deleted)-1} wiadomości!", delete_after=5)
        except (IndexError, ValueError):
            await message.channel.send("Użycie: !usun <liczba>", delete_after=5)
    if message.content == "!grafik":
        await message.channel.send("Poniedziałek: 8:00 - 15:30")
        await message.channel.send("Wtorek: 9:30 - 16:00")
        await message.channel.send("Środa: 7:30 - 15:00")
        await message.channel.send("Czwartek: 10:00 - 17:00")

    if message.content == "!dodaj":
        await message.channel.send("Podaj pierwszą liczbę: ")

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg1 = await client.wait_for("message", check=check, timeout=30)
            a = float(msg1.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        await message.channel.send("Podaj drugą liczbę: ")

        try:
            msg2 = await client.wait_for("message", check=check, timeout=30)
            b = float(msg2.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        result = a+b
        await message.channel.send(f"Wynik: {result}")

    if message.content == "!odejmij":
        await message.channel.send("Podaj pierwszą liczbę:")

        def check1(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg1 = await client.wait_for("message", check=check1, timeout=30)
            a1 = float(msg1.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        await message.channel.send("Podaj drugą liczbę:")

        try:
            msg2 = await client.wait_for("message", check=check1, timeout=30)
            b1 = float(msg2.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        result1 = a1 - b1
        await message.channel.send(f"Wynik: {result1}")

    if message.content == "!pomnoz":
        await message.channel.send("Podaj pierwszą liczbę:")

        def check2(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg3 = await client.wait_for("message", check=check2, timeout=30)
            a2 = float(msg3.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        await message.channel.send("Podaj drugą liczbę:")

        try:
            msg4 = await client.wait_for("message", check=check2, timeout=30)
            b2 = float(msg4.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        result2 = a2 * b2
        await message.channel.send(f"Wynik: {result2}")

    if message.content == "!podziel":
        await message.channel.send("Podaj pierwszą liczbę:")

        def check3(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg5 = await client.wait_for("message", check=check3, timeout=30)
            a3 = float(msg5.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        await message.channel.send("Podaj drugą liczbę:")

        try:
            msg6 = await client.wait_for("message", check=check3, timeout=30)
            b3 = float(msg6.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        if b3 == 0:
            return await message.channel.send("BŁĄD: dzielenie przez zero")

        result3 = a3 / b3
        await message.channel.send(f"Wynik: {result3}")

    if message.content == "!wyczysc":
        if not message.author.guild_permissions.manage_messages:
            return await message.channel.send("Nie masz uprawnień do usuwania wiadomości.")

        await message.channel.send("Czyszczenie kanału...")

        while True:
            deleted = await message.channel.purge(limit=100)
            if len(deleted) == 0:
                break

        await message.channel.send("Kanał został wyczyszczony!", delete_after=5)

    if message.content == "!potega":
        await message.channel.send("Podaj podstawę: ")
        def pot(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg7 = await client.wait_for("message", check=pot, timeout=30)
            p = float(msg7.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")

        await message.channel.send("Podaj wykładnik: ")
        try:
            msg8 = await client.wait_for("message", check=pot, timeout=30)
            q = float(msg8.content)
        except:
            return await message.channel.send("Przekroczono czas lub podano zły format liczby")
        result4 = pow(p,q)
        await message.channel.send(f"Wynik: {result4}")

    if message.content == "!kwadratowy":
        await message.channel.send("Podaj liczbę: ")
        def pierw(a):
            return a.author == message.author and a.channel == message.channel

        try:
            msg9 = await client.wait_for("message", check=pierw, timeout=30)
            x = float(msg9.content)
        except:
            return await message.channel.send("Przekroczono limit czasu lub podano zły format liczby")

        if x < 0:
            return await message.channel.send("BŁĄD: liczba ujemma pod pierwiastkiem rzeczywistym")
        result5 = math.sqrt(x)
        await message.channel.send(f"Wynik: {result5}")

    if message.content == "!kwadrat":
        await message.channel.send("Podaj liczbę: ")
        def square(a):
            return a.author == message.author and a.channel == message.channel

        try:
            msg10 = await client.wait_for("message", check=square, timeout=30)
            x = float(msg10.content)
        except:
            return await message.channel.send("Przekroczono limit czasu lub podano zły format liczby")
        result = pow(x,2)
        await message.channel.send(f"Kwadrat liczby {x} to: {result}")

    if message.content == "!dwojka":
        await message.channel.send("Podaj potęgę: ")
        def two(a):
            return a.author == message.author and a.channel == message.channel

        try:
            msg11 = await client.wait_for("message", check=two, timeout=30)
            x = float(msg11.content)
        except:
            return await message.channel.send("Przekroczono limit czasu lub podano zły format liczby")
        result = pow(2,x)
        await message.channel.send(f"{x} potęga dwójki to: {result}")

    if message.content == "!silnia":
        await message.channel.send("Podaj liczbę: ")
        def fact(a):
            return a.author == message.author and a.channel == message.channel

        try:
            msg12 = await client.wait_for("message", check=fact, timeout=30)
            x = int(msg12.content)
        except:
            return await message.channel.send("Przekroczono limit czasu lub podano zły format liczby")
        if x < 0:
            return await message.channel.send("BŁĄD: silnia z liczby z ujemnej")
        result = math.factorial(x)
        await message.channel.send(f"Silnia liczby {x} to: {result}")

    if message.content == "!newton":
        await message.channel.send("Dwumian Newtona składa się z dwóch liczb: n oraz k.")
        await message.channel.send("Podaj najpierw n, a potem k.")

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg_n = await client.wait_for("message", check=check, timeout=30)
            n = int(msg_n.content)
        except:
            return await message.channel.send("Przekroczono limit czasu lub podano zły format liczby")

        try:
            msg_k = await client.wait_for("message", check=check, timeout=30)
            k = int(msg_k.content)
        except:
            return await message.channel.send("Przekroczono limit czasu lub podano zły format liczby")

        if n < 0 or k < 0:
            return await message.channel.send("BŁĄD: jedna z liczb jest ujemna")

        if k > n:
            return await message.channel.send("BŁĄD: k nie może być większe od n")

        result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        await message.channel.send(f"Dwumian Newtona dla liczb {n} oraz {k} to: {result}")

client.run("TOKEN")
