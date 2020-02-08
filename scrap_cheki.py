import requests
import csv
import re
from bs4 import BeautifulSoup

"""Find All Makes"""
makes_list = []
URL = 'https://www.cheki.co.ke/'
page = requests.get(URL)
make = BeautifulSoup('<optgroup label="Alphabetical"><option value="alfa-romeo">Alfa Romeo</option><option value="audi">Audi</option><option value="aveling-barford">Aveling Barford</option><option value="bajaj">Bajaj</option><option value="bedford">Bedford</option><option value="bmw">BMW</option><option value="captain">Captain</option><option value="caterpillar">Caterpillar</option><option value="chana">Chana</option><option value="chevrolet">Chevrolet</option><option value="chrysler">Chrysler</option><option value="citroen">Citroen</option><option value="claas">Claas</option><option value="daihatsu">Daihatsu</option><option value="deutz">Deutz</option><option value="dodge">Dodge</option><option value="dongfeng">Dongfeng</option><option value="eicher">Eicher</option><option value="equipment-machinery">Equipment &amp; Machinery</option><option value="faw">FAW</option><option value="fiat">Fiat</option><option value="ford">Ford</option><option value="great-wall">Great Wall</option><option value="haojin">Haojin</option><option value="haojue">Haojue</option><option value="hino">Hino</option><option value="honda">Honda</option><option value="howo">HOWO</option><option value="hyundai">Hyundai</option><option value="infiniti">Infiniti</option><option value="isuzu">Isuzu</option><option value="jaguar">Jaguar</option><option value="jeep">Jeep</option><option value="jianshe">Jianshe</option><option value="jincheng">Jincheng</option><option value="kawasaki">Kawasaki</option><option value="kia">Kia</option><option value="kibo">Kibo</option><option value="kingbird">Kingbird</option><option value="ktm">KTM</option><option value="land-rover">Land Rover</option><option value="lexus">Lexus</option><option value="leyland">Leyland</option><option value="lifan">Lifan</option><option value="man">Man</option><option value="maserati">Maserati</option><option value="massey-ferguson">Massey-Ferguson</option><option value="mazda">Mazda</option><option value="mercedes-benz">Mercedes-Benz</option><option value="messy">Messy</option><option value="mini">Mini</option><option value="mitsubishi">Mitsubishi</option><option value="murray">Murray</option><option value="new-holland">New Holland</option><option value="nissan">Nissan</option><option value="old-stone-tractor-co">Old Stone Tractor Co</option><option value="omow">OMOW</option><option value="perodua">Perodua</option><option value="peugeot">Peugeot</option><option value="piaggio">Piaggio</option><option value="porsche">Porsche</option><option value="renault">Renault</option><option value="royal">Royal</option><option value="scania">Scania</option><option value="shineray">Shineray</option><option value="sinotruk">Sinotruk</option><option value="skygo">SkyGo</option><option value="smart">Smart</option><option value="sonalika">Sonalika</option><option value="subaru">Subaru</option><option value="suzuki">Suzuki</option><option value="t-king">T-KING</option><option value="tata">Tata</option><option value="toyota">Toyota</option><option value="trailer">Trailer</option><option value="tvs">TVS</option><option value="vauxhall">Vauxhall</option><option value="victa">Victa</option><option value="volkswagen">Volkswagen</option><option value="volvo">Volvo</option><option value="wuzheng">Wuzheng</option><option value="yamaha">Yamaha</option></optgroup>'
                      ,'html.parser')
makes = make.find_all('option')
# print(len(makes))
for ele in makes:
    # Get the make name
    one_make = str(ele)
    one_make = re.findall('"([^"]*)"', one_make)
    makes_list += one_make

"""Find All Models"""
print(len(makes_list))
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    #writer.writerow(["MAKE", "MODELS"])

    for one_make in makes_list:
        # Get the model lists from different make
        URL = 'https://www.cheki.co.ke/models-sef?data='+ one_make
        page = requests.get(URL)
        models = BeautifulSoup(page.content, 'html.parser')
        models_in_one_make = str(models)

        # Filter quotation marks
        tmp = re.findall(r'"(.*?)"', models_in_one_make)
        #[{"id":"145","title":"145"},{"id":"146","title":"146"},{"id":"147","title":"147"},{"id":"155","title":"155"},{"id":"156","title":"156"},{"id":"159","title":"159"},{"id":"1600","title":"1600"},{"id":"164","title":"164"},{"id":"166","title":"166"},{"id":"175","title":"175"},{"id":"1750","title":"1750"},{"id":"179","title":"179"},{"id":"1900","title":"1900"},{"id":"2000","title":"2000"},{"id":"2600","title":"2600"},{"id":"33","title":"33"},{"id":"4c-spider","title":"4C Spider"},{"id":"6","title":"6"},{"id":"66","title":"66"},{"id":"75","title":"75"},{"id":"8c","title":"8C"},{"id":"90","title":"90"},{"id":"alfasud","title":"Alfasud"},{"id":"alfetta","title":"Alfetta"},{"id":"ar","title":"AR"},{"id":"arna","title":"Arna"},{"id":"bella","title":"Bella"},{"id":"berlina","title":"Berlina"},{"id":"brera","title":"Brera"},{"id":"caimano","title":"Caimano"},{"id":"carabo","title":"Carabo"},{"id":"centauri","title":"Centauri"},{"id":"crosswagon","title":"Crosswagon"},{"id":"cuneo","title":"Cuneo"},{"id":"dardo","title":"Dardo"},{"id":"disco","title":"Disco"},{"id":"eagle","title":"Eagle"},{"id":"giulia","title":"Giulia"},{"id":"giulia-qv","title":"Giulia QV"},{"id":"giulia-super","title":"Giulia Super"},{"id":"giulia-super-stile","title":"Giulia Super Stile"},{"id":"giulietta","title":"Giulietta"},{"id":"graduate","title":"Graduate"},{"id":"gt","title":"GT"},{"id":"gta","title":"GTA"},{"id":"gtv","title":"GTV"},{"id":"junior","title":"Junior"},{"id":"kamal","title":"Kamal"},{"id":"mito","title":"MiTo"},{"id":"navajo","title":"Navajo"},{"id":"nuvola","title":"Nuvola"},{"id":"proteo","title":"Proteo"},{"id":"rz","title":"RZ"},{"id":"scarabeo","title":"Scarabeo"},{"id":"scighera","title":"Scighera"},{"id":"spider","title":"Spider"},{"id":"sportiva","title":"Sportiva"},{"id":"sportwagon","title":"Sportwagon"},{"id":"sprint","title":"Sprint"},{"id":"sz","title":"SZ"}]
        #['id', '145', 'title', '145', 'id', '146', 'title', '146', 'id', '147', 'title', '147', 'id', '155', 'title', '155', 'id', '156', 'title', '156', 'id', '159', 'title', '159', 'id', '1600', 'title', '1600', 'id', '164', 'title', '164', 'id', '166', 'title', '166', 'id', '175', 'title', '175', 'id', '1750', 'title', '1750', 'id', '179', 'title', '179', 'id', '1900', 'title', '1900', 'id', '2000', 'title', '2000', 'id', '2600', 'title', '2600', 'id', '33', 'title', '33', 'id', '4c-spider', 'title', '4C Spider', 'id', '6', 'title', '6', 'id', '66', 'title', '66', 'id', '75', 'title', '75', 'id', '8c', 'title', '8C', 'id', '90', 'title', '90', 'id', 'alfasud', 'title', 'Alfasud', 'id', 'alfetta', 'title', 'Alfetta', 'id', 'ar', 'title', 'AR', 'id', 'arna', 'title', 'Arna', 'id', 'bella', 'title', 'Bella', 'id', 'berlina', 'title', 'Berlina', 'id', 'brera', 'title', 'Brera', 'id', 'caimano', 'title', 'Caimano', 'id', 'carabo', 'title', 'Carabo', 'id', 'centauri', 'title', 'Centauri', 'id', 'crosswagon', 'title', 'Crosswagon', 'id', 'cuneo', 'title', 'Cuneo', 'id', 'dardo', 'title', 'Dardo', 'id', 'disco', 'title', 'Disco', 'id', 'eagle', 'title', 'Eagle', 'id', 'giulia', 'title', 'Giulia', 'id', 'giulia-qv', 'title', 'Giulia QV', 'id', 'giulia-super', 'title', 'Giulia Super', 'id', 'giulia-super-stile', 'title', 'Giulia Super Stile', 'id', 'giulietta', 'title', 'Giulietta', 'id', 'graduate', 'title', 'Graduate', 'id', 'gt', 'title', 'GT', 'id', 'gta', 'title', 'GTA', 'id', 'gtv', 'title', 'GTV', 'id', 'junior', 'title', 'Junior', 'id', 'kamal', 'title', 'Kamal', 'id', 'mito', 'title', 'MiTo', 'id', 'navajo', 'title', 'Navajo', 'id', 'nuvola', 'title', 'Nuvola', 'id', 'proteo', 'title', 'Proteo', 'id', 'rz', 'title', 'RZ', 'id', 'scarabeo', 'title', 'Scarabeo', 'id', 'scighera', 'title', 'Scighera', 'id', 'spider', 'title', 'Spider', 'id', 'sportiva', 'title', 'Sportiva', 'id', 'sportwagon', 'title', 'Sportwagon', 'id', 'sprint', 'title', 'Sprint', 'id', 'sz', 'title', 'SZ']
        # print(one_make)
        # print(tmp)

        # Store models
        model_list = []
        for i in range(len(tmp)):
            if tmp[i] == 'title':
                model_list.append(tmp[i+1])
        print(one_make)
        print(model_list)
        writer.writerows([[one_make.upper()], model_list])





