questions = [
    # ========== GRAMMAR SECTION (1-27) ==========
    # Multiple choice questions
    {'id': 1, 'type': 'choice', 'text': 'He asked me ______ meet next Monday.', 'options': ['could we', 'if we could', 'if could we', 'if we will'], 'correct': 'B', 'points': 1},
    {'id': 2, 'type': 'choice', 'text': 'Romantic films always make me ______.', 'options': ['crying', 'to cry', 'cry', 'be crying'], 'correct': 'C', 'points': 1},
    {'id': 3, 'type': 'choice', 'text': 'Yes, I was in Paris on Saturday. Then I flew to Rome and ______ to Moscow only on Wednesday.', 'options': ['returned', 'has returned', 'have returned', 'had returned'], 'correct': 'A', 'points': 1},
    {'id': 4, 'type': 'choice', 'text': 'Who ______ Jessica yesterday?', 'options': ['have seen', 'has seen', 'saw', 'had seen'], 'correct': 'C', 'points': 1},
    {'id': 5, 'type': 'choice', 'text': '"What ______ you do if you lost your job?" – "I could find another one quickly"', 'options': ['will', 'do', 'can', 'would'], 'correct': 'D', 'points': 1},
    {'id': 6, 'type': 'choice', 'text': 'Tom needed ______ information so he surfed the Internet.', 'options': ['-', 'any', 'an', 'any of'], 'correct': 'A', 'points': 1},
    {'id': 7, 'type': 'choice', 'text': 'She missed her flight in the end, ______ she?', 'options': ["hadn't", "didn't", "wasn't", "hasn't"], 'correct': 'B', 'points': 1},
    {'id': 8, 'type': 'choice', 'text': 'If you travel within the European Union you ______ carry a passport, as an identity card is accepted there.', 'options': ["mustn't", "haven't to", "shouldn't", "don't have to"], 'correct': 'D', 'points': 1},
    {'id': 9, 'type': 'open', 'text': 'Это самый плохой день в моей жизни! This is ______ day of my life.', 'correct_answers': ['the worst'], 'points': 1},
    {'id': 10, 'type': 'open', 'text': 'Этот автомобиль был изготовлен в прошлом году. This car __________ last year.', 'correct_answers': ['was made', 'was manufactured', 'was produced'], 'points': 1},
    {'id': 11, 'type': 'choice', 'text': 'It smells nice. She must ______ something very delicious.', 'options': ['cook', 'cooking', 'be cooking', 'been cooking'], 'correct': 'C', 'points': 2},
    {'id': 12, 'type': 'choice', 'text': 'I wish I ______ more free time these days! I really need a break.', 'options': ['have', 'had', 'have had', 'had had'], 'correct': 'B', 'points': 2},
    {'id': 13, 'type': 'choice', 'text': 'When he was young, he ______ his summer holidays in the country.', 'options': ['had spent', 'used to spend', 'used to spent', 'used to have spent'], 'correct': 'B', 'points': 1},
    {'id': 14, 'type': 'choice', 'text': 'By next June, the new road ______.', 'options': ['is built', 'will been built', 'will have been built', 'is being built'], 'correct': 'C', 'points': 1},
    {'id': 15, 'type': 'choice', 'text': 'Luggage ______ to be collected in the luggage reclaim area.', 'options': ['must', 'should', 'is', 'will'], 'correct': 'C', 'points': 2},
    {'id': 16, 'type': 'choice', 'text': 'The residents were made ________ their homes by the authorities.', 'options': ['to leave', 'left', 'to have left', 'have left'], 'correct': 'A', 'points': 2},
    {'id': 17, 'type': 'open', 'text': 'Её родители не хотят, чтобы она выходила замуж. Her parents don\'t want ________ get married.', 'correct_answers': ['her to'], 'points': 2},
    {'id': 18, 'type': 'open', 'text': 'Говорят, что он очень милый человек. Не ___________ to be a very nice person.', 'correct_answers': ['is said'], 'points': 3},
    {'id': 19, 'type': 'open', 'text': 'Как давно ты меня уже ждёшь? How long ___________ for me?', 'correct_answers': ['have you been waiting'], 'points': 2},
    {'id': 20, 'type': 'open', 'text': 'Как ты добираешься до работы? How ___________ to work?', 'correct_answers': ['do you get', 'do you go'], 'points': 2},
    {'id': 21, 'type': 'choice', 'text': 'If he sticks to this bad habit, he risks ______ all his money.', 'options': ['to lose', 'of losing', 'losing', 'lose'], 'correct': 'C', 'points': 3},
    {'id': 22, 'type': 'choice', 'text': 'Before signing the contract you should ______ by a lawyer.', 'options': ['get it checked', 'get checked it', 'checked it', 'get checked'], 'correct': 'A', 'points': 3},
    {'id': 23, 'type': 'choice', 'text': 'If you ______ the test, you would have been offered a job in our company. I\'m sorry, but you didn\'t.', 'options': ['had passed', 'passed', 'would have passed', 'have passed'], 'correct': 'A', 'points': 3},
    {'id': 24, 'type': 'choice', 'text': 'Mary is tired. She ______ for her exam all night.', 'options': ['is preparing', 'has prepared', 'has been preparing', 'is being prepared'], 'correct': 'C', 'points': 1},
    {'id': 25, 'type': 'choice', 'text': 'Coca Cola ______ for more than a century, and it is still a very popular drink.', 'options': ['is produced', 'is been producing', 'has been produced', 'has produced'], 'correct': 'C', 'points': 1},
    {'id': 26, 'type': 'choice', 'text': 'The criminal ______, and that\'s why the police weren\'t searching for him.', 'options': ['is thought to be arrested', 'is thought to have been arrested', 'was thought to have been arrested', 'was thought he was arrested'], 'correct': 'C', 'points': 2},
    {'id': 27, 'type': 'choice', 'text': 'I feel terrible that I didn\'t bring him a present! I should ______ him something.', 'options': ['bought', 'have been bought', 'have been buying', 'have bought'], 'correct': 'D', 'points': 2},

    # ========== VOCABULARY AND READING SECTION (28-53) ==========
    {'id': 28, 'type': 'choice', 'text': 'The actual ______ of sleep you need depends on your age.', 'options': ['size', 'number', 'amount', 'total'], 'correct': 'C', 'points': 1},
    {'id': 29, 'type': 'choice', 'text': 'The new policy gives us a wonderful ______ to reduce our direct costs.', 'options': ['occasion', 'possibility', 'cause', 'opportunity'], 'correct': 'D', 'points': 1},
    {'id': 30, 'type': 'choice', 'text': 'Walking in the country gives you the ______ of exercise and at the same time allows you to experience wonderful scenery.', 'options': ['benefit', 'assistance', 'allowance', 'help'], 'correct': 'A', 'points': 1},
    {'id': 31, 'type': 'choice', 'text': 'John doesn\'t really like cold weather. ______ he\'s going to Iceland on holiday next week.', 'options': ['Even so', 'Consequently', 'As a result', 'Because'], 'correct': 'A', 'points': 1},
    {'id': 32, 'type': 'choice', 'text': 'When you are a busy manager like me, it\'s not a good idea to ______ until tomorrow what you have time to do today.', 'options': ['put off', 'put up', 'put on', 'put through'], 'correct': 'A', 'points': 1},
    {'id': 33, 'type': 'choice', 'text': 'Steve prefers socializing ______ staying at home watching TV.', 'options': ['than', 'instead', 'to', 'from'], 'correct': 'C', 'points': 1},
    {'id': 34, 'type': 'choice', 'text': 'You shouldn\'t ______ her for not speaking to you. After all, it\'s your fault.', 'options': ['accuse', 'apologize', 'blame', 'chat'], 'correct': 'C', 'points': 1},
    {'id': 35, 'type': 'choice', 'text': 'I don\'t ______ having seen you before. Are you sure we have met?', 'options': ['remind', 'memorise', 'forget', 'remember'], 'correct': 'D', 'points': 1},
    {'id': 36, 'type': 'choice', 'text': 'Jenny accepted his proposal immediately. She couldn\'t ______ the opportunity of a lifetime.', 'options': ['miss', 'lose', 'regret', 'leave'], 'correct': 'A', 'points': 1},
    {'id': 37, 'type': 'choice', 'text': 'Passing my exams with good grades was a great ______ for me.', 'options': ['pride', 'fulfillment', 'strength', 'achievement'], 'correct': 'D', 'points': 1},
    {'id': 38, 'type': 'choice', 'text': 'Harry ______ for several posts and is still waiting for a reply.', 'options': ['appointed', 'sought', 'presented', 'applied'], 'correct': 'D', 'points': 1},
    {'id': 39, 'type': 'choice', 'text': 'Somebody ______ their flat while they were on holiday. They took everything.', 'options': ['burgled', 'broke', 'stole', 'robbed'], 'correct': 'A', 'points': 1},
    {'id': 40, 'type': 'choice', 'text': 'He was sent to prison for ______ his boss. She was paying him not to reveal her secret.', 'options': ['pickpocketing', 'blackmailing', 'joyriding', 'robbing'], 'correct': 'B', 'points': 1},
    {'id': 41, 'type': 'choice', 'text': 'Arsenal football team fans hope that their team will ______ for the finals.', 'options': ['cope', 'qualify', 'undertake', 'supervise'], 'correct': 'B', 'points': 1},
    {'id': 42, 'type': 'choice', 'text': 'This is a very exclusive club. We can\'t enter ______ we are members.', 'options': ['even', 'if', 'although', 'unless'], 'correct': 'D', 'points': 1},
    {'id': 43, 'type': 'choice', 'text': 'We watched a film about a strange alien ______ from Mars.', 'options': ['plot', 'blurb', 'creature', 'figure'], 'correct': 'C', 'points': 1},
    {'id': 44, 'type': 'choice', 'text': 'The cost of damage was ______ to be more than $2 billion.', 'options': ['estimated', 'measured', 'ensured', 'encouraged'], 'correct': 'A', 'points': 1},
    {'id': 45, 'type': 'choice', 'text': 'The volcanic eruption had a huge ______ on the residents of the island.', 'options': ['impact', 'accident', 'damage', 'importance'], 'correct': 'A', 'points': 1},
    {'id': 46, 'type': 'choice', 'text': 'The fire was due to a ______ in the electrical wiring system.', 'options': ['injury', 'healing', 'malfunction', 'insurance'], 'correct': 'C', 'points': 1},
    {'id': 47, 'type': 'choice', 'text': 'Competition is ______ in the fast-food business.', 'options': ['efficient', 'intense', 'successful', 'effective'], 'correct': 'B', 'points': 1},
    {'id': 48, 'type': 'choice', 'text': 'Sally Green is on the board of ______.', 'options': ['founders', 'managers', 'owners', 'directors'], 'correct': 'D', 'points': 1},
    {'id': 49, 'type': 'choice', 'text': 'Over the next two months we are going to ______ two new products.', 'options': ['launch', 'innovate', 'start', 'forecast'], 'correct': 'A', 'points': 1},
    {'id': 50, 'type': 'choice', 'text': '"Director ______" Philip Bosman has resigned from his £150,000 job at Presco after the company announced a loss of £2.6 million in its annual report.', 'options': ['fires', 'crashes', 'quits', 'strikes'], 'correct': 'C', 'points': 1},
    {'id': 51, 'type': 'choice', 'text': '"The President ______ the plan." The President has given his support to a plan which aims to reduce the number of drug-abusers.', 'options': ['backs', 'hits', 'smashes', 'drives'], 'correct': 'A', 'points': 1},
    {'id': 52, 'type': 'choice', 'text': '"Festival ______" There were angry scenes at the meeting last night between organizers of a music festival and local residents who do not want it to take place.', 'options': ['scare', 'row', 'tragedy', 'rubbish'], 'correct': 'B', 'points': 1},
{'id': 53, 'type': 'choice', 'text': '"Allan Nicks: That\'s my world"\n\n"I recently spent two years in the Arctic filming the series Blue Planet. When I\'m filming, I like to really feel how lonely the environment is. I prefer to be face to face with the animals I\'m filming. I haven\'t got in the water with killer whales yet, but I plan to. Of course it\'s dangerous if you choose the wrong moment.\n\nOriginally I was a researcher, but for me science lacked excitement. I was able to move into filming in 2005 and have concentrated on wildlife ever since.\n\nWhen I come back home from my trips, I work in the mornings and spend the afternoons swimming to keep fit. Now I\'m fifty, filming is harder. The challenge for me is to continue to deliver high-quality work."\n\nBest summary for the extract is:\n\nA) "I\'m glad I gave up working as a scientist because I\'m now in a position to retire early."\nB) "Now I\'ve reached fifty I realize the dangers involved in filming wildlife are great."\nC) "Although I find the work more difficult now I\'m not as young, I still have film projects I want to do."', 
'options': ['A', 'B', 'C'], 
'correct': 'C', 
'points': 2},
]

print(f"✅ Loaded {len(questions)} questions:")
grammar = len([q for q in questions if q['id'] <= 27])
vocab = len([q for q in questions if q['id'] >= 28])
print(f"   • Grammar: {grammar} questions")
print(f"   • Vocabulary: {vocab} questions")

print(f"   • Total points: {sum(q['points'] for q in questions)}")
