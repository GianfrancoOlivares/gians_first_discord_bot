import discord
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("Hola!")
    elif message.content.startswith('$adios'):
        await message.channel.send(":+1:")
    elif message.content.startswith("$Remoji"):
        await message.channel.send(remoji())
    elif message.content.startswith("$password"):
        await message.channel.send("Su contraseña sera:", gen_pass(10))
    elif message.content.startswith("$randomnum"):
        await message.channel.send("Su numero es:", randomnum())
    elif message.content.startswith("$haz_algo"):
        await message.channel.send(algo())

    else:
        await message.channel.send("lo siento, no se a lo que te refieres. Intente con otro comando", ":confused:")

client.run("MTE0MjQ3MjAxNjI4OTU5NTUwMg.GM6Jdm.VgBYroJhxlNItA_ph6NNTlTb7ft29sh38lVRWA")