import discord
from discord.ext import commands



from customEmbeds import *
from faq import Faq

intents = discord.Intents.default()

TOKEN = "Insert your token here"

bot = commands.Bot(command_prefix='!chatbot ', intents = intents)
slash = SlashCommand(bot, sync_commands=True)

faq = Faq()


# Change this with your bot_id, and channel id of commands and listener
command_id = 983359798223462470
listen_id = 983726376903409714
bot_id = 987288906523349023


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event 
async def on_message(message):
    if message.channel.id == listen_id and message.author.id != bot_id:
        # Get channel id
        channel = bot.get_channel(listen_id)
        # Get answer
        title, answer = faq.get_answer(message.content)
        # Compile embed
        embed = answer_embed(answer, title)
        # Send msg
        await channel.send(embed = embed)

    await bot.process_commands(message)
        

@bot.command(name='addfaq')
@commands.has_role('Moderator')
async def add_faq(ctx, *, args):

    if ctx.channel.id == command_id:
        row = args.split('-')
        faq.add_faq(row)
        # set answer and question
        embed = bot_embed(args, "Added faq: ")
        await ctx.send(embed = embed)



@bot.command(name='removefaq')
@commands.has_role('Moderator')
async def remove_faq(ctx, *, args):
    if ctx.channel.id == command_id:
        faq.remove(args)
        embed = bot_embed(args, "Removed faq")
        await ctx.send(embed = embed)


@bot.command(name='list')
@commands.has_role('Moderator')
async def get_data(ctx, *, args):
    if ctx.channel.id == command_id:
        q = faq.get_faq(int(args))
        embed = show_all(q, "Frequenly Asked Questions:")
        await ctx.send(embed = embed)


@bot.command(name='commands')
@commands.has_role('Moderator')
async def help(ctx):
    if ctx.channel.id == command_id:
        commands = "Use `!chatbot addfaq question-answer` to add a faq to the list\nUse `!chatbot removefaq question` to remove a faq from the list\nUse `!chatbot list page` to get a list of the faq (5 per page and they start from 0)"
        embed = show_all(commands, "Avaliable commands:")
        await ctx.send(embed = embed)

bot.run(TOKEN)

