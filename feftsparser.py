#!/usr/bin/python
# :*: coding: utf_8 :*:
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
"$emote":"$Wa$E"}
for key in keyword:
	print key


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
