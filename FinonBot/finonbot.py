import sqlite3
import os
import disnake as discord
from disnake.ext import commands
import lists
import time

embedColor = 0x520500

premium = []
developers = []

token = "ТОКЕН"

client = commands.Bot(command_prefix=discord.ext.commands.when_mentioned)

def antispam_off_a():
	pass

def antispam_on_a():
	pass


@client.event
async def on_ready():
	print(f'[FinonBot] Работает на аккаунте {client.user.name}#{client.user.discriminator}')

@client.command()
async def ping(ctx):
	start = time.time()
	await ctx.send("Измерение...")
	end = time.time()
	ping = "{0:.2f}".format(end - start)
	await ctx.send(f"Пинг: {ping} ms")

@client.command()
async def бот(ctx):
	await ctx.send("Привет! Это бот у Nikon#5259, Сервер:https://discord.gg/8k9wbbEMYT. В проекте помогал:Honak#1010, zxcdez#6666, GidesPC#7777")


@client.command()
async def say(ctx, *, text:str):
    await ctx.send(text)

# vc commands
@client.slash_command(description="Зайти в голосовой канал")
async def join_voice(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	channel = ctx.author.voice.channel

	if voice and voice.is_connected():
		await voice.move_to(channel)
	else:
		voice = await channel.connect()
		await ctx.send("Я подключился к голосовому каналу", ephemeral=True)
		print(f'[join_voice] [{ctx.author.name} ({ctx.author.id})] Я подключился к голосовому каналу')

@client.slash_command(description="Выйти из голосового канала")
async def leave_voice(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	channel = ctx.author.voice.channel

	if voice and voice.is_connected():
		await voice.disconnect()
		await ctx.send("Я отключился от голосового канала", ephemeral=True)
	else:
		voice = await channel.disconnect()
		await ctx.send("Я отключился от голосового канала", ephemeral=True)

	print(f'[join_voice] [{ctx.author.name} ({ctx.author.id})] Я отключился от голосового канала')

# Nikon commands
@client.slash_command(description="Установит канал приветствия.")
async def welcomechannel(inter, channel:discord.TextChannel=None):
			if inter.author.guild_permissions.administrator:
				db = sqlite3.connect('main.sqlite')
				cursor = db.cursor()
				cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = '{inter.guild.id}'")
				result =  cursor.fetchone()
				if not channel:
					embed=discord.Embed(title='❌ | Ошибка', description='Укажите канал для приветствия',color=embedColor)
					await inter.response.send_message(embed=embed, ephemeral=True)
					return
				else:
					if result is None:
						sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
						val = (inter.guild.id, channel.id)
						embed = discord.Embed(title = '✅ | Канал для приветствия успешно настроен',description=f'Канал настроен до {channel.mention}', color=embedColor)
						await inter.response.send_message(embed=embed, ephemeral=True)
					elif result is not None:
						sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
						val = (channel.id, inter.guild.id)
						embed = discord.Embed(title = '✅ | Канал для приветствия успешно изменен',description=f'Канал изменен до {channel.mention}', color=embedColor)
						await inter.response.send_message(embed=embed, ephemeral=True)
					cursor.execute(sql, val)
					db.commit()
					cursor.close()
					db.close()
					return
			else:
				embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=embedColor)
				await inter.response.send_message(embed=embed)
			print(f"[welcomechannel] [{inter.author} ({inter.author.id})], Сервер: {inter.guild}")	

@client.event
async def on_member_remove(member):
    channel = client.get_channel(989039321287905280)
    userAvatarUrl = member.avatar.url
    embed = discord.Embed(description = f'Пока {member.mention} будем ждать возвращения на сервер {channel.guild.name}. У нас сейчас {len(channel.guild.members)} участников.', color=0x00008b)
    embed.set_image(url = userAvatarUrl)
    await channel.send(embed = embed)

@client.slash_command(description="Статистика бота.")
async def stat(inter):
	file = open('mainclient.py', 'r', encoding = 'utf-8')
	numln = 0
	for line in file:
		numln += 1
		embed = discord.Embed(title="Статистика Finonclient", color=0xFF0000)
		embed.add_field(name = "Серверов", value = len(client.guilds))
		embed.add_field(name = "Пользователей", value = len(set(client.get_all_members())))
		embed.add_field(name = "Каналов", value = len(set(client.get_all_channels())))
		embed.add_field(name = "Голосовых соединений", value = len(client.voice_clients))
		embed.add_field(name = "Задержка", value = f"{(round(client.latency, 2))} секунд")
		embed.add_field(name = "Количество строк кода", value = numln)
		embed.add_field(name = "Задержка", value = f"{(round(client.latency, 2))} секунд")
		embed.add_field(name = "Задержка", value = f"{(round(client.latency, 2))} секунд")
		embed.add_field(name = "Задержка", value = f"{(round(client.latency, 2))} секунд")
		embed.add_field(name = "Задержка", value = f"{(round(client.latency, 2))} секунд")
		embed.add_field(name = "Задержка", value = f"{(round(client.latency, 2))} секунд")
		await inter.response.send_message(embed=embed)

@client.event
async def on_guild_join(guild):
    await client.change_presence(status=discord.Status.dnd,activity=discord.Game(name=f'/help | Серверов: {len(client.guilds)}'))
    channel = client.get_channel(989039321287905280)
    await channel.send(embed = discord.Embed(title="Меня добавили на новый сервер!", description=f"""
ID: {guild.id}
Название: {guild.name}
Владелец: {guild.owner.mention}
Участников: {guild.members}

Всего серверов у бота сейчас: {len(client.guilds)}
""", color=discord.Color.green()))

@client.slash_command(description="Часто задаваемые вопросы по боте.")
async def faq(inter):
	cpage = discord.Embed(
		title = '''FAQ''',
		description = f"""
		**Почему бот не работает?**
		- Потому возможно вы находитесь в чс, хост не работает и нету некоторые права для бота.

		**Почему бот крашнул сервер?**
		- Возможно владельца бота взломали и получили токен Finonclient.

		**Статус**
		Вы в чёрный список попали: **нет**
		Пинг бота: {(round(client.latency, 2))} секунд.
		""", 
		color=0xFF0000
	)

	buttons = discord.ui.View()
	buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.red, custom_id="no",label='Поддержка Finonclient', emoji=":slight_smile:"))
	await inter.send(embed=cpage, view=buttons)
	print(f"Команда faq, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")    

	cpage = discord.Embed(
	title = '''FAQ''',
	description = f"""
	**Почему бот не работает?**
	- Потому возможно вы находитесь в чс, хост не работает и нету некоторые права для бота.

	**Почему бот крашнул сервер?**
	- Возможно владельца бота взломали и получили токен Finonclient.

	**Статус**
	Вы в чёрный список попали: **да**
	Пинг бота: {(round(client.latency, 2))} секунд.
	""", 
	color=0xFF0000)
	buttons = discord.ui.View()
	buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.red, custom_id="no",label='Поддержка Finonclient', emoji=":slight_smile:"))
	await inter.send(embed=cpage, view=buttons)
	print(f"Команда faq, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")    

@client.slash_command(description="FinonPremium описание.")
async def finonpremium(ctx):
    if ctx.author.id not in premium:
        cpage = discord.Embed(
            title = f'FinonPremium',
            description = f"""
			Это Finonclient который улучшенный, будут много команд и другое.

			У вас есть премиум? Нет
			""", 
            color=0xFF0000
		)
    else:
        cpage1 = discord.Embed(
            title = f'FinonPremium',
            description = f"""
			Это Finonclient который улучшенный, будут много команд и другое.

			У вас есть премиум? Да
			""", 
            color=0xFF0000
        )    
        await ctx.send(embed=cpage1)
        await ctx.send(embed=cpage)

class report(discord.ui.Modal):
    async def __init__(self):
        components = [discord.ui.TextInput(
                                        label="Репорт",
                                        placeholder="Сообщите о баги.",
                                        custom_id="name",
                                        max_length=25 #максимальное колво символов
                                        )
                    ]
        super().__init__(title="Введите текст.", components=components)
    async def callback(self, inter: discord.ModalInteraction):
        for key, value in inter.text_values.items():pass
        finontest = client.get_channel(983662140634312705)
        await finontest.send(f'Вызвал ошибку: {inter.author}, Сервер: {inter.guild}, | Ошибка: {value}')
        pass
# @client.slash_command()
# async def report2(ctx):
#     await ctx.response.send_modal(modal=report())

# 	#имя для слеш команды анти спама
# 	asn = 'antispam'
# 	#описание для слеш команды анти спама
# 	asd = 'влияет на удаление флуда(или же по другому спама)'

# 	aon = ['вкл', 'Вкл', 'ВКЛ', 'включить', 'Включить', 'ВКЛЮЧИТЬ', 'on', 'On', 'ON', 'он', 'Он', 'ОН', 'подошла_сюда']

# 	aoff = ['выкл', 'Выкл', 'ВЫКЛ', 'выключить',  'Выключить', 'ВЫКЛЮЧИТЬ', 'off', 'Off', 'OFF', 'of', 'Of', 'OF', 'офф', 'Офф', 'ОФФ', 'пошла_нахуй']

# 	ArgNumAntispamS = discord.SlashOption(name="число", description="сколько нужно одинаковых сообщений чтобы бот посчитал их за флуд?", min_value=4, max_value=30)
# 	ArgAction2AntispamS = discord.SlashOption(name="действие", description="что требуется сделать при нахождении флуда?", choices=["удалить сообщения", "забанить", "кикнуть", "замутить"])
# 	ArgTimeAntispamS = discord.SlashOption(name="время", description="укажите время мута пользователя в секундах (по умолчанию 60 секунд)", default=60)

# 	argsec = discord.SlashOption(name='действие', description='Выберите что нужно сделать (вкл/выкл)', choices=['вкл', 'выкл'])

@client.slash_command(description="Нашли баг? Сообщайте здесь!")
async def report(ctx, *, описание: str):
    finontest = client.get_channel(983662140634312705)
    cpage = discord.Embed(
            title = 'Вызвал ошибку: {ctx.author}, Сервер: {ctx.guild}.',
            description = f"""
Ошибка: {описание}
""", 
            color=0xFF0000
        )
    await ctx.send('Отправлено! За рофл-баги блокирование report!')
    await finontest.send(embed=cpage)

#слеш команда анти инвайта
# @client.slash_command(name=asn, description=asd)
# async def anti_spam(inter, action=argsec, action2=ArgAction2AntispamS, number:int=ArgNumAntispamS, time=ArgTimeAntispamS):
# 	if not inter.author.guild_permissions.administrator:
# 		Embed = discord.Embed(title=':x: | Ошибка', description = 'У вас недостаточно прав, нужные права: `админ`', color=discord.Color.red())
# 		await inter.response.send_message(embed = Embed)
# 		return
# 	if inter.user.guild_permissions.administrator==False:
# 		return await inter.send('У вас недостаточно прав для вызова этой команды', ephemeral=True)
# 	if action in aon:
# 		r = await antispam_on_a(ctx=inter, action=action2, number=number, time=time)
# 	elif action in aoff:
# 		r = await antispam_off_a(ctx=inter)
# 	await inter.send(r)    
# 	inter.guild.owner.send(embed=discord.Embed(
# 			title=f'🔒 | Сервер {member.guild.name} был защищен',
# 			description=f'Был кикнут краш бот с именем {member.mention} ({member.name}) (`{member.id}`)\nЧеловек который добавил краш бота: {member1.mention} ({member1.name}) (`{member1.id}`), забанен ли?: {succes}',
# 			color=discord.Color.green()))

# 			await logs.send(embed=discord.Embed(
# 			title=f'🔒 | Сервер {member.guild.name} был защищен',
# 			description=f'Был кикнут краш бот с именем {member.mention} ({member.name}) (`{member.id}`)\nЧеловек который добавил краш бота: {member1.mention} ({member1.name}) (`{member1.id}`), забанен ли?: {succes}',
# 			color=discord.Color.green()))
# 		elif member.id in lists.notactiveortest:
# 			entry = await member.guild.audit_logs(action=discord.AuditLogAction.client_add, limit=1).get()
# 			member2 = await member.guild.fetch_member(entry.user.id)
# 			await member2.send(embed=discord.Embed(
# 			title=f'⚠ | Бот {member} (`{member.id}`) является тестовым или редко включен.',
# 			description=f'От {member.mention} возможно нет смысла.',
# 			color=discord.Color.dark_orange()))

# 			embed = discord.Embed(title=f'На сервере {member.guild} обнаружен тестовый или редко включащийся бот.', description=f'**Бот:** {member.mention}\n**ID** `{member.id}`\n**Ник** {member}', color=discord.Color.orange())
# 			await logs.send(embed=embed)
# 		elif member.id in lists.whitelisted or member.id in lists.serveronly:
# 			embed = discord.Embed(title=f'Безопасный бот на севрере {member.guild}.', description=f'**Бот:** {member.mention}\n**ID** `{member.id}`\n**Ник** {member}', color=discord.Color.green())
# 			await logs.send(embed=embed)				
# 		elif member.id not in lists.crashclients and member.id not in lists.notactiveortest and member.id not in lists.serveronly and member.id not in lists.whitelisted:
# 			embed = discord.Embed(title='Неизвестный бот!', description=f'Сервер: {member.guild.name}\nБот: {member.mention} **{member}** `{member.id}`\nРазрабы проверьте бота.\nИнвайт: **https://discord.com/api/oauth2/authorize?client_id={member.id}&permissions=8&scope=client%20applications.commands**', color=discord.Color.og_blurple())
# 			await nikon.send(embed=embed)
# 			await logs.send(embed=embed)

@client.slash_command(description="Установит текст приветствия.")
async def welcometext(inter, * , text):
		if inter.author.guild_permissions.administrator:
			db = sqlite3.connect('main.sqlite')
			cursor = db.cursor()
			cursor.execute(f"SELECT msg FROM main WHERE guild_id = {inter.guild.id}")
			result =  cursor.fetchone()
			if not text:
				embed=discord.Embed(title='❌ | Ошибка', description='Укажите текст для приветствия',color=embedColor)
				await inter.response.send_message(embed=embed)
				return
			else: # Го музычку не знаю, я пробовал не получилось(
				if result is None:
					sql = ("INSERT INTO main(guild_id, msg) VALUES(?,?)")
					val = (inter.guild.id, text)
					embed = discord.Embed(title = '✅ | Текст для приветствия успешно создан',description = f"`{text}`", color=embedColor)
					await inter.response.send_message(embed=embed)
				elif result is not None:
					sql = ("UPDATE main SET msg = ? WHERE guild_id = ?")
					val = (text, inter.guild.id)
					embed = discord.Embed(title = '✅ | Текст для приветствия успешно изменен',description = f"`{text}`", color=embedColor)
					await inter.response.send_message(embed=embed)
				cursor.execute(sql, val)
				db.commit()
				cursor.close()
				db.close()
		else:
			embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=embedColor)
			await inter.response.send_message(embed=embed)
			print(f"[welcometext] [{inter.author} ({inter.author.id})] Был установлен текст: {text}")	


@client.slash_command(description="Установит канал прощания.")
async def leavechannel(inter, channel:discord.TextChannel):
			if inter.author.guild_permissions.administrator:
				db = sqlite3.connect('leave.sqlite')
				cursor = db.cursor()
				cursor.execute(f"SELECT channel_id FROM leave WHERE guild_id = '{inter.guild.id}'")
				result =  cursor.fetchone()
				if result is None:
					sql = ("INSERT INTO leave(guild_id, channel_id) VALUES(?,?)")
					val = (inter.guild.id, channel.id)
					embed = discord.Embed(title = '✅ | Канал для прощания успешно настроен',description=f'Канал настроен до {channel.mention}', color=embedColor)
					await inter.response.send_message(embed=embed)
				elif result is not None:
					sql = ("UPDATE leave SET channel_id = ? WHERE guild_id = ?")
					val = (channel.id, inter.guild.id)
					embed = discord.Embed(title = '✅ | Канал для прощания успешно изменен',description=f'Канал изменен до {channel.mention}', color=embedColor)
					await inter.response.send_message(embed=embed)
				cursor.execute(sql, val)
				db.commit()
				cursor.close()
				db.close()
				return
			else:
				embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=embedColor)
				await inter.response.send_message(embed=embed)
			print(f"[leavechannel] [{inter.author} ({inter.author.id})] Был установлен канал: {channel}")	



@client.slash_command(description="Установит текст прощания.")
async def leavetext(inter,*, text):
		if inter.author.guild_permissions.administrator:
			db = sqlite3.connect('leave.sqlite')
			cursor = db.cursor()
			cursor.execute(f"SELECT msg FROM leave WHERE guild_id = {inter.guild.id}")
			result =  cursor.fetchone()
			if result is None:
				sql = ("INSERT INTO leave(guild_id, msg) VALUES(?,?)")
				val = (inter.guild.id, text)
				embed = discord.Embed(title = 'Текст для прощания успешно создан',description = f"`{text}`", color=embedColor)
				await inter.response.send_message(embed=embed)
			elif result is not None:
				sql = ("UPDATE leave SET msg = ? WHERE guild_id = ?")
				val = (text, inter.guild.id)
				embed = discord.Embed(title = 'Текст для прощания успешно изменен',description = f"`{text}`", color=embedColor)
				await inter.response.send_message(embed=embed)
			cursor.execute(sql, val)
			db.commit()
			cursor.close()
			db.close()
		else:
			embed = discord.Embed(title='Ошибка', description = 'Вы не администратор', color=embedColor)
			await inter.response.send_message(embed=embed)
			print(f"[leavetext] [{inter.author} ({inter.author.id})] Был установлен текст: {text}")	

client.run(token)