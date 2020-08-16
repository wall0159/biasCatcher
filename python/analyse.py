import spacy as sp
import re

class Analyse():
    def __init__(self):
        self.nlp = sp.load("en_core_web_lg")
        # removed_words = self.nlp.vocab.prune_vectors(800000)
        # print(removed_words)
        words1000 = "as I his that he was for on are with they be at one have this from by hot word but what some is it you or had the of to and a in we can out other were which do their time if will how said an each tell does set three want air well also play small end put home read hand port large spell add even land here must big high such follow act why ask men change went light kind off need house picture try us again animal point mother world near build self earth father any new work part take get place made live where after back little only round man year came show every good me give our under name very through just form sentence great think say help low line differ turn cause much mean before move right boy old too same she all there when up use your way about many then them write would like so these her long make thing see him two has look more day could go come did number sound no most people my over know water than call first who may down side been now find head stand own page should country found answer school grow study still learn plant cover food sun four between state keep eye never last let thought city tree cross farm hard start might story saw far sea draw left late run don't while press close night real life few north book carry took science eat room friend began idea fish mountain stop once base hear horse cut sure watch color face wood main open seem together next white children begin got walk example ease paper group always music those both mark often letter until mile river car feet care second enough plain girl usual young ready above ever red list though feel talk bird soon body dog family direct pose leave song measure door product black short numeral class wind question happen complete ship area half rock order fire south problem piece told knew pass since top whole king street inch multiply nothing course stay wheel full force blue object decide surface deep moon island foot system busy test record boat common gold possible plane stead dry wonder laugh thousand ago ran check game shape equate hot miss brought heat snow tire bring yes distant fill east paint language among unit power town fine certain fly fall lead cry dark machine note wait plan figure star box noun field rest correct able pound done beauty drive stood contain front teach week final gave green oh quick develop ocean warm free minute strong special mind behind clear tail produce fact space heard best hour better true during hundred five remember step early hold west ground interest reach fast verb sing listen six table travel less morning ten simple several vowel toward war lay against pattern slow center love person money serve appear road map rain rule govern pull cold notice voice energy hunt probable bed brother egg ride cell believe perhaps pick sudden count square reason length represent art subject region size vary settle speak weight general ice matter circle pair include divide syllable felt grand ball yet wave drop heart am present heavy dance engine position arm wide sail material fraction forest sit race window store summer train sleep prove lone leg exercise wall catch mount wish sky board joy winter sat written wild instrument kept glass grass cow job edge sign visit past soft fun bright gas weather month million bear finish happy hope flower clothe strange gone trade melody trip office receive row mouth exact symbol die least trouble shout except wrote seed tone join suggest clean break lady yard rise bad blow oil blood touch grew cent mix team wire cost lost brown wear garden equal sent choose fell fit flow fair bank collect save control decimal ear else quite broke case middle kill son lake moment scale loud spring observe child straight consonant nation dictionary milk speed method organ pay age section dress cloud surprise quiet stone tiny climb cool design poor lot experiment bottom key iron single stick flat twenty skin smile crease hole jump baby eight village meet root buy raise solve metal whether push seven paragraph third shall held hair describe cook floor either result burn hill safe cat century consider type law bit coast copy phrase silent tall sand soil roll temperature finger industry value fight lie beat excite natural view sense capital won't chair danger fruit rich thick soldier process operate practice separate difficult doctor please protect noon crop modern element hit student corner party supply whose locate ring character insect caught period indicate radio spoke atom human history effect electric expect bone rail imagine provide agree thus gentle woman captain guess necessary sharp wing create neighbor wash bat rather crowd corn compare poem string bell depend meat rub tube famous dollar stream fear sight thin triangle planet hurry chief colony clock mine tie enter major fresh search send yellow gun allow print dead spot desert suit current lift rose arrive master track parent shore division sheet substance favor connect post spend chord fat glad original share station dad bread charge proper bar offer segment slave duck instant market degree populate chick dear enemy reply drink occur support speech nature range steam motion path liquid log meant quotient teeth shell neck oxygen sugar death skill women season solution magnet silver thank branch match suffix especially fig afraid huge sister steel discuss forward similar guide experience score apple bought led pitch coat mass card band rope slip win dream evening condition feed tool total basic smell valley nor double seat continue block chart hat sell success company subtract event particular deal swim term opposite wife shoe shoulder spread arrange camp invent cotton born determine quart nine truck noise level chance gather shop stretch throw shine property column molecule select wrong gray repeat require broad prepare salt nose plural anger claim continent"
        self.commonWords = self.nlp(words1000)

        self.ignoreList = list()

        # self.problemWords = 'quigibo' #'she her hers mother wife girl daughter sister father he him his husband boy son brother'
        # self.problemWordsNLP = self.nlp(self.problemWords)
        # self.problemWordsList = self.problemWords.split(" ")
        # words1000 = words1000.split(" ")
        # for remWord in self.problemWordsNLP:
        #     for tok in self.commonWords:
        #         # print(remWord.text, tok.text, remWord.similarity(tok)) #, token.is_oov
        #         if remWord.similarity(tok) > 0.85:
        #              self.ignoreList.append(tok.text)
        #              if tok.text in words1000:
        #                  words1000.remove(tok.text)
        self.ignoreList = words1000.split(" ")
        self.problemWords = 'Bossy Abrasive ball_buster Aggressive Shrill Bolshy Intense Stroppy Forward Mannish Gossipy Dramatic Drama Queen Catty Bitchy Nag Cold Shrew Humourless Mani_hater Banshee Fishwife Lippy Ditzy Feminazi feminist Bridezilla Diva Blonde Feisty Supermum Fierce Spirited Slut Trollop Frigid Easy Tease Loose Man_eater Cougar Prude Slutty Curvy Mumsy Cheap Frumpy Mousey Plus_size Clotheshorse Brunette Ladylike Bubbly Vivacious Flirty Sassy Chatty Demure Modest Emotional Hysterical Hormonal Menstrual housewife housewives pre_menstrual Flaky Moody Over_sensitive Clucky Maternal Neurotic Irrational Mumpreneur Spinster Barren Housewife Houseproud mom Mistress Princess Tomboy Girly Jail_bait Heart_breaker bossy Bitchfest Catfight Caring Compassionate Hard_working Conscientious Dependable Diligent Dedicated Tactful Interpersonal Warm Helpful Cunt Whore Bitch Slut Prostitute Aggressive High_strung highly_strung Temperamental Queen Cold Nag Nagging Shrill Opinionated Uppity Hot Sexy MILF Ugly Mannish Dyke Lesbian Varicose Veins Cancles Wringled Moody PMSing Hairstyle Cute Muffintop muffin_top girls feisty ambitious airhead bolshy bombshell breathless flustered emotional cold clingy crazy exotic intense bridezilla bubbly peppy curvy voluptuous ditsy frigid chill perky prude sweet miss hourglass pear frumpy hormonal hysterical illogical irrational pushy sassy whinging housewife matron princess siren spinster whore vixen goddess plain nosy obnoxious naïve moody manipulative diva enchantress she_devil lass lassie blunt brainless clueless clingy gold-digging witchy wicked trampy trashy superficial minger housewife wife'.lower()
        self.problemWordsNLP = self.nlp(self.problemWords)
        self.problemWordsList = self.problemWords.split(" ")

        self.racistWords = 'black squaw dark nigger redskin indian redskins piccaninny'.lower()
        self.racistWordsNLP = self.nlp(self.racistWords)
        self.racistWordsList = self.racistWords.split(" ")

        # for word in  self.ignoreList:
        #     words1000 = words1000.replace(" " + word + " ", " ")

        # dictionary for word substitutions
        self.wordSubs = {'guys': 'everybody',
                    'ladies': 'everybody',
                    'gentlemen': 'everybody',
                    'mankind': 'humankind',
                    'congressmen': 'members of congress',
                    'boy': 'child',
                    'boys': 'children',
                    'girl': 'child',
                    'girls': 'children',
                    'sister': 'sibling, friend, soulmate',
                    'brother': 'sibling, friend, soulmate',
                    'girlfriend': 'partner, spouse',
                    'boyfriend': 'partner, spouse',
                    'waiter': 'server',
                    'waitress': 'server',
                    'fireman': 'firefighter',
                    'policeman': 'police officer',
                    'landlord': 'owner',
                    'man power': 'workforce',
                    'maiden name': 'fmaily name',
                    'guys': 'team, friends, colleagues',
                    }

        # self.commonWords = words1000.split(" ")
        # print("Stop words")
        # print(self.commonWords)
        # print("Problem Words")
        # print(self.problemWordsList)

        self.reduceProbWords = list()

        for checkword in self.problemWordsNLP:
            for aword in self.problemWordsNLP:
                if checkword.similarity(aword) > 0.5:
                    self.reduceProbWords.append(aword.text)

        self.reduceProbWordsNLP = self.nlp(" ".join(list(set(self.reduceProbWords))))
        print("reduced problem words")
        print(self.reduceProbWordsNLP)
        print(self.ignoreList)

    def processText(self, text):

        ucaseWords = list()
        racistWords = list()

        words = self.nlp(text.lower())
        for aword in words:
            if aword.text in self.ignoreList:
                continue
            if len(aword.text) <3:
                continue
            for probWord in self.reduceProbWordsNLP:
                sim = aword.similarity(probWord)
                print(aword,probWord,sim)
                if sim > 0.75 and (aword.text not in self.wordSubs.keys()):
                    ucaseWords.append(aword.text)
            for probWord in self.racistWordsNLP:
                sim = aword.similarity(probWord)
                print(aword,probWord,sim)
                if sim > 0.75 and (aword.text not in ucaseWords) and (aword.text not in self.wordSubs.keys()):
                    racistWords.append(aword.text)
        print(ucaseWords)
        print(racistWords)
        # remove racist words that are a sub-word of a sexist word
        for word in racistWords:
            if any([w for w in ucaseWords if word in w]):
                racistWords.remove(word)
        # racistWords = [word in racistWords where word not in [probW in ucaseWords]]
        newtext = text.lower()
        newtext = newtext.replace(","," ")
        newtext = newtext.replace("."," ")
        newtext = newtext.replace("!"," ")
        newtext = newtext.replace("-"," ")
        newtext = newtext.replace(";"," ")
        newtext = newtext.replace(":"," ")
        newtext = newtext.replace(" ","  ")
        newtext = " " + newtext+ " "
        for uword in self.wordSubs.keys():
            newtext = newtext.replace(" " + uword + " ",'<div class="tooltip-wrap">'+" " + uword.upper()+'<div class="tooltip-content">instead of "'+ uword + '", try: ' + self.wordSubs[uword]+ '.<br></div></div>')
        for uword in ucaseWords:
            newtext = newtext.replace(" " + uword + " ",'<div class="tooltip-wrap"><p><a href="https://www.urbandictionary.com/define.php?term='+" " + uword.upper()+'">'+uword.upper()+'</a></p><div class="tooltip-content"><p>'+uword+ ' can have sexist connotations.<br><a href="https://en.wiktionary.org/wiki/'+uword+'"> Read its definition and history</a></p></div></div>')
        for uword in racistWords:
            newtext = newtext.replace(" " + uword + " ",'<div class="tooltip-wrap"><p><a href="https://www.urbandictionary.com/define.php?term='+" " + uword.upper()+'">'+uword.upper()+'</a></p><div class="tooltip-content"><p>'+uword+ ' can have racist connotations.<br><a href="https://en.wiktionary.org/wiki/'+uword+'"> Read its definition and history</a></p></div></div>')
        newtext = newtext.replace("  "," ")
        return '\
<!DOCTYPE html>\
<html lang="en" dir="ltr">\
  <head>\
    <meta charset="utf-8">\
    <title>Bias Catcher</title><link rel="stylesheet" href="/static/css/template.css">\
  </head>\
  <body> <header> <div class="container"> <h1 class="logo">Bias Catcher</h1> <strong><nav> <ul class="menu"> <li><a href="/">Home</a></li> </ul> </nav></strong> </div> </header> \
    <h1> Enter some text to detect common biases </h1>\
    <p> So much of what we write contains unconscious gender and other biases. This tool will help you to detect them. Please enter some text below to see an assessment. </p>\
        <form method="POST">\
    <input name="text" value="' + text + '">\
    <input type="submit">\
</form>\
' + newtext + '\
  </body>\
</html>'
