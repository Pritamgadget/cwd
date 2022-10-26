import discord
import os
from discord.ext import commands
from googletrans import Translator
import giphy_client
from giphy_client.rest import ApiException
import random
import re
import asyncio
import datetime
import time
import json
import requests

list1 = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","abusive","acceptable","accessible","accidental","accurate","acid","acidic","acoustic","acrid","actually","ad hoc","adamant","adaptable","addicted","adhesive","adjoining","adorable","adventurous","afraid","aggressive","agonizing","agreeable","ahead","ajar","alcoholic","alert","alike","alive","alleged","alluring","aloof","amazing","ambiguous","ambitious","amuck","amused","amusing","ancient","angry","animated","annoyed","annoying","anxious","apathetic","aquatic","aromatic","arrogant","ashamed","aspiring","assorted","astonishing","attractive","auspicious","automatic","available","average","awake","aware","awesome","awful","axiomatic","bad","barbarous","bashful","bawdy","beautiful","befitting","belligerent","beneficial","bent","berserk","best","better","bewildered","big","billowy","bite-sized","bitter","bizarre","black","black-and-white","bloody","blue","blue-eyed","blushing","boiling","boorish","bored","boring","bouncy","boundless","brainy","brash","brave","brawny","breakable","breezy","brief","bright","bright","broad","broken","brown","bumpy","burly","bustling","busy","cagey","calculating","callous","calm","capable","capricious","careful","careless","caring","cautious","ceaseless","certain","changeable","charming","cheap","cheerful","chemical","chief","childlike","chilly","chivalrous","chubby","chunky","clammy","classy","clean","clear","clever","cloistered","cloudy","closed","clumsy","cluttered","coherent","cold","colorful","colossal","combative","comfortable","common","complete","complex","concerned","condemned","confused","conscious","cooing","cool","cooperative","coordinated","courageous","cowardly","crabby","craven","crazy","creepy","crooked","crowded","cruel","cuddly","cultured","cumbersome","curious","curly","curved","curvy","cut","cute","cute","cynical","daffy","daily","damaged","damaging","damp","dangerous","dapper","dark","dashing","dazzling","dead","deadpan","deafening","dear","debonair","decisive","decorous","deep","deeply","defeated","defective","defiant","delicate","delicious","delightful","demonic","delirious","dependent","depressed","deranged","descriptive","deserted","detailed","determined","devilish","didactic","different","difficult","diligent","direful","dirty","disagreeable","disastrous","discreet","disgusted","disgusting","disillusioned","dispensable","distinct","disturbed","divergent","dizzy","domineering","doubtful","drab","draconian","dramatic","dreary","drunk","dry","dull","dusty","dusty","dynamic","dysfunctional","eager","early","earsplitting","earthy","easy","eatable","economic","educated","efficacious","efficient","eight","elastic","elated","elderly","electric","elegant","elfin","elite","embarrassed","eminent","empty","enchanted","enchanting","encouraging","endurable","energetic","enormous","entertaining","enthusiastic","envious","equable","equal","erect","erratic","ethereal","evanescent","evasive","even","excellent","excited","exciting","exclusive","exotic","expensive","extra-large","extra-small","exuberant","exultant","fabulous","faded","faint","fair","faithful","fallacious","false","familiar","famous","fanatical","fancy","fantastic","far","far-flung","fascinated","fast","fat","faulty","fearful","fearless","feeble","feigned","female","fertile","festive","few","fierce","filthy","fine","finicky","first","five","fixed","flagrant","flaky","flashy","flat","flawless","flimsy","flippant","flowery","fluffy","fluttering","foamy","foolish","foregoing","forgetful","fortunate","four","frail","fragile","frantic","free","freezing","frequent","fresh","fretful","friendly","frightened","frightening","full","fumbling","functional","funny","furry","furtive","future","futuristic","fuzzy","gabby","gainful","gamy","gaping","garrulous","gaudy","general","gentle","giant","giddy","gifted","gigantic","glamorous","gleaming","glib","glistening","glorious","glossy","godly","good","goofy","gorgeous","graceful","grandiose","grateful","gratis","gray","greasy","great","greedy","green","grey","grieving","groovy","grotesque","grouchy","grubby","gruesome","grumpy","guarded","guiltless","gullible","gusty","guttural","habitual","half","hallowed","halting","handsome","handsomely","handy","hanging","hapless","happy","hard","hard-to-find","harmonious","harsh","hateful","heady","healthy","heartbreaking","heavenly","heavy","hellish","helpful","helpless","hesitant","hideous","high","highfalutin","high-pitched","hilarious","hissing","historical","holistic","hollow","homeless","homely","honorable","horrible","hospitable","hot","huge","hulking","humdrum","humorous","hungry","hurried","hurt","hushed","husky","hypnotic","hysterical","icky","icy","idiotic","ignorant","ill","illegal","ill-fated","ill-informed","illustrious","imaginary","immense","imminent","impartial","imperfect","impolite","important","imported","impossible","incandescent","incompetent","inconclusive","industrious","incredible","inexpensive","infamous","innate","innocent","inquisitive","insidious","instinctive","intelligent","interesting","internal","invincible","irate","irritating","itchy","jaded","jagged","jazzy","jealous","jittery","jobless","jolly","joyous","judicious","juicy","jumbled","jumpy","juvenile","kaput","keen","kind","kindhearted","kindly","knotty","knowing","knowledgeable","known","labored","lackadaisical","lacking","lame","lamentable","languid","large","last","late","laughable","lavish","lazy","lean","learned","left","legal","lethal","level","lewd","light","like","likeable","limping","literate","little","lively","lively","living","lonely","long","longing","long-term","loose","lopsided","loud","loutish","lovely","loving","low","lowly","lucky","ludicrous","lumpy","lush","luxuriant","lying","lyrical","macabre","macho","maddening","madly","magenta","magical","magnificent","majestic","makeshift","male","malicious","mammoth","maniacal","many","marked","massive","married","marvelous","material","materialistic","mature","mean","measly","meaty","medical","meek","mellow","melodic","melted","merciful","mere","messy","mighty","military","milky","mindless","miniature","minor","miscreant","misty","mixed","moaning","modern","moldy","momentous","motionless","mountainous","muddled","mundane","murky","mushy","mute","mysterious","naive","nappy","narrow","nasty","natural","naughty","nauseating","near","neat","nebulous","necessary","needless","needy","neighborly","nervous","new","next","nice","nifty","nimble","nine","nippy","noiseless","noisy","nonchalant","nondescript","nonstop","normal","nostalgic","nosy","noxious","null","numberless","numerous","nutritious","nutty","oafish","obedient","obeisant","obese","obnoxious","obscene","obsequious","observant","obsolete","obtainable","oceanic","odd","offbeat","old","old-fashioned","omniscient","one","onerous","open","opposite","optimal","orange","ordinary","organic","ossified","outgoing","outrageous","outstanding","oval","overconfident","overjoyed","overrated","overt","overwrought","painful","painstaking","pale","paltry","panicky","panoramic","parallel","parched","parsimonious","past","pastoral","pathetic","peaceful","penitent","perfect","periodic","permissible","perpetual","petite","petite","phobic","physical","picayune","pink","piquant","placid","plain","plant","plastic","plausible","pleasant","plucky","pointless","poised","polite","political","poor","possessive","possible","powerful","precious","premium","present","pretty","previous","pricey","prickly","private","probable","productive","profuse","protective","proud","psychedelic","psychotic","public","puffy","pumped","puny","purple","purring","pushy","puzzled","puzzling","quack","quaint","quarrelsome","questionable","quick","quickest","quiet","quirky","quixotic","quizzical","rabid","racial","ragged","rainy","rambunctious","rampant","rapid","rare","raspy","ratty","ready","real","rebel","receptive","recondite","red","redundant","reflective","regular","relieved","remarkable","reminiscent","repulsive","resolute","resonant","responsible","rhetorical","rich","right","righteous","rightful","rigid","ripe","ritzy","roasted","robust","romantic","roomy","rotten","rough","round","royal","ruddy","rude","rural","rustic","ruthless","sable","sad","safe","salty","same","sassy","satisfying","savory","scandalous","scarce","scared","scary","scattered","scientific","scintillating","scrawny","screeching","second","second-hand","secret","secretive","sedate","seemly","selective","selfish","separate","serious","shaggy","shaky","shallow","sharp","shiny","shivering","shocking","short","shrill","shut","shy","sick","silent","silent","silky","silly","simple","simplistic","sincere","six","skillful","skinny","sleepy","slim","slimy","slippery","sloppy","slow","small","smart","smelly","smiling","smoggy","smooth","sneaky","snobbish","snotty","soft","soggy","solid","somber","sophisticated","sordid","sore","sore","sour","sparkling","special","spectacular","spicy","spiffy","spiky","spiritual","spiteful","splendid","spooky","spotless","spotted","spotty","spurious","squalid","square","squealing","squeamish","staking","stale","standing","statuesque","steadfast","steady","steep","stereotyped","sticky","stiff","stimulating","stingy","stormy","straight","strange","striped","strong","stupendous","stupid","sturdy","subdued","subsequent","substantial","successful","succinct","sudden","sulky","super","superb","superficial","supreme","swanky","sweet","sweltering","swift","symptomatic","synonymous","taboo","tacit","tacky","talented","tall","tame","tan","tangible","tangy","tart","tasteful","tasteless","tasty","tawdry","tearful","tedious","teeny","teeny-tiny","telling","temporary","ten","tender","tense","tense","tenuous","terrible","terrific","tested","testy","thankful","therapeutic","thick","thin","thinkable","third","thirsty","thirsty","thoughtful","thoughtless","threatening","three","thundering","tidy","tight","tightfisted","tiny","tired","tiresome","toothsome","torpid","tough","towering","tranquil","trashy","tremendous","tricky","trite","troubled","truculent","true","truthful","two","typical","ubiquitous","ugliest","ugly","ultra","unable","unaccountable","unadvised","unarmed","unbecoming","unbiased","uncovered","understood","undesirable","unequal","unequaled","uneven","unhealthy","uninterested","unique","unkempt","unknown","unnatural","unruly","unsightly","unsuitable","untidy","unused","unusual","unwieldy","unwritten","upbeat","uppity","upset","uptight","used","useful","useless","utopian","utter","uttermost","vacuous","vagabond","vague","valuable","various","vast","vengeful","venomous","verdant","versed","victorious","vigorous","violent","violet","vivacious","voiceless","volatile","voracious","vulgar","wacky","waggish","waiting","wakeful","wandering","wanting","warlike","warm","wary","wasteful","watery","weak","wealthy","weary","well-groomed","well-made","well-off","well-to-do","wet","whimsical","whispering","white","whole","wholesale","wicked","wide","wide-eyed","wiggly","wild","willing","windy","wiry","wise","wistful","witty","woebegone","womanly","wonderful","wooden","woozy","workable","worried","worthless","wrathful","wretched","wrong","wry","yellow","yielding","young","youthful","yummy","zany","zealous","zesty","zippy","zonked","account","achiever","acoustics","act","action","activity","actor","addition","adjustment","advertisement","advice","aftermath","afternoon","afterthought","agreement","air","airplane","airport","alarm","amount","amusement","anger","angle","animal","ants","apparatus","apparel","appliance","approval","arch","argument","arithmetic","arm","army","art","attack","attraction","aunt","authority","babies","baby","back","badge","bag","bait","balance","ball","base","baseball","basin","basket","basketball","bat","bath","battle","bead","bear","bed","bedroom","beds","bee","beef","beginner","behavior","belief","believe","bell","bells","berry","bike","bikes","bird","birds","birth","birthday","bit","bite","blade","blood","blow","board","boat","bomb","bone","book","books","boot","border","bottle","boundary","box","boy","brake","branch","brass","breath","brick","bridge","brother","bubble","bucket","building","bulb","burst","bushes","business","butter","button","cabbage","cable","cactus","cake","cakes","calculator","calendar","camera","camp","can","cannon","canvas","cap","caption","car","card","care","carpenter","carriage","cars","cart","cast","cat","cats","cattle","cause","cave","celery","cellar","cemetery","cent","chalk","chance","change","channel","cheese","cherries","cherry","chess","chicken","chickens","children","chin","church","circle","clam","class","cloth","clover","club","coach","coal","coast","coat","cobweb","coil","collar","color","committee","company","comparison","competition","condition","connection","control","cook","copper","corn","cough","country","cover","cow","cows","crack","cracker","crate","crayon","cream","creator","creature","credit","crib","crime","crook","crow","crowd","crown","cub","cup","current","curtain","curve","cushion","dad","daughter","day","death","debt","decision","deer","degree","design","desire","desk","destruction","detail","development","digestion","dime","dinner","dinosaurs","direction","dirt","discovery","discussion","distance","distribution","division","dock","doctor","dog","dogs","doll","dolls","donkey","door","downtown","drain","drawer","dress","drink","driving","drop","duck","ducks","dust","ear","earth","earthquake","edge","education","effect","egg","eggnog","eggs","elbow","end","engine","error","event","example","exchange","existence","expansion","experience","expert","eye","eyes","face","fact","fairies","fall","fang","farm","fear","feeling","field","finger","finger","fire","fireman","fish","flag","flame","flavor","flesh","flight","flock","floor","flower","flowers","fly","fog","fold","food","foot","force","fork","form","fowl","frame","friction","friend","friends","frog","frogs","front","fruit","fuel","furniture","gate","geese","ghost","giants","giraffe","girl","girls","glass","glove","gold","government","governor","grade","grain","grandfather","grandmother","grape","grass","grip","ground","group","growth","guide","guitar","gun","hair","haircut","hall","hammer","hand","hands","harbor","harmony","hat","hate","head","health","heat","hill","history","hobbies","hole","holiday","home","honey","hook","hope","horn","horse","horses","hose","hospital","hot","hour","house","houses","humor","hydrant","ice","icicle","idea","impulse","income","increase","industry","ink","insect","instrument","insurance","interest","invention","iron","island","jail","jam","jar","jeans","jelly","jellyfish","jewel","join","judge","juice","jump","kettle","key","kick","kiss","kittens","kitty","knee","knife","knot","knowledge","laborer","lace","ladybug","lake","lamp","land","language","laugh","leather","leg","legs","letter","letters","lettuce","level","library","limit","line","linen","lip","liquid","loaf","lock","locket","look","loss","love","low","lumber","lunch","lunchroom","machine","magic","maid","mailbox","man","marble","mark","market","mask","mass","match","meal","measure","meat","meeting","memory","men","metal","mice","middle","milk","mind","mine","minister","mint","minute","mist","mitten","mom","money","monkey","month","moon","morning","mother","motion","mountain","mouth","move","muscle","name","nation","neck","need","needle","nerve","nest","night","noise","north","nose","note","notebook","number","nut","oatmeal","observation","ocean","offer","office","oil","orange","oranges","order","oven","page","pail","pan","pancake","paper","parcel","part","partner","party","passenger","payment","peace","pear","pen","pencil","person","pest","pet","pets","pickle","picture","pie","pies","pig","pigs","pin","pipe","pizzas","place","plane","planes","plant","plantation","plants","plastic","plate","play","playground","pleasure","plot","plough","pocket","point","poison","pollution","popcorn","porter","position","pot","potato","powder","power","price","produce","profit","property","prose","protest","pull","pump","punishment","purpose","push","quarter","quartz","queen","question","quicksand","quiet","quill","quilt","quince","quiver","rabbit","rabbits","rail","railway","rain","rainstorm","rake","range","rat","rate","ray","reaction","reading","reason","receipt","recess","record","regret","relation","religion","representative","request","respect","rest","reward","rhythm","rice","riddle","rifle","ring","rings","river","road","robin","rock","rod","roll","roof","room","root","rose","route","rub","rule","run","sack","sail","salt","sand","scale","scarecrow","scarf","scene","scent","school","science","scissors","screw","sea","seashore","seat","secretary","seed","selection","self","sense","servant","shade","shake","shame","shape","sheep","sheet","shelf","ship","shirt","shock","shoe","shoes","shop","show","side","sidewalk","sign","silk","silver","sink","sister","sisters","size","skate","skin","skirt","sky","slave","sleep","sleet","slip","slope","smash","smell","smile","smoke","snail","snails","snake","snakes","sneeze","snow","soap","society","sock","soda","sofa","son","song","songs","sort","sound","soup","space","spade","spark","spiders","sponge","spoon","spot","spring","spy","square","squirrel","stage","stamp","star","start","statement","station","steam","steel","stem","step","stew","stick","sticks","stitch","stocking","stomach","stone","stop","store","story","stove","stranger","straw","stream","street","stretch","string","structure","substance","sugar","suggestion","suit","summer","sun","support","surprise","sweater","swim","swing","system","table","tail","talk","tank","taste","tax","teaching","team","teeth","temper","tendency","tent","territory","test","texture","theory","thing","things","thought","thread","thrill","throat","throne","thumb","thunder","ticket","tiger","time","tin","title","toad","toe","toes","tomatoes","tongue","tooth","toothbrush","toothpaste","top","touch","town","toy","toys","trade","trail","train","trains","tramp","transport","tray","treatment","tree","trees","trick","trip","trouble","trousers","truck","trucks","tub","turkey","turn","twig","twist","umbrella","uncle","underwear","unit","use","vacation","value","van","vase","vegetable","veil","vein","verse","vessel","vest","view","visitor","voice","volcano","volleyball","voyage","walk","wall","war","wash","waste","watch","water","wave","waves","wax","way","wealth","weather","week","weight","wheel","whip","whistle","wilderness","wind","window","wine","wing","winter","wire","wish","woman","women","wood","wool","word","work","worm","wound","wren","wrench","wrist","writer","writing","yak","yam","yard","yarn","year","yoke","zebra","zephyr","zinc","zipper","zoo","accept","add","admire","admit","advise","afford","agree","alert","allow","amuse","analyse","announce","annoy","answer","apologise","appear","applaud","appreciate","approve","argue","arrange","arrest","arrive","ask","attach","attack","attempt","attend","attract","avoid","back","bake","balance","ban","bang","bare","bat","bathe","battle","beam","beg","behave","belong","bleach","bless","blind","blink","blot","blush","boast","boil","bolt","bomb","book","bore","borrow","bounce","bow","box","brake","branch","breathe","bruise","brush","bubble","bump","burn","bury","buzz","calculate","call","camp","care","carry","carve","cause","challenge","change","charge","chase","cheat","check","cheer","chew","choke","chop","claim","clap","clean","clear","clip","close","coach","coil","collect","colour","comb","command","communicate","compare","compete","complain","complete","concentrate","concern","confess","confuse","connect","consider","consist","contain","continue","copy","correct","cough","count","cover","crack","crash","crawl","cross","crush","cry","cure","curl","curve","cycle","dam","damage","dance","dare","decay","deceive","decide","decorate","delay","delight","deliver","depend","describe","desert","deserve","destroy","detect","develop","disagree","disappear","disapprove","disarm","discover","dislike","divide","double","doubt","drag","drain","dream","dress","drip","drop","drown","drum","dry","dust","earn","educate","embarrass","employ","empty","encourage","end","enjoy","enter","entertain","escape","examine","excite","excuse","exercise","exist","expand","expect","explain","explode","extend","face","fade","fail","fancy","fasten","fax","fear","fence","fetch","file","fill","film","fire","fit","fix","flap","flash","float","flood","flow","flower","fold","follow","fool","force","form","found","frame","frighten","fry","gather","gaze","glow","glue","grab","grate","grease","greet","grin","grip","groan","guarantee","guard","guess","guide","hammer","hand","handle","hang","happen","harass","harm","hate","haunt","head","heal","heap","heat","help","hook","hop","hope","hover","hug","hum","hunt","hurry","identify","ignore","imagine","impress","improve","include","increase","influence","inform","inject","injure","instruct","intend","interest","interfere","interrupt","introduce","invent","invite","irritate","itch","jail","jam","jog","join","joke","judge","juggle","jump","kick","kill","kiss","kneel","knit","knock","knot","label","land","last","laugh","launch","learn","level","license","lick","lie","lighten","like","list","listen","live","load","lock","long","look","love","man","manage","march","mark","marry","match","mate","matter","measure","meddle","melt","memorise","mend","mess up","milk","mine","miss","mix","moan","moor","mourn","move","muddle","mug","multiply","murder","nail","name","need","nest","nod","note","notice","number","obey","object","observe","obtain","occur","offend","offer","open","order","overflow","owe","own","pack","paddle","paint","park","part","pass","paste","pat","pause","peck","pedal","peel","peep","perform","permit","phone","pick","pinch","pine","place","plan","plant","play","please","plug","point","poke","polish","pop","possess","post","pour","practise","pray","preach","precede","prefer","prepare","present","preserve","press","pretend","prevent","prick","print","produce","program","promise","protect","provide","pull","pump","punch","puncture","punish","push","question","queue","race","radiate","rain","raise","reach","realise","receive","recognise","record","reduce","reflect","refuse","regret","reign","reject","rejoice","relax","release","rely","remain","remember","remind","remove","repair","repeat","replace","reply","report","reproduce","request","rescue","retire","return","rhyme","rinse","risk","rob","rock","roll","rot","rub","ruin","rule","rush","sack","sail","satisfy","save","saw","scare","scatter","scold","scorch","scrape","scratch","scream","screw","scribble","scrub","seal","search","separate","serve","settle","shade","share","shave","shelter","shiver","shock","shop","shrug","sigh","sign","signal","sin","sip","ski","skip","slap","slip","slow","smash","smell","smile","smoke","snatch","sneeze","sniff","snore","snow","soak","soothe","sound","spare","spark","sparkle","spell","spill","spoil","spot","spray","sprout","squash","squeak","squeal","squeeze","stain","stamp","stare","start","stay","steer","step","stir","stitch","stop","store","strap","strengthen","stretch","strip","stroke","stuff","subtract","succeed","suck","suffer","suggest","suit","supply","support","suppose","surprise","surround","suspect","suspend","switch","talk","tame","tap","taste","tease","telephone","tempt","terrify","test","thank","thaw","tick","tickle","tie","time","tip","tire","touch","tour","tow","trace","trade","train","transport","trap","travel","treat","tremble","trick","trip","trot","trouble","trust","try","tug","tumble","turn","twist","type","undress","unfasten","unite","unlock","unpack","untidy","use","vanish","visit","wail","wait","walk","wander","want","warm","warn","wash","waste","watch","water","wave","weigh","welcome","whine","whip","whirl","whisper","whistle","wink","wipe","wish","wobble","wonder","work","worry","wrap","wreck","wrestle","wriggle","x-ray","yawn","yell","zip","zoom"]


intents = discord.Intents.all()
intents.members = True
client=commands.Bot(command_prefix=['pls ', 'Pls ', 'p', 'P', 'p ', 'P ', 'Pls'], intents = intents)
client.remove_command("help")


deleted_messages = {}
word_game = False


winlist2 = [
  'Yes',
  'No', 'Maybe', 'Yes Daddy', 'Yes Mommy', 'Possibly', "We'll never know", 'You Wish', "Even I can't answer that", 'Never' ]


stabby = [
  'https://i.imgur.com/kRuLOci.gif',
  'https://i.imgur.com/lVC7TRf.gif',
  'https://i.imgur.com/Pz9RKoE.gif',
  'https://i.imgur.com/C5pQjXV.gif',
  'https://i.imgur.com/YZwaY6R.gif',
  'https://i.imgur.com/e14wXXz.gif',
  'https://i.imgur.com/3EK5GoA.gif',
  'https://i.imgur.com/Q7bCnWD.gif',
  'https://i.imgur.com/VKvweoX.gif',
  'https://i.imgur.com/5cEn3Ac.gif'
]

winlist = [
  'Obviously',
  'Its',
  'Duh',
  'Wot idiot wont choose',
  'Well since you asked, I choose'
]

skinningimg = [
  'https://i.imgur.com/MRSyQCb.gif',
  'https://i.imgur.com/1IdsgrN.gif',
  'https://i.imgur.com/CTcQk5Z.gif',
  'https://media.tenor.com/images/286b710f95472348d8ab72722e10254f/tenor.gif',
  'https://media.tenor.com/images/cd95cad8b8576b8f7b74e7d412370d57/tenor.gif',
  'https://media.tenor.com/images/a9cfd5bda83284363a146713fd78b07d/tenor.gif',
  'https://media.tenor.com/images/ab7b184c4bd43df45e1ffc2ffd5be2bd/tenor.gif'
]

whipping = [
  'https://media.tenor.com/images/5b698ada9da22fdfe61368b8ec42333a/tenor.gif',
  'https://media.tenor.com/images/90c3fa16a281c2c61c75d5a06d4bfdde/tenor.gif',
  'https://media.tenor.com/images/a981e678b8ffcb5dc46d217d5f4b1e9a/tenor.gif',
  'https://media.tenor.com/images/208a9d8fd11cbfb13f8ec65957e35078/tenor.gif',
  'https://media.tenor.com/images/59af8444f20a8232ccf9f03846cf486f/tenor.gif',
  'https://media.tenor.com/images/a997c2ab11856a0a2dc88caf6fa99759/tenor.gif',
  'https://media.tenor.com/images/c3450e30a6b1e62040f9c0b37120fb5a/tenor.gif',
  'https://media.tenor.com/images/d47dc1efbc509174fdd4a748fb8f67fc/tenor.gif'
]

spanking = [
  'https://media.tenor.com/images/b54d4d4397f735f9ab75df9a22db269f/tenor.gif',
  'https://media.tenor.com/images/b01abd857e1065f038d191e891cb9f82/tenor.gif',
  'https://media.tenor.com/images/594d794a96d3bb76c00d788c611ec6fa/tenor.gif',
  'https://media.tenor.com/images/8e7fbc4a68e81264e18980cf4f474e64/tenor.gif',
  'https://media.tenor.com/images/5e053219629f067801802c9f5b807220/tenor.gif',
  'https://media.tenor.com/images/605c5c945479bd8fcad2448420b285d9/tenor.gif',
  'https://media.tenor.com/images/5de8e26acdc4cd0b711908911d9dab81/tenor.gif',
  'https://media.tenor.com/images/99bfa3d20f4491ed75f1080a0408f282/tenor.gif',
  'https://media.tenor.com/images/28353a2d8bc02fb809cbad7d4f2894a9/tenor.gif'
]

shooting = [
  'xyz',
]

killed = [
  'abc',
  
]

@client.event
async def on_message(message):
  channel = client.get_channel(904434928303882251)
  embed=discord.Embed(colour=discord.Colour.gold())
  embed.set_author(name=f"User Info ~ {message.author}")
  embed.add_field(name="Message: ", value=message.content, inline=False)
  if message.author != client.user and message.channel == message.author.dm_channel:
        await channel.send(embed=embed)
        
  await client.process_commands(message)
  
@client.command()
async def token(ctx, member: discord.Member):
    list = ["Blued", "Yellowed"]
    user = ctx.author
    servant = range(1, 60)
    pick = random.choice(servant)
    tokens = random.choice(list)
    print(pick, tokens)
    print(member)
    if user is member :
        await ctx.send(f"Can't token yourself Pleb")

    else:
        await ctx.send (f"{user.mention} {tokens} {member.mention} and defeated {pick} servants")

@client.command()
async def advice(ctx):
    url = "https://api.adviceslip.com/advice"
    r = requests.get(url)
    print(r)
    t = json.dumps(r.json())
    l = json.loads(json.dumps(r.json()))
    print(l)
    lstr = l
    lstr = str(lstr)
    advice = lstr.split(":")[-1]
    advice = advice.replace("}", "")
    embed = discord.Embed(color = 0x2ecc71, title = "Random Advice", description = str(advice))
    await ctx.send(content = None, embed = embed)
    
@client.command()
async def wyr(ctx):


    url = "https://would-you-rather.p.rapidapi.com/wyr/random"

    headers = {
	"X-RapidAPI-Key": "0bf015d3c0mshc2fc0c272d6334ap1b5170jsn7e953dbcd498",
	"X-RapidAPI-Host": "would-you-rather.p.rapidapi.com"
     }

    response = requests.request("GET", url, headers=headers)
    question = response.text
    question = question.split(":")[-1]
    question = question.replace("}", "")
    question = question.replace("]", "")
    embed = discord.Embed(color = 0x2ecc71, title = "Would You Rather", description = str(question))
    await ctx.send(content = None, embed = embed)
    embed = discord.Embed(color = 0x2ecc71, title = "Would You Rather", description = str(question))
    await ctx.send(content = None, embed = embed)

    

@client.command()
async def wordplay(ctx):
  global word_game
  if word_game == False:
    word_game = True
    while (word_game==True):
      choose_a_word = random.choice(list1)
      print(choose_a_word)
      lst = [x for x in choose_a_word]
      if len(choose_a_word) <= 3 :
                poppingup = ''.join(random.sample(lst, 1))
                replacing = ''.join(lst)
                hang_word = replacing.replace(poppingup, "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{hang_word}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) < 6 :
                poppingup = (random.sample(lst, 2))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#", 1)
                items = items.replace(poppingup[1], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) < 7 :
                poppingup = (random.sample(lst, 3))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#", 1)
                items = items.replace(poppingup[1], "#", 1)
                items = items.replace(poppingup[2], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) < 10 :
                poppingup = (random.sample(lst, 4))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#", 1)
                items = items.replace(poppingup[1], "#", 1)
                items = items.replace(poppingup[2], "#", 1)
                items = items.replace(poppingup[3], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      elif len(choose_a_word) > 10 :
                poppingup = (random.sample(lst, 5))
                print(poppingup)
                items = choose_a_word.replace(poppingup[0], "#")
                items = items.replace(poppingup[1], "#", 1)
                items = items.replace(poppingup[2], "#", 1)
                items = items.replace(poppingup[3], "#", 1)
                items = items.replace(poppingup[4], "#", 1)
                emb = discord.Embed(color = 0x2ecc71)
                emb.set_author(name = f'The Word Play!')
                emb.add_field(name = 'Word is: ', value = f'{items}', inline = False)
                await ctx.send(embed = emb)
      try:
                msg = await client.wait_for('message', check = lambda x: f"{choose_a_word}" in x.content.lower(), timeout = 10)
                await msg.channel.send(f"{msg.author.mention}, That's correct, The word was **__{choose_a_word.upper()}__**")
      except asyncio.TimeoutError:
            try:
                url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + choose_a_word + "?fields=" + fields
                r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
                t = json.dumps(r.json())
                l = json.loads(json.dumps(r.json()))
                f = l["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
                embed = discord.Embed(color = 0x2ecc71, title = "HINT", description = str(f))
                await ctx.channel.send(content = None, embed = embed)
            except KeyError:
                await ctx.send("**No Hint found in Oxford Dictionary**")
            try:
                 msg = await client.wait_for('message', check = lambda x: f"{choose_a_word}" in x.content.lower(), timeout = 20)
                 await msg.channel.send(f"{msg.author.mention}, That's correct, The word was **__{choose_a_word.upper()}__**")
            except asyncio.TimeoutError:
                    await ctx.send(f"You're out of time, The word was **__{choose_a_word.upper()}__**")

      if word_game == False:
        pass
      else:
        await ctx.send("Next Question in 10 seconds")
        await asyncio.sleep(10)
  else:
    word_game = False
    await ctx.send("**Word game has stopped**")

        

@client.command()
async def calc(ctx, arg):
    y = eval(arg)
    await ctx.send(y)
  
@client.command()
async def rate(ctx, *args):
  list = ["Libby is ugly", "Ugly ass Libby", "Libby at peak of ugliness"]
  cont = random.choice(list)
  await ctx.send(cont)
  
  
@client.command(aliases=['emo', 'e'])
async def emoji(ctx, msgID): 

    msg = await ctx.fetch_message(msgID)
    x = msg.content
    temp = re.findall(r'\d+', x)
    res = list(map(int, temp))
    
    x = f'https://cdn.discordapp.com/emojis/{res}.gif'
    y1 = x.replace("[", "")
    y2 = y1.replace("]", "")
    r = requests.head(f'{y2}')
    rep = r.status_code

    if rep != 200 :
        png = y2.replace(".gif", ".png")
        r2 = requests.head(f'{png}')
        rep2 = r2.status_code
        if rep2 == 200:

            emb = discord.Embed(title='Emoji')
            emb.set_image(url = f'{png}')
            await ctx.send (embed = emb)
        else: 
            jpeg = png.replace(".png", "jpg")
            emb = discord.Embed(title='Emoji')
            emb.set_image(url = f'{jpeg}')
            await ctx.send (embed = emb)  
    else:
         emb = discord.Embed(title='Emoji')
         emb.set_image(url = f'{y2}')
         await ctx.send (embed = emb)

@client.command()
async def steal(ctx,*, member: discord.Member):
    list1 = f"{ctx.author.mention} tried to steal {member.mention}'s luck but failed"
    list2 = f"{ctx.author.mention} stole {member.mention}'s Good luck"
    list22 = f"{ctx.author.mention} stole {member.mention}'s Bad luck"
    list3 = f"{ctx.author.mention} stole {member.mention}'s luck, Not sure Good or Bad"
    lists = [list1, list2, list3, list22]
    choose = random.choice(lists)
    if member is ctx.author :
        await ctx.send("No need to steal your own luck noob")
    elif ctx.author is 705116051024773213 :
        await ctx.send(f"Can't steal Creator's Luck")
    else:
      await ctx.send(choose)
  
@client.command(aliases=['rem', 'r', 'remind'])
async def reminder(ctx,*, args):
 user = ctx.author
 message = "in".join(args.split("in")[:-1])
 args = args.split(" in ")[-1]
 if "h" in args and "m" in args: 
    main = args.split( )
    print(main)
    x = len(main)
    if x is 2:
        hour = main[0]
        hour_int = hour[:-1]
        minutes = main[1]
        minutes_int = minutes[:-1]
        x1 = int(hour_int)
        x2 = int(minutes_int)
        hour_in_seconds = x1*60*60
        minutes_in_seconds = x2*60
        total_time = hour_in_seconds + minutes_in_seconds
        await ctx.send(f"{user.mention} You'll be reminded for {message} in {args}")
        await asyncio.sleep(total_time)
        await user.send(message)

 elif "h" in args:
    hr = args[:-1]
    hr = int(hr)
    hr_in_seconds = hr*60*60
    await ctx.send(f"{user.mention} You'll be reminded for {message} in {args}")
    await asyncio.sleep(hr_in_seconds)
    await user.send(message)

 elif "m" in args:
    min = args[:-1]
    min = int(min)
    min_in_seconds = min*60
    await ctx.send(f"{user.mention} You'll be reminded for {message} in {args}")
    await asyncio.sleep(min_in_seconds)
    await user.send(message)

 else:
    await ctx.send("Use Correct Format: Pls rem (message) in (0)h (0)m")

  
@client.command()
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)
    
        
@client.command(aliases=['st'])    
@commands.has_any_role('Vice Leader', 'Elder', 'Emperor Lord', 'Tao Lord')
async def secttrade(ctx, time):
    time_in_minutes = int(time)
    time_in_sec = time_in_minutes*60
    print(time_in_sec)

    await ctx.send("Sect Trade feed has started")
    await asyncio.sleep(time_in_sec)

    try:
        while True:
            await asyncio.sleep(10800) 
            await ctx.send (f"<@&939054218763972669> : Stocks will refresh in 5 mins. " )
    except KeyboardInterrupt:
        print('\n')


@client.command(aliases=['Dm', 'DM'])
@commands.has_any_role('Vice Leader', 'Elder', 'Emperor Lord', 'Tao Lord')
async def dm(ctx, *, message_and_mentions = None):
    message = None
    mentions = None
    message_and_mentions = message_and_mentions.split(" ")
    message_starting_index = None
    #for separating mentions and messages
    for text_index in range(len(message_and_mentions)):
        if not re.match("\<\@\!?\d*\>|\<\@\&?\d*\>", message_and_mentions[text_index]):
            message_starting_index = text_index
            break
    if message_starting_index is None:
        message_starting_index = len(message_and_mentions)
        message = "This message is sent by " + ctx.author.name
    else:
        message = " ".join(message_and_mentions[message_starting_index:])
    #if there are mentions in the command
    if message_starting_index != 0:
        mentions = []
        for mention in message_and_mentions[:message_starting_index]:
            string_mentions = re.findall("\<\@\!?\d*\>|\<\@\&?\d*\>", mention)
            if string_mentions:
                for mention in string_mentions:
                    print(string_mentions)
                    id = ""; i = 0
                    while i < len(mention):
                        if mention[i].isdigit():
                            id += mention[i]
                        i += 1
                    mentions.append(int(id))
                    await ctx.send("Message Sent!")
        users = []
        for id in mentions:
            user = ctx.message.guild.get_member(id)
            role = ctx.message.guild.get_role(id)
            if user:
                if user not in users:
                    users.append(user)
            elif role:
                for member in ctx.guild.members:
                    if role in member.roles:
                        if member not in users:
                            users.append(member)
        for user in users:
            try:
                await user.send(message)
            except:
                pass
                await ctx.send("Message wasn't sent to a User")
              
    
app_id = 'f1b477f2'
app_key = '2fd4ee4cbe6f6751b878c82559aee353'
language = 'en-us'
fields = 'definitions'


@client.command(aliases=['definee'])
async def define(ctx, word):
    words = word
    print(words)
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language + "/" + words.lower() + "?fields=" + fields
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
    t = json.dumps(r.json())
    l = json.loads(json.dumps(r.json()))
    f = l["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
    embed = discord.Embed(colour = discord.Colour.from_rgb(107, 230, 255), title = 'Oxford Dictionary - ' + word, description = str(f))
    await ctx.send(content = None, embed = embed)
    
@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def stab(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(stabby)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} stabbed {member.mention} ')
  await ctx.send(embed = embed)
  
@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def spank(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(spanking)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} spanked {member.mention} ')
  await ctx.send(embed = embed)
  
@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def whip(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(whipping)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} whipped {member.mention} ')
  await ctx.send(embed = embed)

@client.command()
@commands.has_any_role('Queen of Hearts', 'Pantheon Members')
async def skin(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  
  embed = discord.Embed(color = discord.Colour.red())

  random_link = random.choice(skinningimg)

  embed.set_image(url = random_link)
  await ctx.send (f'{author_name} is skinning {member.mention} ')
  await ctx.send(embed = embed)
  
 



@client.command()
async def say(ctx, *, text):
    if ctx.message.author.id == 705116051024773213:
        message = ctx.message
        await message.delete()

        await ctx.send(f"{text}")
    elif text == "Only Tam is allowed to use it noob.":
        await ctx.send(f"{ctx.message.author.mention} stfu")
    else:
        await ctx.send('Only Tam is allowed to use it noob.')


  
#giveaway
@client.event
async def on_ready():
    # Prints a message when the bot is online and functioning
    await client.change_presence(status=discord.Status.online, activity = discord.Game(name=f'g!helpme for a list of commands! 🥳 🎉 Currently in {len(client.guilds)} servers! 🎉'))
    print('Ready to giveaway!')


@client.command(aliases = ['gw', 'Gw', 'GW', 'gW'])
async def giveaway(ctx):
    # Giveaway command requires the user to have a "Giveaway Host" role to function properly

    # Stores the questions that the bot will ask the user to answer in the channel that the command was made
    # Stores the answers for those questions in a different list
    giveaway_questions = ['Which channel giveaway will be hosted in?', 'Whats the prize?', 'Duration of Giveaway (in seconds)?',]
    giveaway_answers = []

    # Checking to be sure the author is the one who answered and in which channel
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    # Askes the questions from the giveaway_questions list 1 by 1
    # Times out if the host doesn't answer within 30 seconds
    for question in giveaway_questions:
        await ctx.send(question)
        try:
            message = await client.wait_for('message', timeout= 30.0, check= check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time.  Please try again and be sure to send your answer within 30 seconds of the question.')
            return
        else:
            giveaway_answers.append(message.content)

    # Grabbing the channel id from the giveaway_questions list and formatting is properly
    # Displays an exception message if the host fails to mention the channel correctly
    try:
        c_id = int(giveaway_answers[0][2:-1])
    except:
        await ctx.send(f'You failed to mention the channel correctly.  Please do it like this: {ctx.channel.mention}')
        return
    
    # Storing the variables needed to run the rest of the commands
    channel = client.get_channel(c_id)
    prize = str(giveaway_answers[1])
    time = int(giveaway_answers[2])

    # Sends a message to let the host know that the giveaway was started properly
    await ctx.send(f'The giveaway for {prize} will begin shortly.\nPlease direct your attention to {channel.mention}, this giveaway will end in {time} seconds.')

    # Giveaway embed message
    give = discord.Embed(color = 0x2ecc71)
    give.set_author(name = f'GIVEAWAY TIME!', icon_url = 'https://i.imgur.com/VaX0pfM.png')
    give.add_field(name= f'{ctx.author.name} Hosted Giveaway for: {prize}!', value = f'React with 🎉 to enter!\n Ends in {round(time/60, 2)} minutes!', inline = False)
    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = time)
    give.set_footer(text = f'Giveaway ends at {end} UTC!')
    my_message = await channel.send(embed = give)
    
    # Reacts to the message
    await my_message.add_reaction("🎉")
    await asyncio.sleep(time)

    new_message = await channel.fetch_message(my_message.id)

    # Picks a winner
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)

    # Announces the winner
    winning_announcement = discord.Embed(color = 0xff2424)
    winning_announcement.set_author(name = f'THE GIVEAWAY HAS ENDED!', icon_url= 'https://i.imgur.com/DDric14.png')
    winning_announcement.add_field(name = f'🎉 Prize: {prize}', value = f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}', inline = False)
    winning_announcement.set_footer(text = 'Thanks for entering!')
    await channel.send(embed = winning_announcement)



@client.command()
@commands.has_any_role('Vice Leader')
async def reroll(ctx, channel: discord.TextChannel, id_ : int):
    # Reroll command requires the user to have a "Giveaway Host" role to function properly
    try:
        new_message = await channel.fetch_message(id_)
    except:
        await ctx.send("Incorrect id.")
        return
    
    # Picks a new winner
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    winner = random.choice(users)

    # Announces the new winner to the server
    reroll_announcement = discord.Embed(color = 0xff2424)
    reroll_announcement.set_author(name = f'The giveaway was re-rolled by the host!', icon_url = 'https://i.imgur.com/DDric14.png')
    reroll_announcement.add_field(name = f'🥳 New Winner:', value = f'{winner.mention}', inline = False)
    await channel.send(embed = reroll_announcement)
    
@client.command(aliases=['choose'])
async def Choose(ctx, *args):
  winner = random.choice(args)
  winlistx = random.choice(winlist)
  await ctx.send((f'{winlistx} ' '{}  '.format(winner)))
  
@client.command(aliases=['Pick'])
async def pick(ctx, num, *, args):
    list = args.split()
    num = int(num)
    picking = random.sample(list, num)
    listToStr = ' '.join(map(str, picking))
    await ctx.send(listToStr)
  
@client.command()
@commands.has_any_role('Vice Leader')
async def ping(ctx,*, member: discord.Member):
  author_name = ctx.message.author.name
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)
  await ctx.send (f'{author_name} pinged {member.mention}')
  time.sleep(2)



@client.command()
async def help(ctx):
    em = discord.Embed (
        title = 'Help : Page 1/3',
        description = 'Use Pls help <command> for more info on a command',
        colour = discord.Colour.red())
    em.add_field(name = "Snipe : [snipe / s]", value = "Snipe last deleted message")
    em.add_field(name = "Snipe Edit : [snipeedit/se]", value = "Snipe the last edited message")
    em.add_field(name = "DM : [dm]", value = "Send Direct message to somone/everyone via bot")
    em.add_field(name = "Poll : [poll]", value = "Make a simpe 'Yes' or 'No' Poll")
    em.add_field(name = "Choose : [choose] ", value = "Choose one item from a list")
    em.add_field(name = "Pick : [pick] ", value = "Pick Multiple Items from list")
    
    em2 = discord.Embed (
        title = 'Page 2/3',
        description = 'Use Pls help <command> for more info on a command',
        colour = discord.Colour.red())
    em2.add_field(name = "Translate : [translate / ts]", value = "Translate any text into English")
    em2.add_field(name = "Giveaway : [Giveaway, gw] ", value = "Do a Giveaway")
    em2.add_field(name = "8ball : [8ball / 8b] ", value = "Ask your questions")
    em2.add_field(name = "Oxford Dictionary : [define] ", value = "Use Oxford dictionary to fetch meaning of a word")
    em2.add_field(name = "Urban Dictionary [urban] ", value = "Use urban dictionary to fetch meaning")
    em2.add_field(name = "User Info : [info] ", value = "Fetch info a User")
    

    em3 = discord.Embed (
        title = 'Page 3/3',
        description = 'Use Pls help <command> for more info on a command',
        colour = discord.Colour.red()
    )
    em3.add_field(name = "Avatar : [avatar] ", value = "Fetch avatar of a User")
    em3.add_field(name = "Say : [say] ", value = "Make the bot say what you want to say")
    em3.add_field(name = "Reminder0 : [reminder/rem/r] ", value = "Set a reminder")
    em3.add_field(name = "Emoji : [emoji] ", value = "Fetch emoji from any message using message ID")
    em3.add_field(name = "Token : [token] ", value = "Token plebs including their assistance")
    em3.add_field(name = "Steal : [steal] ", value = "Steal Other's Luck")

    em4 = discord.Embed (
        title = 'Page 4/4',
        description = 'Description',
        colour = discord.Colour.red()
    ) 
    em4.add_field(name = "Action Commands ", value = f"hug, kick, punch, stab, lick \n bye, xyz")


    pages = [em, em2, em3, em4]

    message = await ctx.send(embed = em)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author

    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < 2:
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '⏭':
            i = 2
            await message.edit(embed = pages[i])
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 30.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()


@client.command(aliases=['8b', '8ball'])
async def ball(ctx, *args):
  winlistx = random.choice(winlist2)
  await ctx.send(winlistx)


@client.command(aliases=['ts'])
async def translate(ctx, *, inptext = None):
    translator = Translator()
    translated_text = translator.translate(inptext)
    embed = discord.Embed(title="Translate", description = translated_text.text)
    embed.set_footer(text=f"Source Langauge : '{translated_text.src}'")
    await ctx.send(embed = embed)     

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('with OwO'))

@client.command(aliases=['Poll'])
async def poll(ctx, *, question=None):
    if question == None:
        await ctx.send("Please write a poll!")
 
    icon_url = ctx.author.avatar_url 
 
    pollEmbed = discord.Embed(title = "Poll", description = f"{question}")
 
    pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
 
    pollEmbed.timestamp = ctx.message.created_at 
 
    await ctx.message.delete()
 
    poll_msg = await ctx.send(embed = pollEmbed)
 
    await poll_msg.add_reaction("✅")
    await poll_msg.add_reaction("❌")


@client.command(aliases=['Pollop'])
async def pollop(ctx, *, question=None):
    if question == None:
        await ctx.send("Please write a poll!")
 
    icon_url = ctx.author.avatar_url 
 
    pollEmbed = discord.Embed(title = "Poll", description = f"{question}")
 
    pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
 
    pollEmbed.timestamp = ctx.message.created_at 
 
    await ctx.message.delete()
 
    poll_msg = await ctx.send(embed = pollEmbed)
 
    await poll_msg.add_reaction("1️⃣")
    await poll_msg.add_reaction("2️⃣")
    await poll_msg.add_reaction("3️⃣")
    await poll_msg.add_reaction("4️⃣")
    
@client.command(aliases=['Hug'])
async def hug(ctx,*, member: discord.Member, q="hug"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} hugged {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
        
        
@client.command(aliases=['Kick'])
async def kick(ctx,*, member: discord.Member, q="kicked"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='pg')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} kicked {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Lick'])
async def lick(ctx,*, member: discord.Member, q="lick"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} licked {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Slap'])
async def slap(ctx,*, member: discord.Member, q="slapped"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} slapped {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Punch'])
async def punch(ctx,*, member: discord.Member, q="punched"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} punched {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Stare'])
async def stare(ctx,*, member: discord.Member, q="staring"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} is staring at {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Kiss'])
async def kiss(ctx,*, member: discord.Member, q="kiss"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} kissed {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Highfive'])
async def highfive(ctx,*, member: discord.Member, q="highfive"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} gave a highfive to {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

@client.command(aliases=['Bye'])
async def bye(ctx,*, member: discord.Member, q="bye"):

    api_key="0XFxHlEGR4hUO7RxdHslVuqqmWf5kcRm"
    api_instance = giphy_client.DefaultApi()

    author_name = ctx.message.author.name

    try: 
    # Search Endpoint
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=50, rating='r')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.send (f'{author_name} left poor {member.mention}')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    
@client.event
async def on_message_delete(message):
    global deleted_messages
    deleted_messages[message.channel.id] = {'author': message.author.name+'#'+message.author.discriminator, 'content': message.content, 'avatar_url': message.author.avatar_url}

@client.command(aliases=['s'])
async def snipe(ctx):
    global deleted_messages
    if ctx.message.channel.id in deleted_messages:
        embed=discord.Embed(title="",description=f"{deleted_messages[ctx.message.channel.id]['content']}")    
        embed.set_author(name="Sniper", icon_url=deleted_messages[ctx.message.channel.id]['avatar_url'])
        embed.set_footer(text=f"Message deleted by {deleted_messages[ctx.message.channel.id]['author']}")
    else:
        embed=discord.Embed(title="Sniper",description="Nothing to snipe!")
    await ctx.send(embed = embed)

old = {}
new = {}
author = {}

@client.event
async def on_message_edit(before, after):
    global old
    global new
    global author 
    old[before.channel.id] = before.content
    new[after.channel.id] = after.content
    author[after.channel.id] = after.author.name

@client.command(aliases=['se'])
async def snipeedit(ctx):
    if ctx.message.channel.id in new:
        embed=discord.Embed(title="",description=f"Before: {old[ctx.message.channel.id]}\nAfter: {new[ctx.message.channel.id]}")    
        #embed.set_author(name="Sniper", icon_url={after.author.avatar_url})
        embed.set_footer(text=f"Message edited by {author[ctx.message.channel.id]}")       
    else:

        embed=discord.Embed(title="Sniper",description="No Edit to snipe!")
    await ctx.send(embed=embed)
   
@client.command(aliases=['ud'])
async def urban(ctx, *msg):

        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        # Send request to the Urban Dictionary API and grab info
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="No results found!", colour=0xFF0000)
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        # Add results to the embed
        embed = discord.Embed(title="Word", description=word, colour=embed.colour)
        embed.add_field(name="Top definition:", value=response['list'][0]['definition'])
        embed.add_field(name="Examples:", value=response['list'][0]['example'])
        await ctx.send(embed=embed)

@client.command(aliases=['user'])
async def info(ctx, user: discord.Member):

    embed = discord.Embed(title="User profile: " + user.name, colour=user.colour)
    embed.add_field(name="Name:", value=user.name)
    embed.add_field(name="ID:", value=user.id)
    embed.add_field(name="Status:", value=user.status)
    embed.add_field(name="Highest role:", value=user.top_role)
    embed.add_field(name="Joined:", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    

print("Bot is Online")
client.run(os.getenv('TOKEN'))

