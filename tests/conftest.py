from telebot.types import Message, User, Chat


test_content_type = 'text'
test_message_id = 383
test_date = 1580657779
test_json = {'message_id': 383,
          'from':
              {'id': 362857450,
               'is_bot': False,
               'first_name': 'Nikolas',
               'last_name': 'Luchanos',
               'username': 'Luchanos',
               'language_code': 'ru'},
          'chat': {'id': -383813333,
                   'title': 'Мой техдолг',
                   'type': 'group',
                   'all_members_are_administrators': True},
          'date': 1580657779,
          'text': '/bless_me@every_day_bible_bot',
          'entities': [{'offset': 0,
                        'length': 29,
                        'type': 'bot_command'}]}

test_user = User(id=362857450,
                 is_bot= False,
                 first_name='Nikolas',
                 username='Luchanos',
                 last_name='Luchanos',
                 language_code='ru')


test_chat = Chat(type='group',
                 id=-383813333,
                 title='Мой техдолг',
                 all_members_are_administrators=True)

test_msg = Message(message_id=test_message_id,
                   from_user=test_user,
                   date=test_date,
                   chat=test_chat,
                   content_type=test_content_type,
                   options=[],
                   json_string=test_json)
