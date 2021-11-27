import re
import long_responses as long


def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    flat_message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            flat_message_certainty += 1

    message_certainty = float(flat_message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(message_certainty * 100)
    else:
        return 0


def check_messages(message):
    highest_probability_map = {}

    def res(bot_res, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_probability_map
        highest_probability_map[bot_res] = message_probability(message, list_of_words, single_response, required_words)

    # ---------------------------------------------- Responses ---------------------------------------------------------
    res('Hello!', ['hi', 'hallo', 'hey', 'hello'], single_response=True)
    res('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    res('That\'s good to read.', ['i', 'am', 'fine', 'thank', 'you'])
    res(long.R_EATING, ['what', 'do', 'you', 'like', 'to', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_probability_map, key=highest_probability_map.get)

    return long.unknown() if highest_probability_map[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    res = check_messages(split_message)
    return res


while True:
    print('Bot: ' + get_response(input('You: ')))
