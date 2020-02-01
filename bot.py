import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Zalogowano jako', self.user)

    async def on_message(self, message):
        
        # żeby bot nie odpowiadł samemu sobie
        if message.author == self.user:
            return
       
        #statystyki
        elif  message.content.startswith('$stats'):
            url = 'https://bnonews.com/index.php/2020/01/the-latest-coronavirus-cases/' 
            path = '//*[@id="mvp-content-main"]/table[1]/tbody/tr[33]/td[2]/strong'
            path2 = '//*[@id="mvp-content-main"]/table[1]/tbody/tr[33]/td[3]/strong'
            path3 = '//*[@id="mvp-content-main"]/table[1]/tbody/tr[33]/td[4]/strong/text()[3]'
            path4 = '//*//*[@id="mvp-content-main"]/table[3]/tbody/tr[25]/td[2]/strong'
            response = requests.get(url) 
            byte_data = response.content 
            source_code = html.fromstring(byte_data)  
            tree = source_code.xpath(path) + source_code.xpath(path2) + source_code.xpath(path3) + source_code.xpath(path4)
            await message.channel.send('```☢ Chiny: '+tree[0].text_content() + ' chorych | ' +tree[2].replace(" suspected","") + ' podejrzanych | ' + tree[1].text_content() + ' nie żyje '+ '\n' + '☢ Poza Chinami zarażonych jest '+ tree[3].text_content() + ' osób```') 

        #najnowsze informacje o nowych przypadkach
        elif  message.content.startswith('$news'):
            url = 'https://bnonews.com/index.php/2020/01/the-latest-coronavirus-cases/' 
            path = '//*[@id="mvp-content-main"]/ul[2]/li[1]'
            path1 = '//*[@id="mvp-content-main"]/ul[2]/li[2]'
            path2 = '//*[@id="mvp-content-main"]/ul[2]/li[3]'
            path3 = '//*[@id="mvp-content-main"]/ul[2]/li[4]'
            path4 = '//*[@id="mvp-content-main"]/ul[2]/li[5]'
            response = requests.get(url) 
            byte_data = response.content 
            source_code = html.fromstring(byte_data)  
            tree = source_code.xpath(path) + source_code.xpath(path1) + source_code.xpath(path2) + source_code.xpath(path3) + source_code.xpath(path4)
            await message.channel.send('```☢ Ostatnie przypadki: \n' + tree[0].text_content() + '\n' + tree[1].text_content() + '\n' + tree[2].text_content() + '\n' + tree[3].text_content() + '\n' + tree[4].text_content() + '```') 

        #8ball
        elif (message.content.startswith('Czy') or message.content.startswith('czy')) and message.channel.id == 660169524116717569:
            lista = ['Tak', 'Nie', 'Może', 'Zależy jak uważasz', 'Jeszcze jak', 'Nigdy w życiu','Twoja stara','ruchasz psa jak sra','Jak najbardziej','Możliwe że tak', 'Może nie','Nie wiem']
            await message.channel.send(random.choice(lista))

client = MyClient()
client.run('$token')
