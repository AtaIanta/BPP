import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Zalogowano jako', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'czy':
            await message.channel.send('tak')

client = MyClient()
client.run('')