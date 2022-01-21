from .. import loader, utils

class InfoMod(loader.Module):
	strings = {"name": "Anti-Doeb"}

	def __init__(self):
		self.ad = False
		self.wi = []
		self.wu = []

	async def adhelpcmd(self, message):
		await message.edit('''<b>Anti-Doeb от @sblro4eeek

Удаляет все сообщения которые вам отправляют в ЛС</b>

<code>.adon</code><b> - Включить Anti-Doeb</b>
<code>.adoff</code><b> - Выключить Anti-Doeb</b>

<code>.addwl *@юзернейм || или просто пропишите в лс*</code> <b> - Добавит пользователя в белый список, сообщение не будут удалятся от пользователей который находятся в это списке</b>

<code>.wl</code><b> - Покажет уто находится в белом списке</b>

<code>.clswl</code><b> - Очистит белый список</b>
''')

	async def adoncmd(self, message):
		self.ad = True
		await message.edit('<b>Анти Доёб от @sblro4eeek включён.</b>')
	async def adoffcmd(self, message):
		self.ad = False
		await message.edit('<b>Анти Доёб от @sblro4eeek выключён.</b>')


	async def addwlcmd(self, message):
		args = utils.get_args_raw(message)
		try:
			q = await message.client.get_entity(args)
			self.wi.append(f'{q.id}')
			self.wu.append(f'{w.first_name} -> @{w.username} -> {w.id}')
			await message.edit(f'<b>Добавлен:</b>\n{w.first_name} -> @{w.username} -> {w.id}\n\n<b>Посмотреть белый список по команде</b><code>.wl</code>')
		except:
			w = await message.client.get_entity(message.chat_id)
			self.wi.append(f'{message.chat_id}')
			self.wu.append(f'{w.first_name} -> @{w.username} -> {w.id}')
			await message.edit(f'<b>Добавлен:</b>\n{w.first_name} -> @{w.username} -> {w.id}\n\n<b>Посмотреть белый список по команде</b><code>.wl</code>')

	async def wlcmd(self, message):
		i = '\n'.join(self.wi)
		u = '\n'.join(self.wu)
		await message.edit(f'ID:\n{i}')
		await message.respond(f"UM:\n{u}")

	async def clswlcmd(self, message):
		self.wi = []
		self.wu = []
		await message.edit('<b>Белый список очищен</b>')


	async def watcher(self, message):
		me = (await message.client.get_me())
		if (str(message.chat_id)[0]) != '-':
			if str(message.chat_id) not in self.wi:
				if message.sender_id != me.id:
					if self.ad:
						await message.delete()
			else:
				pass