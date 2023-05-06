import json
import re


def find_hashtags(message):
    hashtags = re.findall(r'#\w+', message)
    return hashtags


def get_filtred_msgs_id(filters):
    msg_id = []
    with open('channel_messages.json', 'r') as infile:
        all_msgs = json.load(infile)
        for msg in all_msgs:
            if f"#{filters['category'].lower()}" in msg['message'].lower():
                if f"#{filters['district'][:3].lower()}" in msg['message'].lower():
                    if f"#{filters['type'][:2].lower()}" in msg['message'].lower():
                        try:
                            if f"#{filters['area'][0]}соток" in msg['message'] or \
                                    f"#{filters['area'][2]}соток" in msg['message']:
                                price = re.search(r'#(\d+)дол', msg['message'])
                                if price and filters['price'][0] <= int(price.group(1)) <= filters['price'][1]:
                                    msg_id.append(msg['id'])

                        except IndexError:
                            if f"#{filters['area']}комнатная" in msg['message']:
                                price = re.search(r'#(\d+)дол', msg['message'])
                                if price and filters['price'][0] <= int(price.group(1)) <= filters['price'][1]:
                                    msg_id.append(msg['id'])

        return list(set(msg_id))
