				data = PlayerData()

				data.namedtuple_create(
					db_table_read_user_choice(user_id=message.from_user.id)[0],
					db_table_read_user_contact(user_id=message.from_user.id)[0]
				)

				data.get_player(data.player_list, message.text)
				type_list = ''
				contact_list = ''

				for index in range(0, len(data.sorted_list)):
					type_list += data.sorted_list[index].type + '|'
					contact_list += data.sorted_list[index].contact + ","

				db_table_wright_user_choice(user_choice=type_list, user_id=message.from_user.id)
				db_table_wright_user_contact(user_contact=contact_list, user_id=message.from_user.id)
				add_type = db_table_read_user_type(message.from_user.id)
				finish_types_list = ''
				for tp in add_type:
					finish_types_list += tp + ', '
				finish_types_list += message.text
				db_table_wright_user_type(user_type=finish_types_list, user_id=message.from_user.id)

				if len(data.sorted_list) < contacts_number:
					await send_contact_list_func(contacts=db_table_read_user_contact(message.from_user.id), message=message)
				else:
					most_common = data.most_common(data.sorted_list)
					most_common = most_common[5:]
					await menu_keyboard(most_common, message)

