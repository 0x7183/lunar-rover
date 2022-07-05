from discord.embeds import Embed

descriptions = ["Mnh.... user {} is definitely sus", "{} is the hero that Terra deserves, but not the one it needs right now", "I think that {} faked a task", "I saw {} near the corpse", "{} killed Blue, trust me!" "{} just came out from electrical"]
class CustomEmbed(Embed):
    def init(self, title: str = "", description: str = ""):
        super().init(title=title, description = description, color=0xFF5733)
        
    
    
        
def answer_embed(answer, title):

    # description = random.choice(descriptions)
    embed = CustomEmbed(title=title, description = answer)
    embed.set_footer(text='Created by 7183')
    
    #embed.set_thumbnail(url="attachment://sus.jpg")
    return embed

    
def bot_embed(args, action):

    embed = CustomEmbed()
    embed.add_field(name = action, value=args, inline = False)
    embed.set_footer(text='Created by 7183')
 
    return embed

def show_all(queue, type):
    embed = CustomEmbed()

   
    if len(queue) == 0:
        embed.add_field(name='Info', value='The queue is empty')
    else:
        embed.set_author(name=type)
        embed.add_field(name='\u200b', value = queue, inline=True)
        embed.set_footer(text='Created by 7183')
            
    return embed