import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ambiente(ctx):
    await ctx.send(
        "*🌍 Cuidemos el ambiente - Elige una opción:*\n\n"
        "*1* - Reducir basura\n"
        "*2* - Ahorrar agua y energía\n"
        "*3* - Cuidar plantas y animales\n\n"
        "Escribe *1, 2 o 3* aquí en el chat"
    )

    # Esperar a que el mismo usuario responda 1, 2 o 3
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content in ["1", "2", "3"]

    try:
        msg = await bot.wait_for("message", check=check, timeout=30.0)

        if msg.content == "1":
            await ctx.send("♻️ *CONSEJO 1 - Reducir basura:*\n- Usa bolsa de tela, no de plástico\n- Recicla papel, vidrio y plástico\n- No tires basura en la calle")
        elif msg.content == "2":
            await ctx.send("💧 *CONSEJO 2 - Ahorrar agua y energía:*\n- Cierra la canilla mientras te cepillas\n- Apaga las luces que no uses\n- Desconecta los cargadores")
        elif msg.content == "3":
            await ctx.send("🌱 *CONSEJO 3 - Plantas y animales:*\n- Planta un árbol o una plantita\n- No maltrates animales\n- No arranques flores de parques")

    except:
        await ctx.send("Se acabó el tiempo, vuelve a escribir $ambiente")

bot.run("MTU1NTU5NTMyMDE5OTc0NTYyNg.GiUXfG.kOx5FYiiL9XhstS6PzzMi856ayBTLC6PsoLkRE")