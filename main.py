from flask import Flask, render_template_string
import random

app = Flask(__name__)

WEBSITE_NAME = "SARTHAK TAROT COURSE"


# ============================================================
# MAJOR ARCANA - 22 CARDS
# ============================================================

major_arcana = [
    {
        "name": "The Fool",
        "meaning": "नई शुरुआत, साहस और नए अनुभवों की ओर कदम बढ़ाना।",
        "money": "पैसों में नया अवसर मिल सकता है, लेकिन सोच-समझकर फैसला लें।",
        "education": "नई चीज सीखने और नई शुरुआत करने का अच्छा समय।",
        "health": "ऊर्जा और सकारात्मक सोच पर ध्यान दें।",
        "relationship": "रिश्ते में नई शुरुआत और खुलकर बात करने का संकेत।",
        "business": "नया विचार या नया काम शुरू करने का संकेत।"
    },
    {
        "name": "The Magician",
        "meaning": "कौशल, आत्मविश्वास और अपनी क्षमता का सही उपयोग।",
        "money": "अपनी क्षमता का उपयोग करके कमाई का अवसर।",
        "education": "आप जो सीख रहे हैं उसे सही तरीके से इस्तेमाल करें।",
        "health": "अपनी दिनचर्या और आदतों पर ध्यान दें।",
        "relationship": "बातचीत और समझदारी से रिश्ता बेहतर हो सकता है।",
        "business": "अपने कौशल और विचारों से सफलता पाने का संकेत।"
    },
    {
        "name": "The High Priestess",
        "meaning": "अंतर्ज्ञान, शांति और अंदर की समझ।",
        "money": "जल्दबाजी से बचें और निर्णय से पहले सोचें।",
        "education": "ध्यान लगाकर पढ़ने और गहराई से समझने का समय।",
        "health": "आराम और मानसिक शांति को महत्व दें।",
        "relationship": "भावनाओं को समझने और शांत बातचीत का संकेत।",
        "business": "जानकारी पूरी होने तक महत्वपूर्ण निर्णय रोकना बेहतर हो सकता है।"
    },
    {
        "name": "The Empress",
        "meaning": "विकास, देखभाल, रचनात्मकता और समृद्धि।",
        "money": "विकास और आर्थिक सुधार का संकेत।",
        "education": "सीखने में धीरे-धीरे अच्छा विकास।",
        "health": "आराम, संतुलन और अपनी देखभाल पर ध्यान।",
        "relationship": "प्यार, देखभाल और भावनात्मक गर्माहट।",
        "business": "रचनात्मक विचारों और विकास के लिए अच्छा संकेत।"
    },
    {
        "name": "The Emperor",
        "meaning": "अनुशासन, नेतृत्व और मजबूत निर्णय।",
        "money": "पैसों में योजना और अनुशासन जरूरी है।",
        "education": "नियमित पढ़ाई और अनुशासन से सफलता।",
        "health": "अच्छी दिनचर्या बनाए रखना जरूरी है।",
        "relationship": "रिश्ते में स्थिरता और जिम्मेदारी।",
        "business": "नेतृत्व और मजबूत योजना का संकेत।"
    },
    {
        "name": "The Hierophant",
        "meaning": "परंपरा, ज्ञान और मार्गदर्शन।",
        "money": "अनुभवी व्यक्ति की सलाह उपयोगी हो सकती है।",
        "education": "शिक्षक या मार्गदर्शक से सीखने का अच्छा समय।",
        "health": "अच्छी आदतों और नियमित दिनचर्या पर ध्यान।",
        "relationship": "विश्वास और स्थिरता का संकेत।",
        "business": "नियमों और सही मार्गदर्शन का पालन करें।"
    },
    {
        "name": "The Lovers",
        "meaning": "चुनाव, सामंजस्य और महत्वपूर्ण संबंध।",
        "money": "पैसों से जुड़ा महत्वपूर्ण फैसला।",
        "education": "सही विषय और सही दिशा चुनने का संकेत।",
        "health": "जीवन में संतुलन बनाए रखें।",
        "relationship": "प्यार, समझ और मजबूत संबंध।",
        "business": "सही साझेदारी या महत्वपूर्ण फैसला।"
    },
    {
        "name": "The Chariot",
        "meaning": "दृढ़ इच्छाशक्ति, नियंत्रण और आगे बढ़ना।",
        "money": "लक्ष्य पर ध्यान देने से आर्थिक प्रगति हो सकती है।",
        "education": "मेहनत और ध्यान से पढ़ाई में आगे बढ़ें।",
        "health": "सक्रिय और संतुलित दिनचर्या रखें।",
        "relationship": "रिश्ते में स्पष्ट दिशा और आत्मविश्वास।",
        "business": "लक्ष्य की ओर लगातार आगे बढ़ने का संकेत।"
    },
    {
        "name": "Strength",
        "meaning": "आंतरिक शक्ति, धैर्य और आत्मविश्वास।",
        "money": "धैर्य से आर्थिक स्थिति संभालने का संकेत।",
        "education": "मुश्किल विषयों में भी हार न मानें।",
        "health": "धैर्य और सकारात्मक आदतों पर ध्यान दें।",
        "relationship": "समझदारी और धैर्य रिश्ते को मजबूत कर सकते हैं।",
        "business": "मुश्किल परिस्थितियों में शांत रहकर नेतृत्व करें।"
    },
    {
        "name": "The Hermit",
        "meaning": "आत्मचिंतन, ज्ञान और अकेले सोचने का समय।",
        "money": "बड़ा फैसला लेने से पहले अच्छी तरह सोचें।",
        "education": "अकेले ध्यान लगाकर पढ़ना लाभदायक हो सकता है।",
        "health": "आराम और मानसिक शांति जरूरी है।",
        "relationship": "थोड़ा समय लेकर अपनी भावनाओं को समझें।",
        "business": "रणनीति बनाने और सोचने का समय।"
    },
    {
        "name": "Wheel of Fortune",
        "meaning": "बदलाव, अवसर और परिस्थितियों का घूमना।",
        "money": "आर्थिक स्थिति में बदलाव का संकेत।",
        "education": "नई दिशा या नया अवसर मिल सकता है।",
        "health": "दिनचर्या में सकारात्मक बदलाव करें।",
        "relationship": "रिश्ते में नया मोड़ आ सकता है।",
        "business": "बदलती परिस्थितियों के अनुसार खुद को ढालें।"
    },
    {
        "name": "Justice",
        "meaning": "न्याय, संतुलन और सही निर्णय।",
        "money": "पैसों में निष्पक्ष और सोच-समझकर निर्णय लें।",
        "education": "मेहनत के अनुसार परिणाम पाने का संकेत।",
        "health": "संतुलित दिनचर्या महत्वपूर्ण है।",
        "relationship": "ईमानदारी और बराबरी जरूरी है।",
        "business": "नियम और निष्पक्ष निर्णय महत्वपूर्ण हैं।"
    },
    {
        "name": "The Hanged Man",
        "meaning": "रुकना, नया दृष्टिकोण और धैर्य।",
        "money": "पैसों के मामले में जल्दबाजी न करें।",
        "education": "किसी विषय को अलग नजरिए से समझें।",
        "health": "आराम और संतुलन पर ध्यान दें।",
        "relationship": "स्थिति को दूसरे व्यक्ति के नजरिए से समझें।",
        "business": "रणनीति बदलने की जरूरत हो सकती है।"
    },
    {
        "name": "Death",
        "meaning": "एक चरण का अंत और नए चरण की शुरुआत।",
        "money": "पुरानी आर्थिक आदतों को बदलने का संकेत।",
        "education": "पुराने तरीके छोड़कर नया तरीका अपनाएं।",
        "health": "बेहतर दिनचर्या अपनाने की जरूरत का संकेत।",
        "relationship": "पुराने पैटर्न में बदलाव और नई शुरुआत।",
        "business": "पुराने तरीके खत्म करके नई दिशा अपनाना।"
    },
    {
        "name": "Temperance",
        "meaning": "संतुलन, धैर्य और सही मिश्रण।",
        "money": "कमाई और खर्च में संतुलन रखें।",
        "education": "पढ़ाई और आराम में संतुलन जरूरी है।",
        "health": "संतुलित जीवनशैली अपनाएं।",
        "relationship": "समझ और संतुलन रिश्ते को मजबूत करते हैं।",
        "business": "धैर्य और संतुलित योजना से लाभ।"
    },
    {
        "name": "The Devil",
        "meaning": "बंधन, लालच और गलत आदतों को पहचानना।",
        "money": "अनावश्यक खर्च और लालच से सावधान रहें।",
        "education": "ध्यान भटकाने वाली चीजों से बचें।",
        "health": "अच्छी आदतों को प्राथमिकता दें।",
        "relationship": "अत्यधिक निर्भरता या नियंत्रण से बचें।",
        "business": "गलत समझौते या लालच से सावधान रहें।"
    },
    {
        "name": "The Tower",
        "meaning": "अचानक बदलाव और पुरानी व्यवस्था का टूटना।",
        "money": "आर्थिक मामलों में अचानक बदलाव संभव है।",
        "education": "गलती से सीखकर तरीका बदलने का अवसर।",
        "health": "तनाव कम करने और आराम पर ध्यान दें।",
        "relationship": "सच्चाई सामने आने से बदलाव हो सकता है।",
        "business": "पुरानी योजना बदलने की आवश्यकता हो सकती है।"
    },
    {
        "name": "The Star",
        "meaning": "उम्मीद, प्रेरणा और सकारात्मक दिशा।",
        "money": "आर्थिक स्थिति में उम्मीद और सुधार का संकेत।",
        "education": "अपने लक्ष्य पर विश्वास रखें।",
        "health": "सकारात्मक सोच और आराम महत्वपूर्ण हैं।",
        "relationship": "उम्मीद और भावनात्मक जुड़ाव।",
        "business": "भविष्य के लिए अच्छी उम्मीद और प्रेरणा।"
    },
    {
        "name": "The Moon",
        "meaning": "अनिश्चितता, भावनाएं और भ्रम।",
        "money": "पैसों में अस्पष्ट निर्णय से बचें।",
        "education": "जो समझ न आए उसे दोबारा पढ़ें और पूछें।",
        "health": "आराम और तनाव कम करने पर ध्यान दें।",
        "relationship": "गलतफहमी से बचने के लिए साफ बातचीत करें।",
        "business": "अधूरी जानकारी में फैसला न लें।"
    },
    {
        "name": "The Sun",
        "meaning": "खुशी, सफलता, स्पष्टता और आत्मविश्वास।",
        "money": "आर्थिक मामलों में सकारात्मक ऊर्जा।",
        "education": "सीखने और अच्छे परिणाम के लिए उत्साह।",
        "health": "ऊर्जा और सकारात्मकता का संकेत।",
        "relationship": "खुशी, खुलापन और अच्छा संबंध।",
        "business": "सफलता और स्पष्ट दिशा का संकेत।"
    },
    {
        "name": "Judgement",
        "meaning": "आत्ममूल्यांकन, सीख और नया निर्णय।",
        "money": "पुराने आर्थिक फैसलों से सीखें।",
        "education": "अपनी गलतियों की समीक्षा करके सुधार करें।",
        "health": "अपनी दिनचर्या का मूल्यांकन करें।",
        "relationship": "पुरानी बातों को समझकर आगे बढ़ने का संकेत।",
        "business": "पिछले अनुभवों से सीखकर नया निर्णय लें।"
    },
    {
        "name": "The World",
        "meaning": "पूर्णता, उपलब्धि और एक चक्र का पूरा होना।",
        "money": "किसी आर्थिक लक्ष्य की पूर्णता का संकेत।",
        "education": "एक महत्वपूर्ण सीख या लक्ष्य पूरा होना।",
        "health": "संतुलन और पूर्णता की ओर बढ़ना।",
        "relationship": "रिश्ते में समझ और पूर्णता।",
        "business": "एक बड़े लक्ष्य को पूरा करने का संकेत।"
    }
]


# ============================================================
# MINOR ARCANA - 56 CARDS
# ============================================================

minor_data = {
    "Wands": [
        ("Ace of Wands", "नई ऊर्जा और नई शुरुआत"),
        ("Two of Wands", "भविष्य की योजना और विकल्प"),
        ("Three of Wands", "प्रगति और आगे की तैयारी"),
        ("Four of Wands", "खुशी, स्थिरता और उत्सव"),
        ("Five of Wands", "प्रतिस्पर्धा और अलग-अलग विचार"),
        ("Six of Wands", "जीत, सम्मान और आत्मविश्वास"),
        ("Seven of Wands", "अपने विचार के लिए खड़े रहना"),
        ("Eight of Wands", "तेजी और अचानक प्रगति"),
        ("Nine of Wands", "धैर्य और लगातार प्रयास"),
        ("Ten of Wands", "जिम्मेदारी और अधिक काम"),
        ("Page of Wands", "नई सीख और उत्साह"),
        ("Knight of Wands", "जोश और तेजी से आगे बढ़ना"),
        ("Queen of Wands", "आत्मविश्वास और रचनात्मकता"),
        ("King of Wands", "नेतृत्व और बड़ी सोच")
    ],

    "Cups": [
        ("Ace of Cups", "नई भावनाएं और भावनात्मक शुरुआत"),
        ("Two of Cups", "आपसी समझ और जुड़ाव"),
        ("Three of Cups", "दोस्ती, खुशी और साथ"),
        ("Four of Cups", "सोच-विचार और असंतोष"),
        ("Five of Cups", "निराशा से सीखना"),
        ("Six of Cups", "पुरानी यादें और अपनापन"),
        ("Seven of Cups", "कई विकल्प और कल्पना"),
        ("Eight of Cups", "पुरानी चीज से आगे बढ़ना"),
        ("Nine of Cups", "संतोष और इच्छा की पूर्ति"),
        ("Ten of Cups", "खुशी और भावनात्मक सामंजस्य"),
        ("Page of Cups", "नई भावना और रचनात्मकता"),
        ("Knight of Cups", "भावनात्मक संदेश और कल्पना"),
        ("Queen of Cups", "समझ, करुणा और भावनात्मक बुद्धिमत्ता"),
        ("King of Cups", "भावनात्मक संतुलन और समझदारी")
    ],

    "Swords": [
        ("Ace of Swords", "स्पष्टता और नई सोच"),
        ("Two of Swords", "निर्णय और दो विकल्प"),
        ("Three of Swords", "भावनात्मक कठिनाई से सीखना"),
        ("Four of Swords", "आराम और विचार करने का समय"),
        ("Five of Swords", "मतभेद और सावधानी"),
        ("Six of Swords", "कठिन स्थिति से आगे बढ़ना"),
        ("Seven of Swords", "रणनीति और सावधानी"),
        ("Eight of Swords", "खुद को सीमित महसूस करना"),
        ("Nine of Swords", "चिंता और ज्यादा सोचने से बचना"),
        ("Ten of Swords", "एक कठिन चरण का अंत"),
        ("Page of Swords", "जिज्ञासा और नई जानकारी"),
        ("Knight of Swords", "तेज सोच और तेज कार्रवाई"),
        ("Queen of Swords", "स्पष्ट सोच और ईमानदारी"),
        ("King of Swords", "तर्क, ज्ञान और निष्पक्ष निर्णय")
    ],

    "Pentacles": [
        ("Ace of Pentacles", "नया अवसर और स्थिर शुरुआत"),
        ("Two of Pentacles", "संतुलन और कई जिम्मेदारियां"),
        ("Three of Pentacles", "टीमवर्क और कौशल"),
        ("Four of Pentacles", "सुरक्षा और चीजों को संभालकर रखना"),
        ("Five of Pentacles", "कठिन समय और सहायता की जरूरत"),
        ("Six of Pentacles", "देना, लेना और सहयोग"),
        ("Seven of Pentacles", "धैर्य और मेहनत का परिणाम"),
        ("Eight of Pentacles", "अभ्यास और कौशल में सुधार"),
        ("Nine of Pentacles", "आत्मनिर्भरता और उपलब्धि"),
        ("Ten of Pentacles", "स्थिरता और लंबे समय की सफलता"),
        ("Page of Pentacles", "नई पढ़ाई और व्यावहारिक सीख"),
        ("Knight of Pentacles", "धीमी लेकिन लगातार प्रगति"),
        ("Queen of Pentacles", "व्यावहारिक सोच और देखभाल"),
        ("King of Pentacles", "स्थिरता, अनुभव और सफलता")
    ]
}


minor_arcana = []

for suit, cards in minor_data.items():
    for name, meaning in cards:
        minor_arcana.append({
            "name": name,
            "suit": suit,
            "meaning": meaning,
            "money": meaning,
            "education": meaning,
            "health": meaning,
            "relationship": meaning,
            "business": meaning
        })


# ============================================================
# ALL 78 CARDS
# ============================================================

all_cards = major_arcana + minor_arcana


# ============================================================
# QUIZ QUESTIONS
# ============================================================

quiz_bank = [
    {
        "question": "कुल कितने Tarot Cards होते हैं?",
        "options": ["56", "72", "78", "82"],
        "answer": "78"
    },
    {
        "question": "Major Arcana में कितने Cards होते हैं?",
        "options": ["20", "22", "24", "26"],
        "answer": "22"
    },
    {
        "question": "Minor Arcana में कितने Cards होते हैं?",
        "options": ["44", "52", "56", "60"],
        "answer": "56"
    },
    {
        "question": "Minor Arcana में कितने Suits होते हैं?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "The Fool किस Arcana का Card है?",
        "options": ["Minor Arcana", "Major Arcana", "Cups", "Pentacles"],
        "answer": "Major Arcana"
    },
    {
        "question": "The Magician मुख्य रूप से किससे जुड़ा है?",
        "options": ["कौशल और क्षमता", "भ्रम", "अंत", "आराम"],
        "answer": "कौशल और क्षमता"
    },
    {
        "question": "The Empress किससे जुड़ा है?",
        "options": ["विकास", "डर", "संघर्ष", "अनिश्चितता"],
        "answer": "विकास"
    },
    {
        "question": "The Emperor किसका संकेत देता है?",
        "options": ["अनुशासन", "भ्रम", "अकेलापन", "कल्पना"],
        "answer": "अनुशासन"
    },
    {
        "question": "The Lovers किससे जुड़ा है?",
        "options": ["चुनाव और संबंध", "आराम", "अंत", "प्रतिस्पर्धा"],
        "answer": "चुनाव और संबंध"
    },
    {
        "question": "The Chariot किससे जुड़ा है?",
        "options": ["आगे बढ़ना", "रुकना", "भ्रम", "पुरानी यादें"],
        "answer": "आगे बढ़ना"
    },
    {
        "question": "Strength का मुख्य अर्थ क्या है?",
        "options": ["आंतरिक शक्ति", "हार", "भ्रम", "अकेलापन"],
        "answer": "आंतरिक शक्ति"
    },
    {
        "question": "The Hermit किससे जुड़ा है?",
        "options": ["आत्मचिंतन", "उत्सव", "प्रतिस्पर्धा", "तेजी"],
        "answer": "आत्मचिंतन"
    },
    {
        "question": "Wheel of Fortune किसका संकेत देता है?",
        "options": ["बदलाव", "स्थिरता", "अंत", "आराम"],
        "answer": "बदलाव"
    },
    {
        "question": "Justice किससे जुड़ा है?",
        "options": ["न्याय और संतुलन", "कल्पना", "डर", "जोश"],
        "answer": "न्याय और संतुलन"
    },
    {
        "question": "Temperance का मुख्य संदेश क्या है?",
        "options": ["संतुलन", "जल्दबाजी", "संघर्ष", "भ्रम"],
        "answer": "संतुलन"
    },
    {
        "question": "The Star किसका संकेत है?",
        "options": ["उम्मीद", "भ्रम", "हार", "मतभेद"],
        "answer": "उम्मीद"
    },
    {
        "question": "The Sun किससे जुड़ा है?",
        "options": ["खुशी और स्पष्टता", "डर", "अकेलापन", "रुकावट"],
        "answer": "खुशी और स्पष्टता"
    },
    {
        "question": "The World किसका संकेत देता है?",
        "options": ["पूर्णता", "भ्रम", "संघर्ष", "अनिश्चितता"],
        "answer": "पूर्णता"
    },
    {
        "question": "Wands का सामान्य संबंध किससे है?",
        "options": ["ऊर्जा और कार्य", "भावनाएं", "तर्क", "भौतिक स्थिरता"],
        "answer": "ऊर्जा और कार्य"
    },
    {
        "question": "Cups का सामान्य संबंध किससे है?",
        "options": ["भावनाएं", "ऊर्जा", "तर्क", "धन"],
        "answer": "भावनाएं"
    },
    {
        "question": "Swords का सामान्य संबंध किससे है?",
        "options": ["सोच और निर्णय", "भावनाएं", "उत्सव", "धन"],
        "answer": "सोच और निर्णय"
    },
    {
        "question": "Pentacles का सामान्य संबंध किससे है?",
        "options": ["भौतिक जीवन", "भावनाएं", "कल्पना", "रिश्ते"],
        "answer": "भौतिक जीवन"
    },
    {
        "question": "Ace of Wands किसका संकेत देता है?",
        "options": ["नई ऊर्जा", "अंत", "आराम", "भ्रम"],
        "answer": "नई ऊर्जा"
    },
    {
        "question": "Two of Cups किससे जुड़ा है?",
        "options": ["आपसी समझ", "संघर्ष", "अकेलापन", "भ्रम"],
        "answer": "आपसी समझ"
    },
    {
        "question": "Ace of Swords किससे जुड़ा है?",
        "options": ["स्पष्टता", "पुरानी यादें", "उत्सव", "आराम"],
        "answer": "स्पष्टता"
    },
    {
        "question": "Eight of Pentacles किससे जुड़ा है?",
        "options": ["अभ्यास और कौशल", "भ्रम", "अंत", "डर"],
        "answer": "अभ्यास और कौशल"
    },
    {
        "question": "Nine of Cups किससे जुड़ा है?",
        "options": ["संतोष", "संघर्ष", "अनिश्चितता", "अकेलापन"],
        "answer": "संतोष"
    },
    {
        "question": "Six of Wands किसका संकेत है?",
        "options": ["जीत और सम्मान", "डर", "भ्रम", "रुकावट"],
        "answer": "जीत और सम्मान"
    },
    {
        "question": "Queen of Cups किससे जुड़ी है?",
        "options": ["समझ और करुणा", "तेजी", "प्रतिस्पर्धा", "भौतिक सफलता"],
        "answer": "समझ और करुणा"
    },
    {
        "question": "King of Swords किससे जुड़ा है?",
        "options": ["तर्क और निर्णय", "भावनात्मक शुरुआत", "उत्सव", "कल्पना"],
        "answer": "तर्क और निर्णय"
    },
    {
        "question": "Ten of Pentacles किससे जुड़ा है?",
        "options": ["स्थिरता", "भ्रम", "तेजी", "असंतोष"],
        "answer": "स्थिरता"
    },
    {
        "question": "The Moon किससे जुड़ा है?",
        "options": ["अनिश्चितता", "स्पष्टता", "जीत", "पूर्णता"],
        "answer": "अनिश्चितता"
    },
    {
        "question": "The Tower किससे जुड़ा है?",
        "options": ["अचानक बदलाव", "स्थिरता", "आराम", "उत्सव"],
        "answer": "अचानक बदलाव"
    },
    {
        "question": "Death Card का शैक्षिक अर्थ क्या हो सकता है?",
        "options": [
            "पुराना तरीका बदलना",
            "कुछ भी न सीखना",
            "हमेशा जीतना",
            "केवल आराम करना"
        ],
        "answer": "पुराना तरीका बदलना"
    },
    {
        "question": "The High Priestess किससे जुड़ी है?",
        "options": ["अंतर्ज्ञान", "प्रतिस्पर्धा", "धन", "उत्सव"],
        "answer": "अंतर्ज्ञान"
    },
    {
        "question": "The Hierophant किससे जुड़ा है?",
        "options": ["ज्ञान और मार्गदर्शन", "भ्रम", "तेजी", "अचानक बदलाव"],
        "answer": "ज्ञान और मार्गदर्शन"
    },
    {
        "question": "The Hanged Man किसका संदेश देता है?",
        "options": ["नया दृष्टिकोण", "जल्दबाजी", "प्रतिस्पर्धा", "उत्सव"],
        "answer": "नया दृष्टिकोण"
    },
    {
        "question": "Judgement किससे जुड़ा है?",
        "options": ["आत्ममूल्यांकन", "भ्रम", "अकेलापन", "प्रतिस्पर्धा"],
        "answer": "आत्ममूल्यांकन"
    },
    {
        "question": "The Devil किससे सावधान रहने का संकेत दे सकता है?",
        "options": ["गलत आदतों से", "अच्छी योजना से", "सीखने से", "अनुशासन से"],
        "answer": "गलत आदतों से"
    },
    {
        "question": "Page of Pentacles किससे जुड़ा है?",
        "options": ["नई पढ़ाई", "अचानक अंत", "भ्रम", "संघर्ष"],
        "answer": "नई पढ़ाई"
    },
    {
        "question": "Knight of Pentacles किसका संकेत देता है?",
        "options": ["लगातार प्रगति", "जल्दबाजी", "भ्रम", "अचानक अंत"],
        "answer": "लगातार प्रगति"
    },
    {
        "question": "Four of Wands किससे जुड़ा है?",
        "options": ["खुशी और उत्सव", "चिंता", "अकेलापन", "अनिश्चितता"],
        "answer": "खुशी और उत्सव"
    },
    {
        "question": "Seven of Cups किससे जुड़ा है?",
        "options": ["कई विकल्प", "पूर्णता", "स्थिरता", "अनुशासन"],
        "answer": "कई विकल्प"
    },
    {
        "question": "Four of Swords किसका संकेत देता है?",
        "options": ["आराम", "प्रतिस्पर्धा", "तेजी", "नई शुरुआत"],
        "answer": "आराम"
    },
    {
        "question": "Three of Pentacles किससे जुड़ा है?",
        "options": ["टीमवर्क", "भ्रम", "अंत", "डर"],
        "answer": "टीमवर्क"
    },
    {
        "question": "Nine of Wands किससे जुड़ा है?",
        "options": ["धैर्य", "भ्रम", "अंत", "असंतोष"],
        "answer": "धैर्य"
    },
    {
        "question": "Ten of Cups किससे जुड़ा है?",
        "options": ["भावनात्मक खुशी", "अचानक बदलाव", "भ्रम", "प्रतिस्पर्धा"],
        "answer": "भावनात्मक खुशी"
    }
]


# ============================================================
# HTML
# ============================================================

HTML = r"""
<!DOCTYPE html>
<html lang="hi">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{{ website_name }}</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, "Noto Sans Devanagari", sans-serif;
    background: linear-gradient(135deg, #160b2e, #32105c, #111827);
    color: white;
    min-height: 100vh;
}

header {
    padding: 25px 15px;
    text-align: center;
    background: rgba(0,0,0,0.35);
    border-bottom: 2px solid rgba(255,255,255,0.12);
}

.logo {
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 2px;
}

.subtitle {
    margin-top: 8px;
    font-size: 16px;
    color: #ddd;
}

nav {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    padding: 15px;
    background: rgba(0,0,0,0.25);
}

nav button {
    border: none;
    border-radius: 12px;
    padding: 12px 17px;
    background: #ffffff;
    color: #211033;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
}

nav button:hover {
    transform: translateY(-2px);
    background: #f4dfff;
}

.container {
    width: min(1150px, 94%);
    margin: 25px auto;
}

.page {
    display: none;
}

.page.active {
    display: block;
}

.hero {
    text-align: center;
    padding: 50px 20px;
    border-radius: 25px;
    background: rgba(255,255,255,0.08);
    box-shadow: 0 15px 50px rgba(0,0,0,0.25);
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 19px;
    color: #ddd;
}

.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
    gap: 18px;
    margin-top: 25px;
}

.card {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.18);
}

.card h3 {
    color: #ffe08a;
    font-size: 23px;
    margin-top: 0;
}

.card p {
    line-height: 1.7;
    color: #eee;
}

.category {
    margin-top: 12px;
    padding: 10px;
    border-radius: 10px;
    background: rgba(0,0,0,0.22);
}

.category b {
    display: block;
    margin-bottom: 4px;
    color: #fff;
}

.search {
    width: 100%;
    padding: 15px;
    border-radius: 12px;
    border: none;
    margin: 15px 0;
    font-size: 16px;
}

.section-title {
    text-align: center;
    font-size: 35px;
    margin-top: 20px;
}

.big-button {
    border: none;
    padding: 15px 22px;
    border-radius: 13px;
    background: #ffcc66;
    color: #24132e;
    font-weight: bold;
    cursor: pointer;
    font-size: 16px;
    margin: 8px;
}

.quiz-box {
    max-width: 850px;
    margin: 25px auto;
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.09);
}

.question {
    margin-bottom: 25px;
    padding: 20px;
    border-radius: 15px;
    background: rgba(0,0,0,0.22);
}

.question h3 {
    font-size: 20px;
}

.option {
    width: 100%;
    text-align: left;
    padding: 13px;
    margin: 7px 0;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-size: 15px;
}

.option:hover {
    background: #ddd;
}

.correct {
    background: #55d68a !important;
    color: #071d10;
    font-weight: bold;
}

.wrong {
    background: #ff7676 !important;
    color: #280707;
    font-weight: bold;
}

.feedback {
    margin-top: 10px;
    font-weight: bold;
}

.refresh {
    font-size: 18px;
}

.theme-buttons {
    text-align: center;
    margin: 25px;
}

footer {
    text-align: center;
    padding: 30px;
    color: #bbb;
}

@media(max-width:600px) {

    .logo {
        font-size: 25px;
    }

    .hero h1 {
        font-size: 34px;
    }

    .section-title {
        font-size: 28px;
    }

}

</style>
</head>


<body>

<header>

    <div class="logo">
        🔮 SARTHAK TAROT COURSE
    </div>

    <div class="subtitle">
        Tarot सीखें — 78 Cards की आसान Learning
    </div>

</header>


<nav>

    <button onclick="showPage('home')">🏠 Home</button>

    <button onclick="showPage('learning')">📚 Learning</button>

    <button onclick="showPage('major')">🌟 Major Arcana</button>

    <button onclick="showPage('minor')">🃏 Minor Arcana</button>

    <button onclick="showPage('quiz')">🧠 Quiz</button>

    <button onclick="showPage('theme')">🎨 Theme</button>

</nav>


<div class="container">


<!-- HOME -->

<section id="home" class="page active">

    <div class="hero">

        <h1>🔮 SARTHAK TAROT COURSE</h1>

        <p>
            Tarot Cards को आसान हिन्दी में सीखें।
        </p>

        <p>
            यहाँ आपको 22 Major Arcana और 56 Minor Arcana सहित सभी 78 Cards मिलेंगे।
        </p>

        <button class="big-button" onclick="showPage('learning')">
            📚 Learning शुरू करें
        </button>

        <button class="big-button" onclick="showPage('quiz')">
            🧠 Quiz शुरू करें
        </button>

    </div>

</section>


<!-- LEARNING -->

<section id="learning" class="page">

    <h2 class="section-title">
        📚 Tarot Learning
    </h2>

    <div class="hero">

        <h2>Tarot के 78 Cards</h2>

        <p>
            Tarot Deck में कुल 78 Cards होते हैं।
        </p>

        <p>
            22 Major Arcana + 56 Minor Arcana = 78 Cards
        </p>

        <button class="big-button" onclick="showPage('major')">
            22 Major Arcana
        </button>

        <button class="big-button" onclick="showPage('minor')">
            56 Minor Arcana
        </button>

    </div>

</section>


<!-- MAJOR -->

<section id="major" class="page">

    <h2 class="section-title">
        🌟 Major Arcana — 22 Cards
    </h2>

    <input
        class="search"
        id="majorSearch"
        placeholder="Card Name खोजें..."
        oninput="searchCards('majorGrid', 'majorSearch')"
    >

    <div class="card-grid" id="majorGrid">

        {% for card in major %}

        <div class="card searchable">

            <h3>{{ card.name }}</h3>

            <p>
                <b>मुख्य अर्थ:</b><br>
                {{ card.meaning }}
            </p>

            <div class="category">
                <b>पैसा</b>
                {{ card.money }}
            </div>

            <div class="category">
                <b>Education</b>
                {{ card.education }}
            </div>

            <div class="category">
                <b>Health</b>
                {{ card.health }}
            </div>

            <div class="category">
                <b>Relationship</b>
                {{ card.relationship }}
            </div>

            <div class="category">
                <b>Business</b>
                {{ card.business }}
            </div>

        </div>

        {% endfor %}

    </div>

</section>


<!-- MINOR -->

<section id="minor" class="page">

    <h2 class="section-title">
        🃏 Minor Arcana — 56 Cards
    </h2>

    <input
        class="search"
        id="minorSearch"
        placeholder="Card Name खोजें..."
        oninput="searchCards('minorGrid', 'minorSearch')"
    >

    <div class="card-grid" id="minorGrid">

        {% for card in minor %}

        <div class="card searchable">

            <h3>{{ card.name }}</h3>

            <p>
                <b>Suit:</b> {{ card.suit }}
            </p>

            <p>
                <b>मुख्य अर्थ:</b><br>
                {{ card.meaning }}
            </p>

            <div class="category">
                <b>पैसा</b>
                {{ card.money }}
            </div>

            <div class="category">
                <b>Education</b>
                {{ card.education }}
            </div>

            <div class="category">
                <b>Health</b>
                {{ card.health }}
            </div>

            <div class="category">
                <b>Relationship</b>
                {{ card.relationship }}
            </div>

            <div class="category">
                <b>Business</b>
                {{ card.business }}
            </div>

        </div>

        {% endfor %}

    </div>

</section>


<!-- QUIZ -->

<section id="quiz" class="page">

    <h2 class="section-title">
        🧠 Tarot Quiz
    </h2>

    <div style="text-align:center">

        <button class="big-button refresh" onclick="newQuiz()">
            🔄 Refresh Quiz
        </button>

        <p>
            हर बार 10 अलग-अलग प्रश्न दिखाए जाएंगे।
        </p>

    </div>

    <div id="quizContainer"></div>

    <div style="text-align:center">

        <button class="big-button" onclick="checkScore()">
            🏆 Score देखें
        </button>

    </div>

    <div id="scoreBox"></div>

</section>


<!-- THEME -->

<section id="theme" class="page">

    <h2 class="section-title">
        🎨 Theme
    </h2>

    <div class="hero">

        <h2>अपनी Theme चुनें</h2>

        <div class="theme-buttons">

            <button class="big-button"
                onclick="changeTheme('purple')">
                🟣 Purple
            </button>

            <button class="big-button"
                onclick="changeTheme('blue')">
                🔵 Blue
            </button>

            <button class="big-button"
                onclick="changeTheme('green')">
                🟢 Green
            </button>

            <button class="big-button"
                onclick="changeTheme('red')">
                🔴 Red
            </button>

        </div>

    </div>

</section>


</div>


<footer>

    © SARTHAK TAROT COURSE

</footer>


<script>


// ============================================================
// QUIZ DATA
// ============================================================

const quizBank = {{ quiz_bank | tojson }};

let currentQuiz = [];

let score = 0;

let answered = 0;


// ============================================================
// PAGE SWITCH
// ============================================================

function showPage(pageId) {

    document.querySelectorAll(".page").forEach(page => {
        page.classList.remove("active");
    });

    document.getElementById(pageId).classList.add("active");

    if (pageId === "quiz") {
        newQuiz();
    }

}


// ============================================================
// SHUFFLE
// ============================================================

function shuffle(array) {

    let copy = [...array];

    for (let i = copy.length - 1; i > 0; i--) {

        const j = Math.floor(Math.random() * (i + 1));

        [copy[i], copy[j]] = [copy[j], copy[i]];

    }

    return copy;

}


// ============================================================
// NEW QUIZ
// ============================================================

function newQuiz() {

    score = 0;

    answered = 0;

    document.getElementById("scoreBox").innerHTML = "";

    currentQuiz = shuffle(quizBank).slice(0, 10);

    const container = document.getElementById("quizContainer");

    container.innerHTML = "";

    currentQuiz.forEach((quiz, index) => {

        const questionBox = document.createElement("div");

        questionBox.className = "quiz-box";

        questionBox.innerHTML = `
            <div class="question">

                <h3>
                    ${index + 1}. ${quiz.question}
                </h3>

                <div class="options"></div>

                <div class="feedback"></div>

            </div>
        `;

        const optionsBox =
            questionBox.querySelector(".options");

        shuffle(quiz.options).forEach(option => {

            const button = document.createElement("button");

            button.className = "option";

            button.textContent = option;

            button.onclick = function() {

                answerQuestion(
                    button,
                    quiz.answer,
                    optionsBox,
                    questionBox
                );

            };

            optionsBox.appendChild(button);

        });

        container.appendChild(questionBox);

    });

}


// ============================================================
// ANSWER
// ============================================================

function answerQuestion(
    clickedButton,
    correctAnswer,
    optionsBox,
    questionBox
) {

    if (questionBox.dataset.answered === "true") {
        return;
    }

    questionBox.dataset.answered = "true";

    answered++;

    const buttons =
        optionsBox.querySelectorAll(".option");

    buttons.forEach(button => {

        button.disabled = true;

        if (button.textContent === correctAnswer) {

            button.classList.add("correct");

        }

    });


    const feedback =
        questionBox.querySelector(".feedback");


    if (clickedButton.textContent === correctAnswer) {

        clickedButton.classList.add("correct");

        feedback.innerHTML =
            "✅ सही उत्तर!";

        score++;

    } else {

        clickedButton.classList.add("wrong");

        feedback.innerHTML =
            "❌ गलत उत्तर! सही उत्तर: <b>"
            + correctAnswer
            + "</b>";

    }

}


// ============================================================
// SCORE
// ============================================================

function checkScore() {

    const scoreBox =
        document.getElementById("scoreBox");

    let message = "";

    if (answered < 10) {

        message =
            "पहले सभी 10 प्रश्नों के उत्तर दें।";

    } else if (score === 10) {

        message =
            "🔥 शानदार! आपने 10/10 किया!";

    } else if (score >= 8) {

        message =
            "🌟 बहुत बढ़िया! आपकी तैयारी अच्छी है।";

    } else if (score >= 5) {

        message =
            "👍 अच्छा प्रयास! थोड़ा और अभ्यास करें।";

    } else {

        message =
            "📚 Cards को दोबारा पढ़ें और फिर Quiz दें।";

    }


    scoreBox.innerHTML = `
        <div class="hero">

            <h2>
                आपका Score: ${score}/10
            </h2>

            <p>${message}</p>

        </div>
    `;

}


// ============================================================
// SEARCH
// ============================================================

function searchCards(gridId, searchId) {

    const search =
        document.getElementById(searchId)
        .value
        .toLowerCase();

    const cards =
        document
        .getElementById(gridId)
        .querySelectorAll(".searchable");

    cards.forEach(card => {

        const text =
            card.textContent.toLowerCase();

        if (text.includes(search)) {

            card.style.display = "";

        } else {

            card.style.display = "none";

        }

    });

}


// ============================================================
// THEMES
// ============================================================

function changeTheme(theme) {

    if (theme === "purple") {

        document.body.style.background =
            "linear-gradient(135deg,#160b2e,#32105c,#111827)";

    }

    if (theme === "blue") {

        document.body.style.background =
            "linear-gradient(135deg,#071e3d,#0b4f6c,#111827)";

    }

    if (theme === "green") {

        document.body.style.background =
            "linear-gradient(135deg,#062b1c,#0b5d3b,#111827)";

    }

    if (theme === "red") {

        document.body.style.background =
            "linear-gradient(135deg,#3b0710,#7f1d1d,#111827)";

    }

    localStorage.setItem("tarotTheme", theme);

}


// ============================================================
// LOAD SAVED THEME
// ============================================================

const savedTheme =
    localStorage.getItem("tarotTheme");

if (savedTheme) {

    changeTheme(savedTheme);

}


// ============================================================
// IMPORTANT:
// BROWSER REFRESH = NEW QUIZ
// ============================================================

newQuiz();

</script>

</body>

</html>
"""


# ============================================================
# ROUTE
# ============================================================

@app.route("/")
def home():

    return render_template_string(
        HTML,
        website_name=WEBSITE_NAME,
        major=major_arcana,
        minor=minor_arcana,
        quiz_bank=quiz_bank
    )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )