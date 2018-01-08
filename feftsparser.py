#!/usr/bin/python
# :*: coding: utf_8 :*:

import re

#steps
#parse through string
#convert
#print out
#i'll work on a window later but for now

def reverse(dictionary):
	# for sifting through the reference list
	# I've set up the ones that matter. NPCs will come later.
	# That's two counts of laziness. I impress myself :o
	for key in dictionary:
		print "\""+dictionary[key]+"\": \""+key+"\","

# now to try out the lambda thing I learned in theory class
# or maybe the regex lessons from 351

#look up syntax trees in python
keyword = {
"$show":"$Wm",
"$left":"3$w0",
"$right":"7$w0",
"$id":"$Ws",
"\\n":"|",
"$emote":"$Wa$E",
"$switch":"$k$p"}


emote = {
	"sweat":"汗" ,
	"blush":"照",
	"default":"通常",
	"surprise":"びっくり",
	"angry":"怒",
	"hurt":"苦",
	"laugh":"笑",
	"smug":"キメ",
	"yell":"やけくそ",
	"possessed":"囚"}
neutral1 = {
	"Corrin":"MU",
	"Anna":"アンナ",
	"Azura":"アクア",
	"Felicia":"フェリシア",
	"Izana":"イザナ",
	"Jakob":"ジョーカー",
	"Kaze":"モズメ",
	"Shura":"アシュラ",
	"Silas":"サイラス"}

neutral2 = {
	"Dwyer":"ディーア", 
	"KanaF":"カンナ男", 
	"KanaM":"カンナ女", 
	"Midori":"ミドリコ", 
	"Shigure":"シグレ", 
	"Sophie":"ゾフィー"}

hoshido1 = {
	"Ryouma": "リョウマ",
	"Oboro": "オボロ",
	"Reina": "ユウギリ",
	"Kaden": "ニシキ",
	"Hinoka": "ヒノカ",
	"Takumi": "タクミ",
	"Kagero": "カゲロウ",
	"Orochi": "オロチ",
	"Hana": "カザハナ",
	"Hinata": "ヒナタ",
	"Subaki": "ツバキ",
	"Hayato": "ツクヨミ",
	"Sakura": "サクラ",
	"Setsuna": "セツナ",
	"Scarlet": "クリムゾン",
	"Yukimura": "ユキムラ",
	"Saizo": "サイゾウ",
	"Rinkah": "リンカ",
	"Azama": "アサマ"}

hoshido2 ={
	"Kiragi": "キサラギ",
	"Mitama": "ミタマ",
	"Hisame": "ヒサメ",
	"Rhajat": "シャラ",
	"Selkie": "キヌ",
	"Shiro": "シノノメ",
	"Caeldori": "マトイ",
	"Asugi": "グレイ"}

nohr1 = {
	"Benny": "ブノワ",
	"Flora": "フローラ",
	"Laslow": "ラズワルド",
	"Leo": "レオン",
	"Keaton": "フランネル",
	"Xander": "マークス",
	"Charlotte": "シャーロッテ",
	"Elise": "エリーゼ　",
	"Peri": "ピエリ",
	"Effie": "エルフィ",
	"Serena": "ルーナ",
	"Gunther": "ギュンター",
	"Niles": "ゼロ",
	"Camilla": "カミラ",
	"Odin": "オーディン",
	"Beruka": "ベルカ",
	"Arthur": "ハロルド",
	"Nyx": "ニュクス"}

nohr2 = {
	"Velouria": "ベロア",
	"Ophelia": "オフェリア",
	"Soleil": "ソレイユ",
	"Forrest": "フォレオ",
	"Siegbert": "ジークベルト",
	"Ignatius": "イグニス",
	"Nina": "エポニーヌ",
	"Percy": "ルッツ"}

normal = {
"Zola": "ゾーラ",
"Anthony": "ロンタオ",
"Iago": "マクベス",
"Garon": "ガロン",
"Hans": "ガンズ",
"Mikoto": "ミコト",
"Arete": "シェンメイ",
"Sumeragi": "スメラギ"}

alternate = {
"AltArete": "シェンメイ影",
"AltSumeragi": "スメラギ影",
"AltMikoto": "ミコト影",
"AltGaron": "スライムガロン"
}


extra = {
"Layla": "ララ",
"RainbowSage": "虹の賢者",
"Cassita": "カシータ",
"HoodSumeragi": "フードマン"
}

boss = {
"Fuga": "フウガ",
"Kotaro": "コタロウ",
"Kilma": "クーリア"
}

other ={
"Lucina": "ルキナ",
"Marth": "マルス",
"Robin": "ルフレ"
}

enemy = {
"Faceless": "ノスフェラトゥ",
"Stoneborn": "ゴーレム"}

villager = {
"NohrOldWoman": "村人おばさん黒",
"HoshidoBoy": "村人お兄さん白",
"HoshidoOldMan": "村人おじいさん白",
"NohrGirl": "村人お姉さん黒",
"NohrBoy": "村人お兄さん黒",
"HoshidoGirl": "村人お姉さん白",
"HoshidoChild": "村人子供白",
"NohrChild": "村人子供黒",
"HoshidianOldWoman": "村人おばさん白",
"NohrOldMan": "村人おじいさん黒"
}

dragon = {
"Anankos2": "竜の状態の透魔竜",
"Anankos": "面をつけた透魔竜",
"BlightDragon": "暗夜竜"}

dlc = {
"HoodAnankos": "善ハイドラ",
"Chrom2": "クロム左",
"GoldFaceless": "金ノスフェラトゥ",
"Lissa": "リズ",
"Lilith": "影リリス",
"Severa": "セレナ",
"Owain": "ウード",
"Chrom": "クロム右",
"Frederick": "フレデリク",
"Inigo": "アズール"
}

generic = {
"OniChieftain": "修羅男",
"Berserker": "バーサーカー男",
"Paladin": "パラディン男",
"NineTails": "九尾の狐男",
"MasterofArms": "兵法者男",
"MasterNinja2": "忍男",
"Apothecary": "薬商人男",
"Villager": "村人女",
"MaligKnight": "レヴナントナイト男",
"Hero2": "マーシナリー男",
"Replica": "絡繰人形",
"Myrmidon": "侍男",
"Priestess2": "巫女",
"Trickster": "アドベンチャラー男",
"Basara": "婆娑羅男",
"Merchant": "大商人男",
"Trueblade": "剣聖男",
"DarkMage": "ダークマージ男",
"Troubadour": "ロッドナイト女",
"Sniper": "弓聖男",
"Cavalier": "ソシアルナイト男",
"Knight": "アーマーナイト男",
"Fighter": "アクスファイター男",
"Diviner": "呪い師男",
"Sentinel": "槍聖男",
"FalconKnight": "聖天馬武者女",
"Strategist": "ストラテジスト女",
"Sage": "陰陽師男",
"Thief": "シーフ男",
"WyvernLord": "ドラゴンマスター男",
"Maid": "メイド女",
"KinshiKnight": "金鵄武者女",
"Priestess": "戦巫女",
"Mechanist": "絡繰師",
"DarkKnight": "ダークナイト男",
"Blacksmith": "鍛冶男",
"Oni": "鬼人男",
"VesselGaron": "マーナガルム男",
"General": "ジェネラル男",
"Sorcerer": "ソーサラー男",
"BowKnight": "ボウナイト男",
"Wolfskin": "ガルー男",
"Archer": "弓使い男",
"SpearFighter": "槍術士男",
"GreatKnight": "グレートナイト男",
"WyvernRider": "ドラゴンナイト男",
"Kitsune": "妖狐男",
"Hero": "ブレイブヒーロー男",
"GreatMaster": "山伏男",
"MasterNinja": "上忍男",
"ShadowUnit)": "カゲマン",
"Lancer": "ランサー男",
"PegasusKnight": "天馬武者女"}
reverse(generic)
# print "$showNina|$left|$idNina|$emotesmug,|Hey Brian! Look! It works! :D"

# print "will parse into"
# print keyword["$show"]+nohr2["Nina"]+"|"+keyword["$left"]+"|"+keyword["$id"]+nohr2["Nina"]+"|"+keyword["$emote"]+emote["smug"]+",|"+"Hey Brian! Look! It works! :D"
# print "then we copy paste to the right >>>"