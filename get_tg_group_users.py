import csv
from telethon import TelegramClient

api_id = 00000000
api_hash = 'abcdefghijklmnop1234567890'
chat_to_look_for = 'Chat group name'

client = TelegramClient(f'{api_id}-session', api_id, api_hash)


async def main(dialog_name: str, path_to_csv: str):
    dialogs = await client.get_dialogs()

    all_dialogs = {d.entity.title: d.entity for d in dialogs if d.is_group}
    chat = all_dialogs[dialog_name]
    participants = await client.get_participants(chat)
    print(f'Total number of participants in {len(participants)}')

    with open(path_to_csv, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['id', 'first_name', 'last_name', 'username'])
        for u in participants:
            writer.writerow([u.id, u.first_name, u.last_name, u.username])

if __name__ == '__main__':
    chat_normalized_name = chat_to_look_for.replace(' ', '_').lower()
    path_to_csv_file = f'./{chat_normalized_name}.csv'
    with client:
        client.loop.run_until_complete(main(chat_to_look_for, path_to_csv_file))
