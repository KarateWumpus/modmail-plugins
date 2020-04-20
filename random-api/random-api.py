import discord
import asyncio
import json
from discord.ext import commands
from core import checks
from core.models import PermissionLevel


class RandomApi(commands.Cog):
    """This plugin uses https://some-random-api.ml to get a lotta random stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def dog(self, ctx):
        """Get a Dog fact and a Dog image"""
        
        getfact = await self.bot.session.get('https://some-random-api.ml/facts/dog')
        getimg = await self.bot.session.get('https://some-random-api.ml/img/dog')
        
        facttext = await getfact.text()
        imgtext = await getimg.text()
        
        factjson = json.loads(facttext)
        imgjson = json.loads(imgtext)
        
        embed = discord.Embed(title = "Dog", description = factjson["fact"], color = 0x7289da)
        embed.set_image(url=imgjson["link"])
        await ctx.send(embed = embed)


    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def cat(self, ctx):
        """Get a Cat fact and a Cat image"""
        
        getfact = await self.bot.session.get('https://some-random-api.ml/facts/cat')
        getimg = await self.bot.session.get('https://some-random-api.ml/img/cat')
        
        facttext = await getfact.text()
        imgtext = await getimg.text()
        
        factjson = json.loads(facttext)
        imgjson = json.loads(imgtext)
        
        embed = discord.Embed(title = "Cat", description = factjson["fact"], color = 0x7289da)
        embed.set_image(url=imgjson["link"])
        await ctx.send(embed = embed)


    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def fox(self, ctx):
        """Get a Fox fact and a Fox image"""
        
        getfact = await self.bot.session.get('https://some-random-api.ml/facts/fox')
        getimg = await self.bot.session.get('https://some-random-api.ml/img/fox')
        
        facttext = await getfact.text()
        imgtext = await getimg.text()
        
        factjson = json.loads(facttext)
        imgjson = json.loads(imgtext)
        
        embed = discord.Embed(title = "Fox", description = factjson["fact"], color = 0x7289da)
        embed.set_image(url=imgjson["link"])
        await ctx.send(embed = embed)

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def koala(self, ctx):
        """Get a Koala fact and a Koala image"""
        
        getfact = await self.bot.session.get('https://some-random-api.ml/facts/koala')
        getimg = await self.bot.session.get('https://some-random-api.ml/img/koala')
        
        facttext = await getfact.text()
        imgtext = await getimg.text()
        
        factjson = json.loads(facttext)
        imgjson = json.loads(imgtext)
        
        embed = discord.Embed(title = "Koala", description = factjson["fact"], color = 0x7289da)
        embed.set_image(url=imgjson["link"])
        await ctx.send(embed = embed)

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def panda(self, ctx):
        """Get a Panda fact and a Panda image"""
        
        getfact = await self.bot.session.get('https://some-random-api.ml/facts/panda')
        getimg = await self.bot.session.get('https://some-random-api.ml/img/panda')
        
        facttext = await getfact.text()
        imgtext = await getimg.text()
        
        factjson = json.loads(facttext)
        imgjson = json.loads(imgtext)
        
        embed = discord.Embed(title = "Koala", description = factjson["fact"], color = 0x7289da)
        embed.set_image(url=imgjson["link"])
        await ctx.send(embed = embed)

        
def setup(bot):
    bot.add_cog(RandomApi(bot))
