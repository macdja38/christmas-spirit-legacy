def try_join(client, msg, channel):
    joined = 0
    linked = 0
    if "discord.gg" in msg or "discordapp.gg/invite" in msg:
        msg = msg.replace("http://", "https ://").replace("https://", " https://").replace("\""," ")
        msg.replace
        for s in msg.rsplit(" "):
            if "discord.gg" in s:
                linked += 1
                if client.accept_invite(s):
                    joined += 1
        client.send_message(channel, "I Joined " + str(joined) + "/" + str(linked) + " Channels, Thanks for helping spread the christmas Spirit!")
    return joined
"""(http(s)?:\/\/discord(\.gg|app\.com\/invite)\/([\w]{16}|([\w]+-?){3}))"""
