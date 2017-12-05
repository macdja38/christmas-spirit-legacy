import discord
import os
import sys
sys.path.append(os.path.dirname(__file__) + "/functions")
import Scrapper_Regex as Scrapper
import Hatify

client = discord.Client()
client.login('email', 'password')


@client.event
def on_message(message):
    lower_case = message.content.lower()
    if message.author.id == client.user.id:
        return 0
    if message.content.startswith('!!officialservernumber'):
        client.send_message(message.channel, "Currently spreading christmas cheer to **" +
                            str(len(set((user.id for server in client.servers for user in server.members)))) +
                            "** users across **" + str(sum([len(s.channels) for s in client.servers])) +
                            "** channels in **" + str(len(client.servers)) + "** servers.")
    if (client.user in message.mentions or lower_case.startswith('!!hat')) and not message.author.id ==\
            "85257659694993408":
        client.send_message(message.author, "Your Avatar is being prepared.")
        Hatify.hatme(message.author).save("temp.jpg")
        client.send_file(message.author, "temp.jpg")
        client.send_message(message.author, "Thank you for Supporting Christmas Spirit everywhere!\n" +
                            "If you want to spread the Christmas Spirit simply paste links where I can see them.\n" +
                            "If you want to place your hat yourself, " +
                            "please join https://discord.gg/0fNfubYk62MIbRAh\n" +
                            "and type !xmas")
        '''client.send_file(message.channel, "hat.png")'''
    if message.author.id == "85257659694993408" and lower_case.startswith('!!hat') and len(message.mentions) > 0:
        client.send_message(message.channel, "Your Avatar is being prepared.")
        Hatify.hatme(message.mentions[0]).save("temp.jpg")
        client.send_file(message.channel, "temp.jpg")
        client.send_message(message.channel, "``` Thank you for Supporting Christmas Spirit everywhere!\n" +
                            " If you want to spread the Christmas Spirit simply paste links where I can see them.\n```")
    if ("info" in lower_case or "hello" in lower_case or "hi" in lower_case or "help" in lower_case) and\
            message.channel.is_private:
        client.send_message(message.channel, "Hi, I'm Christmas Spirit, type !!hat to get your hat and an explanation")
    Scrapper.try_join(client, message.content, message.channel)


@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
