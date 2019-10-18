import discord
import asyncio
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

#Cog = getattr(commands, 'Cog', object)

class Debug(commands.Cog):

    """Debug One Or More Commands, Useful For Beginners Or People Who Want A Quick Debug Link"""

    
    
    def __init__(self, bot):

        self.bot = bot
  
    @commands.group(name="dbug", invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def dbug(self, ctx):
        """Send Debug Links Directly To Hastebin In Much Shorter Time Than Normal, Useful For People That Dont Know As Much About ModMail"""

        await ctx.send_help(ctx.command)
        
   
    @dbug.command(name="start")
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def start(self, ctx):
        """Start A Debug Session, Do As The Bot Says, And Then It Will Work Perfectly"""
        
        timer = 15

        await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"Process Started, Deleting Cached Logs"
        ))
        
        await asyncio.sleep(0.5)
        
        await ctx.invoke(self.bot.get_command("debug wipe"))
        
        await asyncio.sleep(0.3)
        
        msg = await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"Timer Starting In 3 Seconds, You Have 15 Seconds To Do The Command That Doesnt Work And Then You Will Get A Debug Link"
        ))
        
        await asyncio.sleep(3)
         
        msg = await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"{timer} Seconds Back, Do The Command Now"
        ))
        
        for i in range(timer):
            for i in range(10):
                await asyncio.sleep(0.1)
                
            timer = timer-1
            await msg.edit(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"{timer} Seconds Back, Do The Command Now"
            ))
        
        msg = await ctx.send(embed=discord.Embed(
            color=discord.Color.blurple(),
            description=f"Done, Your Hastebin Link Is Coming Now, While You Wait For It, Remeber To :star: The [Repo](https://github.com/kyb3r/modmail) If You Havent Done Already"
        ))
        
        await asyncio.sleep(3)
        
        await ctx.invoke(self.bot.get_command("debug hastebin"))

def setup(bot):
    bot.add_cog(Debug(bot))
