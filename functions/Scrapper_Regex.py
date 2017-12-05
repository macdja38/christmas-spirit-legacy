import re


def try_join(client, msg, channel):
    joined = 0
    linked = 0
    if "discord.gg" in msg or "discordapp" in msg:
        invites = re.findall("(discord(\.gg|app\.com\/invite)\/([\w]{16}|([\w]+-?){3}))",msg)
        print(invites)
        for s in invites:
            linked += 1
            print(s)
            if client.accept_invite("https://discord.gg/" + s[2]):
                joined += 1
    if joined > 0:
        client.send_message(channel, "I Joined " + str(joined) + "/" + str(linked) + " Channels, Thanks for helping spread the christmas Spirit!")
        print("I Joined " + str(joined) + "/" + str(linked) + " Channels, Thanks for helping spread the christmas Spirit!")
    return joined
    """(http(s)?:\/\/discord(\.gg|app\.com\/invite)\/([\w]{16}|([\w]+-?){3}))"""
