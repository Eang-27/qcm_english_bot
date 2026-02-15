import random
VOCABULARY_QUESTIONS = {
    "A1": [
        {
            "q": "I'm very ___. I need to eat something.",
            "options": ["hungry", "thirsty", "tired", "happy"],
            "answer": 0
        },
        {
            "q": "What ___ is it? It's 3 o'clock.",
            "options": ["day", "time", "hour", "minute"],
            "answer": 1
        },
        {
            "q": "Can you ___ the door, please?",
            "options": ["open", "opened", "opening", "opens"],
            "answer": 0
        },
        {
            "q": "My ___ color is blue.",
            "options": ["favorite", "love", "like", "best"],
            "answer": 0
        },
        {
            "q": "I go to ___ at 10 PM every night.",
            "options": ["bed", "sleep", "bedroom", "night"],
            "answer": 0
        },
        {
            "q": "She works in a ___. She helps sick people.",
            "options": ["school", "shop", "hospital", "bank"],
            "answer": 2
        },
        {
            "q": "It's raining. Take your ___.",
            "options": ["coat", "umbrella", "hat", "shoes"],
            "answer": 1
        },
        {
            "q": "I need to buy some ___ for breakfast.",
            "options": ["bread", "water", "chair", "table"],
            "answer": 0
        },
        {
            "q": "The opposite of 'hot' is ___.",
            "options": ["warm", "cold", "cool", "freezing"],
            "answer": 1
        },
        {
            "q": "My ___ is in April.",
            "options": ["birthday", "birth", "born", "day"],
            "answer": 0
        },
        {
            "q": "I usually ___ to work by bus.",
            "options": ["go", "come", "walk", "drive"],
            "answer": 0
        },
        {
            "q": "Can you ___ me your pen?",
            "options": ["give", "borrow", "lend", "take"],
            "answer": 2
        },
        {
            "q": "She has long ___ hair.",
            "options": ["black", "big", "short", "small"],
            "answer": 0
        },
        {
            "q": "I ___ English at school.",
            "options": ["learn", "teach", "study", "know"],
            "answer": 0
        },
        {
            "q": "The book is ___ the table.",
            "options": ["in", "on", "at", "under"],
            "answer": 1
        },
    ],
    
    "A2": [
        {
            "q": "The weather is terrible today. It's ___.",
            "options": ["raining", "sunny", "beautiful", "nice"],
            "answer": 0
        },
        {
            "q": "I need to ___ my homework before dinner.",
            "options": ["make", "do", "take", "have"],
            "answer": 1
        },
        {
            "q": "Can you ___ me a favor?",
            "options": ["make", "do", "give", "take"],
            "answer": 1
        },
        {
            "q": "I'm ___ forward to seeing you.",
            "options": ["looking", "watching", "seeing", "waiting"],
            "answer": 0
        },
        {
            "q": "She has a good sense of ___.",
            "options": ["humor", "laugh", "fun", "joke"],
            "answer": 0
        },
        {
            "q": "Please ___ a seat.",
            "options": ["take", "sit", "make", "have"],
            "answer": 0
        },
        {
            "q": "I'll ___ you at the station.",
            "options": ["meet", "see", "find", "get"],
            "answer": 0
        },
        {
            "q": "She always ___ a lot of questions.",
            "options": ["makes", "does", "asks", "says"],
            "answer": 2
        },
        {
            "q": "Don't ___ about it. Everything will be fine.",
            "options": ["think", "worry", "care", "mind"],
            "answer": 1
        },
        {
            "q": "I need to ___ some money from the bank.",
            "options": ["take", "get", "withdraw", "receive"],
            "answer": 2
        },
        {
            "q": "The opposite of 'cheap' is ___.",
            "options": ["expensive", "costly", "dear", "pricey"],
            "answer": 0
        },
        {
            "q": "Can you ___ the difference?",
            "options": ["say", "tell", "speak", "talk"],
            "answer": 1
        },
        {
            "q": "I'll ___ my best to help you.",
            "options": ["make", "do", "try", "give"],
            "answer": 1
        },
        {
            "q": "She ___ an appointment with the doctor.",
            "options": ["took", "made", "did", "had"],
            "answer": 1
        },
        {
            "q": "Please ___ attention to what I'm saying.",
            "options": ["give", "take", "make", "pay"],
            "answer": 3
        },
    ],
    
    "B1": [
    {"q": "The government plans to ___ taxes next year.",
     "options": ["increase", "arrive", "listen", "climb"], "answer": 0},
    
    {"q": "Pollution has a serious ___ on health.",
     "options": ["effect", "food", "friend", "lesson"], "answer": 0},
    
    {"q": "She made an important ___.",
     "options": ["feeling", "think", "chair", "decision"], "answer": 3},
    
    {"q": "The company faces strong ___.",
     "options": ["competition", "holiday", "music", "weather"], "answer": "competition"},
    
    {"q": "We need to find a ___ to this problem.",
     "options": ["solution", "shoe", "window", "shirt"], "answer": "solution"},
    
    {"q": "He is very ___ in science.",
     "options": ["interested", "interesting", "interest", "interests"], "answer": "interested"},
    
    {"q": "The number of students has ___.",
     "options": ["increased", "slept", "broken", "fallen"], "answer": "increased"},
    
    {"q": "The teacher explained the lesson ___.",
     "options": ["clearly", "clear", "clearness", "cleared"], "answer": "clearly"},
    
    {"q": "She showed great ___.",
     "options": ["confidence", "coffee", "traffic", "forest"], "answer": "confidence"},
    
    {"q": "The economy is facing a serious ___.",
     "options": ["crisis", "picnic", "party", "game"], "answer": "crisis"},
    
    {"q": "The results were very ___.",
     "options": ["significant", "yellow", "cheap", "short"], "answer": "significant"},
    
    {"q": "He apologized ___ being late.",
     "options": ["for", "to", "at", "with"], "answer": "for"},
    
    {"q": "The project was ___ because of lack of money.",
     "options": ["delayed", "completed", "improved", "approved"], "answer": "delayed"},
    
    {"q": "She is responsible ___ the project.",
     "options": ["for", "of", "with", "at"], "answer": "for"},
    
    {"q": "The issue is highly ___.",
     "options": ["controversial", "blue", "small", "easy"], "answer": "controversial"},
    
    {"q": "The government must ___ new laws.",
     "options": ["enforce", "eat", "sleep", "paint"], "answer": "enforce"},
    
    {"q": "He gave a short ___.",
     "options": ["speech", "banana", "shoe", "garden"], "answer": "speech"},
    
    {"q": "The policy had a positive ___.",
     "options": ["impact", "apple", "music", "shirt"], "answer": "impact"},
    
    {"q": "There is strong ___ between diet and health.",
     "options": ["connection", "window", "lesson", "chair"], "answer": "connection"}
{"q": "The results are ___ with previous studies.",
 "options": ["consistent", "hungry", "cheap", "angry"], "answer": 0}, 
        {"q": "The government plans to ___ taxes next year.", "options": ["increase", "arrive", "listen", "climb"], "answer": "increase"},
    {"q": "Pollution has a serious ___ on health.", "options": ["effect", "food", "friend", "lesson"], "answer": "effect"},
    {"q": "She made an important ___.", "options": ["decision", "banana", "chair", "river"], "answer": "decision"},
    {"q": "The company faces strong ___.", "options": ["competition", "holiday", "music", "weather"], "answer": "competition"},
    {"q": "We need to find a ___ to this problem.", "options": ["solution", "shoe", "window", "shirt"], "answer": "solution"},
    {"q": "He is very ___ in science.", "options": ["interested", "interesting", "interest", "interests"], "answer": "interested"},
    {"q": "The number of students has ___.", "options": ["increased", "slept", "broken", "fallen"], "answer": "increased"},
    {"q": "The teacher explained the lesson ___.", "options": ["clearly", "clear", "clearness", "cleared"], "answer": "clearly"},
    {"q": "She showed great ___.", "options": ["confidence", "coffee", "traffic", "forest"], "answer": "confidence"},
    {"q": "The economy is facing a serious ___.", "options": ["crisis", "picnic", "party", "game"], "answer": "crisis"},
        {
            "q": "The project was completed ___ schedule.",
            "options": ["on", "in", "at", "by"],
            "answer": 0
        },
        {
            "q": "She's very ___ about environmental issues.",
            "options": ["concerned", "worried", "anxious", "nervous"],
            "answer": 0
        },
        {
            "q": "The company decided to ___ the contract.",
            "options": ["cancel", "terminate", "finish", "end"],
            "answer": 1
        },
        {
            "q": "I couldn't ___ up with his rude behavior.",
            "options": ["put", "keep", "make", "take"],
            "answer": 0
        },
        {
            "q": "The meeting has been ___ until next week.",
            "options": ["delayed", "postponed", "cancelled", "moved"],
            "answer": 1
        },
        {
            "q": "She has a natural ___ for languages.",
            "options": ["talent", "skill", "ability", "aptitude"],
            "answer": 3
        },
        {
            "q": "The medicine should ___ the pain.",
            "options": ["reduce", "relieve", "ease", "lessen"],
            "answer": 1
        },
        {
            "q": "We need to ___ a solution to this problem.",
            "options": ["find", "discover", "achieve", "reach"],
            "answer": 0
        },
        {
            "q": "The evidence ___ his innocence.",
            "options": ["proves", "shows", "demonstrates", "confirms"],
            "answer": 3
        },
        {
            "q": "She tends to ___ conclusions too quickly.",
            "options": ["make", "jump to", "reach", "draw"],
            "answer": 1
        },
        {
            "q": "The government implemented new ___ to reduce pollution.",
            "options": ["rules", "regulations", "laws", "policies"],
            "answer": 3
        },
        {
            "q": "His speech made a strong ___ on the audience.",
            "options": ["effect", "impact", "influence", "impression"],
            "answer": 3
        },
        {
            "q": "The results ___ our initial hypothesis.",
            "options": ["support", "prove", "confirm", "verify"],
            "answer": 0
        },
        {
            "q": "She has a ___ understanding of the subject.",
            "options": ["deep", "strong", "thorough", "complete"],
            "answer": 2
        },
        {
            "q": "The company is ___ financial difficulties.",
            "options": ["facing", "meeting", "having", "experiencing"],
            "answer": 3
        },
    ],
    
    "B2": [
        {
            "q": "The proposal was met with ___ opposition.",
            "options": ["fierce", "strong", "heavy", "intense"],
            "answer": 0
        },
        {
            "q": "The new policy has ___ controversy.",
            "options": ["sparked", "caused", "created", "made"],
            "answer": 0
        },
        {
            "q": "She has a ___ for mathematics.",
            "options": ["talent", "gift", "flair", "knack"],
            "answer": 3
        },
        {
            "q": "The investigation ___ serious misconduct.",
            "options": ["revealed", "uncovered", "exposed", "disclosed"],
            "answer": 1
        },
        {
            "q": "The company aims to ___ market share.",
            "options": ["increase", "expand", "grow", "boost"],
            "answer": 0
        },
        {
            "q": "The defendant ___ all the charges.",
            "options": ["refused", "rejected", "denied", "declined"],
            "answer": 2
        },
        {
            "q": "The treaty ___ both countries to reduce emissions.",
            "options": ["obliges", "requires", "compels", "forces"],
            "answer": 0
        },
        {
            "q": "The evidence was deemed ___ in court.",
            "options": ["inadmissible", "unacceptable", "invalid", "irrelevant"],
            "answer": 0
        },
        {
            "q": "The report ___ several key findings.",
            "options": ["highlights", "emphasizes", "stresses", "underlines"],
            "answer": 0
        },
        {
            "q": "The author ___ from personal experience.",
            "options": ["draws", "takes", "gets", "derives"],
            "answer": 0
        },
        {
            "q": "The policy has come under ___ scrutiny.",
            "options": ["intense", "severe", "heavy", "close"],
            "answer": 0
        },
        {
            "q": "The company is seeking to ___ its operations.",
            "options": ["streamline", "simplify", "reduce", "optimize"],
            "answer": 0
        },
        {
            "q": "The decision was ___ criticized.",
            "options": ["widely", "broadly", "extensively", "generally"],
            "answer": 0
        },
        {
            "q": "The findings ___ further investigation.",
            "options": ["warrant", "justify", "merit", "require"],
            "answer": 0
        },
        {
            "q": "The legislation aims to ___ discrimination.",
            "options": ["combat", "fight", "tackle", "address"],
            "answer": 0
        },
    ],
    
    "C1": [
        {
            "q": "The government's austerity measures have ___ widespread discontent.",
            "options": ["provoked", "instigated", "engendered", "precipitated"],
            "answer": 2
        },
        {
            "q": "The committee decided to ___ the proposed changes.",
            "options": ["implement", "enact", "effectuate", "institute"],
            "answer": 1
        },
        {
            "q": "The evidence was ___ by expert testimony.",
            "options": ["supported", "corroborated", "substantiated", "validated"],
            "answer": 1
        },
        {
            "q": "The policy was designed to ___ economic growth.",
            "options": ["stimulate", "foster", "promote", "facilitate"],
            "answer": 1
        },
        {
            "q": "The report ___ significant concerns about safety.",
            "options": ["raises", "poses", "presents", "articulates"],
            "answer": 0
        },
        {
            "q": "The legal framework remains ___ unclear.",
            "options": ["somewhat", "rather", "fairly", "decidedly"],
            "answer": 1
        },
        {
            "q": "The organization seeks to ___ international cooperation.",
            "options": ["promote", "foster", "facilitate", "encourage"],
            "answer": 2
        },
        {
            "q": "The phenomenon is ___ to urban areas.",
            "options": ["particular", "specific", "peculiar", "unique"],
            "answer": 2
        },
        {
            "q": "The study ___ the need for further research.",
            "options": ["underscores", "emphasizes", "highlights", "stresses"],
            "answer": 0
        },
        {
            "q": "The proposal was deemed financially ___.",
            "options": ["unfeasible", "impractical", "unviable", "untenable"],
            "answer": 2
        },
        {
            "q": "The treaty aims to ___ climate change.",
            "options": ["mitigate", "alleviate", "ameliorate", "assuage"],
            "answer": 0
        },
        {
            "q": "The decision has ___ implications for policy.",
            "options": ["profound", "significant", "substantial", "considerable"],
            "answer": 0
        },
        {
            "q": "The author ___ complex philosophical concepts.",
            "options": ["explores", "examines", "investigates", "elucidates"],
            "answer": 3
        },
        {
            "q": "The legislation was enacted to ___ existing laws.",
            "options": ["supplement", "complement", "augment", "reinforce"],
            "answer": 1
        },
        {
            "q": "The research ___ conventional wisdom.",
            "options": ["challenges", "disputes", "contests", "refutes"],
            "answer": 0
        },
    {"q": "The government introduced new policies to ___ economic growth.", 
     "options": ["stimulate", "destroy", "reduce", "ignore"], "answer": 0},

    {"q": "Many scientists are concerned about the rapid ___ of climate change.", 
     "options": ["decline", "acceleration", "prevention", "disappearance"], "answer": 1},

    {"q": "The company aims to ___ its market share in Asia.", 
     "options": ["expand", "shorten", "weaken", "limit"], "answer": 0},

    {"q": "There is growing ___ that artificial intelligence may replace human jobs.", 
     "options": ["agreement", "concern", "celebration", "certainty"], "answer": 1},

    {"q": "The research provides ___ evidence to support the theory.", 
     "options": ["weak", "limited", "compelling", "minor"], "answer": 2},

    {"q": "Many students face financial ___ while studying abroad.", 
     "options": ["advantages", "benefits", "constraints", "luxuries"], "answer": 2},

    {"q": "The new system is designed to improve workplace ___.", 
     "options": ["efficiency", "confusion", "failure", "delay"], "answer": 0},

    {"q": "Pollution has a detrimental ___ on public health.", 
     "options": ["effect", "result", "impact", "damage"], "answer": 2},

    {"q": "The results were ___ different from what we expected.", 
     "options": ["significantly", "barely", "hardly", "slightly"], "answer": 0},

    {"q": "The government should take ___ action to address unemployment.", 
     "options": ["immediate", "slow", "optional", "minor"], "answer": 0},

    {"q": "The company faced fierce ___ from its competitors.", 
     "options": ["cooperation", "competition", "celebration", "discussion"], "answer": 1},

    {"q": "The policy was implemented to reduce income ___.", 
     "options": ["equality", "inequality", "similarity", "balance"], "answer": 1},

    {"q": "The professor delivered a ___ lecture on global economics.", 
     "options": ["boring", "insightful", "ordinary", "basic"], "answer": 1},

    {"q": "The number of car accidents has ___ dramatically over the past decade.", 
     "options": ["increased", "improved", "solved", "recovered"], "answer": 0},

    {"q": "The issue remains highly ___ among experts.", 
     "options": ["controversial", "clear", "obvious", "simple"], "answer": 0},

    {"q": "The organization provides financial ___ to low-income families.", 
     "options": ["assistance", "damage", "restriction", "punishment"], "answer": 0},

    {"q": "The project was ___ due to a lack of funding.", 
     "options": ["completed", "delayed", "accelerated", "approved"], "answer": 1},

    {"q": "The findings highlight the ___ of early education.", 
     "options": ["importance", "weakness", "difficulty", "danger"], "answer": 0},

    {"q": "The company has adopted a more environmentally ___ approach.", 
     "options": ["friendly", "hostile", "harmful", "careless"], "answer": 0},

    {"q": "There is a growing demand for highly ___ workers.", 
     "options": ["skilled", "lazy", "weak", "untrained"], "answer": 0},

    {"q": "The government must ___ stricter regulations.", 
     "options": ["enforce", "ignore", "remove", "avoid"], "answer": 0},

    {"q": "The new law has had a profound ___ on society.", 
     "options": ["impact", "problem", "question", "debate"], "answer": 0},

    {"q": "The scientist proposed a ___ solution to the problem.", 
     "options": ["temporary", "innovative", "traditional", "simple"], "answer": 1},

    {"q": "The company is facing serious financial ___.", 
     "options": ["stability", "growth", "difficulties", "profits"], "answer": 2},

    {"q": "The government aims to ___ poverty in rural areas.", 
     "options": ["reduce", "increase", "expand", "ignore"], "answer": 0},

    {"q": "The results were ___ with previous studies.", 
     "options": ["consistent", "confused", "inconsistent", "irrelevant"], "answer": 0},

    {"q": "The rapid ___ of technology has transformed communication.", 
     "options": ["development", "decline", "loss", "damage"], "answer": 0},

    {"q": "The company needs to ___ its strategy to remain competitive.", 
     "options": ["adapt", "destroy", "ignore", "remove"], "answer": 0},

    {"q": "The study emphasizes the need for sustainable ___.", 
     "options": ["development", "destruction", "reduction", "decline"], "answer": 0},

    {"q": "The problem is becoming increasingly ___.", 
     "options": ["serious", "minor", "simple", "clear"], "answer": 0}
    ],
    
    "C2": [
        {
            "q": "The author's prose is characterized by ___ precision.",
            "options": ["meticulous", "scrupulous", "fastidious", "punctilious"],
            "answer": 0
        },
        {
            "q": "The argument is predicated on ___ assumptions.",
            "options": ["dubious", "questionable", "tenuous", "specious"],
            "answer": 2
        },
        {
            "q": "The policy has proven to be politically ___.",
            "options": ["contentious", "divisive", "fractious", "polarizing"],
            "answer": 3
        },
        {
            "q": "The scholar's work ___ traditional interpretations.",
            "options": ["challenges", "subverts", "undermines", "contravenes"],
            "answer": 1
        },
        {
            "q": "The narrative is imbued with ___ symbolism.",
            "options": ["allegorical", "metaphorical", "emblematic", "figurative"],
            "answer": 0
        },
        {
            "q": "The legislation seeks to ___ systemic inequities.",
            "options": ["rectify", "redress", "remedy", "ameliorate"],
            "answer": 1
        },
        {
            "q": "The phenomenon remains ___ understood.",
            "options": ["incompletely", "imperfectly", "inadequately", "insufficiently"],
            "answer": 1
        },
        {
            "q": "The theory has been ___ by empirical research.",
            "options": ["vindicated", "corroborated", "substantiated", "validated"],
            "answer": 0
        },
        {
            "q": "The discourse is marked by ___ complexity.",
            "options": ["Byzantine", "labyrinthine", "convoluted", "intricate"],
            "answer": 1
        },
        {
            "q": "The writer employs ___ irony throughout.",
            "options": ["subtle", "nuanced", "understated", "oblique"],
            "answer": 1
        },
        {
            "q": "The policy remains ___ controversial.",
            "options": ["perennially", "perpetually", "persistently", "invariably"],
            "answer": 0
        },
        {
            "q": "The analysis is both ___ and comprehensive.",
            "options": ["incisive", "penetrating", "trenchant", "perspicacious"],
            "answer": 2
        },
        {
            "q": "The argument proceeds from ___ premises.",
            "options": ["axiomatic", "self-evident", "incontrovertible", "apodictic"],
            "answer": 3
        },
        {
            "q": "The work is ___ of modernist aesthetics.",
            "options": ["emblematic", "paradigmatic", "exemplary", "archetypal"],
            "answer": 1
        },
        {
            "q": "The critique is both ___ and erudite.",
            "options": ["cogent", "compelling", "persuasive", "trenchant"],
            "answer": 3
        },
    ],
    "A1": [
        {"q": "I feel very ___ today.", "options": ["happy", "economic", "complex", "global"], "answer": 0},
        {"q": "She has a ___ cat.", "options": ["blue", "small", "difficult", "expensive"], "answer": 1},
        {"q": "I ___ my homework every day.", "options": ["do", "make", "build", "create"], "answer": 0},
        {"q": "This book is very ___.", "options": ["interesting", "pollution", "government", "analysis"], "answer": 0},
        {"q": "We eat ___ every morning.", "options": ["breakfast", "internet", "money", "traffic"], "answer": 0},
        {"q": "My father works in an ___.", "options": ["office", "forest", "airport", "river"], "answer": 0},
        {"q": "She is my best ___.", "options": ["friend", "system", "project", "policy"], "answer": 0},
        {"q": "I like to ___ music.", "options": ["listen to", "watch", "look", "read"], "answer": 0},
        {"q": "The sun is very ___ today.", "options": ["hot", "slow", "cheap", "late"], "answer": 0},
        {"q": "He can ___ English.", "options": ["speak", "build", "grow", "drive"], "answer": 0}
    ],

    "A2": [
        {"q": "I usually ___ up at 7 a.m.", "options": ["wake", "stand", "sit", "open"], "answer": 0},
        {"q": "She is afraid of ___.", "options": ["spiders", "economy", "science", "culture"], "answer": 0},
        {"q": "The movie was very ___.", "options": ["boring", "pollution", "industry", "research"], "answer": 0},
        {"q": "I need to buy some ___ for dinner.", "options": ["food", "traffic", "homework", "advice"], "answer": 0},
        {"q": "He is wearing a ___ jacket.", "options": ["black", "global", "academic", "social"], "answer": 0},
        {"q": "We went on a school ___.", "options": ["trip", "policy", "analysis", "debate"], "answer": 0},
        {"q": "She sent me a ___.", "options": ["message", "theory", "project", "strategy"], "answer": 0},
        {"q": "I forgot my ___.", "options": ["keys", "environment", "education", "evidence"], "answer": 0},
        {"q": "The shop is ___ today.", "options": ["closed", "advanced", "complex", "efficient"], "answer": 0},
        {"q": "He is very ___ at football.", "options": ["good", "significant", "major", "formal"], "answer": 0}
    ],

    "B1": [
        {"q": "The government plans to ___ taxes next year.", "options": ["increase", "listen", "arrive", "climb"], "answer": 0},
        {"q": "The company is facing financial ___.", "options": ["problems", "happiness", "weather", "flowers"], "answer": 0},
        {"q": "She made a very important ___.", "options": ["decision", "banana", "river", "chair"], "answer": 0},
        {"q": "Pollution has become a serious ___.", "options": ["issue", "friend", "meal", "holiday"], "answer": 0},
        {"q": "He gave a short ___.", "options": ["speech", "apple", "shoe", "garden"], "answer": 0},
        {"q": "There is a strong ___ between diet and health.", "options": ["connection", "chair", "lesson", "window"], "answer": 0},
        {"q": "The number of students has ___.", "options": ["increased", "slept", "broken", "fallen asleep"], "answer": 0},
        {"q": "She showed great ___.", "options": ["confidence", "sandwich", "forest", "traffic"], "answer": 0},
        {"q": "We need to find a ___.", "options": ["solution", "shirt", "pen", "song"], "answer": 0},
        {"q": "He is responsible for the ___.", "options": ["project", "banana", "holiday", "shoe"], "answer": 0}
    ],

    "B2": [
        {"q": "The company aims to ___ its profits.", "options": ["maximize", "sleep", "ignore", "forget"], "answer": 0},
        {"q": "There is growing ___ about climate change.", "options": ["concern", "banana", "music", "friend"], "answer": 0},
        {"q": "The results were highly ___.", "options": ["significant", "yellow", "tall", "cheap"], "answer": 0},
        {"q": "The government introduced new ___.", "options": ["regulations", "sandwiches", "flowers", "chairs"], "answer": 0},
        {"q": "The issue remains ___.", "options": ["controversial", "happy", "blue", "simple"], "answer": 0},
        {"q": "The policy had a negative ___.", "options": ["impact", "table", "window", "river"], "answer": 0},
        {"q": "The company must ___ quickly.", "options": ["adapt", "eat", "sleep", "run"], "answer": 0},
        {"q": "The study provides strong ___.", "options": ["evidence", "chicken", "holiday", "shirt"], "answer": 0},
        {"q": "There are several ___ to consider.", "options": ["factors", "bananas", "roads", "pens"], "answer": 0},
        {"q": "The economy is facing a ___.", "options": ["crisis", "picnic", "lesson", "gift"], "answer": 0}
    ],

    "C1": [
        {"q": "The proposal was met with widespread ___.", "options": ["criticism", "apples", "happiness", "chairs"], "answer": 0},
        {"q": "The findings were ___ with previous research.", "options": ["consistent", "hungry", "cheap", "angry"], "answer": 0},
        {"q": "The government must ___ corruption.", "options": ["combat", "cook", "paint", "carry"], "answer": 0},
        {"q": "The issue is highly ___.", "options": ["complex", "yellow", "short", "easy"], "answer": 0},
        {"q": "She demonstrated remarkable ___.", "options": ["resilience", "banana", "holiday", "music"], "answer": 0},
        {"q": "The company faces fierce ___.", "options": ["competition", "weather", "chair", "coffee"], "answer": 0},
        {"q": "The results were ___ unexpected.", "options": ["utterly", "slightly", "barely", "weakly"], "answer": 0},
        {"q": "The theory remains largely ___.", "options": ["unchallenged", "hungry", "blue", "fast"], "answer": 0},
        {"q": "The policy has long-term ___.", "options": ["implications", "apples", "flowers", "cars"], "answer": 0},
        {"q": "The argument lacks sufficient ___.", "options": ["evidence", "music", "traffic", "bread"], "answer": 0}
    ],

    "C2": [
        {"q": "The speech was remarkably ___.", "options": ["eloquent", "happy", "big", "short"], "answer": 0},
        {"q": "The theory was eventually ___.", "options": ["refuted", "eaten", "bought", "cleaned"], "answer": 0},
        {"q": "The policy proved to be ___.", "options": ["counterproductive", "blue", "cheap", "friendly"], "answer": 0},
        {"q": "He delivered a ___ critique.", "options": ["scathing", "small", "warm", "soft"], "answer": 0},
        {"q": "The results were largely ___.", "options": ["inconclusive", "happy", "fast", "tiny"], "answer": 0},
        {"q": "The argument was fundamentally ___.", "options": ["flawed", "green", "tasty", "tall"], "answer": 0},
        {"q": "The decision sparked widespread ___.", "options": ["outrage", "breakfast", "coffee", "lesson"], "answer": 0},
        {"q": "The data was meticulously ___.", "options": ["analyzed", "eaten", "broken", "closed"], "answer": 0},
        {"q": "The theory gained considerable ___.", "options": ["credibility", "apples", "water", "chairs"], "answer": 0},
        {"q": "The strategy was brilliantly ___.", "options": ["executed", "drunk", "cut", "washed"], "answer": 0}
    ],
}
def shuffle_questions(VOCABULARY_QUESTIONS):
    shuffled_list = []
    for q in questions:
        opts = q["options"].copy()
        random.shuffle(opts)
        answer_index = opts.index(q["answer"])
        shuffled_list.append({"q": q["q"], "options": opts, "answer": answer_index})
    return shuffled_list

random_bac_questions = shuffle_questions(questions)

# Example output
for q in random_bac_questions:
    print(q)
