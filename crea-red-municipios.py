#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016 emijrp <emijrp@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation", u"either version 3 of the License", u"or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not", u"see <http://www.gnu.org/licenses/>.

import sys
import time

import pywikibot
import pywikibot.pagegenerators as pagegenerators
import unicodedata

def creaRedireccion(locapedia='', page=''):
    print(u'Creando redirección')
    newtext = u'{{Redirección %s}}' % (locapedia['nombre'])
    page.text = newtext
    page.save(u'BOT - Creando redirección a municipio en %s' % (locapedia['nombre']))

def ponerRedireccionSiEsNecesario(locapedia='', page=''):
    if re.search(ur'(?im)(\#|\{\{)\s*(redirecci[oó]n|redirect)', page.text):
        print(u'Ya tiene una redirección, saltamos')
        continue
    else:
        print(u'Colocando redirección al principio')
        newtext = u'{{Redirección %s}}\n\n%s' % (locapedia['nombre'], page.text)
        if page.text != newtext:
            pywikibot.showDiff(page.text, newtext)
            page.text = newtext
            page.save(u'BOT - Creando redirección a municipio en %s' % (locapedia['nombre']))
                            
def removeaccute(s):
    return ''.join((c for c in unicodedata.normalize('NFD'", u"s) if unicodedata.category(c) != 'Mn'))

def main():
    locapedias = [
        {
            'nombre': u'Almeríapedia',
            'municipios': [u"Abla", u"Abrucena", u"Adra", u"Albanchez", u"Alboloduy", u"Albox", u"Alcolea", u"Alcóntar", u"Alcudia de Monteagud", u"Alhabia", u"Alhama de Almería", u"Alicún", u"Almería", u"Almócita", u"Alsodux", u"Antas", u"Arboleas", u"Armuña de Almanzora", u"Bacares", u"Balanegra", u"Bayárcal", u"Bayarque", u"Bédar", u"Beires", u"Benahadux", u"Benitagla", u"Benizalón", u"Bentarique", u"Berja", u"Canjáyar", u"Cantoria", u"Carboneras", u"Castro de Filabres", u"Chercos", u"Chirivel", u"Cóbdar", u"Cuevas del Almanzora", u"Dalías", u"El Ejido", u"Enix", u"Felix", u"Fines", u"Fiñana", u"Fondón", u"Gádor", u"Los Gallardos", u"Garrucha", u"Gérgal", u"Huécija", u"Huércal de Almería", u"Huércal-Overa", u"Íllar", u"Instinción", u"Laroya", u"Láujar de Andarax", u"Líjar", u"Lubrín", u"Lucainena de las Torres", u"Lúcar", u"Macael", u"María", u"Mojácar", u"La Mojonera", u"Nacimiento", u"Níjar", u"Ohanes", u"Olula de Castro", u"Olula del Río", u"Oria", u"Padules", u"Partaloa", u"Paterna del Río", u"Pechina", u"Pulpí", u"Purchena", u"Rágol", u"Rioja", u"Roquetas de Mar", u"Santa Cruz de Marchena", u"Santa Fe de Mondújar", u"Senés", u"Serón", u"Sierro", u"Somontín", u"Sorbas", u"Suflí", u"Tabernas", u"Taberno", u"Tahal", u"Terque", u"Tíjola", u"Las Tres Villas", u"Turre", u"Turrillas", u"Uleila del Campo", u"Urrácal", u"Velefique", u"Vélez-Blanco", u"Vélez-Rubio", u"Vera", u"Viator", u"Vícar", u"Zurgena"], 
        }, 
        {
            'nombre': u'Cádizpedia', 
            'municipios': [u"Alcalá de los Gazules", u"Alcalá del Valle", u"Algar", u"Algeciras", u"Algodonales", u"Arcos de la Frontera", u"Barbate", u"Los Barrios", u"Benalup-Casas Viejas", u"Benaocaz", u"Bornos", u"El Bosque", u"Cádiz", u"Castellar de la Frontera", u"Chiclana de la Frontera", u"Chipiona", u"Conil de la Frontera", u"Espera", u"El Gastor", u"Grazalema", u"Jerez de la Frontera", u"Jimena de la Frontera", u"La Línea de la Concepción", u"Medina-Sidonia", u"Olvera", u"Paterna de Rivera", u"Prado del Rey", u"El Puerto de Santa María", u"Puerto Real", u"Puerto Serrano", u"Rota", u"San Fernando", u"San José del Valle", u"San Roque", u"Sanlúcar de Barrameda", u"Setenil de las Bodegas", u"Tarifa", u"Torre Alháquime", u"Trebujena", u"Ubrique", u"Vejer de la Frontera", u"Villaluenga del Rosario", u"Villamartín", u"Zahara"], 
        }, 
        {
            'nombre': u'Córdobapedia', 
            'municipios': [u"Adamuz", u"Aguilar de la Frontera", u"Alcaracejos", u"Almedinilla", u"Almodóvar del Río", u"Añora", u"Baena", u"Belalcázar", u"Belmez", u"Benamejí", u"Los Blázquez", u"Bujalance", u"Cabra", u"Cañete de las Torres", u"Carcabuey", u"Cardeña", u"La Carlota", u"El Carpio", u"Castro del Río", u"Conquista", u"Córdoba", u"Doña Mencía", u"Dos Torres", u"Encinas Reales", u"Espejo", u"Espiel", u"Fernán-Núñez", u"Fuente la Lancha", u"Fuente Obejuna", u"Fuente Palmera", u"Fuente-Tójar", u"La Granjuela", u"Guadalcázar", u"El Guijo", u"Hinojosa del Duque", u"Hornachuelos", u"Iznájar", u"Lucena", u"Luque", u"Montalbán de Córdoba", u"Montemayor", u"Montilla", u"Montoro", u"Monturque", u"Moriles", u"Nueva Carteya", u"Obejo", u"Palenciana", u"Palma del Río", u"Pedro Abad", u"Pedroche", u"Peñarroya-Pueblonuevo", u"Posadas", u"Pozoblanco", u"Priego de Córdoba", u"Puente Genil", u"La Rambla", u"Rute", u"San Sebastián de los Ballesteros", u"Santa Eufemia", u"Santaella", u"Torrecampo", u"Valenzuela", u"Valsequillo", u"La Victoria", u"Villa del Río", u"Villafranca de Córdoba", u"Villaharta", u"Villanueva de Córdoba", u"Villanueva del Duque", u"Villanueva del Rey", u"Villaralto", u"Villaviciosa de Córdoba", u"El Viso", u"Zuheros"], 
        }, 
        {
            'nombre': u'Granadapedia', 
            'municipios': [u"Agrón", u"Alamedilla", u"Albolote", u"Albondón", u"Albuñán", u"Albuñol", u"Albuñuelas", u"Aldeire", u"Alfacar", u"Algarinejo", u"Alhama de Granada", u"Alhendín", u"Alicún de Ortega", u"Almegíjar", u"Almuñécar", u"Alpujarra de la Sierra", u"Alquife", u"Arenas del Rey", u"Armilla", u"Atarfe", u"Baza", u"Beas de Granada", u"Beas de Guadix", u"Benalúa", u"Benalúa de las Villas", u"Benamaurel", u"Bérchules", u"Bubión", u"Busquístar", u"Cacín", u"Cádiar", u"Cájar", u"La Calahorra", u"Calicasas", u"Campotéjar", u"Caniles", u"Cáñar", u"Capileira", u"Carataunas", u"Cástaras", u"Castilléjar", u"Castril", u"Cenes de la Vega", u"Chauchina", u"Chimeneas", u"Churriana de la Vega", u"Cijuela", u"Cogollos de Guadix", u"Cogollos de la Vega", u"Colomera", u"Cortes de Baza", u"Cortes y Graena", u"Cuevas del Campo", u"Cúllar", u"Cúllar Vega", u"Darro", u"Dehesas de Guadix", u"Dehesas Viejas", u"Deifontes", u"Diezma", u"Dílar", u"Dólar", u"Domingo Pérez de Granada", u"Dúdar", u"Dúrcal", u"Escúzar", u"Ferreira", u"Fonelas", u"Freila", u"Fuente Vaqueros", u"Las Gabias", u"Galera", u"Gobernador", u"Gójar", u"Gor", u"Gorafe", u"Granada", u"Guadahortuna", u"Guadix", u"Los Guájares", u"Gualchos", u"Güejar Sierra", u"Güevéjar", u"Huélago", u"Huéneja", u"Huéscar", u"Huétor de Santillán", u"Huétor Tájar", u"Huétor Vega", u"Íllora", u"Ítrabo", u"Iznalloz", u"Játar", u"Jayena", u"Jérez del Marquesado", u"Jete", u"Jun", u"Juviles", u"Láchar", u"Lanjarón", u"Lanteira", u"Lecrín", u"Lentegí", u"Lobras", u"Loja", u"Lugros", u"Lújar", u"La Malahá", u"Maracena", u"Marchal", u"Moclín", u"Molvízar", u"Monachil", u"Montefrío", u"Montejícar", u"Montillana", u"Moraleda de Zafayona", u"Morelábor", u"Motril", u"Murtas", u"Nevada", u"Nigüelas", u"Nívar", u"Ogíjares", u"Orce", u"Órgiva", u"Otívar", u"Padul", u"Pampaneira", u"Pedro Martínez", u"Peligros", u"La Peza", u"El Pinar", u"Pinos Genil", u"Pinos Puente", u"Píñar", u"Polícar", u"Polopos", u"Pórtugos", u"Puebla de Don Fadrique", u"Pulianas", u"Purullena", u"Quéntar", u"Rubite", u"Salar", u"Salobreña", u"Santa Cruz del Comercio", u"Santa Fe", u"Soportújar", u"Sorvilán", u"La Taha", u"Torre-Cardela", u"Torvizcón", u"Trevélez", u"Turón", u"Ugíjar", u"Valderrubio", u"El Valle", u"Valle del Zalabí", u"Válor", u"Vegas del Genil", u"Vélez de Benaudalla", u"Ventas de Huelma", u"Villa de Otura", u"Villamena", u"Villanueva de las Torres", u"Villanueva Mesía", u"Víznar", u"Zafarraya", u"Zagra", u"La Zubia", u"Zújar"], 
        }, 
        {
            'nombre': u'Huelvapedia', 
            'municipios': [u"Alájar", u"Aljaraque", u"El Almendro", u"Almonaster la Real", u"Almonte", u"Alosno", u"Aracena", u"Aroche", u"Arroyomolinos de León", u"Ayamonte", u"Beas", u"Berrocal", u"Bollullos Par del Condado", u"Bonares", u"Cabezas Rubias", u"Cala", u"Calañas", u"El Campillo", u"Campofrío", u"Cañaveral de León", u"Cartaya", u"Castaño del Robledo", u"El Cerro de Andévalo", u"Chucena", u"Corteconcepción", u"Cortegana", u"Cortelazor", u"Cumbres de Enmedio", u"Cumbres de San Bartolomé", u"Cumbres Mayores", u"Encinasola", u"Escacena del Campo", u"Fuenteheridos", u"Galaroza", u"Gibraleón", u"La Granada de Río-Tinto", u"El Granado", u"Higuera de la Sierra", u"Hinojales", u"Hinojos", u"Huelva", u"Isla Cristina", u"Jabugo", u"Lepe", u"Linares de la Sierra", u"Lucena del Puerto", u"Manzanilla", u"Los Marines", u"Minas de Riotinto", u"Moguer", u"La Nava", u"Nerva", u"Niebla", u"La Palma del Condado", u"Palos de la Frontera", u"Paterna del Campo", u"Paymogo", u"Puebla de Guzmán", u"Puerto Moral", u"Punta Umbría", u"Rociana del Condado", u"Rosal de la Frontera", u"San Bartolomé de la Torre", u"San Juan del Puerto", u"San Silvestre de Guzmán", u"Sanlúcar de Guadiana", u"Santa Ana la Real", u"Santa Bárbara de Casa", u"Santa Olalla del Cala", u"Trigueros", u"Valdelarco", u"Valverde del Camino", u"Villablanca", u"Villalba del Alcor", u"Villanueva de las Cruces", u"Villanueva de los Castillejos", u"Villarrasa", u"Zalamea la Real", u"Zufre"], 
        }, 
        {
            'nombre': u'Jaénpedia', 
            'municipios': [u"Albanchez de Mágina", u"Alcalá la Real", u"Alcaudete", u"Aldeaquemada", u"Andújar", u"Arjona", u"Arjonilla", u"Arquillos", u"Arroyo del Ojanco", u"Baeza", u"Bailén", u"Baños de la Encina", u"Beas de Segura", u"Bedmar y Garcíez", u"Begíjar", u"Bélmez de la Moraleda", u"Benatae", u"Cabra del Santo Cristo", u"Cambil", u"Campillo de Arenas", u"Canena", u"Carboneros", u"Cárcheles", u"La Carolina", u"Castellar", u"Castillo de Locubín", u"Cazalilla", u"Cazorla", u"Chiclana de Segura", u"Chilluévar", u"Escañuela", u"Espelúy", u"Frailes", u"Fuensanta de Martos", u"Fuerte del Rey", u"Génave", u"La Guardia de Jaén", u"Guarromán", u"Higuera de Calatrava", u"Hinojares", u"Hornos", u"Huelma", u"Huesa", u"Ibros", u"La Iruela", u"Iznatoraf", u"Jabalquinto", u"Jaén", u"Jamilena", u"Jimena", u"Jódar", u"Lahiguera", u"Larva", u"Linares", u"Lopera", u"Lupión", u"Mancha Real", u"Marmolejo", u"Martos", u"Mengíbar", u"Montizón", u"Navas de San Juan", u"Noalejo", u"Orcera", u"Peal de Becerro", u"Pegalajar", u"Porcuna", u"Pozo Alcón", u"Puente de Génave", u"La Puerta de Segura", u"Quesada", u"Rus", u"Sabiote", u"Santa Elena", u"Santiago de Calatrava", u"Santiago-Pontones", u"Santisteban del Puerto", u"Santo Tomé", u"Segura de la Sierra", u"Siles", u"Sorihuela del Guadalimar", u"Torre del Campo", u"Torreblascopedro", u"Torredonjimeno", u"Torreperogil", u"Torres", u"Torres de Albanchez", u"Úbeda", u"Valdepeñas de Jaén", u"Vilches", u"Villacarrillo", u"Villanueva de la Reina", u"Villanueva del Arzobispo", u"Villardompardo", u"Los Villares", u"Villarrodrigo", u"Villatorres"], 
        }, 
        {
            'nombre': u'Málagapedia', 
            'municipios': [u"Alameda", u"Alcaucín", u"Alfarnate", u"Alfarnatejo", u"Algarrobo", u"Algatocín", u"Alhaurín de la Torre", u"Alhaurín el Grande", u"Almáchar", u"Almargen", u"Almogía", u"Álora", u"Alozaina", u"Alpandeire", u"Antequera", u"Árchez", u"Archidona", u"Ardales", u"Arenas", u"Arriate", u"Atajate", u"Benadalid", u"Benahavís", u"Benalauría", u"Benalmádena", u"Benamargosa", u"Benamocarra", u"Benaoján", u"Benarrabá", u"El Borge", u"El Burgo", u"Campillos", u"Canillas de Aceituno", u"Canillas de Albaida", u"Cañete la Real", u"Carratraca", u"Cartajima", u"Cártama", u"Casabermeja", u"Casarabonela", u"Casares", u"Coín", u"Colmenar", u"Comares", u"Cómpeta", u"Cortes de la Frontera", u"Cuevas Bajas", u"Cuevas de San Marcos", u"Cuevas del Becerro", u"Cútar", u"Estepona", u"Faraján", u"Frigiliana", u"Fuengirola", u"Fuente de Piedra", u"Gaucín", u"Genalguacil", u"Guaro", u"Humilladero", u"Igualeja", u"Istán", u"Iznate", u"Jimera de Líbar", u"Jubrique", u"Júzcar", u"Macharaviaya", u"Málaga", u"Manilva", u"Marbella", u"Mijas", u"Moclinejo", u"Mollina", u"Monda", u"Montecorto", u"Montejaque", u"Nerja", u"Ojén", u"Parauta", u"Periana", u"Pizarra", u"Pujerra", u"Rincón de la Victoria", u"Riogordo", u"Ronda", u"Salares", u"Sayalonga", u"Sedella", u"Serrato", u"Sierra de Yeguas", u"Teba", u"Tolox", u"Torremolinos", u"Torrox", u"Totalán", u"Valle de Abdalajís", u"Vélez-Málaga", u"Villanueva de Algaidas", u"Villanueva de la Concepción", u"Villanueva de Tapia", u"Villanueva del Rosario", u"Villanueva del Trabuco", u"Viñuela", u"Yunquera"], 
        }, 
        {
            'nombre': u'Sevillapedia', 
            'municipios': [u"Aguadulce", u"Alanís", u"Albaida del Aljarafe", u"Alcalá de Guadaíra", u"Alcalá del Río", u"Alcolea del Río", u"La Algaba", u"Algámitas", u"Almadén de la Plata", u"Almensilla", u"Arahal", u"Aznalcázar", u"Aznalcóllar", u"Badolatosa", u"Benacazón", u"Bollullos de la Mitación", u"Bormujos", u"Brenes", u"Burguillos", u"Las Cabezas de San Juan", u"Camas", u"La Campana", u"Cantillana", u"Cañada Rosal", u"Carmona", u"Carrión de los Céspedes", u"Casariche", u"Castilblanco de los Arroyos", u"Castilleja de Guzmán", u"Castilleja de la Cuesta", u"Castilleja del Campo", u"El Castillo de las Guardas", u"Cazalla de la Sierra", u"Constantina", u"Coria del Río", u"Coripe", u"El Coronil", u"Los Corrales", u"El Cuervo de Sevilla", u"Dos Hermanas", u"Écija", u"Espartinas", u"Estepa", u"Fuentes de Andalucía", u"El Garrobo", u"Gelves", u"Gerena", u"Gilena", u"Gines", u"Guadalcanal", u"Guillena", u"Herrera", u"Huévar del Aljarafe", u"Isla Mayor", u"La Lantejuela", u"Lebrija", u"Lora de Estepa", u"Lora del Río", u"La Luisiana", u"El Madroño", u"Mairena del Alcor", u"Mairena del Aljarafe", u"Marchena", u"Marinaleda", u"Martín de la Jara", u"Los Molares", u"Montellano", u"Morón de la Frontera", u"Las Navas de la Concepción", u"Olivares", u"Osuna", u"Los Palacios y Villafranca", u"Palomares del Río", u"Paradas", u"Pedrera", u"El Pedroso", u"Peñaflor", u"Pilas", u"Pruna", u"La Puebla de Cazalla", u"La Puebla de los Infantes", u"La Puebla del Río", u"El Real de la Jara", u"La Rinconada", u"La Roda de Andalucía", u"El Ronquillo", u"El Rubio", u"Salteras", u"San Juan de Aznalfarache", u"San Nicolás del Puerto", u"Sanlúcar la Mayor", u"Santiponce", u"El Saucejo", u"Sevilla", u"Tocina", u"Tomares", u"Umbrete", u"Utrera", u"Valencina de la Concepción", u"Villamanrique de la Condesa", u"Villanueva de San Juan", u"Villanueva del Ariscal", u"Villanueva del Río y Minas", u"Villaverde del Río", u"El Viso del Alcor"], 
        }, 
    ]
    
    site = pywikibot.Site('wikanda', 'wikanda')
    
    for locapedia in locapedias:
        for municipio in locapedia['municipios']:
            municipiosinacentos = removeaccute(municipio)
            if municipiosinacentos == municipio:
                page = pywikibot.Page(site, municipio)
                if page.exists():
                    ponerRedireccionSiEsNecesario(locapedia=locapedia, page=page)
                else:
                    creaRedireccion(locapedia=locapedia, page=page)
            else:
                page = pywikibot.Page(site, municipio)
                pagesinacentos = pywikibot.Page(site, municipiosinacentos)
                if pagesinacentos.exists():
                    if page.exists():
                        ponerRedireccionSiEsNecesario(locapedia=locapedia, page=page)
                    else:
                        pagesinacentos.move(municipio, reason=u"BOT - Trasladando a título correcto")
                else:
                    newtext = u'#redirect [[%s]]' % (municipio)
                    pagesinacentos.text = newtext
                    pagesinacentos.save(u'BOT - Creando redirección a municipio')
                    if page.exists():
                        ponerRedireccionSiEsNecesario(locapedia=locapedia, page=page)
                    else:
                        creaRedireccion(locapedia=locapedia, page=page)

if __name__ == '__main__':
    main()
