#encoding=utf-8
import jieba
jieba.set_dictionary('dict.txt.big')
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sentence = """遠離塵囂.享受大自然.。
第一次造訪.此趟行程主要目的是環島.希望可以概覽蘭嶼全貌.包租車輛半天.民宿主人鄭小姐兼導遊開著車帶領環島.沿途天然美景令人讚嘆:鱷魚岩.玉女岩.雙獅岩.軍艦岩......各種巧妙造型.亮麗姿色.都一 一拍照留戀.鄭小姐是土生土長達悟族人.途經六大部落.瞭若指掌.並介紹文化.飲食習慣.原來飛魚在地吃法是煮著吃.天然健康.真是收穫豐富.因第二天上午就離開.還有其他好行程--看日出.大天池.夜間生態....就留待下次了.
台灣僅存尚未被開發的美麗島嶼。
因必須從台灣搭船約兩個多小時，才能到達的蘭嶼，是一般人比較不會特地選擇去的地方。但相對的，它的美麗，讓去的人一輩子難忘，加上當地達悟族的特色，更加深了他迷人的色彩。
靈魂得到救贖的地方。
有別於本島的商業化及現代化，蘭嶼是我到各地旅遊最感受到原始在地的地方，依舊騎著機車環島，環繞蘭嶼，經過各村部落，感受到的不外乎原住民的文化，雖然也慢慢受到本島居民的現代化進駐，但在環島的末段，在某座小學旁，感到當地民眾的純樸，讓我頓時感到心靈上的救贖，似乎為這個在大都市生活已久的我，得到另一種不同的感受
蘭嶼。
蘭嶼 位於台灣.台東外海偏遠小島島上交通以船跟飛機為主 但物資只有船運 飛機每小時一班 船就要3天一班船島上交通只有向民宿租借機車來蘭嶼 建議夏天至秋天 此兩季節為旺季.也是蘭嶼飛魚季的開始(包含大船下海)來蘭嶼不是以玩為主 而是來放鬆 欣賞海景 看看蘭嶼人的文化當地的涼亭 是許多遊客要注意的地方 是禁止穿鞋上去的 而要把鞋子脫掉才能在涼亭上休息(因為涼亭在蘭嶼是屬於休息的地方)蘭嶼最好以三天兩夜第一天浮淺加逛附近的景點第二天一大早可以去蘭嶼的東清部落 欣賞日出 順在在那吃早餐.然後環島一圈 欣賞蘭嶼的海景跟個個景點在晚上時 6.7點時 可以去無餓不座的餐廳吃個晚餐由於蘭嶼物資不方便 所以在地的飲食都會比較貴 所以別介意至於機場附近有一家麵攤 叫機場路路的麵攤 價位還不算貴 有去蘭嶼的可以去吃吃蘭嶼環島一圈 慢慢騎 可要2.3個小時 所以基本要兩天的時間早上去 隔天的下午回台東 這才不會太趕時間還有交通的費用 飛機跟船的價位 只差3.4百 但是時間差很多 就要好好斟酌了
飛魚 Q島 丁字褲。
蘭嶼是個美麗的地方，它的美麗源自於海洋資源與黝黑的蘭嶼人，但已經沒落的一段時間，沒有昔日的純樸與自然感。總之，對於我的記憶來說，想停留在以前的時候，偶爾去看看也不錯。
遠離都市，放空沉澱的好去處。
我沒有去過海島，我想這海島就從台灣的蘭嶼開始。當我搭上蘭嶼海上交通，帶著忐忑的心情，不知道是否真的是一個原始的荒島，且太枯燥。但我們上船後就不久出現海豚伴隨我們的船隻，陪我們一起同行，我想:這是一個充滿驚喜的旅程。當我踏上蘭嶼的陸地，海水的清澈是我在台灣看不的港口。一下船，港口就有好幾位小朋友無憂的在跳港，反覆的爬上爬下，我想這童年，是最無憂無慮的。先租了摩特車看看這個讓我驚豔的島嶼。蘭嶼的居民大約四千多人，那裏的羊跟人差不多樣多，但騎車別撞到羊，因為你必須陪錢，賠了錢又無法把羊帶走的。到蘭嶼和當地居民保持最重要的溝通放式:不催促，不殺價，你如果願意開口跟他們聊一聊，他們會很樂意把歡樂帶給你。到了夜晚，每個村提供的餐點不一樣，你們可以自己去品嚐。晚上月光皎潔時，找個無光害得地方你會發現不時地出現流星。早上的艷陽高照，你考可以下水去浮淺，很幸運的我們，又看到了海龜。下午黃昏時找個涼亭，吹著海風看看夕陽小睡一下。真的很棒的旅程。
前所未有的生活體驗。
去蘭嶼，盡量排個四到五天的行程吧。你可以先在頭兩天走馬看花似的做完所有事，像是：夜遊、浮淺、溯溪…等。然後用剩下的一到兩天，睡到自然醒；選幾個喜歡的地點，好好坐著。看看海，發個呆，或許在一間海邊的小店裡看個書，還是跟山羊一起對看都好。絕對能夠治癒你被各種爛事給糟蹋過後的心神狀態。住宿地點，我個人推薦住在紅頭或者漁人部落，生活機能相對方便。如果真的很想看日出，那就早點起床騎車去吧（但夜晚的路請盡量騎慢一點）。最後要注意的是，蘭嶼常有突然的大雨，一定要有防水對策。
2013的飛魚季。
這是一個藍天白雲加上翠綠草地跟山坡的漂亮地方!但是，它真的很遠!!這是我第二次蘭嶼旅行，第一次飛魚季造訪，蘭嶼真是太好拍照的地方!!不管是人文(拍殺飛魚、傳統服飾的達悟族人、地下屋之前，要徵求對方的同意!因為我們去旅遊，而他們是生活!!)自然景觀、或是自組攝影團外拍麻豆都是上上之選。除了來回暈船的經驗之外應該沒有甚麼好抱怨的啦!!
一個淨土但需要我們的幫助。
再訪蘭嶼，一定要做的活動就是浮淺呀！！一樣的龍門港，一樣絢爛的珊瑚，但有總珊瑚顏色變少的感覺，雖然還是美翻天，但是經過那麼灘頭或是村莊，只有一種感覺，蘭嶼的美麗需要我們大家的守護，別讓垃圾的破窗效應愈發擴大，請一起營造美好乾淨的蘭嶼吧
傳統與現代夾縫的蘭嶼。
懷著一份既興奮又忐忑的心情到達開元港_蘭嶼在港邊摩托車集中區領了車後先將物品送到蘭恩基金會,再沿東80公路(唯一環島公路)騎到民宿.雖說是公路,但猶如寬敞的產業道路,沿路會看到一片又一片的水芋田(水耕)及旱芋田(土耕)外,不時也會遇見逛大街的家豚和山羊群.因此,不要太在意路上的小黑石及自然養分(羊豬糞).沒有太多的新建物,卻有一間又一間的新建民宿.藍天,白雲,高聳綿延的青山,清澈見底的海水,浮潛,騎累了路旁的發呆亭稍歇一會,吹吹海風也是不錯的享受.騎在島上唯一橫貫公路,隨著公路向上延伸,由高處往下看,蘭嶼的美景一覽無遺. 夜探潮間帶角鴞(蘭嶼獨有的小型貓頭鷹)時,記得抬頭觀賞一望無際的星空,找一找北斗七星.將自己歸零,才能感受到蘭嶼的自然.
與出國旅行是相同頻率,回到本島仍有無限幸福感!!! :)。
去了一次蘭嶼,就戀棧那邊了! 人仍在台灣玩,但覺得跟出國旅行的心情完全吻合,回到本島仍有無限幸福感! :) 美麗山海與羊群相襯,按下相機快門的那剎間,又是一張明信片。最喜歡的部落是東清,因為那邊是我每天說早安及晚安的地方,期待每日太陽與月亮的交替輪班,感受美麗日出與月昇的感動。下雨後,淺藍、靛藍、深藍三種顏色漸層鋪陳在八代灣上,頓時覺得自己像是在國外海邊上,不過畢竟自己也是位於太平洋其中一個島嶼的小角落。當地達悟族非常熱情,會主動和觀光客互動。Life sucks without true love在這裡不存在,一個樂於助人的人之島-蘭嶼。
愜意而美好。
自在、舒暢、悠閒、放鬆，來一趟蘭嶼，會讓一切忙碌歸零，調整好自己重新出發。蘭嶼是我每每會向朋友推薦的旅遊景點，體驗一下台灣東南角的自然與純真，美麗的景色，就算無事待在發呆亭也是一種奢華。蘭嶼在我腦海裡的記憶，是當我們騎著小機車延著海邊騎乘邊吹著風，正覺得自己已經完完全全融入這美景時，看到一位金髮外藉女旅客，戴著耳機聽著音樂，閉上眼、拎著鞋，敞開雙臂赤腳走在濱海路，當海風飄起她的淡色髮絲時，我不禁想她那時肯定是整個島上最享受、最幸福的人了吧！蘭嶼有太多的美麗、也會帶給你接受不完的驚喜。尤其晚上遊玩時，要記得注意那些站在峭壁上成群睡覺的羊咩咩喔...
發呆也可以很幸福:)。
蘭嶼的海與天空都好藍，在這裡最好的行程就是 沒有行程 ，我們最喜歡待在發呆亭，甚麼事也不做，靜靜躺著或坐著，看著藍藍的海，任海風輕輕吹拂就覺得很幸福。我們曾分別在這住過3晚與4晚，若假可以多請幾天，我覺得待上一個星期也不會覺得多。在一次返回後壁湖的船上，聽到兩個歐巴桑在聊天，意思大約是 蘭嶼也沒甚好玩的，幾個小時就看完了 ，若只是想環島一圈，到此一遊，拍拍照，的確不用2個小時就OK了。不過大老遠跑來這裡，或許過程還吐了好幾次，若不能多留幾晚好好感受蘭嶼的慢活氣息與美麗風情真的是太可惜了。
一個人.朋友們.你都會找到新的自己.發現你愛上這樣的原始。
很原始的地方,當地的友人都很友善,騎機車環島速速解決也要兩個小時,但到那邊漫活的四處發呆,散心！如果你你不怕水,勢必嘗試一下浮淺甚至淺深潛,你會發現你找不到第二處,台灣純淨的藍,及安靜的海洋.....會讓你愛上這個這樣的地方
不去會後悔的地方。
一個人文 自然 生態 融會貫通的地方在這裏打開工作室是一片彩色走過下一村是一堆山豬嗯？上一村才差點撞到肥羊誒...
蘭嶼的藍。
蘭嶼，一個很原始的地方，住著六大部落。在蘭嶼~ 羊群們就是老大，隨處可見發呆亭，害我們一群人動不動就想上去待一下，放空自己只管享受眼前這份寧靜。飛魚 & 拼板舟是蘭嶼的特色，可以花錢體驗坐在拼板舟上的感覺，我划的時候是沒有進水，但倒是有看到其他人一直把水往外撈XD 到蘭嶼我很推薦花錢體驗夜觀，看看蘭嶼的動植物，了解他們的生態環境，還可看見可愛的貓頭鷹^^ 蘭嶼的海非常清澈，不太商業化，但是物價卻偏高，若有預算倒是很推薦吃當地的美食，海鮮類真的很新鮮又好吃，還有當地的地瓜也非常好吃，讓我難以忘懷的好滋味^^ 總之蘭嶼很棒，若你需要適時的放空自己，享受大自然，美景當前所有煩惱都拋去，那麼你很需要來一趟蘭嶼體驗當地的美，並親眼看看蘭嶼的藍：）
回歸純真. 放空。
海是不可思議的藍, 熱情的達悟族人, 隨意逛大街的豬牛羊雞.......在蘭嶼最好的活動就是..什麼都不要做, 放空
生日行。
真的很漂亮~藝術品般的拼板舟,帶紅色的雲離自己好近,路上的紅綠燈就是 鹿,一早起床出民宿看到的就是一堆小豬,追日出,然後很優閒的吃早餐跟民宿老闆聊個天,騎著摩拖車環島一圈,雖然天黑時挺嚇人,傍晚坐在海旁,看那些當自己家游泳池的小孩玩水,總之很舒服這幾天。
充滿原始魅力的島嶼。
認為他是台灣外島中的淨土,因為交通的不便也使得他保留了很晚整的原始風味,不像綠島充滿了商業氣息,島上的居住選擇有限可是卻可以發現處處的生機,活躍在岩壁上山羊,在街上閒晃的黑豬,島上熱情的居明在買東西的時候請你吃現抓的螃蟹,是一個忘記煩惱和塵囂的世外桃源
原住民真的超可愛。
這裡跟綠島比較起來真的是純樸很多，豬、牛、羊在路上到處走！也沒有任何24小時的便利商店，但也因為如此更可以把物質放為最低，感受那當地生活知足的笑容！
蘭嶼生活~。
第一次到蘭嶼,炎炎夏日真的會使人昏昏欲睡...而和藹且熱情的當地人、美麗的星空,日出與日落、大自然的天籟,以及隨處可見的海～這一切真的很難讓人不愛上這裡！與朋友一起坐在海邊...吃著現出爐的窯烤pizza,吃著當地飛魚餐,喝點飲料或小酒,是多麼享受的一件事阿,但夜裡沒有路燈真的很恐怖...待了三天兩夜,都捨不得離開了 :'(一定要再找機會去的~~
蘭嶼，一個讓人不得不愛的地方!!。
 走向世界，不一定就能走進世界。 而我卻在蘭嶼走 進 入了另一個世界.....在蘭嶼，你可以靠自己很近,因為那裡的人、天空和海....在蘭嶼，銀河、流星是天空的樣子，看海是每天必做的事，上山下海是這兒的文化也是生活方式，風趣體貼是這兒的人互動的方式....蘭嶼處處是驚喜和感動,但需要行動和時間去體會，蘭嶼是我第一次遇到當地人騎車或開車經過時,會刻意將行車速度慢下來慢速通過的地方,因為,不希望路人的衣服溼了!!!蘭嶼，是一個會讓人不得不愛的地方!!
蘭嶼星空。
今年夏天我獨自來到蘭嶼，起初是想看看自己是否有能力一個人旅行，結果一個月來認識了許多不同類型的朋友，他們帶著我體驗特殊活動，最難忘的經驗是睡屋頂，在這裡不僅僅是人們熱情，連星星也是如此熱情的撒滿整片天空，無時無刻都能看見流星，那種說不出來的感動總讓人難以忘懷!!
I Love Lanyu!。
蘭嶼很漂亮也很舒服看過那裏的天空之後你會覺得城市裡的天空像是拙劣的仿造品充滿著令人難以呼吸的塵埃阻擋了視線也阻擋了直接和天空面對面的機會早上湛藍的天空晚上的滿天星星更重要的是溫和與熱情的人們讓人想一直一直的待在那裏
讓你捨不得拿起像機的瑰麗寶地。
常常有人說，台東花蓮是台灣最後一塊淨土，但常常我們忘了還有外島，這個需要２個多小時船程的美麗小島－蘭嶼．我們會記得他是因為新聞上反覆說著新年的第一道曙光還有核廢料，但我們真正忘記的是他最真實且樸實的美麗！我這次第一次照訪，就呆了７天６夜，離開時還有無數的不捨，回想在規劃時，常常東想西想一大堆，但造訪蘭嶼真的不必要這麼麻煩，其實只要把心放開，就好了！蘭嶼的美是無法用言詞表達的，蘭嶼的悠閒也是無法訴說的，我只去過一次......但我想再去很多回!這是第一個地方讓我回味無窮，對一切都感到感到眷戀，一種家的悠閒感！也讓我回到台北時一時感到不適應...哈哈苦笑!蘭嶼絕對是個值得呆上１周以上的地方，值得慢慢品嘗，沒去過蘭嶼......別說你看過最美的台灣!
看得到各種藍色的蘭嶼。
在台灣生長這麼久，在夢想了20年後，第一次踏上蘭嶼這個小島，程著那很多人都暈得亂七八糟的船，接近蘭嶼的碼頭，迎接我的是幾隻在海面飛躍的飛魚。So surprise.大家都說蘭嶼四天夠了，不就是一個島嗎? 遊客去那邊潛水、看山看海。而對我來說最奇妙的是海的顏色，在台灣或是澎湖綠島金門馬祖，我從來沒有看過海有這麼多顏色。跟著朋友在蘭嶼島晃了四天三夜，匆匆的又回到台灣。但回台灣之後，卻發現這趟旅程少了些甚麼? 多了很多遺憾。於是我們一家三口決定在暑假再次踏上這個島一星期。去尋找我們的缺口。如果說我想要建議各位遊客些甚麼? 請愛這個島的遊客們一定要耐心看一下，一起來保護這座小島。一個地方的永續包含環境、社會文化與在地經濟。很多遊客為了省錢而不願意花錢請導遊；但回頭想想，你已經花了很多旅費來到這裡，若是無法深入當地文化，讓在地居民有經濟來源，那未來這個美麗的小島，仍舊會美麗嗎?因此只有三件事特別提醒大家。1.在島上大家很可能去夜間觀察，但請您一定不要拿閃光燈照來照去，去拜訪夜間生物時，也請不要用白光照他們，建議還是找當地的導遊帶你去，他們會用yellow or red 玻璃紙包在手電筒上，帶你們去觀察。2.這一座島垃圾分類系統不太健全，物資等都靠船運，也因此大家喝的飲料瓶最後會去哪裡呢??? 如果可以請您盡可能自己帶水壺，島上很多地方可以加水。而製造的瓶子鋁罐等，也看看是否當地有人做回收，不然就壓一壓自己帶回本島也是一種做法。 3.達悟族有很多文化禁忌，到別人家我們還是得是度尊重主人，也不要隨便拿著相機就對著人拍。多一句的問候，多一點尊重，或許會有不同的收穫。
得盡早造訪的好地方。
多年前,利用四月春假期間與孩子們從後壁湖搭船前往蘭嶼,那是我多次搭船經驗中最舒適的幾次之一,不曉得是海流還是海風助陣?很快就抵達美麗的蘭嶼,因為事先經由安排,入住當地人經營的民宿,雖不豪華或美觀,但是乾淨,最主要還是人,真誠好客熱情,天然美景非常值得用雙腳去探索,無論陸上或者海洋~但也正慢慢開發中,能盡早去蘭嶼旅遊,越能感受她天然又純真及對於大自然敬畏的人性~~
台灣最棒的淨土。
已經去過這裡兩次，每次都給我很棒的回憶，騎摩托車環島一直尋找著地圖上的奇岩怪石真的非常有趣。天氣好的時候，夜晚的星空真的會讓人離不開那個小島。島上有很多很專業的夜間嚮導，會告訴遊客很多很有趣的蘭嶼小故事跟傳說。這個小島有別於台灣其他離島地方，文化與民俗風情因為當地的原住民而非常有自己的風格。我也在這裡獻出了第一次深潛的經驗，海裡生物非常豐富，教練也非常專業。深為台灣人一定要來體驗一下蘭嶼的生活。我們還有很棒的淨土，希望去的遊客們要好好愛惜這個地方。
讓人與自然融為一體的小島。
蘭嶼不像臺灣的一部份，它比較像是一個人們能與自然共存的國度。適合中長期渡假，更能體驗雅美文化！這裡的人純樸、熱情，隨處就能遇見羊群跟小豬，走出戶外就能看到海洋與美景。海底也好美～游泳與潛水更是不能錯過的活動！交通不便是很大的問題，坐船２～４個小時、坐飛機２５分鐘　卻不一定都搭得上！來蘭嶼，請抱持著一顆輕鬆的心～無法進入蘭嶼沒關係，隔天一早再試！無法離開蘭嶼也沒關係～請多再享受一天這裡的美景～海島物資缺乏、也需要被保護來這裡必需適應沒什麼東西好吃又昂貴的狀況在這裡請盡量減少製造垃圾，避免使用一次性的物品請抱持開放的態度、並尊重當地文化～就能有很大的收獲囉!!
體驗當地人民簡單的生活。
要是喜歡戶外,體驗新的文化,這裡是個好地方!趁着土著傳統和文化尚未被現代文明同化,還沒成為俗氣的旅遊勝地之前趕緊去吧。老一輩的亞美人還保持着傳統的農作和捕魚的生活方式,要是真想體驗一下的話,千萬不要夏天去,人太多了!我是四月底去的,剛好在旺季之前。對了,去的話最好住在村子里,這裏的地下房屋保存得非常好。這裏沒有太多風景,就海岸線有很多石頭而已,可以跳水和潜水。來這裏玩最好的辦法就是租個模特車,每天100RMB,然後可以沿着海岸騎着玩。來這裏最好保持開放的心態,融入亞美人的生活。可能有些老年人看起來防衛心理很強,對遊客也不是很客氣,但也遇到了很多熱情友好的當地人,注意他們的習俗和忌諱就是,比如不要拿着相機拍人和捕魚等等。
"""
# print "Input：", sentence
words = jieba.cut(sentence, cut_all=False)
# print "Output 精確模式 Full Mode："
tags = jieba.analyse.extract_tags(sentence, 100)
print "Output："
print ",".join(tags)
# print len(tags)
# for word in tags:
#     print word