# coding: utf8
from __future__ import unicode_literals


"""
Example sentences to test spaCy and its language models.

>>> from spacy.lang.ru.examples import sentences
>>> docs = nlp.pipe(sentences)
"""


sentences = [
    #Translations from English:
    "Apple рассматривает возможность покупки стартапа из Соединённого Королевства за $1 млрд",
    "Беспилотные автомобили перекладывают страховую ответственность на производителя",
    "В Сан-Франциско рассматривается возможность запрета роботов-курьеров, которые перемещаются по тротуару",
    "Лондон — это большой город в Соединённом Королевстве",
    
    #Native Russian sentences:
    #Colloquial:
    "Да, нет, наверное!",#Typical polite refusal
    "Обратите внимание на необыкновенную красоту этого города-героя Москвы, столицы нашей Родины!",#From a tour guide speech
    
    #Examples of Bookish Russian:
    #Quote from "The Golden Calf"
    "Рио-де-Жанейро — это моя мечта, и не смейте касаться её своими грязными лапами!",
    
    #Quotes from "Ivan Vasilievich changes his occupation"
    "Ты пошто боярыню обидел, смерд?!!",
    "Оставь меня, старушка, я в печали!",
    
    #Quotes from Dostoevsky:
    "Уж коли я, такой же, как и ты, человек грешный, над тобой умилился и пожалел тебя, кольми паче бог", 
    "В мечтах я нередко, говорит, доходил до страстных помыслов о служении человечеству и может быть действительно пошел бы на крест за людей, если б это вдруг как-нибудь потребовалось, а между тем я двух дней не в состоянии прожить ни с кем в одной комнате, о чем знаю из опыта",
    "Зато всегда так происходило, что чем более я ненавидел людей в частности, тем пламеннее становилась любовь моя к человечеству вообще",
    
    #Quotes from Chekhov:
    "Ненужные дела и разговоры всё об одном отхватывают на свою долю лучшую часть времени, лучшие силы, и в конце концов остается какая-то куцая, бескрылая жизнь, какая-то чепуха, и уйти и бежать нельзя, точно сидишь в сумасшедшем доме или в арестантских ротах!",
    
    #Quotes from Turgenev:
    "Нравится тебе женщина, старайся добиться толку; а нельзя — ну, не надо, отвернись — земля не клином сошлась",
    "Узенькое местечко, которое я занимаю, до того крохотно в сравнении с остальным пространством, где меня нет и где дела до меня нет; и часть времени, которую мне удастся прожить, так ничтожна перед вечностью, где меня не было и не будет...",
    
    #Quotes from newspapers:
    #Komsomolskaya Pravda:
    "На заседании президиума правительства Москвы принято решение присвоить статус инвестиционного приоритетного проекта города Москвы киностудии Союзмультфильм",
    "Глава Минобороны Сергей Шойгу заявил, что обстановка на этом стратегическом направлении требует непрерывного совершенствования боевого состава войск",
    #Argumenty i Facty:
    "На реплику лже-Говина — дескать, он (Волков) будет лучшим революционером — Стамп с энтузиазмом ответил: Непременно!",
]
