import discord 
import asyncio 
import numpy 
import emoji 
import time 
import random
import os
import sqlite3 
import datetime
from discord.ext import commands 
from discord.utils import get
from discord.ext import tasks
from datetime import datetime 

bot = commands.Bot(command_prefix=".")

bot.remove_command(help)

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()+lines[1].strip()

newtoken = read_token()

#-----------------------------EVENTS-----------------------------#



@bot.event
async def on_ready():
    game = discord.Game("Google <DSC>")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("{} has logged in..".format(bot.user.name))


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(659699480555421706)
    message = """Tech Sniffer Dünyasına Hoşgeldin {}!!""".format(member.mention)
    await channel.send(message)


@bot.event 
async def on_member_removed(member):
    channel = bot.get_channel(659699480555421706)
    message = f"{member} artık bir sniffer değil.."
    await channel.send(message)

#-----------------------------COMMANDS-----------------------------#


@bot.command()
async def yardım(ctx):
    embed = discord.Embed(title="**KOMUT REHBERİ**", description="---------------------", color=0x2392c2) 

    embed.add_field(name="**.etkinlik**", value="```Yakındaki etkinlikleri gösterir```")
    embed.add_field(name="**.techsniffer**", value="```Tech Sniffer hakkında bilgi verir```")
    embed.add_field(name="**.atölye**", value="```Güncel atölyeleri gösterir```")
    embed.add_field(name="**.profil**", value="```Kullanıcı hakkında bilgi verir```")
    embed.add_field(name="**.kültür**", value="```Genel kültür bilgileri verir```")

    await ctx.send(embed=embed)



@bot.command()
async def etkinlik(ctx):
    embed = discord.Embed(name="", description="```12 Aralık Perşembe günü GCP Essentials Etkinliği gerçekleşecek```", color=0xc71616)
    await ctx.send(embed=embed)

@bot.command()
async def atölye(ctx):
    pass 

@bot.command()
@commands.has_role("Mod")
async def soru(ctx):
	msg = "new"
	a1 = await ctx.channel.send(msg)
	reactions = ["🇦", "🇧", "🇨", "🇩"]
	await asyncio.sleep(5)
	for r in reactions:
		await a1.add_reaction(r)


@bot.command()
@commands.has_role("Mod")
async def sil(ctx, amount:int):

    await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_role("Helper")
async def rapor(ctx, message):
    pass 

@bot.command(pass_context=True)
async def kültür(ctx):
	
    
	UNIVERSE = ['Güneş ışınları dünyaya 8 dakikada ulaşır', 'Jüpiter diğer gezegenlerden ağırdır', 'Her saniye bir yıldız yok oluyor',
	'Kara delikler ölü yıldızların kalıntılarıdır', 'Astronotlara göre, uzay kurumuş et, sıcak metal ve kaynak dumanı gibi kokuyor', 'Bizden 33 ışık yılı uzaklıkta, tamamen yanan buz ile kaplı bir gezegen var', 'Uyanık olduğu esnada, insan beyni küçük bir ampulü yakacak kadar elektrik üretiyor',
	'Venüs, diğer gezegenlere göre ters yönde dönen tek gezegendir', 'Pireler kendilerinin 100 katı kadar yükseğe zıplayabilirler', 'Mavi balinaların dillerinin ağırlığı yetişkin bir filin ağırlığı kadardır', "Bukalemun'un dili kendi vücudu kadar uzayabilir",
	'Boz ayılar 48 km hızla koşabilirler', '"Jaguar" kelimesinin yerli Amerikan dilindeki anlamı "bir sıçramada öldürür"dür', 'Deniz atları tek eşli canlılardır. Hayatları boyunca sadece tek bir eşleri olur', 'İstiridyeler yaşamları boyunca birçok kez kendi cinsiyetlerini değiştirirler',
	'Yeni doğmuş zürafalar doğumdan yarım saat sonra ayaklarının üzerine kalkabilirler', 'Kar leoparları bir seferde 15 metre ileriye zıplayabilirler', 'Karıncayiyenler günde 35 bin karınca yerler', 'En uzun yaşayan Galapagos kaplumbağası 152. yaşına girmiştir',
	'Mavi Balinalar Yemek Yemeden Ve Su İçmeden 18 Gün Durabilirler', 'Uçan balıklar su üzerinde 59 km hıza ulaşabilirler ve 199 metre yol katedebilirler', 'Devekuşları koşarken bir adımda 5 metre ilerlerler ve 69 km hıza ulaşabilirler', 'Kurtlar günde 9 kg et yerler',
	'Ölümsüz olan bir denizanası türü vardır ', 'Bir Köpekbalığı 100 Milyon Damla Deniz Suyu İçindeki Bir Damla Kanı Hissedebilir', 'Balinalar Balık Değildir, Deniz De Yaşayan Memeli Hayvanlardır', 'Bir Ahtapotun 3 Tane Kalbi Vardır. Bunun Nedeni Fazla Kollara Sahip Olmasıdır',
	'Dünyada 5615 farklı dil konuşuluyor', 'Ölçülen En Yüksek Sıcaklık El Aziziye/libyada 58 Derece', 'Karidesin kalbi kafasının içindedir', 'Timsah yiyen bir balık türü vardır',
	'Japonya Resmi Dini Olmayan Tek Ülkedir', 'Dünyadaki Tüm Uçaklarda Kaza Anında Paraşüt Yerine Can Yeleği Verilir', 'Çinliler Birisini Gözden Kaybolana Kadar Selamlar', 'Dünyanın Bir Numaralı Domuz Üreticisi Ve Tüketicisi Çinlilerdir.',
	"Rusya'nın yüz ölçümü Plüton'dan büyüktür", "İzlanda'da tabelanızda yazması koşulu ile sahte doktorluk yapmanız bir suç değil", "Hindistan'da 44 milyon çocuk işçi var", 'Hz. Muhammed (s.a.v) 1935 yılında ABD Anayasa mahkemesi tarafından dünyanın en büyük adalet sağlayıcısı olarak gösterilmiştir',
	'Eski mısırda kedi öldürmenin cezası idamdı', "Antik Yunan'da Doğmak Ve Ölmek Yasalara Aykırıdır", "Singapur'da Bacak Bacak Üstüne Atmak Yasaktır", 'Sigara içenlerin yüzde 82`si gelişmekte olan ülkelerde yaşıyor',
	'Ördeğin Sesi Yankı Yapmaz', "Antik Yunan'da Doğmak Ve Ölmek Yasalara Aykırıdır", "Tibetliler, Moğollar ve Çin'in bazı yörelerindeki insanlar çaylarına şeker yerine tuz katarlar", 'Eski Mısırlılar kedileri öldüğünde kaşlarını kökünden kazıyarak yas tutuyorlardı',
	'Kediler için 7.kattan düşmek,32.kattan düşmekten daha tehlikelidir', 'Deve Tek Seferde 250 Ltre Su İçebilir', 'Güvercinin Kemiklerinin Ağırlığı,tüylerinden Daha Hafiftir', 'Eşeğin Gözleri 4 Ayağını Da Görebilecek Niteliktedir',
	'Kedilerin İşitme Duyusu İnsanlarınkinden Ve Köpeklerinkinden Hassastır', 'Develer Yaklaşık 40 Gün Susuz Kalabilirler', 'İnekler Merdivenleri Çıkabilir Ancak İnemez', 'Kediler 100 Farklı Ses Çıkarır, Köpeklerse 10 Farklı Ses Çıkarır',
	'Kediler tatlı yiyeceklerin tadını alamazlar', 'Kaydedilen En Uzun Tavuk Uçuşu 13 Saniyedir', 'Atlar Bir Ay Ayakta Kalabilirler', 'Kedi ve köpekler de insanlar gibi solak ya da sağlak olabilirler',
	'Her gün 200.000 yeni insan doğmaktadır', 'Koyunlar, tamamen gömülü bir halde karın altında yaklaşık 4 ile 9 gün arasında kalabilirler', 'Ördek Dünyanın En Zararsız Hayvanıdır', 'Tüm Dünyadaki Kedi Ve Köpekler Yılda 11 Milyar$ Mama Tüketmektedir',
	'İçtiğimiz Sular 3 Milyar Yaşındadır', "Dünya Nüfusunun %50'si Telefonla Hiç Konuşmadı", "Denizlerdeki atıkların %90'ı plastiklerdir", 'Her kıta, yılda ortalama olarak 2 santimetre kadar yer değiştirmektedir',
	'Dünyadaki tüm buzullar erirse deniz seviyesi 65 m kadar aratacaktır', 'Dünyanın üçte biri savaş halinde', 'Gelmiş Geçmiş Dünya Nüfusunun (90 Milyar) Yarısı Dişi Sivrisinekler Tarafından Öldürüldü', 'Dünyadaki Altın Rezervi Bir Kenarı 20 Metre Olan Bir Küp Kadardır',
	'Dünyada 27 milyon köle var', 'Dünyadaki insanların üçte ikisi hiç kar görmedi', 'Her yıl, 2.000 adet yeni deniz türü tanımlanmaktadır', "Dünya'ya her gün 8.600.000 yıldırım düşmektedir",
	"1. Dünya Savaşı'nda Askerlerin Çoğu Sağırdı", 'Parmak İzleri Gibi Dil İzleri de İnsana Özeldir', 'Josephine Cochrane adlı kadın Bulaşık Makinasını icat etmiştir', 'Kurşun Geçirmez Yeleği, Yangın Çıkışını, Cam Sileceği Ve Lazer Yazıcıyı Kadınlar İcat Etmiştir',
	'Normal Bir İnsan Ortalama Yedi Dakika İçerisinde Uykuya Dalar', 'Bir Kadının Sahip Olduğu En Fazla Çocuk Sayısı 69', "Özgürlük Heykeli'nin Ayak Numarası 879'dur", "İnsanların %80'inden fazlası isminden ve ses tonundan memnun değildir",
	'En Uzun Rüya Sadece Ve Sadece 7 Saniyedir', 'Bakteriler Hücrelerin 10 Katı Kadardır', 'Maymunlar Her Yıl Uçak Kazalarından Daha Fazla İnsan Ölümüne Neden Oluyor', 'İngiltere`deki bütün kuğular kraliçenin malıdır',
	'İnsan Ömrünün Yaklaşık Üç Yılı Tuvalette Geçer', 'Otomobil Sayısı İnsan Sayısından 3 Kat Daha Hızlı Artıyor', 'Yanlış Dereceli Gözlük Gözü Bozmaz', 'İnsanlar Ömrü Boyunca 20 Kg Toz Yutarlar',
	'Yaklaşık 85 Milyon İnsan Çölde Yaşıyor', 'Birinci Dünya Savaşında 2.500.000 Tane Atın Kullanıldığını Biliyor Musunuz?', "Polonya Kralı August'un 350 Tane Çocuğunun Olduğunu Biliyor Musunuz?", 'İnsan Beyni En Fazla 150 Arkadaş Kabul Eder',
	'İlk Reklam Filmi Dondurma İçin Çekilmiştir', 'Yer Çekimsiz Bir Yerde Mumun Alevi Küre Şeklinde Olur', 'İnek Kestiğiniz Zaman 1 Saat Yaşayabiliyor', 'Birçok Ruj Çeşidi Balık Pulu İçerir',
	'Sırt Üstü Uyuyan Tek Canlı İnsandır', 'Sadece İnsanlar Ve Yunuslar Cinsellik Yapmaktan Hoşlanırlar', 'Dünyada Yasa Dışı Uyuşturucu Pazarı Tahmini 400 Milyar Dolar', 'Bir İnsan 1`den 1 Milyara Kadar 12 Yılda Sayar',
	"Dünyada her yıl 50.000'den fazla deprem olmaktadır", "1923 'de 1 Oy, Adolf Hitler 'i Nazi Partisinin Liderliğine Getirdi", 'Bir İnsan Bütün Kaslarını Bir Noktaya Yoğunlaştırırsa 25 Tonu Kaldırabilir', 'Bir İnsan Gözüne Sabun Süremez',
	'Kadınların sır saklayabildikleri ortalama süre 47 saat ve 15 dakikadır', 'Eğer kulaklıklarınızı burun deliklerinize sokup ağzınızı açarsanız konuşuyormuşsunuz gibi ses çıkar', 'Kupa papazı, bıyıksız olan tek papazdır', 'Satrançta ilk on hamleyi oynamanız için önünüzde tam 170.000.000.000.000.000.000.000.000 olasılık vardır',
	'Geceleri sabaha göre %1 daha kısa olursunuz', 'Her yıl 10 dil ölüyor', 'Bir Amerikan doları banknotunun ortalama ömrü 18 ay', 'İntiharla ölenlerin sayısı, çatışmalarda ölenlerden fazla',
	'Mario, Blokları Eliyle Kırar; Kafasıyla Değil', 'Soğan Dograrken Sakız Çiğnerseniz Gözleriniz Yaşarmaz', 'Bir insanla ne kadar saçmalıyorsanız, o kadar samimisinizdir', 'Leonardo Da Vinci aynı anda bir eliyle yazı yazıp diğer eliyle resim yapabiliyordu', ]
	'111.111.111 X 111.111.111=? Sonuç=12,345,678,987,654,321', 'Bir Ton Kağıt Geri Dönüştürüldügünde 17 Ağaç Kurtarılır', 'Dünyada Her Sekiz Saniyede Bir Bebek Doğmaktadır', 'Pi sayısı 2012 itibariyle bir trilyonuncu basamağına kadar hesaplandı',
	'Kalp krizleri, daha çok Pazartesi günleri meydana geliyor', "Amerika'da Her Saat 40 Kişi Kanserden Hayatını Kaybediyor", 'Deniz Yıldızlarının Beyni Yoktur', '1 kuruşun maliyeti 2 kuruş olduğundan ücretimden kalkmıştır',
	'Bilgisayar Ekranına Bakmak Gözü Bozmaz,sadece Gözü Yorar', 'Yediğimiz Bir Besinin Ağzımızdan Midemize Gitmesi 7 Saniye Sürer', 'Gün İçinde Uyuyacağınız 1 Saatlik Uyku, 4 Saatlik Gece Uykusuna Bedeldir', 'Mavi renk stresi azaltır. Uzun süre vakit geçirdiğiniz alana mavi eşyalar koyun',
	"Google'de Zerg Rush Yazarsanız Sayfa Kendi Kendini Yemeye Başlayacaktır", 'Motorlu araçlar dakikada 2 insanı öldürüyor', "Apple'ın bütün reklamlarında saat 9.41'i gösterir", 'Ketçap 1830´lu yıllarda ilaç olarak satılırdı',

	universeSelection = random.choice(UNIVERSE)
	embed = discord.Embed(title='', description=f'**{universeSelection}**', color=0x1bcc35)
	await ctx.send(embed=embed)




bot.run(newtoken)
