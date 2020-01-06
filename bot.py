import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Zalogowano jako', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'czy':
            lista = ['Tak', 'Nie', 'Może', 'Zależy jak uważasz', 'Jeszcze jak', 'Nigdy w życiu','Twoja stara','ruchasz psa jak sra','Jak najbardziej','Możliwe że tak', 'Może nie','Nie wiem']
            await message.channel.send(random.choice(lista))

client = MyClient()
client.run('')
