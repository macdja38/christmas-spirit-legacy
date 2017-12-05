import requests
from bs4 import BeautifulSoup
def vacuum(self, message):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        p = requests.get(message.options[0], headers=headers)
        print(p)
        soup = BeautifulSoup(p.text, 'html.parser')
        links = []
        for link in soup.find_all(href=re.compile('discord.gg')):
            links.append(link['href'])
        i = 0
        for link in links:
            if self.core.accept_invite(link):
                i += 1
        response = '`Joined {} servers !`'.format(str(i))
        self.core.send_message(message.channel, response)