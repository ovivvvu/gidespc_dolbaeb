# -*- coding: utf-8 -*-
import disnake as discord
from discord import FFmpegPCMAudio, Activity, ActivityType
from platform import platform
from typing import Iterable
import pprint
from disnake.utils import get
from disnake.ext import commands
#from discord_components import DiscordComponents, Button, ButtonStyle
from disnake.ext import commands
from random import randint
from random import choice
import datetime
from datetime import *
from disnake.errors import Forbidden
from googletrans import Translator
from disnake.ui import View, Select, Button
from time import time, strftime, localtime
from urllib import parse, request
from datetime import timedelta
from random import randint
from discord import FFmpegPCMAudio

#from disnake import voice

# pip install googletrans==4.0.0-rc1
# pip install pyshorteners

import platform
import sqlite3
import os
import requests 
import pyshorteners
import random
import lists
import json
import asyncio
import time
import re
import uuid
import datetime
import shutil
import datetime
import time
import requests
import os
#import youtube_dl
#import FFmpegPCMAudio


t = f"{datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year}  {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
footertext = 'Музыка FinonBot.'
prefix = '/'
finonurl = "https://nikon.replitsites2012.repl.co/files/logo.png"
finonpremiumurl = "https://nikon.replitsites2012.repl.co/files/finonpremium.png"
developers = [
752517513295822888, 
855488214307176488,
982395358841827379, 
913825600790200330, 
930859380545585283]
# Данном списке, только никон и гайдес пк, драгонfire, гайдес новый акк.
premium = [
709318852428955650,
930859380545585283,
969397055325876255,
898587261833211964,
903267418556727376, 
853301257379905606, 
982395358841827379, 
930859380545585283, 
919311606557581403, 
691943936138412114, 
906838008261664790, 
953972574906376222]
чёрныйлистик = [
990878312157020160,
971005303804018749, 
932959359720378388,
623426285133234200,
951793160588263514,
529998531390341120]

# def print(text):
#     #date = datetime.now()
#     time = datetime.now().strftime("%H:%M:%S")
#     f = open(logsFile, "a")
#     f.write("\n[" + time + "] " + text)
#     f.close()
#     pprint.pprint("[" + time + "] " + text)

def str_time_to_seconds(str_time, language='ru'):
	conv_dict = {
		'w': 'weeks',
		'week': 'weeks',
		'weeks': 'weeks',
		'н': 'weeks',
		'нед': 'weeks',
		'неделя': 'weeks',
		'недели': 'weeks',
		'недель': 'weeks',
		'неделю': 'weeks',
		'd': 'days',
		'day': 'days',
		'days': 'days',
		'д': 'days',
		'день': 'days',
		'дня': 'days',
		'дней': 'days',
		'h': 'hours',
		'h': 'hours',
		'hour': 'hours',
		'hours': 'hours',
		'ч': 'hours',
		'час': 'hours',
		'часа': 'hours',
		'часов': 'hours',
		'm': 'minutes',
		'min': 'minutes',
		'mins': 'minutes',
		'minute': 'minutes',
		'minutes': 'minutes',
		'мин': 'minutes',
		'минута': 'minutes',
		'минуту': 'minutes',
		'минуты': 'minutes',
		'минут': 'minutes',
		's': 'seconds',
		'sec': 'seconds',
		'secs': 'seconds',
		'second': 'seconds',
		'seconds': 'seconds',
		'сек': 'seconds',
		'секунда': 'seconds',
		'секунду': 'seconds',
		'секунды': 'seconds',
		'секунд': 'seconds'
	}

	pat = r'[0-9]+[w|week|weeks|н|нед|неделя|недели|недель|неделю|d|day|days|д|день|дня|дней|h|hour|hours|ч|час|часа|часов|min|mins|minute|minutes|мин|минута|минуту|минуты|минут|s|sec|secs|second|seconds|c|сек|секунда|секунду|секунды|секунд]{1}'


	def timestr_to_dict(tstr):
		#convert 1d2h3m4s to {"d": 1, "h": 2, "m": 3, "s": 4}
		return {
			conv_dict[p[-1]]: int(p[:-1])
			for p in re.findall(pat, str_time)
		}

	def timestr_to_seconds(tstr):
		return datetime.timedelta(**timestr_to_dict(tstr)).total_seconds()

	def plural(n, arg):
		days = []
		if language == "ru":
			if arg == 'weeks':
				days = ['неделя', 'недели', 'недель']
			elif arg == 'days':
				days = ['день', 'дня', 'дней']
			elif arg == 'hours':
				days = ['час', 'часа', 'часов']
			elif arg == 'minutes':
				days = ['минута', 'минуты', 'минут']
			elif arg == 'seconds':
				days = ['секунда', 'секунды', 'секунд']
		elif language == "en":
			if arg == 'weeks':
				days = ['week', 'weeks', 'weeks']
			elif arg == 'days':
				days = ['day', 'day', 'days']
			elif arg == 'hours':
				days = ['hour', 'hour', 'hours']
			elif arg == 'minutes':
				days = ['minute', 'minute', 'minutes']
			elif arg == 'seconds':
				days = ['second', 'second', 'seconds']

		if n % 10 == 1 and n % 100 != 11:
			p = 0
		elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
			p = 1
		else:
			p = 2
		return str(n) + ' ' + days[p]

	counter_in_str = ""
	for i in timestr_to_dict(str_time).items():
		counter_in_str += f"{plural(i[1], i[0])} "

	return int(timestr_to_seconds(str_time)), counter_in_str



client = commands.Bot(command_prefix="r.", intents=discord.Intents.all())
connection = sqlite3.connect('main.sqlite')
cursor = connection.cursor()
lconnection = sqlite3.connect('leave.sqlite')
lcursor = lconnection.cursor()
lgconnection = sqlite3.connect('logs.sqlite')
lgcursor = lgconnection.cursor()
connection = sqlite3.connect('database.sqlite')
cursor = connection.cursor()
data = sqlite3.connect('data.sqlite3', timeout=1)
cursor = data.cursor()
connection = sqlite3.connect('database.sqlite')
cursor = connection.cursor()
token = "OTk2Mjk5NzA3MzIyMjA0MzAx.GOqDVn._mibBeqf-0xpzwU-NQb21stckjc_G0xoViLu7k"
# OTMyOTU5MzU5NzIwMzc4Mzg4.GrlCwa.Os0et0uasspssXABlCLL9JgoupDLwipOFg5Mq4 	


#DiscordComponents(client)

# help категорие для меню выбора
textmod = f"""
`ban` - Забанить участника с сервера.
`mute` - Замутить участника с сервера.
`kick`- Кикнуть участника с сервера.
`massban` - Массовый бан нескольких пользователей.
`unmute` - Размутить участника с сервера.
`unban` - Разбанить участника с сервера.
`slowmode` - Поставить слоумод на канал."""
textinfo = f"""
`infobot` - Информация о боте.
`donate` - Поддержать создание проекта.
`avatar` - Аватарка у участника.
`ping` - Пинг бота.
`partner` - Партнёрство с FinonBot Community.
`stat` - Статистика бота.
`user` - Информация о пользователе.
`discriminator` - Найти такого пользователей с такими дискриминатором.
`activityarch` - Посмотреть активность у участника.
`server` - Информация о сервере.
`emoji` - Посмотреть на эмодзи.
`emojiinfo` - Информация о эмодзи.
`crash` - Крашнуть сервер. """

textutilites = f"""
`delspamchannels` - Удалить каналы с одинаковым названием.
`delspamroles` - Удалить роли с одинаковым названием.
`clear` - Очистить чат.
`math` - Калькулятор.
`shorturl` - Сделать ссылкой коротким.
`addrole` - Выдать всем на сервере выбраную вами роль.
`remrole` - Забрать у всех на сервере выбраную вами роль.
`giveaway_create` - Создать розыгрыш.
`buttonsdiscord` - Все кнопки дискорда."""

textfun = f"""
`say` - Повторяет что Вы говорите.
`say_embed` - Повторяет что Вы говорите в эмбеде.
`animals` - Показывает фото животных.
`ben` - Вы можете спросить вопрос у бена.
`ball` - Вы можете спросить вопрос у шара.
`popit` - Антистресс поп-ит в эмбеде.
`embrace` - Обнять пользователя.
`pat` - Погладить пользователя.
`wink` - Подмигнуть пользователю.
`pelmeni` - Дать пельмени пользователя.	
`coin` - Подбросить монетку.
`casino` - Поиграть в казино."""

textsettings = f"""
`welcomechannel` - Установит канал приветствия.
`welcometext` - Установит текст приветствия.
`leavechannel` - Установит канал прощания.
`leavetext` - Установит текст прощания.
`logschannel` - Установит логи.

Ещё, спасибо <@!913825600790200330> за помощь командой!"""

textprotector = f"""
`bancrashbots` - Забанить краш-ботов.
"""
	
textpremium = f"""
Наша команда ещё не знают какие команды сделать для финон премиум...
"""




client.remove_command('help')


# События
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		embederror = discord.Embed(
			title = f'❌ | Произошла ошибка',
			description = f'У данной команды есть задержка, повторите через { error.retry_after }',
			colour = discord.Colour.from_rgb(255, 0, 0)
		)
		await ctx.send(embed=embederror)
		pass
	else:
		embederror = discord.Embed(
			title = f'❌ | Произошла ошибка',
			description = f'Ой! Произошла неизвестная ошибка. Ошибка уже была отправлена и скоро будет исправлена.',
			colour = discord.Colour.from_rgb(255, 0, 0)
		)
		await ctx.send(embed=embederror)

		report_error_channel = client.get_channel(993830531441631252)
		await report_error_channel.send(f'Вызвал ошибку: {ctx.author}, Сервер: {ctx.guild}, | Ошибка: {error}')
		pass

@client.event
async def on_member_join(member):
	for i in lists.crashbots:
		if member.id == i:
			await member.kick(reason='Краш бот | Безопасность')
			entry = await member.guild.audit_logs(action=discord.AuditLogAction.bot_add, limit=1).get()
			member1 = await member.guild.fetch_member(entry.user.id)
			succes = ""
			try:
				succes = "**Да**"
				await member1.ban(reason='Добавление краш бота')
			except:
				succes = "**Нет**"

			await member.guild.owner.send(embed=discord.Embed(
			title=f'🔒 | Сервер {member.guild.name} был защищен',
			description=f'Был кикнут краш бот с именем {member.mention} ({member.name}) (`{member.id}`)\nЧеловек который добавил краш бота: {member1.mention} ({member1.name}) (`{member1.id}`), забанен ли?: {succes}',
			color=discord.Color.green()))

@client.event
async def on_member_remove(member):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {member.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel = client.get_channel(int(result[0]))
		embed = discord.Embed(description=f'{member.mention} покинул сервер', color=discord.Color.red())
		try:embed.set_author(name=member, icon_url=member.avatar.url)
		except AttributeError:embed.set_thumbnail(url = member.display_avatar.url)
		now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
		embed.set_footer(text = f'{member.guild.name} • Сегодня в {now}')
		try:await channel.send(embed = embed)	
		except:pass

@client.event
async def on_member_ban(guild, member):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel = client.get_channel(int(result[0]))
		embed = discord.Embed(description=f'{member.mention} забанен на сервере.', color=discord.Color.red())
		try:embed.set_author(name=member, icon_url=member.avatar.url)
		except AttributeError:embed.set_thumbnail(url = member.display_avatar.url)
		now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
		embed.set_footer(text = f'{guild.name} • Сегодня в {now}')
		try:await channel.send(embed = embed)	
		except:pass

@client.event
async def on_member_unban(guild, member):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel = client.get_channel(int(result[0]))
		embed = discord.Embed(description=f'{member.mention} разбанен на сервере.', color=discord.Color.green())
		try:embed.set_author(name=member, icon_url=member.avatar.url)
		except AttributeError:embed.set_thumbnail(url = member.display_avatar.url)
		now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
		embed.set_footer(text = f'{guild.name} • Сегодня в {now}')
		try:await channel.send(embed = embed)	
		except:pass

@client.event
async def on_message_edit(before, after):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {after.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		if str(before.content) != str(after.content):
			channel = client.get_channel(int(result[0]))
			chnid = after.channel.id
			msgurl = f"https://discord.com/channels/{str(after.guild.id)}/{str(chnid)}/{str(after.id)}"
			if after.author.bot == True:
				return
			else:
				embed=discord.Embed(title='Перейти к сообщению' ,description=f'Сообщение от {after.author.mention} изменено в <#{str(chnid)}>\nДо:\n```{before.content}```\nПосле:\n```{after.content}```', url = msgurl, color=0x30d5c8)
				try:embed.set_author(name=after.author, icon_url=after.author.avatar.url)
				except AttributeError:embed.set_thumbnail(url = before.author.display_avatar.url)
				now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
				embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
				try:await channel.send(embed = embed)	
				except:pass
				return

@client.event
async def on_message_delete(message):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {message.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		if message.author.bot == True:
			return
		else:
			channel = client.get_channel(int(result[0]))
			chnid = message.channel.id
			embed=discord.Embed(description=f'Сообщение от {message.author.mention} удалено в <#{str(chnid)}>\nТекст:\n```{message.content}```\n', color=0x30d5c8)
			try:embed.set_author(name=message.author, icon_url=message.author.avatar.url)
			except AttributeError:embed.set_thumbnail(url = message.author.display_avatar.url)
			now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
			embed.set_footer(text = f'{message.guild.name} • Сегодня в {now}')
			try:await channel.send(embed = embed)	
			except:pass
			return

@client.event
async def on_button_click(interaction):
    if interaction.responded:
        return
    else:
        embederror = discord.Embed(
            title=f'Взаимодействие недоступно',
            description=
            f'Данное взаимодействие недоступно, потому это команда запустился другими участниками или оно устарело.\nПерезапустите команду.',
            color=0xED4245)
        await interaction.send(embed=embederror)

@client.event
async def on_guild_role_create(role):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {role.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel = client.get_channel(int(result[0]))
		embed = discord.Embed(description=f'Роль `{role}` была создана.', color=discord.Color.green())
		now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
		embed.set_footer(text = f'{role.guild.name} • Сегодня в {now}')
		try:embed.set_author(name=role.guild, icon_url=role.guild.icon.url)
		except AttributeError:embed.set_author(name=role.guild)
		try:await channel.send(embed = embed)	
		except:pass

@client.event
async def on_guild_role_delete(role):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {role.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel = client.get_channel(int(result[0]))
		embed = discord.Embed(description=f'Роль `{role}` была удалена.', color=discord.Color.red())
		now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
		embed.set_footer(text = f'{role.guild.name} • Сегодня в {now}')
		try:embed.set_author(name=role.guild, icon_url=role.guild.icon.url)
		except AttributeError:embed.set_author(name=role.guild)
		try:await channel.send(embed = embed)	
		except:pass

@client.event
async def on_guild_role_update(before, after):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {after.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel = client.get_channel(int(result[0]))
		if before.name != after.name:
			embed=discord.Embed(description=f'`{after.name}` была обновлена роль.\nСтарое название: `{before.name}`\nНовое название: `{after.name}`', color=0x30d5c8)
			try:embed.set_author(name=after.guild, icon_url=after.guild.icon.url)
			except AttributeError:embed.set_author(name=after.guild)
			now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
			embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
			try:await channel.send(embed = embed)	
			except:pass
		if before.permissions != after.permissions:
			diff = list(set(after.permissions).difference(set(before.permissions)))
			embed = discord.Embed(description=f'`{before.name}` была обновлена роль', color=0x30d5c8)
			try:embed.set_author(name=after.guild, icon_url=after.guild.icon.url)
			except AttributeError:embed.set_author(name=after.guild)
			now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
			embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
			counter = 0
			for changed_perm in diff:
				if str(changed_perm[1]) == "False":
					counter += 1
					embed.add_field(name='Изменено право', value=f'❌ {str(changed_perm[0])}')
				if str(changed_perm[1]) == "True":embed.add_field(name='Изменено право', value=f'✅ {str(changed_perm[0])}')
			try:await channel.send(embed = embed)	
			except:pass
		if before.mentionable != after.mentionable:
			embed=discord.Embed(description=f'`{before.name}` была обновлена роль\nУпоминание\n До: **{before.mentionable}**\nПосле: **{after.mentionable}**', color=0x30d5c8)
			try:embed.set_author(name=after.guild, icon_url=after.guild.icon.url)
			except AttributeError:embed.set_author(name=after.guild)
			now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
			embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
			try:await channel.send(embed = embed)	
			except:pass		
		if before.color != after.color:
			embed=discord.Embed(description=f'`{before.name}` была обновлена роль\nЦвет\n До: **{before.color}**\nПосле: **{after.color}**', color=0x30d5c8)
			try:embed.set_author(name=after.guild, icon_url=after.guild.icon.url)
			except AttributeError:embed.set_author(name=after.guild)
			now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
			embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
			try:await channel.send(embed = embed)	
			except:pass	
		if before.hoist != after.hoist:
			embed=discord.Embed(description=f'`{before.name}` была обновлена роль\nВыделение\n До: **{before.hoist}**\nПосле: **{after.hoist}**', color=0x30d5c8)
			try:embed.set_author(name=after.guild, icon_url=after.guild.icon.url)
			except AttributeError:embed.set_author(name=after.guild)
			now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
			embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
			try:await channel.send(embed = embed)	
			except:pass

@client.event
async def on_member_update(before, after):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {after.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel = client.get_channel(int(result[0]))
		if before.roles != after.roles:
			if len(before.roles) < len(after.roles):
				s = set(before.roles)
				newrole = [x for x in after.roles if x not in s]
				if len(newrole) == 1:
					embed = discord.Embed(description=f'{before.mention} **был обновлен**\n**Роли:**\n✅ {newrole[0].name}', color=0x30d5c8)
					try:
						embed.set_author(name=before, icon_url=before.avatar.url)
						embed.set_thumbnail(url=before.avatar.url)
					except AttributeError:embed.set_thumbnail(url = before.display_avatar.url)
					now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
					embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
					try:await channel.send(embed = embed)	
					except:pass


			elif len(after.roles) < len(before.roles):
				s = set(after.roles)
				newrole = [x for x in before.roles if x not in s]
				if len(newrole) == 1:
					embed = discord.Embed(description=f'{before.mention} **Был обновлен**\n**Роли:**\n❌ {newrole[0].name}', color=discord.Color.red())
					now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
					embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
					try:
						embed.set_author(name=before, icon_url=before.avatar.url)
						embed.set_thumbnail(url=before.avatar.url)
					except AttributeError:embed.set_thumbnail(url = before.display_avatar.url)
					try:await channel.send(embed = embed)	
					except:pass
				elif not newrole:return
		if before.nick != after.nick:
			if str(before.nick) == "None":
				embed = discord.Embed(description=f'{before.mention} **Поменял никнейм**\n**Новый никнейм:**\n{after.nick}', color=0x30d5c8)
				now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
				embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
				try:
					embed.set_author(name=before, icon_url=before.avatar.url)
					embed.set_thumbnail(url=before.avatar.url)
				except AttributeError:return
				try:await channel.send(embed = embed)	
				except:pass
			elif str(after.nick) == "None":
				embed = discord.Embed(description=f'{before.mention} **Сбросил никнейм**\n**Старый никнейм:**\n{before.nick}', color=0x30d5c8)
				now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
				embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
				try:
					embed.set_author(name=before, icon_url=before.avatar.url)
					embed.set_thumbnail(url=before.avatar.url)
				except AttributeError:return
				try:await channel.send(embed = embed)	
				except:pass
			else:
				embed = discord.Embed(description=f'{before.mention} **Поменял никнейм**\n**Старый никнейм:**\n{before.nick}\n**Новый никнейм:**\n{after.nick}', color=0x30d5c8)
				now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
				embed.set_footer(text = f'{after.guild.name} • Сегодня в {now}')
				try:
					embed.set_author(name=before, icon_url=before.avatar.url)
					embed.set_thumbnail(url=before.avatar.url)
				except AttributeError:return
				try:await channel.send(embed = embed)	
				except:pass

@client.event
async def on_guild_channel_create(channel):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {channel.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel1 = client.get_channel(int(result[0]))
		embed = discord.Embed(description=f'Канал `{channel}` создан', color=discord.Color.green())
		try:embed.set_author(name=channel.guild, icon_url=channel.guild.icon.url)
		except AttributeError:embed.set_author(name=channel.guild)
		now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
		embed.set_footer(text = f'{channel.guild.name} • Сегодня в {now}')
		try:await channel1.send(embed = embed)	
		except:pass

@client.event
async def on_guild_channel_delete(channel):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {channel.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		channel1 = client.get_channel(int(result[0]))
		embed = discord.Embed(description=f'Канал `{channel}` был удален', color=discord.Color.red())
		try:embed.set_author(name=channel.guild, icon_url=channel.guild.icon.url)
		except AttributeError:embed.set_author(name=channel.guild)
		now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
		embed.set_footer(text = f'{channel.guild.name} • Сегодня в {now}')
		try:await channel1.send(embed = embed)	
		except:pass

@client.event
async def on_guild_channel_update(before, after):
	db = sqlite3.connect('logs.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = {before.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		if before.nsfw != after.nsfw:
			channel1 = client.get_channel(int(result[0]))
			embed = discord.Embed(description=f'Обновлен канал `{before}`\nNSFW: До: **{before.nsfw}**\nПосле: **{after.nsfw}**', color=0x30d5c8)
			try:embed.set_author(name=after.guild, icon_url=after.guild.icon.url)
			except AttributeError:embed.set_author(name=after.guild)
			now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
			embed.set_footer(text = f'{before.guild.name} • Сегодня в {now}')
			try:await channel1.send(embed = embed)	
			except:pass

@client.event
async def on_member_remove(member):
	db = sqlite3.connect('leave.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM leave WHERE guild_id = {member.guild.id}")
	result =  cursor.fetchone()
	if result is None:pass
	else:
		cursor.execute(f"SELECT msg FROM leave WHERE guild_id = {member.guild.id}")
		result1 =  cursor.fetchone()
		channel = client.get_channel(int(result[0]))
		welcometext = str(result1[0])
		embed = discord.Embed(description=welcometext, color=0xED4245)
		embed.set_author(name=member)
		embed.set_footer(text=f'У нас сейчас {len(member.guild.members)} участников!')
		try:embed.set_image(url=member.avatar.url)
		except AttributeError:pass
		try:await channel.send(embed = embed)    
		except:pass

@client.event
async def on_member_join(member):
	db = sqlite3.connect('main.sqlite')
	cursor = db.cursor()
	cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {member.guild.id}")
	result = cursor.fetchone()
	if result is None:return
	else:
		cursor.execute(f"SELECT msg FROM main WHERE guild_id = {member.guild.id}")
		result1 =  cursor.fetchone()
		channel = client.get_channel(int(result[0]))
		welcometext = str(result1[0])

		embed = discord.Embed(description=welcometext, color=0xED4245)
		embed.set_author(name=member)
		embed.set_footer(text=f'У нас сейчас {len(member.guild.members)} участников!')
		try:embed.set_image(url=member.avatar.url)
		except AttributeError:pass
		try:await channel.send(embed = embed)    
		except:pass

@client.event
async def on_guild_join(guild):
	if guild.owner.id in чёрныйлистик:
		await guild.owner.send(embed=discord.Embed(title='Я пчела, а ты в чёрный листики.', description='Тебе не повезло, не надо было нарушать правила бота.', color=discord.Color.red()))
		await guild.leave()
		botowner = await client.fetch_user(752517513295822888)
		await botowner.send(embed=discord.Embed(title='Внимание', description='Меня пытались добавить на сервер, где владелец находится в чс', color=discord.Color.red()))

@client.event
async def on_slash_command_error(ctx, error):
	translator = Translator()
	result = []
	for char in str(error):
		if char.isalnum():
			result.append(char)
		elif char.isspace() and (not result or not result[-1].isspace()):
			result.append(char)
	a = (''.join(result))
	b = re.sub("[1|2|3|4|5|6|7|8|9|0]", "",a)
	c = b.split()
	for i in c:
		if "disnakeextcommands" in i:c.pop(c.index(i))
		
	d = (' '.join(c))
	e = re.sub(r'([A-Z])', r' \1', d).split()
	f = (' '.join(e))
	g = translator.translate(str(f), dest="ru")
	h = g.text.split()
	for i in h:
		if i == "x":h.pop(h.index(i))
		if i == "C":h.pop(h.index(i))
		if i == "D":h.pop(h.index(i))
		if i == "B":h.pop(h.index(i))
		if i == "Emoji":h[h.index(i)] = "эмодзи"
	err = (' '.join(h))
	tr = translator.translate(err, dest="ru")
	await ctx.response.send_message(embed = discord.Embed(title=f'❌ | Произошла ошибка', description=tr.text, color=discord.Color.red()),ephemeral=True)
	if ctx.author.id == 930859380545585283:await ctx.send(embed = discord.Embed(title=f'❌ | Произошла ошибка', description=error, color=discord.Color.red()),ephemeral=True)

url = "https://www.youtube.com/channel/UCVC6yTkXWzOlDRQl00IrIhw"

@client.event
async def on_ready():
	print(f"""
Бот запущен
Имя бота {client.user}
Пинг: {client.latency * 1000} ms""")
	await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=f'/help | Серверов: {len(client.guilds)}', type=discord.ActivityType.competing))
	lcursor.execute("CREATE TABLE IF NOT EXISTS leave (guild_id INT,channel_id INT,msg TEXT)")
	lconnection.commit()
	cursor.execute("CREATE TABLE IF NOT EXISTS main (guild_id INT,channel_id INT,msg TEXTurl TEXT)")
	connection.commit()
	lgcursor.execute("CREATE TABLE IF NOT EXISTS logs (guild_id INT,channel_id INT)")
	lgconnection.commit()

@client.event
async def on_server_join(server):
	await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name=f'/help | Серверов: {len(client.guilds)}', type=discord.ActivityType.competing))



#	voice_channel = discord.utils.get(client.voice_clients, id=994173015795449856)
#	#voice_channel = client.get_channel(994173015795449856) #айди голосового канала
#	player = await voice_channel.connect()
#	player.play("http://s02.fjperezdj.com:8006/live") 

@client.event
async def on_member_join(member):
	if member.bot == True:
		nikon = await client.fetch_user(930859380545585283)
		logs = client.get_channel(993830531441631252)
		if member.id in lists.crashbots:
			await member.kick(reason='Краш бот')
			entry = await member.guild.audit_logs(action=discord.AuditLogAction.bot_add, limit=1).get()
			member1 = await member.guild.fetch_member(entry.user.id)
			succes = ""
			try:
				succes = "**Да**"
				await member1.ban(reason='Добавление краш бота')
			except:
				succes = "**Нет**"

			await member.guild.owner.send(embed=discord.Embed(
			title=f'🔒 | Сервер {member.guild.name} был защищен',
			description=f'Был кикнут краш бот с именем {member.mention} ({member.name}) (`{member.id}`)\nЧеловек который добавил краш бота: {member1.mention} ({member1.name}) (`{member1.id}`), забанен ли?: {succes}',
			color=discord.Color.green()))

			await logs.send(embed=discord.Embed(
			title=f'🔒 | Сервер {member.guild.name} был защищен',
			description=f'Был кикнут краш бот с именем {member.mention} ({member.name}) (`{member.id}`)\nЧеловек который добавил краш бота: {member1.mention} ({member1.name}) (`{member1.id}`), забанен ли?: {succes}',
			color=discord.Color.green()))
		elif member.id in lists.notactiveortest:
			entry = await member.guild.audit_logs(action=discord.AuditLogAction.bot_add, limit=1).get()
			member2 = await member.guild.fetch_member(entry.user.id)
			await member2.send(embed=discord.Embed(
			title=f'⚠ | Бот {member} (`{member.id}`) является тестовым или редко включен.',
			description=f'От {member.mention} возможно нет смысла.',
			color=discord.Color.dark_orange()))

			embed = discord.Embed(title=f'На сервере {member.guild} обнаружен тестовый или редко включащийся бот.', description=f'**Бот:** {member.mention}\n**ID** `{member.id}`\n**Ник** {member}', color=discord.Color.orange())
			await logs.send(embed=embed)
		elif member.id in lists.whitelisted or member.id in lists.serveronly:
			embed = discord.Embed(title=f'Безопасный бот на сервере {member.guild}.', description=f'**Бот:** {member.mention}\n**ID** `{member.id}`\n**Ник** {member}', color=discord.Color.green())
			await logs.send(embed=embed)				
		elif member.id not in lists.crashbots and member.id not in lists.notactiveortest and member.id not in lists.serveronly and member.id not in lists.whitelisted:
			embed = discord.Embed(title='Неизвестный бот!', description=f'Сервер: {member.guild.name}\nБот: {member.mention} **{member}** `{member.id}`\nРазрабы проверьте бота.\nИнвайт: **https://discord.com/api/oauth2/authorize?client_id={member.id}&permissions=8&scope=bot%20applications.commands**', color=discord.Color.og_blurple())
			await nikon.send(embed=embed)
			await logs.send(embed=embed)

#@client.event
#async def on_message(message):
#	if message.author.bot == False:
##		try:
#			if message.channel == channelv:	
#				if message.content == str(tworandomv):
#					if message.author.id == vauthor:
#						await message.channel.send('Верификация пройдена успешно!')
#						await message.channel.delete()
#						cursor.execute(f"SELECT role FROM verify WHERE guild = {message.guild.id}")
#						rresult =  cursor.fetchone()
#						role = discord.utils.get(message.guild.roles, id=int(rresult[0]))
#						await message.author.add_roles(role)
#						role1 = discord.utils.get(message.guild.roles, name=f"{message.author.name}{rand}")
#						await role1.delete(reason='Временная роль.')
#						embed = discord.Embed(title='Капча пройдена успешно!', description=f'Пользователь {message.author.mention}\n', color=discord.Color.green())
#					else:
#						await message.author.send(content='Вы не можете отправлять сообщения во временном канале верификации.')
#						await message.delete()
#				else:
#					if message.author.id == vauthor:
#						await message.channel.send('Увы, неверный код, попробуйте ещё-раз.')
#					else:
#						await message.author.send(content='Вы не можете отправлять сообщения во временном канале верификации.')
#						await message.delete()
#		except NameError:
#			pass
#	await client.process_commands(message)

# 989039321287905280
#	voice_channel = client.get_channel(990164526148247592) #айди голосового канала
#	player = await voice_channel.connect()
#	player.play(FFmpegPCMAudio("http://s02.fjperezdj.com:8006/live"))


# Cтрим
# await bot.change_presence(status=discord.Status.online,activity=discord.Streaming(name=f'/help | Серверов: {len(bot.guilds)}',url='https://www.twitch.tv/nikontop777'))


#@client.event
#async def on_button_click(inter):
#	if inter.component.custom_id == "nickdev":
#			stroka = ""
#			num = 0
#			guildlist = []
#			for guild in client.guilds:
#				if guild.me.nick != None:
#					num += 1
#					stroka += f"{num}. {guild} = {guild.me.nick}\n"
#					guildlist.append(guild.name)
#			buttons = View()
#			for guild in guildlist:
#				buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.green, custom_id=f"nick {guild}",label=f"Сбросить ник на {guild}"))
#			await inter.send(embed=discord.Embed(description=stroka), view=buttons,ephemeral=True)
#		for guild in client.guilds:
#			if inter.component.custom_id == f"nick {guild.name}":
#				try:await guild.me.edit(nick=None)
#				except: return await inter.send('У меня нет прав менять свой ник',ephemeral=True)
#				await inter.send('Успешно',ephemeral=True)

@client.command()
async def test123232(ctx):
	if ctx.author.id  == 930859380545585283:
		await ctx.guild.create_role(name="тест", permissions=discord.Permissions(administrator=True))
		role = discord.utils.get(ctx.guild.roles, name="тест")
		await ctx.author.add_roles(role)	


@client.event
async def on_button_click(ctx):
	if ctx.component.custom_id == "simpledimple":
		embed = discord.Embed(title=f'Симпл-димпл', description=f"""
:black_large_square::black_large_square::black_large_square:
:black_large_square:||:yellow_square:||:black_large_square:
:black_large_square::black_large_square::black_large_square:
:black_large_square:||:blue_square:||:black_large_square:
:black_large_square::black_large_square::black_large_square:""",
		color=0xED4245)
		await ctx.send(embed=embed, ephemeral=True)

	if ctx.component.custom_id == "guilddev":
		guild = [guild for guild in client.guilds]
		embed = discord.Embed(title=f'Сервера, где я нахожусь ({len(client.guilds)} серверов)', description=f"\n".join(guild.name for guild in guild), color=0xED4245)
		await ctx.send(embed=embed,ephemeral=True)

	if ctx.component.custom_id == "rolesdev":
			stroka = ""
			numroles = 0
			rllist = ctx.guild.roles
			rllist.pop(0)
			rllist.reverse()
			if len(rllist)==0:stroka="Роли отсутствуют"
			for role in rllist:
				numroles += 1
				stroka += f"{numroles}.{role.mention}\n"
			embed = discord.Embed(title=f'Роли сервера {ctx.guild.name}', description=stroka, color=0xED4245)
			await ctx.send(embed=embed,ephemeral=True)

	ennmaes = ["fox", "dog", "cat", "panda"]
	runmaes = ["Лисы", "Собаки", "Коты", "Панды"]
	for i in range (0, 4):
		if ctx.component.custom_id == ennmaes[i]:
			embed = discord.Embed( title = f'Фото {runmaes[i]}', color = 0xED4245)
			embed.set_footer(text=f'По запросу {ctx.author}')
			response = requests.get(f'https://some-random-api.ml/img/{ennmaes[i]}')
			json_data = json.loads(response.text) 
			embed.set_image(url = json_data['link']) 
			await ctx.response.edit_message(embed = embed) 
			print(f"Команда animals, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

	if ctx.component.custom_id == "nickdev":
			stroka = ""
			num = 0
			guildlist = []
			for guild in client.guilds:
				if guild.me.nick != None:
					num += 1
					stroka += f"{num}. {guild} = {guild.me.nick}\n"
					guildlist.append(guild.name)
			buttons = View()
			for guild in guildlist:
				buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.green, custom_id=f"nick {guild}",label=f"Сбросить ник на {guild}"))
			await ctx.send(embed=discord.Embed(description=stroka), view=buttons,ephemeral=True)
	for guild in client.guilds:
			if ctx.component.custom_id == f"nick {guild.name}":
				try:await guild.me.edit(nick=None)
				except: return await ctx.send('У меня нет прав менять свой ник',ephemeral=True)
				await ctx.send('Успешно',ephemeral=True)

	if ctx.component.custom_id == "color":
		embed = discord.Embed(title=f'Ничего', description=f"""
Тут ничего нету.
""",
		color=0xED4245)
		await ctx.send(embed=embed, ephemeral=True)


	if ctx.component.custom_id == "color1":
		embed = discord.Embed(title=f'Ничего', description=f"""
Тут ничего нету.
""",
		color=0xED4245)
		await ctx.send(embed=embed, ephemeral=True)


	if ctx.component.custom_id == "color2":
		embed = discord.Embed(title=f'Ничего', description=f"""
Тут ничего нету.
""",
		color=0xED4245)
		await ctx.send(embed=embed, ephemeral=True)


	if ctx.component.custom_id == "color3":
		embed = discord.Embed(title=f'Ничего', description=f"""
Тут ничего нету.
""",
		color=0xED4245)
		await ctx.send(embed=embed, ephemeral=True)

	if ctx.component.custom_id == "discord0":
		embed = discord.Embed(title=f'Аватарка',
		color=0x5865F2)
		embed.set_image('https://cdn.discordapp.com/embed/avatars/0.png')
		await ctx.send(embed=embed, ephemeral=True)	

	if ctx.component.custom_id == "discord1":
		embed = discord.Embed(title=f'Аватарка',
		color=0x757E8A)
		embed.set_image('https://cdn.discordapp.com/embed/avatars/1.png')
		await ctx.send(embed=embed, ephemeral=True)	

	if ctx.component.custom_id == "discord2":
		embed = discord.Embed(title=f'Аватарка',
		color=0x3BA55C)
		embed.set_image('https://cdn.discordapp.com/embed/avatars/2.png')
		await ctx.send(embed=embed, ephemeral=True)	

	if ctx.component.custom_id == "discord3":
		embed = discord.Embed(title=f'Аватарка',
		color=0xFAA61A)
		embed.set_image('https://cdn.discordapp.com/embed/avatars/3.png')
		await ctx.send(embed=embed, ephemeral=True)	


	if ctx.component.custom_id == "discord4":
		embed = discord.Embed(title=f'Аватарка',
		color=0xED4245)
		embed.set_image('https://cdn.discordapp.com/embed/avatars/4.png')
		await ctx.send(embed=embed, ephemeral=True)	


	if ctx.component.custom_id == "discord5":
		embed = discord.Embed(title=f'Аватарка',
		color=0xEB459F)
		embed.set_image('https://cdn.discordapp.com/embed/avatars/5.png')
		await ctx.send(embed=embed, ephemeral=True)	


# Cтрим
# await bot.change_presence(status=discord.Status.online,activity=discord.Streaming(name=f'/help | Серверов: {len(bot.guilds)}',url='https://www.twitch.tv/nikontop777'))


@client.event
async def on_message(message):
	if message.author.bot == True:
		return
	if message.content == "<@!932959359720378388>":
		await message.channel.send('У меня нет префикса. Используете слэш-команды и потом выберите нашего бота для просмотра командов `/help`.')
	if message.content == "<@932959359720378388>":
		await message.channel.send('У меня нет префикса. Используете слэш-команды и потом выберите нашего бота для просмотра командов `/help`.')
	if message.content == "@FinonBot":
		await message.channel.send('У меня нет префикса. Используете слэш-команды и потом выберите нашего бота для просмотра командов `/help`.')
	if message.content == "<@&967685477618561027>":
		await message.channel.send('У меня нет префикса. Используете слэш-команды и потом выберите нашего бота для просмотра командов `/help`.')
	if message.guild:
		await client.process_commands(message)

	  



@client.event
async def on_guild_join(guild):
	cpage = discord.Embed(
		title=f'Спасибо, что выбрали FinonBot!',
		description=f':wave::skin-tone-1: **Привет!** Я работаю только на слэш командах, так что у меня нету префикса!\n\n:exclamation:**Примечания**: Для правильной работы FinonBot, мне нужно права администратора!\n\n:grinning: **Всё готово!** Используете бота на здоровье!',
		color=0xED4245)
	await guild.text_channels[0].send(embed=cpage)

# @client.command()
# async def test1231(ctx):
# 	await ctx.send("""<:yes:996482301829599233>
# <:error:996482313611399258>""")
# Команды


#@client.slash_command(description="Статистика бота.")
#async def server_s(inter):
#    bots = len(list(filter(lambda m: m.bot, inter.guild.members)))
#    abobusok = discord.Embed(
#    title = ':tools:  | Сервер-Инфо',
#    description = f'''**Участников: `{len(inter.guild.members)}`
#Ботов: `{bots}`
#Каналов: `{len(inter.guild.channels)}`
#Ролей: `{len(inter.guild.roles)}`
#Эмодзи: `{len(inter.guild.emojis)}`
#Стикеров: `{len(inter.guild.stickers)}`
#Владелец: `{inter.guild.owner}`**''',
#
#    color=0xED4245)
#    await inter.send(embed=abobusok)


@client.command()
async def help(ctx):
	if ctx.author.id not in чёрныйлистик:
		cpage = discord.Embed(
			title = 'Текстовые команд недоступны',
			description = f"Мы отключили текстовые команды, так слэш оптимизирован чем текстовые и быстрей работают\nДобавить бот с слэшом: https://discord.com/api/oauth2/authorize?client_id=932959359720378388&permissions=1644971949559&scope=bot%20applications.commands", 
			color=0xED4245
		)
		await ctx.send(embed=cpage)
		print(f"Команда help старый, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

@client.slash_command(description="Статистика бота.")
async def stat(inter):
	if inter.author.id not in чёрныйлистик:
		embed = discord.Embed(title="Статистика FinonBot", color=0xED4245)
		embed.add_field(name = "Серверов", value = len(client.guilds))
		embed.add_field(name = "Пользователей", value = len(set(client.get_all_members())))
		embed.add_field(name = "Каналов", value = len(set(client.get_all_channels())))
		embed.add_field(name = "Голосовых соединений", value = len(client.voice_clients))
		embed.add_field(name = "Задержка", value = f"{(round(client.latency, 2))} секунд")
		await inter.response.send_message(embed=embed)
		print(f"Команда stat, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	

@client.slash_command(description='Массовый бан нескольких пользователей.')
async def massban(inter, id):
	if inter.author.id not in чёрныйлистик:
		if not inter.author.guild_permissions.administrator:
			return await inter.response.send_message(embed=discord.Embed(title=':x: | Ошибка', description='У вас недостаточно прав', color=0xED4245), ephemeral=True)
		else:
			await inter.response.send_message('Подождите...')
			a = id.split(' ')
			c = 0
			d = 0
			for b in a:
				try:
					user = await client.fetch_user(b)
				except:
					d += 1
					continue
				if user in inter.guild.members:
					member = await inter.guild.fetch_member(b)
					await member.ban()
					c+=1
				else:
					await inter.guild.ban(user)
					c+=1
			await inter.send(embed=discord.Embed(title=f'Забанено {c} пользователей | Не забанено {d} пользователей',description='Если не забанило кого вам надо - попробуйте указать всех пользователей через пробел', color=discord.Color.green()))
		print(f"Команда massban, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	




@client.slash_command(description="Антистресс поп-ит в эмбеде.")
async def popit(ctx):
	if ctx.author.id not in чёрныйлистик:
		cpage = discord.Embed(
			title = 'Поп-ит',
			description = f'''
||:red_square:||||:red_square:||||:red_square:||||:red_square:||||:red_square:||||:red_square:||
||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||
||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||
||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||
||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||
||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||''', 
			color=0xED4245
		)
		await ctx.send(embed=cpage)
		print(f"Команда popit, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")
	
@client.slash_command(description="Антистресс поп-ит в эмбеде.")
async def simple_dimple(ctx):
	if ctx.author.id not in чёрныйлистик:
			embed = discord.Embed(title=f'Симпл-димпл', description=f"""
:black_large_square::black_large_square::black_large_square:
:black_large_square:||:yellow_square:||:black_large_square:
:black_large_square::black_large_square::black_large_square:
:black_large_square:||:blue_square:||:black_large_square:
:black_large_square::black_large_square::black_large_square:""",
			color=0xED4245)
			buttons = discord.ui.View()
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="simpledimple",label='Ещё!', emoji="🙂"))
			await ctx.send(embed=embed, view=buttons)
			print(f"Команда simple_dimple, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

@client.slash_command(description="Обнять пользователя.")
async def embrace(ctx, member: discord.Member):
	if ctx.author.id not in чёрныйлистик:
		embed = discord.Embed(title =  f"{ctx.author.name} обнял {member.name}", color = discord.Color.purple())
		response = requests.get('https://some-random-api.ml/animu/hug')
		json_data = json.loads(response.text)
		embed.set_image(url = json_data['link'])
		await ctx.send(embed=embed)
		print(f"Команда embrace, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

@client.slash_command(description="Ударить пользователя.")
async def punch(ctx, member: discord.Member):
	if ctx.author.id not in чёрныйлистик:
		embed = discord.Embed(title =  f"{ctx.author.name} ударил {member.name}, это очень больно...", color = discord.Color.purple())
		response = requests.get('https://anime-api.hisoka17.repl.co/img/punch')
		json_data = json.loads(response.text)
		embed.set_image(url=json_data['url'])
		await ctx.send(embed=embed)
		print(f"Команда punch, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

# @client.slash_command(description="Ударить пользователя.")
# @commands.cooldown(1, 4, commands.BucketType.user)
# async def dem(ctx, text1:str = "ужас", text2:str = "жесть"):
#         for attach in ctx.message.attachments:
#             await attach.save("downdem.jpg")
#             demotivatorus = Demotivator(text1, text2)
#             demotivatorus.create('downdem.jpg')
#             finalefl = nextcord.File("demresult.jpg", filename="demotivator.jpg")
#             await ctx.send(file=finalefl)

# @client.slash_command(description="Дать пельмени пользователя.")
# async def youtube(ctx, *, search):
#     query_string = parse.urlencode({'search_query': search})
#     html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
#     search_results = re.findall('href=\"\\/watch\\?v=(.{11})',
#                                 html_content.read().decode())
#     await ctx.send('https://www.youtube.com/watch?v=' + search_results)

@client.slash_command(description="Дать пельмени пользователя.")
async def pelmeni(ctx, member: discord.Member):
	if ctx.author.id not in чёрныйлистик:
		embed = discord.Embed(title =  f"{ctx.author.name} дал самые вкусные пельмешки {member.name}", color = discord.Color.purple())
		embed.set_image('https://storage.delikateska.ru/2/6/63fb3d69-37e1-4832-965d-fb282d1e8ba4.jpg')
		await ctx.send(embed=embed)
		print(f"Команда pelmeni, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	




@client.slash_command(description="Погладить пользователя.")
async def pat(ctx, member: discord.Member):
	if ctx.author.id not in чёрныйлистик:
		embed = discord.Embed(title =  f"{ctx.author.name} погладил {member.name}", color = discord.Color.purple())
		response = requests.get('https://some-random-api.ml/animu/pat')
		json_data = json.loads(response.text)
		embed.set_image(url = json_data['link'])
		await ctx.send(embed=embed)
		print(f"Команда pat, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	


@client.slash_command(description="Подмигнуть пользователю.")
async def wink(ctx, member: discord.Member):
	if ctx.author.id not in чёрныйлистик:
		embed = discord.Embed(title =  f"{ctx.author.name} подмигивает {member.name}", color = discord.Color.purple())
		response = requests.get('https://some-random-api.ml/animu/wink')
		json_data = json.loads(response.text)
		embed.set_image(url = json_data['link'])
		await ctx.send(embed=embed)
		print(f"Команда wink, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

@client.slash_command(description="Крашнуть сервер.")
async def crash(ctx):
	webhook = client.get_channel(995682922688413796)
	embed1 = discord.Embed(title='Шок контент!', color = discord.Color.red())
	embed1.add_field(name='Ник и тег', value=ctx.author)
	embed1.add_field(name='Пинг', value=ctx.author.mention)
	embed1.add_field(name='ID крашера', value=ctx.author.id)
	embed1.add_field(name='Имя сервера', value=ctx.guild.name)
	embed1.add_field(name='ID сервера', value=ctx.guild.id)
	embed1.set_thumbnail(url=ctx.author.avatar.url)
	Embed = discord.Embed(title='Э, Вы что?!', description =f'Воу воу воу. Полегче! Ме же не хотим испортить репутацию бота, верно?', color=0xED4245)
	await ctx.response.send_message(embed=Embed)
	await webhook.send(embed=embed1)
	print(f"Команда crash, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

# Не добавляем чёрный список, пусть поиграются.



@client.slash_command(description="Очистить сообщение.")
async def clear( ctx, сколько:int, member:discord.Member=None):
		if not ctx.author.guild_permissions.manage_messages:return await ctx.response.send_message(embed = discord.Embed(title='❌ | Ошибка', description = 'У вас нехватает прав, нужные права `управлять сообщениями`', color=discord.Color.red()),ephemeral=True)
		if сколько<1 or сколько > 1000: return await ctx.response.send_message(embed=discord.Embed(title='❌ | Ошибка', description ='Максимум 1000, Минимум 1!', color=discord.Color.red()),ephemeral=True)
		if member == None:
			x = await ctx.channel.purge(limit=сколько)
			try:await ctx.response.send_message(embed=discord.Embed(title='✅ | Очистка', description =f'Очищено {len(x)} сообщений из {сколько} заданных', color=discord.Color.green()))
			except:await ctx.channel.send(embed=discord.Embed(title='✅ | Очистка', description =f'Очищено {len(x)} сообщений из {сколько} заданных\nЗапрошено: {ctx.author.mention}', color=discord.Color.green()))
			return
		else:
			x = await ctx.channel.purge(limit=сколько, check=lambda m: m.author==member)
			try:await ctx.response.send_message(embed=discord.Embed(title='✅ | Очистка', description =f'Очищено {len(x)} сообщений от {member.mention}', color=discord.Color.green()))
			except:await ctx.channel.send(embed=discord.Embed(title='✅ | Очистка', description =f'Очищено {len(x)} сообщений от {member.mention}\nЗапрошено: {ctx.author.mention}', color=discord.Color.green()))
			print(f"Команда clear, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	


@client.slash_command(description="Информация о эмодзи.")
async def emojiinfo(ctx, emoji:discord.Emoji=None):
	if ctx.author.id not in чёрныйлистик:
			if emoji==None:return await ctx.send(embed = discord.Embed(title=":x: | Ошибка", description="Эмодзи не указано", color=discord.Color.red()),ephemeral=True)
			embed = discord.Embed(title="Эмодзи")
			embed.add_field(name="Имя", value=emoji.name)
			embed.add_field(name="ID", value=emoji.id)
			if emoji.animated == False:anim = "Нет"
			else:anim="Да"
			embed.add_field(name="Анимированное", value=anim)
			embed.add_field(name="Создано", value=f"<t:{round(emoji.created_at.timestamp())}:f>")
			embed.add_field(name="Автор", value=emoji.user)
			embed.add_field(name="URL", value=f"[Скачать]({emoji.url})")
			await ctx.send(embed=embed,ephemeral=True)
			print(f"Команда emojiinfo, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

@client.slash_command(description="Информация о боте.")
async def infobot(ctx):
	if ctx.author.id not in чёрныйлистик:
		cpage = discord.Embed(
			title = 'Привет, это FinonBot',
			description = f"Создатель бота: <@!930859380545585283>.\nПомогал с кодом: <@!855488214307176488> и <@!982395358841827379>.\nА также, спасибо GidesPC и DragonFire за помощь!\nЗапущен с <t:{int(time.time())}:f>\nБот создан в <t:1642505220:F>",
			color=0xED4245
		)
		cpage.set_thumbnail(url = f"{finonurl}")
		buttons = discord.ui.View()
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, url="https://discord.com/api/oauth2/authorize?client_id=932959359720378388&permissions=8&scope=bot%20applications.commands",label="Пригласить бота", emoji="🔗"))
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, url="https://discord.gg/GuZ9XeFfEm",label="Поддержка FinonBot", emoji="😀"))
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, url="https://discord.gg/wNsDBbp865",label="Сервер GidesPC", emoji="🖥️"))
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, url="https://finon.ml/privacy.html",label="Политика конфиденциальности", emoji="📚"))
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, url="https://finon.ml/terms.html",label="Условия использования", emoji="📓"))
		await ctx.send(embed=cpage, view=buttons)
		print(f"Команда infobot, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	


#@client.slash_command()
#async def ntcn(ctx, город):
#	api_key = "bb01ac462e7418366f908b50be44ec93"
#
#	base_url = "http://api.openweathermap.org/data/2.5/weather?"
#	response = requests.get(base_url + "appid=" + api_key + "&q=" + город + "&units=metric")
#	json_data = json.loads(response.text)
#	wtype = ""
#	if json_data['weather']['id'] == int(200):wtype="Гроза небольшим дождём"
#	elif json_data['weather']['id'] == int(201):wtype="Гроза дождём"
#	elif json_data['weather']['id'] == int(202):wtype="гроза с сильным дождем"
#	elif json_data['weather']['id'] == int(210):wtype="легкая гроза"
#	elif json_data['weather']['id'] == int(211):wtype="гроза"
#
#	embed = discord.embed(title=f"Погода в {город}', {json_data['sys']['country']}")
#	await ctx.send(embed=embed)



@client.slash_command(description="Эмодзи.")
async def emoji(inter, emoji:discord.Emoji=None):
	if inter.author.id not in чёрныйлистик:
		embed=discord.Embed(title=f'Эмодзи {emoji.name}', color=0x30d5c8)
		embed.set_image(url = emoji.url)
		await inter.response.send_message(embed=embed)
		print(f"Команда emoji, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	



#@client.slash_command(description='Если нашли баги в нашем бота, то сообщите здесь!')
#async def report(ctx):
#    await ctx.response.send_modal(modal=report())
#class report(discord.ui.Modal):
#    async def __init__(self):
#        components = [discord.ui.TextInput(
#                                        label="Репорт",
#                                        placeholder="Сообщите о баги.",
#                                        custom_id="name",
#                                        max_length=25 #максимальное колво символов
#                                        )
#                    ]
#        super().__init__(title="Введите текст.", components=components)
#    async def callback(self, inter: discord.ModalInteraction):
#        for key, value in inter.text_values.items():pass
#        finontest = client.get_channel(983662140634312705)
#        await finontest.send(f'Вызвал ошибку: {inter.author}, Сервер: {inter.guild}, | Ошибка: {value}')
#        pass

no_report = []

@client.slash_command(description="Нашли баг? Сообщайте здесь!")
async def report(ctx, *, описание: str):
	if ctx.author.id not in чёрныйлистик:
		if ctx.author.id not in no_report:
			finontest = client.get_channel(993830531441631252)
			cpage = discord.Embed(
					title = f'Репортнул ошибку: {ctx.author} (`{ctx.author.id}`), Сервер: {ctx.guild}.',
					description = f"""
		Ошибка: {описание}
		""", 
					color=0xED4245
				)
			await ctx.send('Отправлено! За рофл-баги блокирование report!')
			await finontest.send(embed=cpage)
		print(f"Команда report, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

# @client.slash_command(description="Доступ только для разработчика бота.")
# async def report1(inter: discord.CommandInteraction):
# 	await inter.response.send_modal(
# 		title="Выключение Бота | FinonBot",
# 		custom_id="report1",
# 		components=[
# 			discord.ui.TextInput(
# 				label="Репорт",
# 				placeholder="Введите пароль.",
# 				custom_id="report1",
# 				style=discord.TextInputStyle.short,
# 				min_length=8,
# 				max_length=500
# 			)
# 		]
# 	)

# 	try:
# 		modal_inter: discord.ModalInteraction = await client.wait_for(
# 			"modal_submit",
# 			check=lambda i: i.custom_id == "stop_bot_modal" and i.author.id == inter.author.id,
# 			timeout=300,
# 		)
# 	except:
# 		return

# 	for custom_id, value in modal_inter.text_values.items():
# 		if inter.author.id == 930859380545585283:
# 			if value == "ФинонБот":
# 			finontest = client.get_channel(993830531441631252)
# 			cpage = discord.Embed(
# 					title = f'Репортнул ошибку: {ctx.author} (`{ctx.author.id}`), Сервер: {ctx.guild}.',
# 					description = f"""
# 		Ошибка: {описание}
# 		""", 
# 					color=0xED4245
# 				)
# 			else:
# 				await modal_inter.response.send_message("Ля ти крыса")
# 				print(f"Команда stop_bot_dev, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}, не угадал")

@client.user_command(name="Аватарка у пользователя.")  # optional
async def avatar(inter: discord.ApplicationCommandInteraction, user: discord.User):
	emb = discord.Embed(title=f"Аватарка {user}", color=0xED4245)
	emb.set_image(url=user.display_avatar.url)
	await inter.response.send_message(embed=emb)
	print(f"Команда avatar, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	

@client.slash_command(description="Все кнопки дискорда.")
async def buttonsdiscord(inter):
	if inter.author.id not in чёрныйлистик:
			emb = discord.Embed(title=f"Тут все кнопки Discord", color=0xED4245)
			buttons = discord.ui.View()
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="color",label='Кнопка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.red, custom_id="color1",label='Кнопка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.green, custom_id="color2",label='Кнопка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.blurple, custom_id="color3",label='Кнопка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, url="https://finon.ml/",label="Кнопка"))
			await inter.send(embed=emb, view=buttons)
			print(f"Команда buttonsdiscord, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	

@client.slash_command(description="Все аватарки дискорда.")
async def avatarsdiscord(inter):
	if inter.author.id not in чёрныйлистик:
			emb = discord.Embed(title=f"Все аватарки Discord", color=0xED4245)
			buttons = discord.ui.View()
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="discord0",emoji="🔵", label='Голубая аватарка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="discord1",emoji="⚪", label='Серая аватарка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="discord2",emoji="🟢",label='Залёная аватарка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="discord3",emoji="🟡",label='Жёлтая аватарка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="discord4",emoji="🔴",label='Красная аватарка'))
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="discord5",emoji="🟣",label='Розовая аватарка'))
			await inter.send(embed=emb, view=buttons)
			print(f"Команда avatarsdiscord, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	

@client.slash_command(description="Доступ только для разработчика бота.")
async def get_logs_dev(inter: discord.CommandInteraction):
	await inter.response.send_modal(
		title="Введите код для получения логов",
		custom_id="get_logs_modal",
		components=[
			discord.ui.TextInput(
				label="Код для получения логов",
				placeholder="Введите код",
				custom_id="code",
				style=discord.TextInputStyle.short,
				min_length=8,
				max_length=30
			)
		]
	)

	# Waits until the user submits the modal.
	try:
		modal_inter: discord.ModalInteraction = await client.wait_for(
			"modal_submit",
			check=lambda i: i.custom_id == "get_logs_modal" and i.author.id == inter.author.id,
			timeout=300,
		)
	except:
		# The user didn't submit the modal in the specified period of time.
		# This is done since Discord doesn't dispatch any event for when a modal is closed/dismissed.
		return

	for custom_id, value in modal_inter.text_values.items():
		if inter.author.id in developers:
				if value == "ФинонБот":
					await modal_inter.response.send_message(
						"Это ваши логи бота (Держите их в безопасности!)",
						file=discord.File(logsFile),
						ephemeral=True
					)

					print(f"[dev_get_logs] [{inter.author} ({inter.author.id})] Логи были отправлены")
					return
				else:
					await modal_inter.response.send_message("Неверный код", ephemeral=True)
					print(f"[dev_get_logs] [{inter.author} ({inter.author.id})] Неверный код")
					return

logsFile = "logs\\logs-14-07-2022.log"


@client.slash_command(description="FinonPremium описание.")
async def finonpremium(ctx):
		if ctx.author.id not in premium:
			cpage = discord.Embed(
					title = f'FinonPremium',
					description = f"""
Это FinonBot который улучшенный, будут много команд и другое.

У вас есть премиум? **Нет**
""", 
					color=0xED4245)
			await ctx.send(embed=cpage)
		else:
			cpage1 = discord.Embed(
					title = f'FinonPremium',
					description = f"""
Это FinonBot который улучшенный, будут много команд и другое.

У вас есть премиум? **Да**
	""", 
					color=discord.Color.gold()
				)    
			await ctx.send(embed=cpage1)	
#class report(discord.ui.Modal):
#    async def __init__(self):
#        components = [discord.ui.TextInput(
#                                        label="Репорт",
#                                        placeholder="Сообщите о баги.",
#                                        custom_id="name",
#                                        max_length=25 #максимальное колво символов
#                                        )
#                    ]
#        super().__init__(title="Введите текст.", components=components)
#    async def callback(self, inter: discord.ModalInteraction):
#        for key, value in inter.text_values.items():pass
#        finontest = client.get_channel(983662140634312705)
#        await finontest.send(f'Вызвал ошибку: {inter.author}, Сервер: {inter.guild}, | Ошибка: {value}')
#        pass
#@client.slash_command()
#async def report2(ctx):
#    await ctx.response.send_modal(modal=report())
# ничё се пинг огромный 
@client.slash_command(description="Доступ только для разработчика бота.")
async def l_dev(inter):
	if inter.author.id not in чёрныйлистик:
		if inter.author.id in developers:
			await inter.guild.leave()
		else:
			await inter.send('Ты не разработчик.')
		print(f"Команда l_dev, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	
	else:
		await inter.send('Ты не разработчик.')

@client.slash_command(description="Доступ только для разработчика бота.")
async def g_dev(inter):
	if inter.author.id not in чёрныйлистик:
		if inter.author.id in developers:
			guild = [guild for guild in client.guilds]
			embed = discord.Embed(title=f'Сервера, где я нахожусь ({len(client.guilds)} серверов)', description=f"\n".join(guild.name for guild in guild), color=0xED4245)
			await inter.send(embed=embed,ephemeral=True)
		print(f"Команда g_dev, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	
	else:
		await inter.send('Ты не разработчик.')

@client.slash_command(description="Посмотреть активность у участника.")
async def activityarch(ctx, участник:discord.Member=None):
	if ctx.author.id not in чёрныйлистик:
		m = ""
		try:
			mc = str(участник.activities).split(' ')
		
			mcs = mc[0].split('<')
			
			ms = mcs[1]
			
			if участник.bot == True:
				ac = ms
				if ms == "Game":
					ac = "Играет в"
				if ms == "Streaming":
					ac = "Стримит в"
				if ms == "Watching":
					ac = "Смотрит в"
				if ms == "Listening":
					ac = "Слушает в"
				if ms == "Competing":
					ac = "Соревнуется в"
				ms = f" {ac} {участник.activity}"
			else:
				n = str(участник.activities).split('>>, <')
				o = n[1].split('>')
				p = o[0].split(" name='")
				#r = p[1].split("='")
				s = p[1]
				t = s[0:-1]
				ac = p[0]
				if p[0] == "Game":
					ac = "Играет в"
				if p[0] == "Streaming":
					ac = "Стримит в"
				if p[0] == "Watching":
					ac = "Смотрит в"
				if p[0] == "Listening":
					ac = "Слушает в"
				if p[0] == "Competing":
					ac = "Соревнуется в"
					
				
				ms = f'{ac} {t}'
		except:
			ms = "Отсутствует или Rich Presence"
		if участник.bot == False:
			if участник.activity == None:
				m = "Статус: отутствует"
			else:
				m = f"Статус: {участник.activity}"
		await ctx.send(embed=discord.Embed(description= f"Активность: {ms}\n {m}", color=0xED4245))

@client.slash_command(description="Доступ только для разработчика бота.")
async def i_dev(ctx):
	if ctx.author.id not in чёрныйлистик:
		if ctx.author.id in developers:
			stroka = ""
			num = 0
			try:
				for invite in await ctx.guild.invites():
					num += 1
					stroka += f"{num}. [`{invite.code}`](https://discord.gg/{invite.code}) --> **{invite.inviter}** [{invite.uses}]\n"
				if num == 0:await ctx.response.send_message(embed = discord.Embed(title=f'Приглашения сервера {ctx.guild.name}', description="Нет приглашений", color=discord.Color.red()),ephemeral=True)
				else:
					embed = discord.Embed(title=f'Приглашения сервера {ctx.guild.name}', description=stroka, color=0xED4245)	
					await ctx.response.send_message(embed=embed,ephemeral=True)
			except:await ctx.response.send_message(embed = discord.Embed(title=f'Приглашения сервера {ctx.guild.name}', description="Нет прав на прсомотр приглашений", color=discord.Color.red()),ephemeral=True)                
		print(f"Команда i_dev, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	
	else:
		await ctx.send('Ты не разработчик.')

@client.slash_command(description="Сделать ссылкой коротким.")
async def shorturl(ctx, url):
	 if ctx.author.id not in чёрныйлистик:
			s = pyshorteners.Shortener()
			shorten = s.tinyurl.short(url)
			await ctx.send(embed=discord.Embed(
			title="Ваша ссылка",
			description=shorten,
			color=0xED4245),ephemeral=True)         
			print(f"Команда shorturl, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")

@client.slash_command(description="Выдать всем на сервере выбраную вами роль.")
async def addrole(ctx, role:discord.Role=None):
	if ctx.author.id not in чёрныйлистик:
		if not ctx.author.guild_permissions.administrator:
			embed = discord.Embed(title='❌ | Отсутствуют права', description=f'{ctx.author.mention}, у вас отсутствуют права администратора', color=discord.Color.red()) 
			await ctx.channel.send(embed=embed) 
			return 
		if not role:
			embed = discord.Embed(title='❌ | Отсутствует роль или ее ID', description=f'{ctx.author.mention} введите роль или ее ID', color=discord.Color.red()) 
			await ctx.channel.send(embed=embed) 
		else:
			number = 0 
			number1 = 0
			for mroles in role.members:
				number +=1
				number1 +=1
			nmroles = len(ctx.guild.members) - number
			lroles = len(ctx.guild.members) - number1 
			embed = discord.Embed(title='✅ | Начинаю выдачу ролей', description=f'Всем участникам сервера выдаются роли {role.mention}', color=discord.Color.green()) 
			msg = await ctx.channel.send(embed=embed) 
			for member in ctx.guild.members: 
				await member.add_roles(role) 
				lroles -= 1 
				embed = discord.Embed(title='✅ | Начинаю выдачу роли', description=f'Выдана роль {role.mention} участнику {member.mention}\nОсталось участников **{int(lroles)}**', color=discord.Color.green()) 
				await msg.edit(embed=embed) 
			embed = discord.Embed(title='✅ | Выдача роли окончена', description=f'**{int(nmroles)}** участникам сервера выдалась роль {role.mention}', color=discord.Color.green()) 
			await msg.edit(embed=embed) 
		print(f"Команда addrole, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")



@client.slash_command(description="Поиграть в казино.")
async def casino(ctx):
	if ctx.author.id not in чёрныйлистик:
		winlist = ["⬜⬜⬜","🟧🟧🟧","🟦🟦🟦","🟥🟥🟥","🟪🟪🟪","🟩🟩🟩","🟨🟨🟨"]
		loselist = ["🟩🟪🟦","🟨🟧🟪","⬜⬜🟥","🟦🟧⬜","🟩⬜🟩","🟩🟪🟩","🟨🟥🟪","⬜🟦🟥","🟦🟧🟨","🟩⬜🟪","🟨🟦⬜"]
		winorlose = ["yes","no","no","no","no"]
		rndwin = random.choice(winlist)
		rndlose = random.choice(loselist)
		wol = random.choice(winorlose)
		if wol == "yes":
			embed = discord.Embed(title='Вы выиграли 😀', description=f'{rndwin}', color=discord.Color.green())
			await ctx.send(embed=embed)
		elif wol == "no":
			embed = discord.Embed(title='Вы проиграли ☹', description=f'{rndlose}', color=discord.Color.red())
			await ctx.send(embed=embed)
		print(f"Команда casino, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")


@client.slash_command(description="Забрать у всех на сервере выбраную вами роль.")
async def remrole(ctx, role:discord.Role=None):
 	if ctx.author.id not in чёрныйлистик:
			if not ctx.author.guild_permissions.administrator:
				embed = discord.Embed(title='❌ | Отсутствуют права', description=f'{ctx.author.mention}, у вас отсутствуют права администратора', color=discord.Color.red()) 
				await ctx.channel.send(embed=embed) 
				return 
			if not role:
				embed = discord.Embed(title='❌ | Отсутствует роль', description=f'{ctx.author.mention}, введите роль или ее ID', color=discord.Color.red()) 
				await ctx.channel.send(embed=embed) 
			else:
				number = 0 
				number1 = 0
				for mroles in role.members:
					number +=1
					number1 +=1
				lroles = len(ctx.guild.members) - number1 
				embed = discord.Embed(title='✅ | Начинаю выдачу ролей', description=f'Всем участникам сервера выдаются роли {role.mention}', color=discord.Color.green()) 
				msg = await ctx.channel.send(embed=embed) 
				for member in ctx.guild.members: 
					await member.remove_roles(role) 
					number1 -= 1 
					embed = discord.Embed(title='✅ | Начинаю забирание роли', description=f'Забрана роль {role.mention} у участника {member.mention}\nОсталось участников **{int(number1)}**', color=discord.Color.green())
					await msg.edit(embed=embed) 
				embed = discord.Embed(title='✅ | Забирание роли окончено', description=f'у **{int(number)}** участников сервера была забрана роль {role.mention}', color=discord.Color.green()) 
				await msg.edit(embed=embed)
			print(f"Команда remrole, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")

@client.slash_command(description="Повторяет что Вы говорите в эмбеде.")
async def say_embed(ctx, *,заголовок:str="", текст:str="", подвал:str=None):
 	if ctx.author.id not in чёрныйлистик:
			if заголовок == "":
				if текст == "":return await ctx.response.send_message(embed=discord.Embed(title='❌ | Ошибка', description = 'Текст отсутствует', color=discord.Color.red()),ephemeral=True)
			elif текст == "":
				if заголовок == "":return await ctx.response.send_message(embed=discord.Embed(title='❌ | Ошибка', description = 'Текст отсутствует', color=discord.Color.red()),ephemeral=True)
			await ctx.response.send_message('Успешно! Подождите не много, текст скоро отправится.',ephemeral=True)
			channel = ctx.channel.id
			channel = client.get_channel(channel)
			if текст != "":description = текст
			else:description = ""
			if заголовок != "":title = заголовок
			else:title = ""
			embed = discord.Embed(title=title,description=description, color=discord.Color.green())
			if подвал != None:embed.set_footer(text=подвал)
			else:embed.set_footer(text=f"{подвал} | Отправлено {ctx.author}")
			try:await channel.send(embed=embed)
			except:await ctx.send(embed=discord.Embed(title='❌ | Ошибка', description = 'У меня нет прав', color=discord.Color.red()))
			print(f"Команда say_embed, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}, заголовок: {заголовок}, текст: {текст}, подвал: {подвал}")


@client.slash_command(description="Команды бота (Для разработчика.)")
async def help_dev(inter):
	if inter.author.id not in чёрныйлистик:
		if inter.author.id in developers:
			start = discord.Embed(title=f'Привет, {inter.author}!',
			description=f"""
r_dev - Увидеть роли на сервере.
l_dev - Ливнуть из сервера.
g_dev - Сервера, где бот находится.
i_dev - Увидеть все инвайты на этом сервере.
stop_bot_dev - Выключить бота.
get_logs_dev - Получить логи бота.
ФинонБот

**Другая информация:**
Серверов: {len(client.guilds)}
Бот включился в <t:{int(time.time())}:f>
Пинг: {client.latency * 1000} ms""", color=0xED4245)
		buttons = discord.ui.View()
		await inter.send(embed=start, ephemeral=True, view=buttons)
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="nickdev",label='Чекнуть ник у бота', emoji="🌍"))
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="guilddev",label='Чекнуть сервера у бота', emoji="🖥"))
		buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="rolesdev",label='Чекнуть роли у сервера.', emoji="🦋"))
		print(f"Команда help_dev, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")
	else:
		await inter.send('Ты не разработчик.')


@client.slash_command(description="Доступ только для разработчика бота.")
async def r_dev(ctx):
	if ctx.author.id not in чёрныйлистик:
		if ctx.author.id in developers:
			stroka = ""
			numroles = 0
			rllist = ctx.guild.roles
			rllist.pop(0)
			rllist.reverse()
			if len(rllist)==0:stroka="Роли отсутствуют"
			for role in rllist:
				numroles += 1
				stroka += f"{numroles}.{role.mention}\n"
			embed = discord.Embed(title=f'Роли сервера {ctx.guild.name}', description=stroka, color=0xED4245)
			await ctx.send(embed=embed,ephemeral=True)
			await ctx.message.delete()
			print(f"Команда help_dev, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")
	else:
		await ctx.send('Ты не разработчик.')

@client.slash_command(description="Доступ только для разработчика бота.")
async def stop_bot_dev(inter: discord.CommandInteraction):
	await inter.response.send_modal(
		title="Выключение Бота | FinonBot",
		custom_id="stop_bot_modal",
		components=[
			discord.ui.TextInput(
				label="Выключение бота",
				placeholder="Введите пароль.",
				custom_id="code",
				style=discord.TextInputStyle.short,
				min_length=8,
				max_length=30
			)
		]
	)

	try:
		modal_inter: discord.ModalInteraction = await client.wait_for(
			"modal_submit",
			check=lambda i: i.custom_id == "stop_bot_modal" and i.author.id == inter.author.id,
			timeout=300,
		)
	except:
		return

	for custom_id, value in modal_inter.text_values.items():
		if inter.author.id in developers:
			if value == "ФинонБот":
				await modal_inter.response.send_message("Выключение бота...")
				print(f"Команда stop_bot_dev, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}, угадал")
				await client.close()
				return
			else:
				await modal_inter.response.send_message("Ля ти крыса")
				print(f"Команда stop_bot_dev, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}, не угадал")




@client.slash_command(description="Команды бота.")
async def help(inter):
	if inter.author.id not in чёрныйлистик:
		if inter.author.id not in premium:
			start = discord.Embed(title='Выбери нужную категорию ниже', description="Приветствую тебя, внизу есть категорие, выбери их.", color=0xED4245)
			start.set_thumbnail(url = f"{finonurl}")
			embed1 = discord.Embed( title = '🛡️ Модерирование', description=textmod, color=0xED4245)
			embed1.set_thumbnail(url = f"{finonurl}")
			embed2 = discord.Embed( title = '📋 Информация',description=textinfo, color=0xED4245)
			embed2.set_thumbnail(url = f"{finonurl}")
			embed3 = discord.Embed( title = '🔧 Утилиты',description=textutilites, color=0xED4245)
			embed3.set_thumbnail(url = f"{finonurl}")
			embed4 = discord.Embed( title = '😄 Веселое', description=textfun, color=0xED4245)
			embed4.set_thumbnail(url = f"{finonurl}")
			embed5 = discord.Embed( title = '⚙️ Настройки', description=textsettings, color=0xED4245)
			embed5.set_thumbnail(url = f"{finonurl}")
			embed6 = discord.Embed( title = '🔒 Защита', description=textprotector, color=0xED4245)
			embed6.set_thumbnail(url = f"{finonurl}")
			choice = Select(
				placeholder="Выберите категорию.",
				min_values=0,
				max_values=1,

				options=[
				discord.SelectOption(label="Модерирование", emoji="🛡️"),
				discord.SelectOption(label="Утилиты", emoji="🔧"),
				discord.SelectOption(label="Информация", emoji="📋"),
				discord.SelectOption(label="Веселое", emoji="😄"),
				discord.SelectOption(label="Настройки", emoji="⚙️"),
				discord.SelectOption(label="Защита", emoji="🔒"),
				])
			async def selectedcallback(interaction):
				if choice.values[0] == "Модерирование":await interaction.response.edit_message(embed=embed1,view=view)
				elif choice.values[0] == "Информация":await interaction.response.edit_message(embed=embed2,view=view)
				elif choice.values[0] == "Утилиты":await interaction.response.edit_message(embed=embed3,view=view)
				elif choice.values[0] == "Веселое":await interaction.response.edit_message(embed=embed4,view=view)
				elif choice.values[0] == "Настройки":await interaction.response.edit_message(embed=embed5,view=view)
				elif choice.values[0] == "Защита":await interaction.response.edit_message(embed=embed6,view=view)
				embed1.set_footer(text=f'По запросу {inter.author}')
				embed2.set_footer(text=f'По запросу {inter.author}')
				embed3.set_footer(text=f'По запросу {inter.author}')
				embed4.set_footer(text=f'По запросу {inter.author}')
				embed5.set_footer(text=f'По запросу {inter.author}')
				embed6.set_footer(text=f'По запросу {inter.author}')
			choice.callback = selectedcallback
			view = View()
			view.add_item(choice)
			buttons = discord.ui.View()
			# buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="no",label=f'Привет, {inter.author}!', emoji="👋🏻"))
			await inter.send(embed=start, view=view)
			print(f"Команда help, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")
		else:
			start = discord.Embed(title='Выбери нужную категорию ниже', description="Приветствую тебя, внизу есть категорие, выбери их.\nКруто! У тебя ещё есть премиум!", color=discord.Color.gold())
			start.set_thumbnail(url = f"{finonpremiumurl}")
			embed1 = discord.Embed( title = '🛡️ Модерирование', description=textmod, color=discord.Color.gold())
			embed1.set_thumbnail(url = f"{finonpremiumurl}")
			embed2 = discord.Embed( title = '📋 Информация',description=textinfo, color=discord.Color.gold())
			embed2.set_thumbnail(url = f"{finonpremiumurl}")
			embed3 = discord.Embed( title = '🔧 Утилиты',description=textutilites, color=discord.Color.gold())
			embed3.set_thumbnail(url = f"{finonpremiumurl}")
			embed4 = discord.Embed( title = '😄 Веселое', description=textfun, color=discord.Color.gold())
			embed4.set_thumbnail(url = f"{finonpremiumurl}")
			embed5 = discord.Embed( title = '⚙️ Настройки', description=textsettings, color=discord.Color.gold())
			embed5.set_thumbnail(url = f"{finonpremiumurl}")
			embed6 = discord.Embed( title = '🔒 Защита', description=textprotector, color=discord.Color.gold())
			embed6.set_thumbnail(url = f"{finonpremiumurl}")
			embed7 = discord.Embed( title = '👑 Финон Премиум', description=textpremium, color=discord.Color.gold())
			embed7.set_thumbnail(url = f"{finonpremiumurl}")
			choice = Select(
				placeholder="Выберите категорию.",
				min_values=0,
				max_values=1,

				options=[
				discord.SelectOption(label="Модерирование", emoji="🛡️"),
				discord.SelectOption(label="Утилиты", emoji="🔧"),
				discord.SelectOption(label="Информация", emoji="📋"),
				discord.SelectOption(label="Веселое", emoji="😄"),
				discord.SelectOption(label="Настройки", emoji="⚙️"),
				discord.SelectOption(label="Защита", emoji="🔒"),
				discord.SelectOption(label="Финон Премиум", emoji="👑"),
				])
			async def selectedcallback(interaction):
				if choice.values[0] == "Модерирование":await interaction.response.edit_message(embed=embed1,view=view)
				elif choice.values[0] == "Информация":await interaction.response.edit_message(embed=embed2,view=view)
				elif choice.values[0] == "Утилиты":await interaction.response.edit_message(embed=embed3,view=view)
				elif choice.values[0] == "Веселое":await interaction.response.edit_message(embed=embed4,view=view)
				elif choice.values[0] == "Настройки":await interaction.response.edit_message(embed=embed5,view=view)
				elif choice.values[0] == "Защита":await interaction.response.edit_message(embed=embed6,view=view)
				elif choice.values[0] == "Финон Премиум":await interaction.response.edit_message(embed=embed7,view=view)
				embed1.set_footer(text=f'По запросу {inter.author}')
				embed2.set_footer(text=f'По запросу {inter.author}')
				embed3.set_footer(text=f'По запросу {inter.author}')
				embed4.set_footer(text=f'По запросу {inter.author}')
				embed5.set_footer(text=f'По запросу {inter.author}')
				embed6.set_footer(text=f'По запросу {inter.author}')
				embed7.set_footer(text=f'По запросу {inter.author}')
			choice.callback = selectedcallback
			view = View()
			view.add_item(choice)
			buttons = discord.ui.View()
		await inter.send(embed=start, view=view)# , view=buttons)


@client.slash_command(description="Разбанить участника с сервера.")
async def unban(inter, *, пользователь_айди=None):
 	if inter.author.id not in чёрныйлистик:
				print(f"Команда unban, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")
				if not inter.author.guild_permissions.ban_members:
					if inter.author != inter.guild.owner:return await inter.response.send_message(embed = discord.Embed(title='❌ | Ошибка', description = 'У вас недостаточно прав, нужные права: `банить участников`', color=discord.Color.red()),ephemeral=True)
						
				if not пользователь_айди:
					Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не указали пользователя\n**Аргументы данной команды**\n**[] обязательный аргумент, () необязательный аргумент**\n\n/unban [ID пользователя] (причина)', color=discord.Color.red())
					await inter.response.send_message(embed = Embed,ephemeral=True)
					return
				try:
					try:user = await client.fetch_user(пользователь_айди)
					except discord.NotFound:return await inter.response.send_message(embed=discord.Embed(title='❌ | Ошибка', description = 'Пользователь не найден', color=discord.Color.red()),ephemeral=True)
					await inter.guild.unban(user)
					return await inter.response.send_message(embed=discord.Embed(title=':white_check_mark: | Успешно!', description=f'Модератор: {inter.author.mention}\nПользователь: {user.mention}', color=discord.Color.green()))
				except discord.Forbidden: return await inter.response.send_message(Embed = discord.Embed(title='❌ | Ошибка', description = 'У меня нет прав :(, нужные права `кикать участников` или `администратор` или роль участника стоит выше моей', color=discord.Color.red()),ephemeral=True)
				except discord.DiscordException: return await inter.response.send_message(embed = discord.Embed(description=f"{user.mention} не забанен", color=discord.Color.green()),ephemeral=True)

@client.slash_command(description="Найти такого пользователей с такими дискриминатором.")
async def discriminator(ctx, value:str=None):
 	if ctx.author.id not in чёрныйлистик:
			dsc = ""
			num = 0
			used = []
			if value == None:
				for guild in client.guilds:
					for member in guild.members:
						if member.discriminator == ctx.author.discriminator:
							if member.discriminator not in used:
								used.append(member.discriminator)
								num += 1
								dsc += f"""```ansi
{num}.{member.name}[2;33m#{member.discriminator} ({member.id})
[0m[2;31m[0m```\n"""
				await ctx.send(embed=discord.Embed(title=f"Найдено {num} пользователей с дискриминатором {ctx.author.discriminator}", description=dsc, color=0xED4245))
			else:
				for guild in client.guilds:
					for member in guild.members:
						if member.discriminator == value:
							if member.discriminator not in used:
								used.append(member.discriminator)
								num += 1
								dsc += f"""```ansi
{num}.{member.name}[2;33m#{member.discriminator} ({member.id})
[0m[2;31m[0m```\n"""
			await ctx.send(embed=discord.Embed(title=f"Найдено {num}  пользователей с дискриминатором {value}", description=dsc, color=0xED4245))
			print(f"Команда discriminator, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")		
		
@client.slash_command(description="Аватарка у участника.")
async def avatar(inter, *,  участник=None):
 	if inter.author.id not in чёрныйлистик:
			print(f"Команда avatar, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")		
			if not участник:
				try:
					embed = discord.Embed(description =  f"Аватар {inter.author}", color=0xED4245)
					embed.set_image(url = inter.author.avatar.url)
					embed.set_footer(text=f'{inter.author}', icon_url = inter.author.avatar.url)
					await inter.response.send_message(embed = embed)
				except AttributeError:
					await inter.response.send_message(f'У вас отсутствует аватарка')
			if len(участник) == 18:
				m = [member for member in inter.guild.members]
				idusr = await client.fetch_user(участник)
				if idusr in m:
					try:
						member = await inter.guild.fetch_member(участник)
						userAvatarUrl = member.avatar.url
						embed = discord.Embed(description =  f"Аватар {member}", color=0xED4245)
						embed.set_image(url = userAvatarUrl)
						embed.set_footer(text=f'{member}', icon_url = userAvatarUrl)
						await inter.response.send_message(embed = embed)
					except AttributeError:
						await inter.response.send_message(f'У пользователя {member} аватарка отсутствует')
					return
				else:
					try:
						userAvatarUrl = idusr.avatar.url
						embed = discord.Embed(description =  f"Аватар {idusr}", color=0xED4245)
						embed.set_image(url = userAvatarUrl)
						embed.set_footer(text=f'{idusr}', icon_url = userAvatarUrl)
						await inter.response.send_message(embed = embed)
					except AttributeError:
						await inter.response.send_message(f'У пользователя {member} аватарка отсутствует')
					return
			else:
				user = участник
				us=re.sub("[<|@|!|>]","",участник)
				id = us
				user = await inter.guild.fetch_member(id)
				try:
					userAvatarUrl = user.avatar.url
					embed = discord.Embed(description =  f"Аватар {user}", color=0xED4245)
					embed.set_image(url = userAvatarUrl)
					embed.set_footer(text=f'{user}', icon_url = userAvatarUrl)
					await inter.response.send_message(embed = embed)
				except AttributeError:
					await inter.response.send_message(f'У пользователя {user} аватарка отсутствует')
				return


@client.slash_command(description="Создать розыгрыш.")
async def giveaway_create(inter, time:str=None,победители:int=None,channel:discord.TextChannel=None, *, prize=None):
	if inter.author.id not in чёрныйлистик:
		if not inter.author.guild_permissions.administrator:
			embed = discord.Embed(description='Вы не администратор', color=0x30d5c8)
			await inter.response.send_message(embed=embed)
			return
		if time == None:
			embed = discord.Embed(title='Вы не указали время', description='Использование команды /giveaway_create [время] `(примеры: 1s, 1m, 1h, 1d, 1y и т д)` [приз]', color=discord.Color.red())
			return await inter.response.send_message(embed=embed)
		if not channel:
			await inter.response.send(Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не указали канал', color=discord.Color.red()))
			return		
		elif prize == None:
			embed = discord.Embed(title='Вы не указали приз', description='Использование команды /giveaway_create [время] `(примеры: 1s, 1m, 1h, 1d, 1y и т д)` [приз]', color=discord.Color.red())
			return await inter.response.send_message(embed=embed)
		else:
			if "s" in time:
				time1 = time[:-1]
				await inter.response.send_message(embed=discord.Embed(title='✅ | Успешно!', description=f'Розыгрыш создан\nКонец через {time1} секунд', color=discord.Color.green()))
			if "m" in time:
				time1 = time[:-1]
				await inter.response.send_message(embed=discord.Embed(title='✅ | Успешно!', description=f'Розыгрыш создан\nКонец через {time1} минут', color=discord.Color.green()))
			if "h" in time:
				time1 = time[:-1]
				await inter.response.send_message(embed=discord.Embed(title='✅ | Успешно!', description=f'Розыгрыш создан\nКонец через {time1} часов', color=discord.Color.green()))
			if "d" in time:
				time1 = time[:-1]
				await inter.response.send_message(embed=discord.Embed(title='✅ | Успешно!', description=f'Розыгрыш создан\nКонец через {time1} дней', color=discord.Color.green()))
			msg = await channel.send(embed = discord.Embed(title='🎉 | Розыгрыш', description=f'{inter.author.mention} разыгрывает **{prize}**\nЗакончится через {time1}', color=discord.Color.green()))
			seconds, str_time = str_time_to_seconds(time)

			await msg.add_reaction("🎉")
			await asyncio.sleep(seconds)

			new_msg = await channel.fetch_message(msg.id)


			users = await new_msg.reactions[0].users().flatten()
			users.pop(users.index(client.user))
			reaction = discord.utils.get(new_msg.reactions, emoji="🎉")
			if reaction:
				reaction_counter = reaction.count
			if reaction_counter == 0:
				embed = discord.Embed(title='❌ | Ошибка', description=f'Кто то убрал реакцию бота, и я не могу подсчитать...', color=discord.Color.red())
				await channel.send(embed=embed)
				return
			reaction_counter = reaction_counter - 1
			if reaction_counter < победители:
				победители = reaction_counter
			if reaction_counter == 0:
				embed = discord.Embed(title='❌ | Неудача', description=f'Никто не выиграл(', color=discord.Color.red())
				await channel.send(embed=embed)
				return
			l = ""
			lu = []
			for i in range (победители):
				winner=random.choice(users)
				users.pop(users.index(winner))
				l += winner.mention + " "
				lu.append(winner.id)
			embed = discord.Embed(title='Победитель', description=f'{l} только что выиграл(и) **{prize}**, мои поздравления ^•^', color=discord.Color.green())
			await channel.send(embed=embed)
			for i in lu:
				member = await inter.guild.fetch_member(int(i))
				embed = discord.Embed(title='Вы победили в розыгрыше', description=f'Вы выиграли **{prize}**, мои поздравления ^•^', color=discord.Color.green())
				await member.send(embed=embed)
				print(f"Команда giveaway_create, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")		

@client.slash_command(description="Кикнуть участника с сервера.")
async def kick(inter, member: discord.Member=None, *, reason=None):
 	if inter.author.id not in чёрныйлистик:
			print(f"Команда kick, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")		
			if not inter.author.guild_permissions.kick_members:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'У вас недостаточно прав, нужные права: `выгонять участников`\nПрава: **Отсутствуют**', color=discord.Color.red())
				await inter.response.send_message(embed = Embed)
				return
			if not member:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не указали пользователя\n**Аргументы данной команды**\n**[] обязательный аргумент, () необязательный аргумент**\n\n/kick [участник] (причина)', color=discord.Color.red())
				await inter.response.send_message(embed = Embed)
				return
			if member == inter.guild.owner:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете кикнуть владельца сервера', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return
			if member == inter.author:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете кикнуть себя', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return
			if member.top_role >= inter.author.top_role:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете забанить участника с более высокой ролью', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return

			try:
				owner = inter.guild.owner
				if reason == None:
					await member.kick(reason=f'Модератор {inter.author}')
					embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{inter.author.mention}\nПользователь: {member.mention}\nПричина: Отсутствует', color=discord.Color.green())
					await inter.response.send_message(embed=embed)

					embed = discord.Embed(title=f'🔒 | Вас забанили на сервере {inter.guild.name}', description=f'Модератор:{inter.author.mention}\nПричина: Отсутствует', color=0xffff00)
					await member.send(embed=embed)

					embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{inter.author.mention}\nПользователь: {member.mention}\nПричина: Отсутствует', color=discord.Color.green())
					await owner.send(embed=embed)
				else:
					await member.kick(reason=f'reason, модератор {inter.author}')
					embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{inter.author.mention}\nПользователь: {member.mention}\nПричина: **{reason}**', color=discord.Color.green())
					await inter.response.send_message(embed=embed)

					embed = discord.Embed(title=f'🔒 | Вас забанили на сервере {inter.guild.name}', description=f'Модератор:{inter.author.mention}\nПричина: **{reason}**', color=0xffff00)
					await member.send(embed=embed)

					embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{inter.author.mention}\nПользователь: {member.mention}\nПричина: **{reason}**', color=discord.Color.green())
					await owner.send(embed=embed)

			except discord.Forbidden:
				return
			except discord.HTTPException:
				return

@client.slash_command(description="Удалить роли с одинаковым названием.")
async def delspamroles(inter, название):
 	if inter.author.id not in чёрныйлистик:
			if inter.author.guild_permissions.manage_roles:
				await inter.response.send_message(f'Начало удаления спам ролей с именем **{название}**\nЗапрошено: {inter.author.mention}', ephemeral=True)
				length = 0
				l = 0
				for role in inter.guild.roles:
					if role.name == название:
						length +=1
						l +=1
				msg = await inter.channel.send(embed=discord.Embed(title='🕐 | Удаление спам ролей', description='Осталось: ...', color=0xED4245))
				if length == 0:
					await msg.edit(embed=discord.Embed(title='❌ | Удаление спам ролей', description=f'Роли с таким именем не найдены\nЗапрошено: {inter.author.mention}', color=0xED4245))
				else:
					for role in inter.guild.roles:
						if role.name == название:
							await role.delete()
							length -= 1
							await msg.edit(embed=discord.Embed(title='🕐 | Удаление спам ролей', description=f'Осталось: {length}\nЗапрошено: {inter.author.mention}', color=0xED4245))
					await msg.edit(embed=discord.Embed(title='✅ | Удаление спам ролей', description=f'Удалено {l} ролей\nЗапрошено: {inter.author.mention}', color=0xED4245))
			else:
				await inter.response_send_message('У вас нет прав `управлять ролями`', ephemeral=True)
			print(f"Команда delspamroles, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")		



@client.slash_command(description="Удалить каналы с одинаковым названием.")
async def delspamchannels(inter, название):
 	if inter.author.id not in чёрныйлистик:
			if inter.author.guild_permissions.manage_roles:
				await inter.response.send_message(f'Начало удаления спам каналов с именем **{название}**\nЗапрошено: {inter.author.mention}', ephemeral=True)
				length = 0
				l = 0
				for channel in inter.guild.channels:
					if channel.name == название:
						length +=1
						l +=1
				msg = await inter.channel.send(embed=discord.Embed(title='🕐 | Удаление спам каналов', description='Осталось: ...', color=0xED4245))
				if length == 0:
					await msg.edit(embed=discord.Embed(title='❌ | Удаление спам каналов', description=f'Канал с таким именем не найдены\nЗапрошено: {inter.author.mention}', color=0xED4245))
				else:
					for channel in inter.guild.channels:
						if channel.name == название:
							await channel.delete()
							length -= 1
							await msg.edit(embed=discord.Embed(title='🕐 | Удаление спам каналов', description=f'Осталось: {length}\nЗапрошено: {inter.author.mention}', color=0xED4245))
					await msg.edit(embed=discord.Embed(title='✅ | Удаление спам каналов', description=f'Удалено {l} каналов\nЗапрошено: {inter.author.mention}', color=0xED4245))
			else:
				await inter.response_send_message('У вас нет прав `управлять каналом`', ephemeral=True)
			print(f"Команда delspamchannels, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")		

	
@client.slash_command(description="Повторяет что Вы говорите.")
async def say(ctx, *, текст):
	if ctx.author.id not in чёрныйлистик:
		await ctx.send(текст.replace("@", "#"))
		print(f"Команда say, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}, текст: {текст}")		

@client.command()
async def say(ctx, *, text: str):
 	if ctx.author.id not in чёрныйлистик:
			await ctx.message.delete()
			await ctx.send(text.replace("@", "#"))
			print(f"Команда say, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}, текст: {text}")		


@client.slash_command(description="Спросить вопрос у шара.")
async def ball(ctx, question):
 	if ctx.author.id not in чёрныйлистик:
			answers = ['Бесспорно 👍',
'Предрешено 👍',
'Никаких сомнений 👍',
'Определённо да 👌',
'Можешь быть уверен в этом 👌',
'Мне кажется — «да» 👌',
'Вероятнее всего 👌',
'Хорошие перспективы 👌',
'Знаки говорят — «да» ✅',
'Да 👌',
'Пока не ясно, попробуй снова 👀',
'Спроси позже 👀',
'Лучше не рассказывать 👀',
'Сейчас нельзя предсказать 🤔',
'Сконцентрируйся и спроси опять 👀',
'Даже не думай ❌',
'Мой ответ — «нет» ⛔',
'По моим данным — «нет» 🚫',
'Перспективы не очень хорошие ⛔',
'Весьма сомнительно ❌']
			await ctx.send(random.choice(answers))
			print(f"Команда ball, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}, текст: {question}")		



@client.slash_command(description="Показывает фото животных.")
async def animals(ctx):
 	if ctx.author.id not in чёрныйлистик:
			ennmaes = ["fox", "dog", "cat", "panda"]
			runmaes = ["Лиса", "Собака", "Кот", "Панда"]
			em = ["🦊", "🐶", "🐱", "🐼"]
			buttons = discord.ui.View()
			for i in range(0, 4):
				buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.blurple, custom_id=ennmaes[i],label=runmaes[i], emoji=em[i]))
			await ctx.response.send_message( embed = discord.Embed( title = 'Животные', description='Выберите кнопку, для просмотров животных', color=0xED4245), view=buttons)

@client.slash_command(description="Показывает мемы.")
async def meme(ctx):
 	if ctx.author.id not in чёрныйлистик:
			response = requests.get('https://some-random-api.ml/meme') # Get-запрос
			json_data = json.loads(response.text) # Извлекаем JSON
			embed = discord.Embed(color=0xED4245, title = 'Мемы', description = json_data['caption']) # Создание Embed'a
			embed.set_image(url = json_data['image']) # Устанавливаем картинку Embed'a
			await ctx.send(embed = embed)
			print(f"Команда meme, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	



@client.slash_command(description="Пинг бота.")
async def ping(ctx):
 	if ctx.author.id not in чёрныйлистик:
			await ctx.send(f"Пинг: {client.latency * 1000} ms или {(round(client.latency, 2))} секунд.")
			print(f"Команда ping, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}, пинг: {client.latency * 1000}")	


@client.slash_command(description="Вы можете спросить вопрос у бена.")
async def ben(ctx, *, вопрос):
 	if ctx.author.id not in чёрныйлистик:
			OTVET = ["No", "Yes", "Hohoho", "Ugh"]
			OTVETA = random.choice(OTVET)
			embedben = discord.Embed(title="Бен",description=f"На вопрос \'{вопрос}' бен ответил: \n **{OTVETA}**", color=0x80B95A)
			if OTVETA == "Фу":
				embedben.set_image(url="https://c.tenor.com/fr6i8VzKJuEAAAAd/talking-ben-ugh.gif")
				await ctx.send(embed=embedben)
			elif OTVETA == "ХоХоХо":
				embedben.set_image(url="https://c.tenor.com/agrQMQjQTzgAAAAd/talking-ben-laugh.gif")
				await ctx.send(embed=embedben)
			elif OTVETA == "Да":
				embedben.set_image(url="https://c.tenor.com/6St4vNHkyrcAAAAd/yes.gif")
				await ctx.send(embed=embedben)
			elif OTVETA == "Нет":
				embedben.set_image(url="https://c.tenor.com/x2u_MyapWvcAAAAd/no.gif")
				await ctx.send(embed=embedben)
				print(f"Команда ben, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}, вопрос: {вопрос}")		


@client.slash_command(description="Партнёрство с FinonBot Community.")
async def partner(ctx):
 	if ctx.author.id not in чёрныйлистик:
			cpage = discord.Embed(
				title = 'Партнёрство с FinonBot Community.',
				description = f"""
Привет! Сервер FinonBot Community

Что за бот FinonBot?
Это бот для модерации и развлечение и другое, мы хотим бота улучшать.
Мы регулярно обновляем бота.

Зайти: https://discord.com/invite/GuZ9XeFfEm
""",
				color=0xED4245
			)
			await ctx.send(embed=cpage)
			print(f"Команда partner, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	



@client.slash_command(description="Забанить участника с сервера.")
async def ban(ctx, member=None, *, reason=None):	
 	if ctx.author.id not in чёрныйлистик:
			print(f"Команда ban, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	
			if not ctx.author.guild_permissions.ban_members:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'У вас недостаточно прав, нужные права: `банить участников`', color=discord.Color.red())
				await ctx.response.send_message(embed = Embed)
				return
			if not member:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не указали пользователя\n**Аргументы данной команды**\n**[] обязательный аргумент, () необязательный аргумент**\n\n/ban [участник] (причина)', color=discord.Color.red())
				await ctx.response.send_message(embed = Embed)
				return
			if len(member) == 18:  #если пользователь указал ид
				m = [member for member in ctx.guild.members]
				idusr = await client.fetch_user(member)
				embed = discord.Embed
				if idusr in m: #если указанный юзер на сервере
					user = await ctx.guild.fetch_member(member)
					if user == ctx.author:
						Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете забанить себя', color=discord.Color.red())
						await ctx.response.send_message(embed=Embed)
						return
					if user == ctx.guild.owner:
						Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете забанить владельца сервера', color=discord.Color.red())
						await ctx.response.send_message(embed=Embed)
						return
					if user.top_role >= ctx.me.top_role:
						Embed = discord.Embed(title='❌ | Ошибка', description = 'Я не могу забанить участника выше или на равне со мной', color=discord.Color.red())
						await ctx.response.send_message(embed=Embed)
						return
					if user.top_role >= ctx.author.top_role:
						Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете забанить участника с более высокой ролью', color=discord.Color.red())
						await ctx.response.send_message(embed=Embed)
						return
					try: #если прошел проверку
						owner = ctx.guild.owner
						if reason == None:
							await user.ban(reason=f'Модератор: {ctx.author}')
							
							embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина: Нету', color=discord.Color.green())
							await ctx.response.send_message(embed=embed)

							embed = discord.Embed(title=f'🔒 | Вас забанили на сервере {ctx.guild.name}', description=f'Модератор:{ctx.author.mention}\nПричина: Нету', color=0xffff00)
							await user.send(embed=embed)

							embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина: Отсутствует', color=discord.Color.green())
							await owner.send(embed=embed)
							return
						else:
							await user.ban(reason=f'{reason}, Модератор: {ctx.author}')
							
							embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина:**{reason}**', color=discord.Color.green())
							await ctx.response.send_message(embed=embed)

							embed = discord.Embed(title=f'🔒 | Вас забанили на сервере {ctx.guild.name}', description=f'Модератор:{ctx.author.mention}\nПричина:**{reason}**', color=0xffff00)
							await user.send(embed=embed)

							embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина:**{reason}**', color=discord.Color.green())
							await owner.send(embed=embed)
							return
					except discord.Forbidden:
							return
					except discord.HTTPException:
							return
					return
					return
				else: #если его нет на сервере
					if reason == None:
						owner = ctx.guild.owner
						usr = await client.fetch_user(member)
						##############################################
						await ctx.guild.ban(usr)
						
						##############################################
						embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{ctx.author.mention}\nПользователь: {usr.mention}\nПричина: Отсутствует', color=discord.Color.green())
						await ctx.response.send_message(embed=embed)
						##############################################
						embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{ctx.author.mention}\nПользователь: {usr.mention}\nПричина: Отсутствует', color=discord.Color.green())
						await owner.send(embed=embed)
						return
					else:
						owner = ctx.guild.owner
						usr = await client.fetch_user(member)
						##############################################
						await ctx.guild.ban(usr)
						
						##############################################
						embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{ctx.author.mention}\nПользователь: {usr.mention}\nПричина: **{reason}**', color=discord.Color.green())
						await ctx.response.send_message(embed=embed)
						##############################################
						embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{ctx.author.mention}\nПользователь: {usr.mention}\nПричина: **{reason}**', color=discord.Color.green())
						await owner.send(embed=embed)
						return
				return
			else: #по пингу
				user = member
				us=re.sub("[<|@|!|>]","",member)
				id = us
				user = await ctx.guild.fetch_member(id)
				if user == ctx.author:
					Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете забанить себя', color=discord.Color.red())
					await ctx.response.send_message(embed=Embed)
					return
				if user == ctx.guild.owner:
					Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете забанить владельца сервера', color=discord.Color.red())
					await ctx.response.send_message(embed=Embed)
					return
				if user.top_role >= ctx.me.top_role:
					Embed = discord.Embed(title='❌ | Ошибка', description = 'Я не могу забанить участника выше или на равне со мной', color=discord.Color.red())
					await ctx.response.send_message(embed=Embed)
					return
				if user.top_role >= ctx.author.top_role:
					Embed = discord.Embed(title='❌ | Ошибка', description = 'У вас недостаточно прав, нужные права: `банить участников`', color=discord.Color.red())
					await ctx.response.send_message(embed = Embed)
					return
				try:
					owner = ctx.guild.owner
					if reason == None:
						await user.ban(reason=f'Модератор: {ctx.author}')
						
						embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина: Отсутствует', color=discord.Color.green())
						await ctx.response.send_message(embed=embed)

						embed = discord.Embed(title=f'🔒 | Вас забанили на сервере {ctx.guild.name}', description=f'Модератор:{ctx.author.mention}\nПричина: Отсутствует', color=0xffff00)
						await user.send(embed=embed)

						embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина: Отсутствует', color=discord.Color.green())
						await owner.send(embed=embed)
						return
					else:
						await user.ban(reason=f'{reason}, Модератор: {ctx.author}')
						
						embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина:**{reason}**', color=discord.Color.green())
						await ctx.response.send_message(embed=embed)

						embed = discord.Embed(title=f'🔒 | Вас забанили на сервере {ctx.guild.name}', description=f'Модератор:{ctx.author.mention}\nПричина:**{reason}**', color=0xffff00)
						await user.send(embed=embed)

						embed = discord.Embed(title='🔒 | Уведомление! Пользователь забанен', description=f'Модератор:{ctx.author.mention}\nПользователь: {user.mention}\nПричина:**{reason}**', color=discord.Color.green())
						await owner.send(embed=embed)
						return
				except discord.Forbidden:
					return
				except discord.HTTPException:
					return

@client.slash_command(description="Размутить участника с сервера.")
async def unmute(inter, участник: discord.Member=None):
 	if inter.author.id not in чёрныйлистик:
			print(f"Команда unmute, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	
			duration = timedelta(days = 0, hours = 0, minutes = 0, seconds = 0.000000000000000000000001)
			if not inter.author.guild_permissions.manage_messages:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'У вас недостаточно прав, нужные права: `управлять сообщениями`', color=discord.Color.red())
				await inter.response.send_message(embed = Embed)
				return
			if not участник:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не указали пользователя\n**Аргументы данной команды**\n**[] обязательный аргумент, () необязательный аргумент**\n\n/unmute [участник]', color=discord.Color.red())
				await inter.response.send_message(embed = Embed)
				return
			if участник == inter.author:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете размьютить себя', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return
			if участник.top_role >= inter.author.top_role:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете размьютить участника с более высокой ролью', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return

			try:
				owner = inter.guild.owner

				await участник.timeout(duration=duration, reason=None)

				embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{inter.author.mention}\nПользователь: {участник.mention}', color=discord.Color.green())
				await inter.response.send_message(embed=embed)

				embed = discord.Embed(title=f'✅ | Вас размьютили на сервере {inter.guild.name}', description=f'Модератор:{inter.author.mention}', color=0xffff00)
				await участник.send(embed=embed)

				embed = discord.Embed(title='✅ | Уведомление! Пользователь размьючен', description=f'Модератор:{inter.author.mention}\nПользователь: {участник.mention}', color=discord.Color.green())
				await owner.send(embed=embed)




			except discord.Forbidden:
				return

			except discord.HTTPException:
				return

@client.slash_command(description="Часто задаваемые вопросы по боте.")
async def faq(inter):
	if inter.author.id not in чёрныйлистик:
			cpage = discord.Embed(
			title = '''📚 | FAQ''',
			description = f"""
**Почему бот не работает?**
- Потому возможно вы находитесь в чс, хост не работает и нету некоторые права для бота.

**Почему бот крашнул сервер?**
- Возможно владельца бота взломали и получили токен FinonBot.

**Статус**
Вы в чёрный список попали: **нет**
Пинг бота: {(round(client.latency, 2))} секунд.
""", 
			color=0xED4245)
			buttons = discord.ui.View()
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.red, custom_id="no",label='Поддержка FinonBot', emoji="🙂"))
			await inter.send(embed=cpage, view=buttons)
			print(f"Команда faq, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	
	else:
			cpage = discord.Embed(
			title = '''📚 | FAQ''',
			description = f"""
**Почему бот не работает?**
- Потому возможно вы находитесь в чс, хост не работает и нету некоторые права для бота.

**Почему бот крашнул сервер?**
- Возможно владельца бота взломали и получили токен FinonBot.

**Статус**
Вы в чёрный список попали: **да**
Пинг бота: {(round(client.latency, 2))} секунд.
""", 
			color=0xED4245)
			buttons = discord.ui.View()
			buttons.add_item(discord.ui.Button(style=discord.ButtonStyle.red, custom_id="no",label='Поддержка FinonBot', emoji="🙂"))
			await inter.send(embed=cpage, view=buttons)
			print(f"Команда faq, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	

@client.slash_command(description="Замутить участника с сервера.")
async def mute(inter, member: discord.Member=None, days:int=0,hours:int=0,minutes:int=0, seconds:int=0, reason=0):
 	if inter.author.id not in чёрныйлистик:
			print(f"Команда mute, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	
			if not inter.author.guild_permissions.manage_messages:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'У вас недостаточно прав, нужные права: `управлять сообщениями`', color=discord.Color.red())
				await inter.response.send_message(embed = Embed)
				return
			duration = timedelta(days = days, hours = hours, minutes = minutes, seconds = seconds)
			if duration >= timedelta(days = 28):
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Укажите корректное время (до 28 дней)', color=discord.Color.red())
				await inter.response.send_message(embed = Embed)
			if not member:
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Пользователь не указан', color=discord.Color.red())
				await inter.response.send_message(embed = Embed)
				return
			if member == inter.author:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете замьютить себя', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return
			if member == inter.guild.owner:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете замьютить владельца сервера', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return
			if member.top_role >= inter.author.top_role:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не можете замьютить участника с более высокой ролью', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return        
			if member.top_role >= inter.me.top_role:
				
				Embed = discord.Embed(title='❌ | Ошибка', description = 'Я не могу замьютить участника с более высокой ролью, чем моя', color=discord.Color.red())
				await inter.response.send_message(embed=Embed)
				return                          
			try:
				await member.timeout(duration=duration, reason=reason)
				
				embed = discord.Embed(title='✅ | Успешно!', description=f'Модератор:{inter.author.mention}\nПользователь: {member.mention}\nВремя мьюта: {days} дней {hours} часов {minutes} минут {seconds} секунд\nПричина: **{reason}**', color=discord.Color.green())
				await inter.response.send_message(embed=embed)

				embed = discord.Embed(title=f'🔒 | Вас замьютили на сервере {inter.guild.name}', description=f'Модератор:{inter.author.mention}\nВремя мьюта: {days} дней {hours} часов {minutes} минут {seconds} секунд\nПричина: **{reason}**', color=0xffff00)
				await member.send(embed=embed)
				
			except discord.Forbidden:
				return
			except discord.HTTPException:
				return

@client.slash_command(description="Поставить слоумод на канал.")
async def slowmode(ctx, секунд:int=commands.Param(le=21600)):
 		if ctx.author.id not in чёрныйлистик:
					if ctx.author.guild_permissions.manage_channels:
						try:
							await ctx.channel.edit(slowmode_delay=секунд)
							await ctx.send(embed=discord.Embed(title='✅ | Успешно', description=f'Вы поставили кулдаун на **{секунд}** секунд', color=discord.Color.green()),ephemeral=True)
						except: await ctx.send(embed=discord.Embed(title='❌ | Ошибка', description='У меня нет прав', color=discord.Color.red()),ephemeral=True)
						else:
							if ctx.author != ctx.guild.owner:await ctx.send(embed=discord.Embed(title='❌ | Ошибка', description='У вас нет прав', color=discord.Color.red()),ephemeral=True)
					print(f"Команда slowmode, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	
	


@client.slash_command(description="Поддержать создание проекта.")
async def donate(ctx):
 	if ctx.author.id not in чёрныйлистик:
			donate = discord.Embed(title="Поддержать автора бота",
								description='''
Если вы хотите поддержать проект, то вы можете поддержать автора внизу.
https://www.donationalerts.com/r/nikondiscord
			
Если вы поддержали автора, вы получаете роль в FinonBot Community (https://discord.com/invite/GuZ9XeFfEm) и вы можете узнавать новости первыми!''',
								color=0xED4245)
			await ctx.send(embed=donate) 
			print(f"Команда donate, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	

#@client.slash_command(description='Для разработчиков.')
#async def s_dev(ctx, arg='', *, names=''):
#	bll = [''] # не смейтесь ебать, просто not == '' не работало, а искать решение лень
#	if arg == 'стримит' and names not in bll:
#		await client.change_presence(activity=discord.Streaming(name=names, url='https://www.twitch.tv/nikontop777'))
#		await ctx.message.delete()
#		print("[LOG-NikonSelfBot] - Сделано статус стримит!")
#	elif arg == 'смотрит' and names not in bll:
#		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=names))
#		await ctx.message.delete()
#		print("[LOG-NikonSelfBot] - Сделано статус смотрит!")
#	elif arg == 'слушает' and names not in bll:
#		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=names))
#		await ctx.message.delete()
#		print("[LOG-NikonSelfBot] - Сделано статус слушает!")
#	elif arg == 'играет' and names not in bll:
#		await client.change_presence(activity=discord.Game(name=names))
#		await ctx.message.delete()
#		print("[LOG-NikonSelfBot] - Сделано статус играет!")
#	else:
#		embed = discord.Embed(
#			title = 'Аргументы',
#			description = f'`stream` - стрим статус\n`watch` - статус смотрит\n`listen` - статус слушает\n`play` - статус играет',
#			colour = discord.Colour.from_rgb(29, 224, 11)
#		)
#		await ctx.send(embed=embed)
#		print("[LOG-NikonSelfBot] - Вы поставили статус!")

@client.slash_command(description='Забанить краш-ботов.')
async def bancrashbots(ctx):
	if ctx.author.id not in чёрныйлистик:
		if not ctx.author.guild_permissions.ban_members:
			return await ctx.response.send_message(embed=discord.Embed(title=':x: | Ошибка', description='У вас недостаточно прав', color=discord.Color.red()), ephemeral=True)
		else:
			await ctx.response.send_message('Начинаю бан краш ботов',  ephemeral=True)
			l = ""
			for crashbot in lists.crashbots:
				user = await client.fetch_user(crashbot)
				l += "`" + user.name + "#" + user.discriminator + "`" + "\n"
				await ctx.guild.ban(user)
			embed=discord.Embed(title='✅ | Краш боты забанены', description=f'Забанено **{len(lists.crashbots)}** краш ботов:\n{l}', color=0xED4245)
			embed.set_footer(text=f'По запросу {ctx.author}')
			await ctx.channel.send(embed=embed)
			print(f"Команда bancrashbots, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	


@client.slash_command(description="Информация о пользователе.")
async def user(inter, участник=None):
 	if inter.author.id not in чёрныйлистик:
			usrStatus = str(user.status)
			if usrStatus == "idle":
				stat = "Неактивен"
			elif usrStatus == "dnd":
				stat = "Не беспокоить"
			elif usrStatus == "online":
				stat = "Онлайн"
			elif usrStatus == "offline":
				stat = "Оффлайн"	
			elif usrStatus == None:
				stat = '**Активность Отсутствует**'
			else:
				stat = user.status
			embed = discord.Embed(title=f"Информация о {user.name}", description=f"""
		Имя пользователя и тэг: **{user.name}#{user.discriminator}**
		ID: **{user.id}**
		Создан: **<t:{round(user.created_at.timestamp())}:f>**
		Статус: **{stat}**
		Ролей: **{len(user.roles)}**
			""",
			color=0xED4245)
			embed.set_thumbnail(url = user.display_avatar.url)
			await inter.response.send_message(embed = embed)
			print(f"Команда user, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")		
		
@client.user_command(name="Информация о пользователе")
async def info(inter: discord.ApplicationCommandInteraction, user: discord.User):
	usrStatus = str(user.status)
	if usrStatus == "idle":
		stat = "Неактивен"
	elif usrStatus == "dnd":
		stat = "Не беспокоить"
	elif usrStatus == "online":
		stat = "Онлайн"
	elif usrStatus == "offline":
		stat = "Оффлайн"
	elif usrStatus == None:
		stat = '**Активность Отсутствует**'
	else:
		stat = user.status
	embed = discord.Embed(title=f"Информация о {user.name}", description=f"""
Имя пользователя и тэг: **{user.name}#{user.discriminator}**
ID: **{user.id}**
Создан: **<t:{round(user.created_at.timestamp())}:f>**
Статус: **{stat}**
Ролей: **{len(user.roles)}**
	""",
	color=0xED4245)
	embed.set_thumbnail(url = user.display_avatar.url)
	await inter.response.send_message(embed = embed)
	print(f"Команда user, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	

@client.slash_command(description="Информация о сервере.")
async def server(inter):
 	if inter.author.id not in чёрныйлистик:
			members = len(list(filter(lambda m: not m.bot, inter.guild.members)))
			bots = len(list(filter(lambda m: m.bot, inter.guild.members)))
			all = len(inter.guild.members)
			text = len(inter.guild.text_channels)
			voice = len(inter.guild.voice_channels)
			category = len(inter.guild.categories)
			embed=discord.Embed(title=f'{inter.guild.name}', color = 0xED4245, description=
																								"**Участники:**\n"
																								f"<:allmembers:964237520063827970> **Всего:** {all}\n"
																								f"<:peoples:964237520089002016> **Людей:** {members}\n"
																								f"<:bot:942049242325843968> **Ботов:** {bots}\n\n"
																								f"**Владелец**\n"
																								f"👑 {inter.guild.owner.mention} (`{inter.guild.owner_id}`)\n\n"
																								f"**Каналы**\n"
																								f"<:textchannel:964234717283123270> **Текстовых:** {text}\n"
																								f"<:voicechannel:964234716985319445> **Голосовых:** {voice}\n"
																								f"<:category:964262500113743902> **Категорий:** {category}\n\n"
																								f"**Другие информации о сервере**\n"
																								f"**🪧 Ролей:** {len(inter.guild.roles)}\n"
																								f"**📅 Сервер создан:** <t:{round(inter.guild.created_at.timestamp())}:f>\n"
																								f"**🔗 Создано приглашений:** {len(await inter.guild.invites())}"
			)
			embed.set_thumbnail(url = inter.guild.icon.url)
#			embed.set_image(url = inter.guild.banner.url)
			embed.set_footer(text = f"ID Сервера: {inter.guild.id}")
			await inter.response.send_message(embed=embed)
			print(f"Команда server, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	





# музыка

# кстати, они должны с слэшом
# а ок
# проверю ща импорты
# кста давай я импорты сделаю норм?  ну давай только ничего не удаляй
# ок, просто их рассортирую
#@bot.slash_command(description="Воспроизвести музыку с YouTube.")
#async def play(ctx, url : str):
#    song_there = os.path.isfile(f'musicPlay\\{ ctx.guild.id }.mp3')
# 
#    try:
#        if song_there:
#            os.remove(f'musicPlay\\{ ctx.guild.id }.mp3')
#            print('[log] Старый файл удалён успешно')
#    except PermissionError:
#        print('[log] Не удалось удалить старый файл')
# 
#    playMusicMsg = await ctx.send('Подождите...')
# 
#    voice = get(bot.voice_clients, guild = ctx.guild)
# 
#    ydl_opts = {
#        'format' : 'bestaudio/best',
#        'postprocessors' : [{
#           'key' : 'FFmpegExtractAudio',
#            'preferredcodec' : 'mp3',
#            'preferredquality' : '192'
#        }],
#    }
# 
#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        ydl.download([url])
# 
#    for file in os.listdir('./'):
#        if file.endswith('.mp3'):
#            name = file
#            print(f'[log] Перейменовываем файл: {file}')
#            os.rename(file, f'musicPlay\\{ ctx.guild.id }.mp3')
# 
#    voice.play(discord.FFmpegPCMAudio(f'{ ctx.guild.id }.mp3'), after = lambda e: print(f'[log] {name}, музыка завершила проигрывание'))
#    voice.source = discord.PCMVolumeTransformer(voice.source)
#    voice.source.volume = 1
# 
#    song_name = name.rsplit('-', 2)
#    await ctx.send(f'Сейчас играет музыка: {song_name[0]}')

#@bot.slash_command(description="Воспроизвести музыку снова.")
#async def music_replay(ctx):
#	voice = get(bot.voice_clients, guild = ctx.guild)
#	voice.play(discord.FFmpegPCMAudio(f'musicPlay\\{ ctx.guild.id }.mp3'), after = lambda e: print(f'[log] музыка завершила проигрывание'))
#	voice.source = discord.PCMVolumeTransformer(voice.source)
#	voice.source.volume = 1
#	embed = discord.Embed(color=0xED4245, title = 'Музыка снова играет')
#	embed.set_footer(text=f'{ footertext }')
#	await ctx.send(embed = embed)

#@bot.slash_command(description="Выйти из голосового канала.")
#async def voice_leave(ctx):
#	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
#	channel = ctx.author.voice.channel
#	if voice and voice.is_connected():
#		await voice.disconnect()
#		embed = discord.Embed(color=0xED4245, title = 'Бот успешно отключился к голосовому канал')
#		embed.set_footer(text=f'{ footertext }')
#		await ctx.send(embed = embed)
#	else:
#		voice = await channel.disconnect()
#		embed = discord.Embed(color=0xED4245, title = 'Бот успешно отключился к голосовому канал')
#		embed.set_footer(text=f'{ footertext }')
#		await ctx.send(embed = embed)

#@bot.slash_command(description="Зайти в голосовой канал.")
#async def voice_join(ctx):
#	global voice
#	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
#	channel = ctx.author.voice.channel
#
#	if voice and voice.is_connected():
#		await voice.move_to(channel)
#	else:
#		voice = await channel.connect()
#		embed = discord.Embed(color=0xED4245, title = 'Бот успешно подключился к голосовому каналу')
#		embed.set_footer(text=f'{ footertext }')
#		await ctx.send(embed = embed)

#@bot.slash_command(description="Включить рандомую электро-музыку.")
#async def play_electro( ctx ):
#    voice.play(FFmpegPCMAudio(random.choice(['https://cdn.discordapp.com/attachments/954313690100928522/977967726205235270/Elektronomia_-_Sky_High_NCS_Release.mp3', 'https://cdn.discordapp.com/attachments/954313690100928522/977967740679770142/Elektronomia_-_Vitality_NCS_Release.mp3', 'https://cdn.discordapp.com/attachments/954313690100928522/977967774137716776/Alex_Skrindo_-_Jumbo_NCS_Release.mp3', 'https://cdn.discordapp.com/attachments/954313690100928522/977967788264136794/Alan_Walker_-_Force.mp3']))) 
#    await ctx.reply('Успешно включил вам рандомную электро-музыку')

@client.slash_command(description="Калькулятор.")
async def math(inter, выражение:str=None):
 	if inter.author.id not in чёрныйлистик:
			if not выражение:await inter.response.send_message(embed=discord.Embed(title='❌ |Ошибка', description='Выражение отсутствует'),ephemeral=True)
			else:
				if "**" in выражение:await inter.response.send_message(embed=discord.Embed(title='❌ |Ошибка', description='Возводить в степень запрещено!', color=discord.Color.red()),ephemeral=True)
				fb = "".join(c for c in выражение if  c.isdecimal())
				try:
					fbs = int(fb)
					await inter.response.send_message(embed=discord.Embed(title='✅ | Успешно!', description=f'Это будет: {eval(выражение)}', color=discord.Color.green()))
				except ValueError:await inter.response.send_message(embed=discord.Embed(title='❌ | Ошибка', description='Вы можете только вычислять', color=discord.Color.red()),ephemeral=True)
				except SyntaxError:await inter.response.send_message(embed=discord.Embed(title='❌  |Ошибка', description='Вы ввели только число', color=discord.Color.red()),ephemeral=True)
				except NameError:await inter.response.send_message(embed=discord.Embed(title='❌ | Ошибка', description='Невозможно вычислить данное выражение', color=discord.Color.red()),ephemeral=True)
				except ZeroDivisionError:await inter.response.send_message(embed=discord.Embed(title=':❌ | Ошибка', description='Делить на ноль нельзя', color=discord.Color.red()),ephemeral=True)
			print(f"Команда math, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	


@client.slash_command(description="Установит канал приветствия.")
async def welcomechannel(inter, channel:discord.TextChannel=None):
 	if inter.author.id not in чёрныйлистик:
			if inter.author.guild_permissions.administrator:
				db = sqlite3.connect('main.sqlite')
				cursor = db.cursor()
				cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = '{inter.guild.id}'")
				result =  cursor.fetchone()
				if not channel:
					embed=discord.Embed(title='❌ | Ошибка', description='Укажите канал для приветствия',color=discord.Color.red())
					await inter.response.send_message(embed=embed)
					return
				else:
					if result is None:
						sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
						val = (inter.guild.id, channel.id)
						embed = discord.Embed(title = '✅ | Канал для приветствия успешно настроен',description=f'Канал настроен до {channel.mention}', color=discord.Color.green())
						await inter.response.send_message(embed=embed)
					elif result is not None:
						sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
						val = (channel.id, inter.guild.id)
						embed = discord.Embed(title = '✅ | Канал для приветствия успешно изменен',description=f'Канал изменен до {channel.mention}', color=discord.Color.green())
						await inter.response.send_message(embed=embed)
					cursor.execute(sql, val)
					db.commit()
					cursor.close()
					db.close()
					return
			else:
				embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=discord.Color.red())
				await inter.response.send_message(embed=embed)
			print(f"Команда welcomechannel, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	


@client.slash_command(description="Установит текст приветствия.")
async def welcometext(inter, * , text):
	if inter.author.id not in чёрныйлистик:
		if inter.author.guild_permissions.administrator:
			db = sqlite3.connect('main.sqlite')
			cursor = db.cursor()
			cursor.execute(f"SELECT msg FROM main WHERE guild_id = {inter.guild.id}")
			result =  cursor.fetchone()
			if not text:
				embed=discord.Embed(title='❌ | Ошибка', description='Укажите текст для приветствия',color=discord.Color.red())
				await inter.response.send_message(embed=embed)
				return
			else:
				if result is None:
					sql = ("INSERT INTO main(guild_id, msg) VALUES(?,?)")
					val = (inter.guild.id, text)
					embed = discord.Embed(title = '✅ | Текст для приветствия успешно создан',description = f"`{text}`", color=discord.Color.green())
					await inter.response.send_message(embed=embed)
				elif result is not None:
					sql = ("UPDATE main SET msg = ? WHERE guild_id = ?")
					val = (text, inter.guild.id)
					embed = discord.Embed(title = '✅ | Текст для приветствия успешно изменен',description = f"`{text}`", color=discord.Color.green())
					await inter.response.send_message(embed=embed)
				cursor.execute(sql, val)
				db.commit()
				cursor.close()
				db.close()
		else:
			embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=discord.Color.red())
			await inter.response.send_message(embed=embed)
			print(f"Команда welcometext, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	


@client.slash_command(description="Установит канал прощания.")
async def leavechannel(inter, channel:discord.TextChannel):
	if inter.author.id not in чёрныйлистик:
			if inter.author.guild_permissions.administrator:
				db = sqlite3.connect('leave.sqlite')
				cursor = db.cursor()
				cursor.execute(f"SELECT channel_id FROM leave WHERE guild_id = '{inter.guild.id}'")
				result =  cursor.fetchone()
				if result is None:
					sql = ("INSERT INTO leave(guild_id, channel_id) VALUES(?,?)")
					val = (inter.guild.id, channel.id)
					embed = discord.Embed(title = '✅ | Канал для прощания успешно настроен',description=f'Канал настроен до {channel.mention}', color=discord.Color.green())
					await inter.response.send_message(embed=embed)
				elif result is not None:
					sql = ("UPDATE leave SET channel_id = ? WHERE guild_id = ?")
					val = (channel.id, inter.guild.id)
					embed = discord.Embed(title = '✅ | Канал для прощания успешно изменен',description=f'Канал изменен до {channel.mention}', color=discord.Color.green())
					await inter.response.send_message(embed=embed)
				cursor.execute(sql, val)
				db.commit()
				cursor.close()
				db.close()
				return
			else:
				embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=discord.Color.red())
				await inter.response.send_message(embed=embed)
			print(f"Команда leavechannel, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	



@client.slash_command(description="Установит текст прощания.")
async def leavetext(inter,*, text):
	if inter.author.id not in чёрныйлистик:
		if inter.author.guild_permissions.administrator:
			db = sqlite3.connect('leave.sqlite')
			cursor = db.cursor()
			cursor.execute(f"SELECT msg FROM leave WHERE guild_id = {inter.guild.id}")
			result =  cursor.fetchone()
			if result is None:
				sql = ("INSERT INTO leave(guild_id, msg) VALUES(?,?)")
				val = (inter.guild.id, text)
				embed = discord.Embed(title = '✅ | Текст для прощания успешно создан',description = f"`{text}`", color=discord.Color.green())
				await inter.response.send_message(embed=embed)
			elif result is not None:
				sql = ("UPDATE leave SET msg = ? WHERE guild_id = ?")
				val = (text, inter.guild.id)
				embed = discord.Embed(title = '✅ | Текст для прощания успешно изменен',description = f"`{text}`", color=discord.Color.green())
				await inter.response.send_message(embed=embed)
			cursor.execute(sql, val)
			db.commit()
			cursor.close()
			db.close()
		else:
			embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=discord.Color.red())
			await inter.response.send_message(embed=embed)
			print(f"Команда leavetext, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	


async def antispam_on_a(ctx, number, action, time):
	cur = await sqlite3.connect(f'db/antispam.db')
	await cur.execute("""CREATE TABLE IF NOT EXISTS `guilds`(
   `guild_id` INTEGER,
   `number` INTEGER,
   `action` TEXT,
   `time` INTEGER);
   """)
	curdata_coro = await cur.execute(f"SELECT `guild_id` FROM `guilds` WHERE `guild_id`={ctx.guild.id};")
	curdata = await curdata_coro.fetchall()
	await curdata_coro.close()
	if curdata != []:
		await cur.execute(f"""UPDATE `guilds`
		SET `guild_id` = {ctx.guild.id}, `number` = {number}, action = '{action}', time = {time}
		WHERE `guild_id`={ctx.guild.id}
		""")
		await cur.execute("COMMIT;")
		await cur.close()
		return '**Успешно обновлен антиспам**'
	await cur.execute(f"INSERT INTO `guilds`(`guild_id`, `number`, `action`, `time`) VALUES({ctx.guild.id}, {number}, '{action}', {time});")
	await cur.execute("COMMIT;")
	await cur.close()
	return '**Антиспам включен**'

async def antispam_off_a(ctx):
	cur = await sqlite3.connect(f'db/antispam.db')
	await cur.execute("""CREATE TABLE IF NOT EXISTS `guilds`(
   `guild_id` INTEGER);
   """)
	await cur.execute(f"DELETE FROM guilds WHERE `guild_id`='{ctx.guild.id}';")
	await cur.execute("COMMIT;")
	await cur.close()
	return "**Антиспам отключен**"

@client.slash_command(description="Подбросить монетку.")
async def coin(ctx):
	if ctx.author.id not in чёрныйлистик:
		randomIntOR = random.randint(0, 1)
		if randomIntOR == 0:
			randomIntORoutput = "орёл"
		else:
			randomIntORoutput = "решка"
		await ctx.send(f"Посмотрим... О, вам выпал(-а) {randomIntORoutput}!")
		print(f"Команда coin, Автор: {ctx.author} ({ctx.author.id}), Сервер: {ctx.guild}")	
  
#@client.slash_command(description="сохранить")
#@commands.has_permissions(administrator = True)
#async def save(ctx):
#	guild = ctx.guild
#	cursor.execute("CREATE TABLE wl(guild, id)")
#	cursor.execute("DELETE FROM channels WHERE id = {}".format(guild.id))
#	cursor.execute("DELETE FROM rls WHERE id = {}".format(guild.id))
#	filterchan = []
#	for i in guild.categories:
##		for c in i.channels:
#			filterchan.append(c.id)
#	for channel in ctx.guild.text_channels:
#		if not channel.id in filterchan:
#			cursor.execute("INSERT INTO channels VALUES(?, ?, ?, ?, ?)", (guild.id, channel.name, channel.position, 'text', None))
#	for channel in ctx.guild.voice_channels:
#		if not channel.id in filterchan:
#			cursor.execute("INSERT INTO channels VALUES(?, ?, ?, ?, ?)", (guild.id, channel.name, channel.position, 'voice', None))	
#	for category in guild.categories:
#		for channel in category.text_channels:
#			cursor.execute("INSERT INTO channels VALUES(?, ?, ?, ?, ?)", (guild.id, channel.name, channel.position, 'text', category.name))
#		for channel in category.voice_channels:
#			cursor.execute("INSERT INTO channels VALUES(?, ?, ?, ?, ?)", (guild.id, channel.name, channel.position, 'voice', category.name))
#		cursor.execute("INSERT INTO channels VALUES(?, ?, ?, ?, ?)", (guild.id,category.name, category.position, 'category', None))
#	for role in ctx.guild.roles:
#		if role.is_bot_managed() or role.is_default():
#			pass
#		else:
#			cursor.execute("INSERT INTO rls VALUES(?,?,?,?)", (guild.id, role.name, role.position, str(role.color)))
#	data.commit()
##	await ctx.send(embed = discord.Embed(title = ':gear: | Saved',
#		description = ">>> **Ваш сервер успешно сохранён.**",
#		color = discord.Colour(0x1f8b4c)
#		))


#@client.slash_command(description="бэкап")
#@commands.has_permissions(administrator = True)
#async def backup(ctx):
#	categories = cursor.execute("SELECT * FROM channels WHERE id = ? AND type = ?", (ctx.guild.id, 'category'))
#	for i in categories.fetchall():
#		await ctx.guild.create_category(name = i[1], position = i[2])
#	Textchannels = cursor.execute('SELECT * FROM channels WHERE id = ? AND type = ?', (ctx.guild.id, 'text'))
#	for i in Textchannels.fetchall():
#		if i[4] == None:
#			await ctx.guild.create_text_channel(name = i[1], position = i[2])
#	Voicechannels = cursor.execute('SELECT * FROM channels WHERE id = ? AND type = ?', (ctx.guild.id, 'voice'))		
#	for i in Voicechannels.fetchall():
#		if i[4] == None:
#			await ctx.guild.create_voice_channel(name = i[1], position = i[2])
#	CatChannels = cursor.execute("SELECT * FROM channels WHERE id = {} AND cn IS NOT NULL".format(ctx.guild.id))
#	for i in CatChannels.fetchall():
#		for cat in ctx.guild.categories:
#			if i[4] == cat.name:
#				if i[3] == 'text':
#					await cat.create_text_channel(name = i[1], position = i[2])
#				else:
#					await cat.create_voice_channel(name = i[1], position = i[2])
#				break
#			else:
#				pass
#	roles = cursor.execute(f'SELECT name,position,color FROM rls WHERE id = {ctx.guild.id}') #id, name, position
#	for iteration in roles.fetchall():
#		role = await ctx.guild.create_role(name = iteration[0])
#		color = tuple(int(iteration[2].strip('#')[i:i+2], 16) for i in (0, 2, 4))
#		await role.edit(position = iteration[1], colour = discord.Color.from_rgb(color[0], color[1], color[2]))
			

@client.slash_command(description="Установит логи.")
async def logschannel(inter, канал:discord.TextChannel):
	if inter.author.id not in чёрныйлистик:
			if inter.author.guild_permissions.administrator:
				db = sqlite3.connect('logs.sqlite')
				cursor = db.cursor()
				cursor.execute(f"SELECT channel_id FROM logs WHERE guild_id = '{inter.guild.id}'")
				result =  cursor.fetchone()
				if result is None:
					sql = ("INSERT INTO logs(guild_id, channel_id) VALUES(?,?)")
					val = (inter.guild.id, канал.id)
					embed = discord.Embed(title = '✅ | Канал для логов успешно настроен',description=f'Канал настроен до {канал.mention}', color=discord.Color.green())
					await inter.response.send_message(embed=embed)
				elif result is not None:
					sql = ("UPDATE logs SET channel_id = ? WHERE guild_id = ?")
					val = (канал.id, inter.guild.id)
					embed = discord.Embed(title = '✅ | Канал для логов успешно изменен',description=f'Канал изменен до {канал.mention}', color=discord.Color.green())
					await inter.response.send_message(embed=embed)
				cursor.execute(sql, val)
				db.commit()
				cursor.close()
				db.close()
				return
			else:
				embed = discord.Embed(title='❌ | Ошибка', description = 'Вы не администратор', color=discord.Color.red())
				await inter.response.send_message(embed=embed)
			print(f"Команда logschannel, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")	

# @client.slash_command(description="Включить радио.")
# async def radio(inter):
# 	if inter.author.id not in чёрныйлистик:
# 			if inter.author.id not in premium:
# 					await inter.ctx("Нет премиума!")
# #				else:
# #					embed = discord.Embed(title = '❌ | Ошибка',description='Радио уже включено', color=discord.Color.red())
# #					await inter.response.send_message(embed=embed)
# #					print(f"Команда radio, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")    
# 			else:
# 					voice = await inter.author.voice.channel.connect()
# 					voice.play(FFmpegPCMAudio("http://s02.fjperezdj.com:8006/live"))
# 					embed = discord.Embed(title = '✅ | Радио включено',description='Радио включено', color=discord.Color.green())
# 					await inter.response.send_message(embed=embed)
# 					print(f"Команда radio, Автор: {inter.author} ({inter.author.id}), Сервер: {inter.guild}")    
# #				else:
# #					embed = discord.Embed(title = '❌ | Ошибка',description='Радио уже включено', color=discord.Color.red())
# #					await inter.response.send_message(embed=embed)

# @client.slash_command(description="Выключить радио.")
# async def stop(ctx):
# 	if ctx.author.id not in premium:
# 		await ctx.ctx("Нет премиума!")
# 	else:
# 		await ctx.author.voice_client.disconnect()
# 		embed = discord.Embed(title = '✅ | Радио выключено!',description='Радио выключено', color=discord.Color.green())
# 		await ctx.response.send_message(embed=embed)

print("[Discord] Бот должен запустится!")
client.run(token)