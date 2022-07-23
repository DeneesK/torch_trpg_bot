import asyncio
import random
from telebot import telebot, types, async_telebot

from settings import*
from database_scrypt import*
from parser import UsersData


bot = telebot.async_telebot.AsyncTeleBot(TOKEN)  # Token imported from settings.py


@bot.message_handler(commands=['start'])
async def send_welcome(message):
	"""
	Sends a welcome message and launches a keyboard to select type
	"""
	delet_row(user_id=message.from_user.id)

	user_id = message.from_user.id
	db_table_row_create(user_id=user_id, count=0)

	types_ranking = UsersData.create_types_ranking()  # creates tuple with most common types according Google table
	await start_keyboard(types_ranking, message)


@bot.message_handler(func=lambda message: True)
async def response_processing(message):
	"""
	Receives and processes all subsequent messages until 
	the contact list  has len more the specified number(check_number from settings)
	"""
	answer = message.text
	count = db_table_read_count(user_id=message.from_user.id)

	if answer in ALL_TYPES and count[0] != 20:  # ALL-TYPES imported from settings
		user_choice = db_table_read_user_choice(user_id=message.from_user.id)

		if user_choice[0]:
			user_choice = user_choice[0] + f'{answer.strip()}, '
			db_table_wright_user_choice(user_choice, user_id=message.from_user.id)
		else:
			user_choice = f'{answer.strip()}, '.capitalize()
			db_table_wright_user_choice(user_choice, user_id=message.from_user.id)

		count = db_table_read_count(user_id=message.from_user.id)
		count = count[0] + 1
		db_table_wright_count(count, user_id=message.from_user.id)

		if count > 1:
			user_type = db_table_read_user_type(user_id=message.from_user.id)
			user_contact = db_table_read_user_contact(user_id=message.from_user.id)
			user_dict = UsersData.create_user_dict(user_type, user_contact)
			suitable_user_dict = UsersData.get_suitable_users(
				answer=answer, 
				users_dict=user_dict
				)
			user_type = UsersData.get_types_from_dict(suitable_user_dict)
			user_contact = UsersData.get_contacts_from_dict(suitable_user_dict)
			db_table_wright_user_type(user_type, user_id=message.from_user.id)
			db_table_wright_user_contact(user_contact, user_id=message.from_user.id)
			most_common_types = UsersData.get_most_common(user_type)
			most_common_types = most_common_types[5:]
			contacts_list = UsersData.create_contacts_list(user_contact)

			await send_contact_list(contacts_list, message) if len(contacts_list) <= check_number else await menu_keyboard(most_common_types, message)
		else:
			suitable_user_dict = UsersData.get_suitable_users(
				answer=answer, 
				users_dict=UsersData.users_dict
				)
			user_type = UsersData.get_types_from_dict(suitable_user_dict)
			user_contact = UsersData.get_contacts_from_dict(suitable_user_dict)
			db_table_wright_user_type(user_type, user_id=message.from_user.id)
			db_table_wright_user_contact(user_contact, user_id=message.from_user.id)

			most_common_types = UsersData.get_most_common(user_type)
			del most_common_types[0:5]
			await menu_keyboard(most_common_types, message)
	
	elif count[0] == 20 and answer not in ALL_TYPES:
		db_table_wright_count(count=21, user_id=message.from_user.id)
		await send_feedback(message)


@bot.message_handler(func=lambda message: True)
async def send_feedback(message):
	if message.text != '/start':
		await bot.send_message(chat_id=CHAT_ID, text=message.text)  # CHAT_ID imported from settings.py
		await bot.reply_to(message, feedback_thanks_message)


async def start_keyboard(types_ranking, message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	buttons = [
		types_ranking[random.randint(0, 2)][0],
		types_ranking[random.randint(3, 5)][0],
		types_ranking[random.randint(6, 8)][0],
		types_ranking[random.randint(9, 11)][0],
	]
	random.shuffle(buttons)
	[keyboard.add(button) for button in buttons]
	await bot.reply_to(message, greeting_text, parse_mode='html', reply_markup=keyboard)


async def menu_keyboard(most_common, message):
	count = db_table_read_count(user_id=message.from_user.id)
	count = count[0]
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	buttons = [
		most_common[random.randint(0, 1)][0],
		most_common[random.randint(2, 3)][0],
		most_common[random.randint(4, 5)][0],
		most_common[random.randint(6, 7)][0],
	]
	random.shuffle(buttons)
	[keyboard.add(button) for button in buttons]
	await bot.reply_to(message, text=answers[count], parse_mode='html', reply_markup=keyboard)


async def send_contact_list(contacts, message):
	chat_id = message.chat.id
	contacts_for_sending = ''
	for contact in contacts:
		contacts_for_sending += f'\n{contact},'

	user_choices = db_table_read_user_choice(user_id=chat_id)

	await bot.send_message(
		chat_id=chat_id,
		text=f"{result_text} \n \n*{user_choices[0].capitalize()}*",  # result_text imported from settings.py
		parse_mode="Markdown",
		reply_markup=types.ReplyKeyboardRemove()
	)

	await bot.send_message(chat_id=chat_id, text=contacts_for_sending)
	await bot.send_message(chat_id=chat_id, text=f"{try_again_text}")
	db_table_wright_count(count=20, user_id=message.from_user.id)


if __name__ == "__main__":
	asyncio.run(bot.infinity_polling())
