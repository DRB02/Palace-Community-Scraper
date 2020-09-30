def install_dependecies():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord_webhook'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'random'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'time'])

try:
    import requests
    from bs4 import BeautifulSoup
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import random
    import time
except:
    install_dependecies()
    import requests
    from bs4 import BeautifulSoup
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import random
    import time

#unquote which one you need
#WebhookUrl = 'webhook1'
#WebhookUrl = ['webhook1', 'webhook2']

mainsite = requests.get('https://palacedrop.com/droplist')
droplist = BeautifulSoup(mainsite.text,"lxml")
link = droplist.find('div',{'id':'latest'}).a.get('href')
droplist_link = 'https://palacedrop.com' + link

def main():
    r = requests.get(droplist_link)
    soup = BeautifulSoup(r.text,"html.parser")
    cards = soup.find_all('div',{'class':'col-md-3 col-sm-6 col-6'})
    for card in cards:
        item = card.find("div",{"style":"text-align:center;margin-left:10px;margin-right:10px;margin-bottom:6px"}).text
        image = card.find("img",{"style":"height:100%;width:100%;object-fit:cover;position:absolute;top:0;left:0"})["src"]

        webhook = DiscordWebhook(url=WebhookUrl, username='Palace Droplist', avatar_url='https://banner2.cleanpng.com/20180813/vcb/kisspng-logo-brand-palace-skateboards-clothing--5b7141ef9e6801.6434516515341491036488.jpg')
        embed = DiscordEmbed(title='Palace Droplist', color=0xa020f0, url=droplist_link)
        embed.set_image(url=image)
        embed.add_embed_field(name='Item:', value='**'+item+'**')
        embed.set_footer(text='Palace Droplist | Developed by DRB02#0001')
        webhook.add_embed(embed)
        time.sleep(0.5)
        webhook.execute()
        print("| WEBHOOK SENT |")
    else:
        print("End of list reached")

main()
