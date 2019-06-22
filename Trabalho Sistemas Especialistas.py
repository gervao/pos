from random import choice
from pyknow import *


class harmonizacao(KnowledgeEngine):
    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Mexicana'))
    def a(self):
        print("Abacate (Guacamole ou Salada)")


    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Mexicana'))
    def b(self):
        print("Abacate (Guacamole ou Salada)")


    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Mexicana'))
    def c(self):
        print("Abacate (Guacamole ou Salada)")


    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Aperitivo'))
    def d(self):
        print("Amêndoas Salgadas")


    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Aperitivo'))
    def e(self):
        print("Amêndoas Salgadas")


    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Peixe'))
    def f(self):
        print("Anchovas")


    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Peixe'))
    def g(self):
        print("Anchovas")


    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Peixe'))
    def h(self):
        print("Anchovas")


    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Peixe'))
    def i(self):
        print("Anchovas")


    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Peixe'))
    def j(self):
        print("Anchovas")


    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Peixe'))
    def k(self):
        print("Anchovas")


    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Peixe'))
    def l(self):
        print("Anchovas")


    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Peixe'))
    def m(self):
        print("Anchovas")


    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def n(self):
        print("Appfelstrudel")


    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def o(self):
        print("Appfelstrudel")


    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def p(self):
        print("Appfelstrudel")


    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def q(self):
        print("Appfelstrudel")


    @Rule(Fact(estilo='Berliner Weisse'), Fact(tpcomida='Frutos do Mar'))
    def r(self):
        print("Arenque (Peixe gorduroso)")


    @Rule(Fact(estilo='Flanders Brown Ale/Oud Bruin'), Fact(tpcomida='Frutos do Mar'))
    def s(self):
        print("Arenque (Peixe gorduroso)")


    @Rule(Fact(estilo='Flanders Red Ale'), Fact(tpcomida='Frutos do Mar'))
    def t(self):
        print("Arenque (Peixe gorduroso)")


    @Rule(Fact(estilo='Lambic - Gueuze'), Fact(tpcomida='Frutos do Mar'))
    def u(self):
        print("Arenque (Peixe gorduroso)")


    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Frutos do Mar'))
    def v(self):
        print("Atum (massas ou sanduíches)")


    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Frutos do Mar'))
    def x(self):
        print("Atum (massas ou sanduíches)")


    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Frutos do Mar'))
    def y(self):
        print("Atum (salada verde ou cru)")


    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Frutos do Mar'))
    def z(self):
        print("Atum (salada verde ou cru)")


    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Frutos do Mar'))
    def aa(self):
        print("Atum (salada verde ou cru)")


    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Pratos'))
    def ab(self):
        print("au poivre guarnecido com batatas au gratinado")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Carne de Aves'))
    def ac(self):
        print("Avestruz")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne de Aves'))
    def ad(self):
        print("Avestruz")

    @Rule(Fact(estilo='Maibock/Helles Bock'), Fact(tpcomida='Carne de Aves'))
    def ae(self):
        print("Avestruz")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Aperitivo'))
    def af(self):
        print("Azeitonas")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Aperitivo'))
    def ag(self):
        print("Azeitonas")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Aperitivo'))
    def ah(self):
        print("Azeitonas")

    @Rule(Fact(estilo='American Amber Ale'), Fact(tpcomida='Peixe'))
    def ai(self):
        print("Bacalhau")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Peixe'))
    def aj(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Peixe'))
    def ak(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Peixe'))
    def al(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Peixe'))
    def am(self):
        print("Bacalhau")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Peixe'))
    def an(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Peixe'))
    def ao(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Peixe'))
    def ap(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Peixe'))
    def aq(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Peixe'))
    def ar(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Special/Premium Bitter'), Fact(tpcomida='Peixe'))
    def aszz(self):
        print("Bacalhau")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Peixe'))
    def at(self):
        print("Bacalhau")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Sobremesa'))
    def au(self):
        print("Banana (base para sobremesas)")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Sobremesa'))
    def av(self):
        print("Banana (base para sobremesas)")

    @Rule(Fact(estilo='German Weizenbock'), Fact(tpcomida='Sobremesa'))
    def ax(self):
        print("Banana (base para sobremesas)")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def ay(self):
        print("Banana (base para sobremesas)")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def az(self):
        print("Banana (base para sobremesas)")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def aaa(self):
        print("Batatas Gratinadas")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Pratos'))
    def aab(self):
        print("Batatas Gratinadas")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Pratos'))
    def aac(self):
        print("Batatas Gratinadas")

    @Rule(Fact(estilo='Belgian Blond Ale'), Fact(tpcomida='Saladas'))
    def aad(self):
        print("Beterraba (salada)")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Saladas'))
    def aae(self):
        print("Beterraba (salada)")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Saladas'))
    def aaf(self):
        print("Beterraba (salada)")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Saladas'))
    def aag(self):
        print("Beterraba (salada)")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Saladas'))
    def aah(self):
        print("Beterraba (salada)")

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Carne de Boi'))
    def aai(self):
        print("Bife Grelhado")

    @Rule(Fact(estilo='American Amber Ale'), Fact(tpcomida='Carne de Boi'))
    def aaj(self):
        print("Bife Grelhado")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Carne de Boi'))
    def aak(self):
        print("Bife Grelhado")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne de Boi'))
    def aal(self):
        print("Bife Grelhado")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Carne de Boi'))
    def aam(self):
        print("Bife Grelhado")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Aperitivo'))
    def aan(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='German Dunkelweizen'), Fact(tpcomida='Aperitivo'))
    def aao(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Aperitivo'))
    def aap(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='German Roggenbier'), Fact(tpcomida='Aperitivo'))
    def aaq(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Aperitivo'))
    def aar(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Aperitivo'))
    def aas(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='Lambic - Gueuze'), Fact(tpcomida='Aperitivo'))
    def aat(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Aperitivo'))
    def aau(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Aperitivo'))
    def aav(self):
        print("Bolinho de Bacalhau")\

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def aax(self):
        print("Brownies")\

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def aay(self):
        print("Brownies")\

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Mexicana'))
    def aaz(self):
        print("Burritos")\

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Mexicana'))
    def aba(self):
        print("Burritos")\

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Mexicana'))
    def abb(self):
        print("Burritos")\

    @Rule(Fact(estilo='Irish Red Ale'), Fact(tpcomida='Mexicana'))
    def abc(self):
        print("Burritos")\

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Frutos do Mar'))
    def abd(self):
        print("Camarão")\

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Frutos do Mar'))
    def abe(self):
        print("Camarão")\

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def abf(self):
        print("Camarão")\

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Frutos do Mar'))
    def abg(self):
        print("Camarão")\

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Frutos do Mar'))
    def abh(self):
        print("Camarão")\

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Frutos do Mar'))
    def abi(self):
        print("Camarão")\

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Frutos do Mar'))
    def abj(self):
        print("Camarão")\

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Frutos do Mar'))
    def abk(self):
        print("Camarão")\

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def abl(self):
        print("Camarão")\

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Frutos do Mar'))
    def abm(self):
        print("Camarão")\

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Frutos do Mar'))
    def abn(self):
        print("Camarão")\

    @Rule(Fact(estilo=' American Lager'), Fact(tpcomida='Frutos do Mar'))
    def abo(self):
        print("Camarão")\

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Frutos do Mar'))
    def abp(self):
        print("Camarão")\

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Frutos do Mar'))
    def abq(self):
        print("Camarão")\

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Frutos do Mar'))
    def abr(self):
        print("Camarão")\

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Frutos do Mar'))
    def abs(self):
        print("Camarão")\

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Frutos do Mar'))
    def abt(self):
        print("Camarão")\

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Frutos do Mar'))
    def abo(self):
        print("Camarão")\

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Frutos do Mar'))
    def abp(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def abq(self):
        print("Caranguejo")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Frutos do Mar'))
    def abr(self):
        print("Caranguejo")

    @Rule(Fact(estilo='Export'), Fact(tpcomida='Frutos do Mar'))
    def abs(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Frutos do Mar'))
    def abt(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Frutos do Mar'))
    def abu(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Kristallweizen'), Fact(tpcomida='Frutos do Mar'))
    def abv(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def abx(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Weizen'), Fact(tpcomida='Frutos do Mar'))
    def aby(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Frutos do Mar'))
    def abz(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Frutos do Mar'))
    def aca(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Frutos do Mar'))
    def acb(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Frutos do Mar'))
    def acc(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Frutos do Mar'))
    def acd(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Frutos do Mar'))
    def ace(self):
        print("Caranguejo")\

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Carne de Boi'))
    def acf(self):
        print("Carne Assada")\

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Carne de Boi'))
    def acg(self):
        print("Carne Assada")\

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Carne de Boi'))
    def ach(self):
        print("Carne Assada")\

    @Rule(Fact(estilo='Extra Special Bitter/English Pale Ale'), Fact(tpcomida='Carne de Boi'))
    def aci(self):
        print("Carne Assada")\

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Carne de Boi'))
    def acj(self):
        print("Carne Assada")\

    @Rule(Fact(estilo='Red Ale'), Fact(tpcomida='Carne de Boi'))
    def ack(self):
        print("Carne Assada")\

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Pratos'))
    def acl(self):
        print("Carne com Chili")\

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Pratos'))
    def acm(self):
        print("Carne com Chili")\

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Pratos'))
    def acn(self):
        print("Carne com Chili")\

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Pratos'))
    def aco(self):
        print("Carne com Chili")\

    @Rule(Fact(estilo='Dark Strong Ale'), Fact(tpcomida='Pratos'))
    def acp(self):
        print("Carne de Panela em Cubos")\

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Pratos'))
    def acq(self):
        print("Carne de Panela em Cubos")\

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Pratos'))
    def acr(self):
        print("Carne de Panela em Cubos")\

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Pratos'))
    def acs(self):
        print("Carne de Panela em Cubos")\

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Carne Suína'))
    def act(self):
        print("Carne Suína Assada")\

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne Suína'))
    def acu(self):
        print("Carne Suína Assada")\

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne Suína'))
    def acv(self):
        print("Carne Suína Assada")\

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Carne Suína'))
    def acx(self):
        print("Carne Suína Assada")\

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Carne Suína'))
    def acy(self):
        print("Carne Suína Assada")\

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Carne Suína'))
    def acz(self):
        print("Carne Suína Assada")\

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Aperitivo'))
    def ada(self):
        print("Carpaccio")\

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Aperitivo'))
    def adb(self):
        print("Carpaccio")\

    @Rule(Fact(estilo='Extra Special Bitter/English Pale Ale'), Fact(tpcomida='Aperitivo'))
    def adc(self):
        print("Carpaccio")\

    @Rule(Fact(estilo='German Weizenbock'), Fact(tpcomida='Aperitivo'))
    def ade(self):
        print("Carpaccio")\

    @Rule(Fact(estilo='Irish Red Ale'), Fact(tpcomida='Aperitivo'))
    def adf(self):
        print("Carpaccio")\

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Pratos'))
    def adg(self):
        print("Cassoulet")\

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Pratos'))
    def adh(self):
        print("Cassoulet")\

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def adi(self):
        print("Cassoulet")

    @Rule(Fact(estilo='Ale'), Fact(tpcomida='Pratos'))
    def adj(self):
        print("Caviar")\

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Pratos'))
    def adk(self):
        print("Caviar")\

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Pratos'))
    def adl(self):
        print("Caviar")\

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Pratos'))
    def adm(self):
        print("Caviar")\

    @Rule(Fact(estilo='American Wheat/Rye'), Fact(tpcomida='Saladas'))
    def adn(self):
        print("Ceasar Salad")\

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Saladas'))
    def ado(self):
        print("Ceasar Salad")\

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Saladas'))
    def adp(self):
        print("Ceasar Salad")\

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Saladas'))
    def adq(self):
        print("Ceasar Salad")\

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Saladas'))
    def adr(self):
        print("Ceasar Salad")\

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Saladas'))
    def ads(self):
        print("Ceasar Salad")\

    @Rule(Fact(estilo='Beer'), Fact(tpcomida='Sobremesa'))
    def adt(self):
        print("Cheesecake")\

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def adu(self):
        print("Cheesecake")\

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def adv(self):
        print("Cheesecake")\

    @Rule(Fact(estilo='Fruit Beer'), Fact(tpcomida='Sobremesa'))
    def adx(self):
        print("Chocolate")\

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def ady(self):
        print("Chocolate")\

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def adz(self):
        print("Chocolate")\

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def aea(self):
        print("Chocolate")\

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def aeb(self):
        print("Chocolate")\

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Aperitivo'))
    def aec(self):
        print("Chouriço")\

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Aperitivo'))
    def aed(self):
        print("Chouriço")\

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Aperitivo'))
    def aef(self):
        print("Chouriço")\

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Aperitivo'))
    def aeg(self):
        print("Chucrute (conserva de repolho)")\

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Aperitivo'))
    def aeh(self):
        print("Chucrute (conserva de repolho)")\

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Aperitivo'))
    def aei(self):
        print("Chucrute (conserva de repolho)")\

    @Rule(Fact(estilo='German Weizenbock'), Fact(tpcomida='Aperitivo'))
    def aej(self):
        print("Chucrute (conserva de repolho)")\

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Aperitivo'))
    def aek(self):
        print("Chucrute (conserva de repolho)")\

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Aperitivo'))
    def ael(self):
        print("Chucrute (conserva de repolho)")\

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Carne de Aves'))
    def aem(self):
        print("Codorna")\

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Carne de Aves'))
    def aen(self):
        print("Codorna")\

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne de Aves'))
    def aeo(self):
        print("Codorna")\

    @Rule(Fact(estilo='Premium Bitter'), Fact(tpcomida='Carne de Aves'))
    def aep(self):
        print("Codorna")\

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Carne Outras'))
    def aeq(self):
        print("Coelho")\

    @Rule(Fact(estilo='Extra Special Bitter/English Pale Ale'), Fact(tpcomida='Carne Outras'))
    def aer(self):
        print("Coelho")\

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Aperitivo'))
    def aes(self):
        print("Cogumelos (Champignon, Shiitake, Maitake, Porto Bello, Shimeji Preto, Shimeji Branco)")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Aperitivo'))
    def aet(self):
        print("Cogumelos (Champignon, Shiitake, Maitake, Porto Bello, Shimeji Preto, Shimeji Branco)")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Aperitivo'))
    def aeu(self):
        print("Cogumelos (Champignon, Shiitake, Maitake, Porto Bello, Shimeji Preto, Shimeji Branco)")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Aperitivo'))
    def aev(self):
        print("Cogumelos (Champignon, Shiitake, Maitake, Porto Bello, Shimeji Preto, Shimeji Branco)")

    @Rule(Fact(estilo='Strong Scotch Ale'), Fact(tpcomida='Aperitivo'))
    def aex(self):
        print("Cogumelos (Champignon, Shiitake, Maitake, Porto Bello, Shimeji Preto, Shimeji Branco)")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne Outras'))
    def aey(self):
        print("Cordeiro Assado")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne Outras'))
    def aez(self):
        print("Cordeiro Assado")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne Outras'))
    def afa(self):
        print("Cordeiro Assado")

    @Rule(Fact(estilo='Old Ale'), Fact(tpcomida='Carne Outras'))
    def afb(self):
        print("Cordeiro Assado")

    @Rule(Fact(estilo='Strong Scotch Ale'), Fact(tpcomida='Carne Outras'))
    def afc(self):
        print("Cordeiro Assado")

    @Rule(Fact(estilo='Amber Ale'), Fact(tpcomida='Carne Outras'))
    def afd(self):
        print("Cordeiro Grelhado")

    @Rule(Fact(estilo='Dark American Lager'), Fact(tpcomida='Carne Outras'))
    def afe(self):
        print("Cordeiro Grelhado")

    @Rule(Fact(estilo='Oatmeal Stout'), Fact(tpcomida='Carne Outras'))
    def aff(self):
        print("Cordeiro Grelhado")

    @Rule(Fact(estilo='Schwarzbier'), Fact(tpcomida='Carne Outras'))
    def afg(self):
        print("Cordeiro Grelhado")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Carne Suína'))
    def afh(self):
        print("Costelinha Suína com Barbecue")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Carne Suína'))
    def afi(self):
        print("Costelinha Suína com Barbecue")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Pratos'))
    def afj(self):
        print("Crème Brulée")

    @Rule(Fact(estilo='Barley Wine'), Fact(tpcomida='Pratos'))
    def afk(self):
        print("Crème Brulée")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def afl(self):
        print("Crème Brulée")

    @Rule(Fact(estilo='Fruit Beer'), Fact(tpcomida='Pratos'))
    def afm(self):
        print("Crème Brulée")

    @Rule(Fact(estilo='Old Ale'), Fact(tpcomida='Pratos'))
    def afn(self):
        print("Crème Brulée")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Pratos'))
    def afo(self):
        print("Crème Brulée")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Pratos'))
    def afp(self):
        print("Crème Brulée")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Pratos'))
    def afq(self):
        print("Cuscuz")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Pratos'))
    def afr(self):
        print("Cuscuz")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def afs(self):
        print("Cuscuz")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def aft(self):
        print("Cuscuz")

    @Rule(Fact(estilo='Helles'), Fact(tpcomida='Pratos'))
    def afu(self):
        print("Cuscuz")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Aperitivo'))
    def afv(self):
        print("Empanadas")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Aperitivo'))
    def afx(self):
        print("Empanadas")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Aperitivo'))
    def afy(self):
        print("Empanadas")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Aperitivo'))
    def afz(self):
        print("Empanadas")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Aperitivo'))
    def aga(self):
        print("Empanadas")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Aperitivo'))
    def agb(self):
        print("Empanadas")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Aperitivo'))
    def agc(self):
        print("Empanadas")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Aperitivo'))
    def agd(self):
        print("Empanadas")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Aperitivo'))
    def age(self):
        print("Empanadas")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Aperitivo'))
    def agf(self):
        print("Empanadas")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Mexicana'))
    def agg(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Mexicana'))
    def agh(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Mexicana'))
    def agi(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Mexicana'))
    def agj(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Mexicana'))
    def agk(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Mexicana'))
    def agl(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Irish Red Ale'), Fact(tpcomida='Mexicana'))
    def agm(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Mexicana'))
    def agn(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Mexicana'))
    def ago(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Mexicana'))
    def agp(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Peixe'))
    def agq(self):
        print("Enguia Defumada")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Peixe'))
    def agr(self):
        print("Enguia Defumada")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Peixe'))
    def ags(self):
        print("Enguia Defumada")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Peixe'))
    def agt(self):
        print("Enguia Defumada")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Pratos'))
    def agu(self):
        print("Escargot")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Pratos'))
    def agv(self):
        print("Escargot")

    @Rule(Fact(estilo='Pilsener'), Fact(tpcomida='Pratos'))
    def agx(self):
        print("Escargot")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Pratos'))
    def agy(self):
        print("Escargot")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Pratos'))
    def agz(self):
        print("Escargot")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Pratos'))
    def aha(self):
        print("Escargot")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Pratos'))
    def ahb(self):
        print("Escargot")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Pratos'))
    def ahc(self):
        print("Escargot")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Pratos'))
    def ahd(self):
        print("Escargot")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne de Aves'))
    def ahe(self):
        print("Faisão")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne de Aves'))
    def ahf(self):
        print("Faisão")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne de Aves'))
    def ahg(self):
        print("Faisão")

    @Rule(Fact(estilo='Extra Special Bitter/English Pale Ale'), Fact(tpcomida='Carne de Aves'))
    def ahh(self):
        print("Faisão")

    @Rule(Fact(estilo='Old Ale'), Fact(tpcomida='Carne de Aves'))
    def ahi(self):
        print("Faisão")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Pratos'))
    def ahj(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='Wine'), Fact(tpcomida='Pratos'))
    def ahk(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def ahl(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Pratos'))
    def ahm(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def ahn(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Pratos'))
    def aho(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='Stout'), Fact(tpcomida='Pratos'))
    def ahp(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne de Boi'))
    def ahq(self):
        print("Fígado")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Carne de Boi'))
    def ahr(self):
        print("Filet Mignon")

    @Rule(Fact(estilo='Barley Wine'), Fact(tpcomida='Sobremesa'))
    def ahs(self):
        print("Foie Gras")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Sobremesa'))
    def aht(self):
        print("Foie Gras")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Sobremesa'))
    def ahu(self):
        print("Foie Gras")

    @Rule(Fact(estilo='Flanders Brown Ale/Oud Bruin'), Fact(tpcomida='Sobremesa'))
    def ahv(self):
        print("Foie Gras")

    @Rule(Fact(estilo='Flanders Red Ale'), Fact(tpcomida='Sobremesa'))
    def ahx(self):
        print("Foie Gras")

    @Rule(Fact(estilo='Lambic - Fruit'), Fact(tpcomida='Sobremesa'))
    def ahy(self):
        print("Foie Gras")

    @Rule(Fact(estilo='Strong Scotch Ale'), Fact(tpcomida='Sobremesa'))
    def ahz(self):
        print("Foie Gras")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Pratos'))
    def aia(self):
        print("Fondue de Queijo")

    @Rule(Fact(estilo='Maibock/Helles Bock'), Fact(tpcomida='Pratos'))
    def aib(self):
        print("Fondue de Queijo")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Pratos'))
    def aic(self):
        print("Fondue de Queijo")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Pratos'))
    def aid(self):
        print("Fondue de Queijo")

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Carne de Aves'))
    def aie(self):
        print("Frango a Passarinho")

    @Rule(Fact(estilo='American Amber Ale'), Fact(tpcomida='Carne de Aves'))
    def aif(self):
        print("Frango a Passarinho")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Carne de Aves'))
    def aig(self):
        print("Frango a Passarinho")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Pratos'))
    def aih(self):
        print("Frango ao Vinho")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Pratos'))
    def aii(self):
        print("Frango ao Vinho")

    @Rule(Fact(estilo='Standard Bitter'), Fact(tpcomida='Carne de Aves'))
    def aij(self):
        print("Frango Assado")

    @Rule(Fact(estilo='American Amber Ale'), Fact(tpcomida='Carne de Aves'))
    def aik(self):
        print("Frango Assado")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Carne de Aves'))
    def ail(self):
        print("Frango Assado")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Carne de Aves'))
    def aim(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne de Aves'))
    def ain(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Carne de Aves'))
    def aio(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne de Aves'))
    def aip(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Irish Red Ale'), Fact(tpcomida='Carne de Aves'))
    def aiq(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Carne de Aves'))
    def air(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Carne de Aves'))
    def ais(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Traditional Bock'), Fact(tpcomida='Carne de Aves'))
    def ait(self):
        print("Frango Assado")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Carne de Aves'))
    def aiu(self):
        print("Frango na Brasa (churrasco)")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Carne de Aves'))
    def aiv(self):
        print("Frango na Brasa (churrasco)")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Carne de Aves'))
    def aix(self):
        print("Frango na Brasa (churrasco)")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Carne de Aves'))
    def aiy(self):
        print("Frango na Brasa (churrasco)")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Carne de Aves'))
    def aiz(self):
        print("Frango na Brasa (churrasco)")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Pratos'))
    def aja(self):
        print("Goulash")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def ajb(self):
        print("Goulash")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def ajc(self):
        print("Goulash")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Pratos'))
    def ajd(self):
        print("Goulash")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Pratos'))
    def aje(self):
        print("Goulash")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Aperitivo'))
    def ajf(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Aperitivo'))
    def ajg(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Aperitivo'))
    def ajh(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Aperitivo'))
    def aji(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Aperitivo'))
    def ajj(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Aperitivo'))
    def ajk(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Aperitivo'))
    def ajl(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Aperitivo'))
    def ajm(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Aperitivo'))
    def ajn(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Aperitivo'))
    def ajo(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Aperitivo'))
    def ajp(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo='German Dunkelweizen'), Fact(tpcomida='Pratos'))
    def ajq(self):
        print("Haddock Assado")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def ajr(self):
        print("Haddock Assado")

    @Rule(Fact(estilo='German Roggenbier'), Fact(tpcomida='Pratos'))
    def ajs(self):
        print("Haddock Assado")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def ajt(self):
        print("Haddock Assado")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Pratos'))
    def aju(self):
        print("Haddock Assado")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Pratos'))
    def ajv(self):
        print("Haddock Assado")

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Lanches'))
    def ajx(self):
        print("Hamburger")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Lanches'))
    def ajy(self):
        print("Hamburger")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Lanches'))
    def ajz(self):
        print("Hamburger")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Lanches'))
    def aka(self):
        print("Hamburger")

    @Rule(Fact(estilo='Dark American Lager'), Fact(tpcomida='Lanches'))
    def akb(self):
        print("Hamburger")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Lanches'))
    def akc(self):
        print("Hamburger")

    @Rule(Fact(estilo='Schwarzbier'), Fact(tpcomida='Lanches'))
    def akd(self):
        print("Hamburger")

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Aperitivo'))
    def ake(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Aperitivo'))
    def akf(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Aperitivo'))
    def akg(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Aperitivo'))
    def akh(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Aperitivo'))
    def aki(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Aperitivo'))
    def akj(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo='Traditional Bock'), Fact(tpcomida='Aperitivo'))
    def akk(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne Outras'))
    def akl(self):
        print("Javali")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Carne Outras'))
    def akm(self):
        print("Javali")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Carne Outras'))
    def akn(self):
        print("Javali")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Carne Outras'))
    def ako(self):
        print("Javali")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Carne Outras'))
    def akp(self):
        print("Javali")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Carne Outras'))
    def akq(self):
        print("Javali")

    @Rule(Fact(estilo='Strong Scotch Ale'), Fact(tpcomida='Carne Outras'))
    def akr(self):
        print("Javali")

    @Rule(Fact(estilo='American Amber Ale'), Fact(tpcomida='Pratos'))
    def aks(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Pratos'))
    def akt(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Dark American Lager'), Fact(tpcomida='Pratos'))
    def aku(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Pratos'))
    def akv(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Pratos'))
    def akx(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def aky(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Extra Special Bitter/English Pale Ale'), Fact(tpcomida='Pratos'))
    def akz(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Pratos'))
    def ala(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Pratos'))
    def alb(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Pratos'))
    def alc(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Schwarzbier'), Fact(tpcomida='Pratos'))
    def ald(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Frutos do Mar'))
    def ale(self):
        print("Lagosta")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Frutos do Mar'))
    def alf(self):
        print("Lagosta")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Frutos do Mar'))
    def alg(self):
        print("Lagosta")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Frutos do Mar'))
    def alh(self):
        print("Lagosta")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Frutos do Mar'))
    def ali(self):
        print("Lagosta")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Frutos do Mar'))
    def alj(self):
        print("Lagosta")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def alk(self):
        print("Lagosta")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Frutos do Mar'))
    def all(self):
        print("Lagosta")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Frutos do Mar'))
    def alm(self):
        print("Lagosta")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Frutos do Mar'))
    def aln(self):
        print("Lagosta")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Frutos do Mar'))
    def alo(self):
        print("Lagosta")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Frutos do Mar'))
    def alp(self):
        print("Lagosta")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Frutos do Mar'))
    def alq(self):
        print("Lagosta")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Frutos do Mar'))
    def alr(self):
        print("Lagosta")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Frutos do Mar'))
    def als(self):
        print("Lagosta")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Frutos do Mar'))
    def alt(self):
        print("Lagostim")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Frutos do Mar'))
    def alu(self):
        print("Lagostim")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Frutos do Mar'))
    def alv(self):
        print("Lagostim")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Frutos do Mar'))
    def alx(self):
        print("Lagostim")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def aly(self):
        print("Lagostim")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Frutos do Mar'))
    def alz(self):
        print("Lagostim")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Frutos do Mar'))
    def ama(self):
        print("Lagostim")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Frutos do Mar'))
    def amb(self):
        print("Lagostim")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Frutos do Mar'))
    def amc(self):
        print("Lagostim")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Frutos do Mar'))
    def amd(self):
        print("Lagostim")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Frutos do Mar'))
    def ame(self):
        print("Lagostim")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Frutos do Mar'))
    def amf(self):
        print("Lagostim")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Frutos do Mar'))
    def amg(self):
        print("Lagostim")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Massas'))
    def amh(self):
        print("Lasanha")

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Massas'))
    def ami(self):
        print("Lasanha")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def amj(self):
        print("Lentilha")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def amk(self):
        print("Lentilha")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Pratos'))
    def aml(self):
        print("Lentilha")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Pratos'))
    def amm(self):
        print("Lentilha")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Carne de Boi'))
    def amn(self):
        print("Língua")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Carne de Boi'))
    def amo(self):
        print("Língua")

    @Rule(Fact(estilo='Special/Premium Bitter'), Fact(tpcomida='Carne de Boi'))
    def amp(self):
        print("Língua")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Frutos do Mar'))
    def amq(self):
        print("Lula Frita")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Frutos do Mar'))
    def amr(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Frutos do Mar'))
    def ams(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Frutos do Mar'))
    def amt(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def amu(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Frutos do Mar'))
    def amv(self):
        print("Lula Frita")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def amx(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Frutos do Mar'))
    def amy(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Frutos do Mar'))
    def amz(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Frutos do Mar'))
    def ana(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Frutos do Mar'))
    def anb(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Frutos do Mar'))
    def anc(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Frutos do Mar'))
    def andz(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Frutos do Mar'))
    def ane(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Frutos do Mar'))
    def anf(self):
        print("Lula Frita")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Pratos'))
    def ang(self):
        print("Lula Recheada")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def anh(self):
        print("Lula Recheada")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def ani(self):
        print("Lula Recheada")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Pratos'))
    def anj(self):
        print("Lula Recheada")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Massas'))
    def ank(self):
        print("Massa à Bolonhesa")

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Massas'))
    def anl(self):
        print("Massa à Bolonhesa")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Massas'))
    def anm(self):
        print("Massa ao Molho Bechamel ou Carbonara")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Massas'))
    def ann(self):
        print("Massa ao Molho Bechamel ou Carbonara")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Massas'))
    def ano(self):
        print("Massa ao Molho Bechamel ou Carbonara")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Massas'))
    def anp(self):
        print("Massa ao Molho de Frutos do Mar")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Massas'))
    def anq(self):
        print("Massa ao Molho de Frutos do Mar")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Massas'))
    def anr(self):
        print("Massa ao Molho de Frutos do Mar")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Massas'))
    def ans(self):
        print("Massa ao Molho de Frutos do Mar")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Massas'))
    def ant(self):
        print("Massa ao Molho de Frutos do Mar")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Massas'))
    def anu(self):
        print("Massa ao Molho Pesto")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Massas'))
    def anv(self):
        print("Massa ao Molho Pesto")

    @Rule(Fact(estilo='Berliner Weisse'), Fact(tpcomida='Frutas'))
    def anx(self):
        print("Melão")

    @Rule(Fact(estilo='Fruit Beer'), Fact(tpcomida='Frutas'))
    def any(self):
        print("Melão")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Frutas'))
    def anz(self):
        print("Melão")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Frutas'))
    def aoa(self):
        print("Melão")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Frutos do Mar'))
    def aob(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Frutos do Mar'))
    def aoc(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def aod(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Frutos do Mar'))
    def aoe(self):
        print("Mexilhões")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Frutos do Mar'))
    def aof(self):
        print("Mexilhões")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def aog(self):
        print("Mexilhões")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Frutos do Mar'))
    def aoh(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Frutos do Mar'))
    def aoi(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Frutos do Mar'))
    def aoj(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Lambic - Gueuze'), Fact(tpcomida='Frutos do Mar'))
    def aok(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Frutos do Mar'))
    def aol(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Frutos do Mar'))
    def aom(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Frutos do Mar'))
    def aon(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Frutos do Mar'))
    def aoo(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Frutos do Mar'))
    def aop(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Frutos do Mar'))
    def aoq(self):
        print("Mexilhões")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Aperitivo'))
    def aor(self):
        print("Milho Cozido")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Aperitivo'))
    def aos(self):
        print("Milho Cozido")

    @Rule(Fact(estilo='Weizen'), Fact(tpcomida='Aperitivo'))
    def aot(self):
        print("Milho Cozido")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Aperitivo'))
    def aou(self):
        print("Milho Cozido")

    @Rule(Fact(estilo='Helles'), Fact(tpcomida='Aperitivo'))
    def aov(self):
        print("Milho Cozido")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Mexicana'))
    def aox(self):
        print("Nachos")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Mexicana'))
    def aoy(self):
        print("Nachos")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Mexicana'))
    def aoz(self):
        print("Nachos")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Mexicana'))
    def apa(self):
        print("Nachos")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Mexicana'))
    def apb(self):
        print("Nachos")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Mexicana'))
    def apc(self):
        print("Nachos")

    @Rule(Fact(estilo='Marzen'), Fact(tpcomida='Mexicana'))
    def apd(self):
        print("Nachos")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Aperitivo'))
    def ape(self):
        print("Nozes")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Aperitivo'))
    def apf(self):
        print("Nozes")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Aperitivo'))
    def apg(self):
        print("Nozes")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Pratos'))
    def aph(self):
        print("Ossobuco")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Pratos'))
    def api(self):
        print("Ossobuco")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def apj(self):
        print("Ossobuco")

    @Rule(Fact(estilo='Strong Scotch Ale'), Fact(tpcomida='Pratos'))
    def apk(self):
        print("Ossobuco")

    @Rule(Fact(estilo='Barley Wine'), Fact(tpcomida='Frutos do Mar'))
    def apl(self):
        print("Ostras")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Frutos do Mar'))
    def apm(self):
        print("Ostras")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Frutos do Mar'))
    def apn(self):
        print("Ostras")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def apo(self):
        print("Ostras")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Frutos do Mar'))
    def app(self):
        print("Ostras")

    @Rule(Fact(estilo='Flanders Red Ale'), Fact(tpcomida='Frutos do Mar'))
    def apq(self):
        print("Ostras")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Frutos do Mar'))
    def apr(self):
        print("Ostras")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Frutos do Mar'))
    def aps(self):
        print("Ostras")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Frutos do Mar'))
    def apt(self):
        print("Ostras")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Frutos do Mar'))
    def apu(self):
        print("Ostras")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Frutos do Mar'))
    def apv(self):
        print("Ostras")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Frutos do Mar'))
    def apx(self):
        print("Ostras")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Frutos do Mar'))
    def apy(self):
        print("Ostras")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Frutos do Mar'))
    def apz(self):
        print("Ostras")

    @Rule(Fact(estilo='German Dunkelweizen'), Fact(tpcomida='Pratos'))
    def aqa(self):
        print("Ovos com Bacon")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def aqb(self):
        print("Ovos com Bacon")

    @Rule(Fact(estilo='German Roggenbier'), Fact(tpcomida='Pratos'))
    def aqc(self):
        print("Ovos com Bacon")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def aqd(self):
        print("Ovos com Bacon")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Pratos'))
    def aqe(self):
        print("Ovos com Bacon")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Pratos'))
    def aqf(self):
        print("Ovos mexidos ou Omeletes")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def aqg(self):
        print("Ovos mexidos ou Omeletes")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def aqh(self):
        print("Ovos mexidos ou Omeletes")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Pratos'))
    def aqi(self):
        print("Ovos mexidos ou Omeletes")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Pratos'))
    def aqj(self):
        print("Ovos mexidos ou Omeletes")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Pratos'))
    def aqk(self):
        print("Ovos mexidos ou Omeletes")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Pratos'))
    def aql(self):
        print("Paella")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Pratos'))
    def aqm(self):
        print("Paella")

    @Rule(Fact(estilo='Maibock/Helles Bock'), Fact(tpcomida='Pratos'))
    def aqn(self):
        print("Paella")

    @Rule(Fact(estilo='Special/Premium Bitter'), Fact(tpcomida='Pratos'))
    def aqo(self):
        print("Paella")

    @Rule(Fact(estilo='Barley Wine'), Fact(tpcomida='Sobremesa'))
    def aqp(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Fruit Beer'), Fact(tpcomida='Sobremesa'))
    def aqq(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def aqr(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Oatmeal Stout'), Fact(tpcomida='Sobremesa'))
    def aqs(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def aqt(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def aqu(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Strong Scotch Ale'), Fact(tpcomida='Sobremesa'))
    def aqv(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def aqx(self):
        print("Panna Cotta")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne Outras'))
    def aqy(self):
        print("Pato Assado")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne de Aves'))
    def aqz(self):
        print("Pato Assado")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne de Aves'))
    def ara(self):
        print("Pato Assado")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Carne de Aves'))
    def arb(self):
        print("Pato Assado")

    @Rule(Fact(estilo='German Dunkelweizen'), Fact(tpcomida='Carne de Aves'))
    def arc(self):
        print("Pato Assado")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Carne de Aves'))
    def ard(self):
        print("Pato Assado")

    @Rule(Fact(estilo='German Roggenbier'), Fact(tpcomida='Carne de Aves	'))
    def are(self):
        print("Pato Assado")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Carne de Aves'))
    def arf(self):
        print("Pato Assado")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Pratos'))
    def arg(self):
        print("Pato au Poivre")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Pratos'))
    def arh(self):
        print("Pato au Poivre")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Pratos'))
    def ari(self):
        print("Pato au Poivre")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Pratos'))
    def arj(self):
        print("Pato com Laranja")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def ark(self):
        print("Pato com Laranja")

    @Rule(Fact(estilo='Fruit Beer'), Fact(tpcomida='Pratos'))
    def arl(self):
        print("Pato com Laranja")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Pratos'))
    def arm(self):
        print("Pato com Laranja")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Pratos'))
    def arn(self):
        print("Pato com Laranja")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Pratos'))
    def aro(self):
        print("Pato com Laranja")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne de Aves'))
    def arp(self):
        print("Perdiz")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne de Aves'))
    def arq(self):
        print("Perdiz")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne de Aves'))
    def arr(self):
        print("Perdiz")

    @Rule(Fact(estilo='Old Ale'), Fact(tpcomida='Carne de Aves'))
    def ars(self):
        print("Perdiz")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Carne de Aves'))
    def art(self):
        print("Peru")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Carne de Aves'))
    def aru(self):
        print("Peru")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Carne de Aves'))
    def arv(self):
        print("Peru")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Carne de Aves'))
    def arx(self):
        print("Peru")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Carne de Aves'))
    def ary(self):
        print("Peru")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Pratos'))
    def arz(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def asa(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Pratos'))
    def asb(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Pratos'))
    def asc(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Pratos'))
    def asd(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Pratos'))
    def ase(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='Irish Red Ale'), Fact(tpcomida='Pratos'))
    def asf(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Pratos'))
    def asg(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Pratos'))
    def ash(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Massas'))
    def asi(self):
        print("Pizza Calabresa")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Massas'))
    def asj(self):
        print("Pizza Calabresa")

    @Rule(Fact(estilo='Irish Red Ale'), Fact(tpcomida='Massas'))
    def ask(self):
        print("Pizza Calabresa")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Massas'))
    def asl(self):
        print("Pizza Calabresa")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Massas'))
    def asm(self):
        print("Pizza Calabresa")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Massas'))
    def asn(self):
        print("Pizza de Banana e Brigadeiro")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Massas'))
    def aso(self):
        print("Pizza de Banana e Brigadeiro")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Massas'))
    def asp(self):
        print("Pizza de Banana e Brigadeiro")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Massas'))
    def asq(self):
        print("Pizza de Banana e Brigadeiro")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Massas'))
    def asr(self):
        print("Pizza de Banana e Brigadeiro")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Massas'))
    def ass(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Massas'))
    def ast(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Massas'))
    def asu(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Massas'))
    def asv(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Massas'))
    def asx(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Massas'))
    def asy(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Massas'))
    def asz(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Massas'))
    def ata(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Massas'))
    def atb(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Frutos do Mar'))
    def atc(self):
        print("Polvo")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Frutos do Mar'))
    def atd(self):
        print("Polvo")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Frutos do Mar'))
    def ate(self):
        print("Polvo")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Frutos do Mar'))
    def atf(self):
        print("Polvo")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Frutos do Mar'))
    def atg(self):
        print("Polvo")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Saladas'))
    def ath(self):
        print("Preparações Salgadas com sabor pronunciado de Bacon")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Saladas'))
    def ati(self):
        print("Preparações Salgadas com sabor pronunciado de Bacon")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Saladas'))
    def atj(self):
        print("Preparações Salgadas com sabor pronunciado de Bacon")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Saladas'))
    def atk(self):
        print("Preparações Salgadas com sabor pronunciado de Bacon")

    @Rule(Fact(estilo='Dark American Lager'), Fact(tpcomida='Aperitivo'))
    def atl(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Aperitivo'))
    def atm(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Aperitivo'))
    def atn(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Aperitivo'))
    def ato(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Aperitivo'))
    def atp(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='German Weizenbock'), Fact(tpcomida='Aperitivo'))
    def atq(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='Maibock/Helles Bock'), Fact(tpcomida='Aperitivo'))
    def atr(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Aperitivo'))
    def ats(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='Schwarzbier'), Fact(tpcomida='Aperitivo'))
    def att(self):
        print("Presunto Crú")

    @Rule(Fact(estilo='American Wheat/Rye'), Fact(tpcomida='Salgado'))
    def atu(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Salgado'))
    def atv(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Salgado'))
    def atx(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Salgado'))
    def aty(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Salgado'))
    def atz(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Salgado'))
    def aua(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Salgado'))
    def aub(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Pratos'))
    def auc(self):
        print("Rabada")

    @Rule(Fact(estilo='Barley Wine'), Fact(tpcomida='Pratos'))
    def aud(self):
        print("Rabada")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Pratos'))
    def aue(self):
        print("Rabada")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Pratos'))
    def auf(self):
        print("Rabada")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def aug(self):
        print("Rabada")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def auh(self):
        print("Rabada")

    @Rule(Fact(estilo='Old Ale'), Fact(tpcomida='Pratos'))
    def aui(self):
        print("Rabada")

    @Rule(Fact(estilo='Strong Scotch Ale'), Fact(tpcomida='Pratos'))
    def auj(self):
        print("Rabada")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Pratos'))
    def auk(self):
        print("Risoto de Abobrinha")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Pratos'))
    def aul(self):
        print("Risoto de Abobrinha")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Pratos'))
    def aum(self):
        print("Risoto de Abobrinha")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Pratos'))
    def aun(self):
        print("Risoto de Frutos do Mar")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def auo(self):
        print("Risoto de Frutos do Mar")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def aup(self):
        print("Risoto de Frutos do Mar")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Pratos'))
    def auq(self):
        print("Risoto de Frutos do Mar")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Pratos'))
    def aur(self):
        print("Risoto de Frutos do Mar")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Pratos'))
    def aus(self):
        print("Risoto de Funghi")

    @Rule(Fact(estilo='Vienna Lager'), Fact(tpcomida='Pratos'))
    def aut(self):
        print("Risoto de Funghi")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def auu(self):
        print("Risoto de Gorgonzola")

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Pratos'))
    def auv(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Pratos'))
    def aux(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='American Pale Ale'), Fact(tpcomida='Pratos'))
    def auy(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def auz(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='Irish Red Ale'), Fact(tpcomida='Pratos'))
    def ava(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Pratos'))
    def avb(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Pratos'))
    def avc(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Pratos'))
    def avd(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='Special/Premium Bitter'), Fact(tpcomida='Pratos'))
    def ave(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Saladas'))
    def avf(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Saladas'))
    def avg(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Saladas'))
    def avh(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Saladas'))
    def avi(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Saladas'))
    def avj(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Saladas'))
    def avk(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Saladas'))
    def avl(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Saladas'))
    def avm(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Saladas'))
    def avn(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Saladas'))
    def avo(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Saladas'))
    def avp(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Saladas'))
    def avq(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Aperitivo'))
    def avr(self):
        print("Salame")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Aperitivo'))
    def avs(self):
        print("Salame")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Aperitivo'))
    def avt(self):
        print("Salame")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Aperitivo'))
    def avu(self):
        print("Salame")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Aperitivo'))
    def avv(self):
        print("Salame")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Aperitivo'))
    def avx(self):
        print("Salame")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Aperitivo'))
    def avy(self):
        print("Salame")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Aperitivo'))
    def avz(self):
        print("Salame")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Aperitivo'))
    def axa(self):
        print("Salame")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Aperitivo'))
    def axb(self):
        print("Salame")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Aperitivo'))
    def axc(self):
        print("Salame")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Aperitivo'))
    def axd(self):
        print("Salame")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Aperitivo'))
    def axe(self):
        print("Salame")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Aperitivo'))
    def axf(self):
        print("Salame")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Aperitivo'))
    def axg(self):
        print("Salame")

    @Rule(Fact(estilo='American Wheat/Rye'), Fact(tpcomida='Peixe'))
    def axh(self):
        print("Salmão")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Peixe'))
    def axi(self):
        print("Salmão")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Peixe'))
    def axj(self):
        print("Salmão")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Peixe'))
    def axk(self):
        print("Salmão")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Peixe'))
    def axl(self):
        print("Salmão")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Peixe'))
    def axm(self):
        print("Salmão")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Peixe'))
    def axn(self):
        print("Salmão")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Peixe'))
    def axo(self):
        print("Salmão")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Peixe'))
    def axp(self):
        print("Salmão")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Peixe'))
    def axq(self):
        print("Salmão")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Peixe'))
    def axr(self):
        print("Salmão")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Peixe'))
    def axs(self):
        print("Salmão")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Peixe'))
    def axt(self):
        print("Salmão")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Peixe'))
    def axu(self):
        print("Salmão")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Peixe'))
    def axv(self):
        print("Salmão")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Pratos'))
    def axx(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Pratos'))
    def axy(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Pratos'))
    def axz(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='German Dunkelweizen'), Fact(tpcomida='Pratos'))
    def aya(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def ayb(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Pratos'))
    def ayc(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='German Roggenbier'), Fact(tpcomida='Pratos'))
    def ayd(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def aye(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Pratos'))
    def ayf(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Lambic - Gueuze'), Fact(tpcomida='Pratos'))
    def ayg(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Pratos'))
    def ayh(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Pratos'))
    def ayi(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Pratos'))
    def ayj(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Pratos'))
    def ayk(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Pratos'))
    def ayl(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Pratos'))
    def aym(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Pratos'))
    def ayn(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Pratos'))
    def ayo(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo='Altbier'), Fact(tpcomida='Aperitivo'))
    def ayp(self):
        print("Salsichas")

    @Rule(Fact(estilo='Belgian Pale Ale'), Fact(tpcomida='Aperitivo'))
    def ayq(self):
        print("Salsichas")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Aperitivo'))
    def ayr(self):
        print("Salsichas")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Aperitivo'))
    def ays(self):
        print("Salsichas")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Aperitivo'))
    def ayt(self):
        print("Salsichas")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Aperitivo'))
    def ayu(self):
        print("Salsichas")

    @Rule(Fact(estilo='Special/Premium Bitter'), Fact(tpcomida='Aperitivo'))
    def ayv(self):
        print("Salsichas")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Aperitivo'))
    def ayx(self):
        print("Sardinha")

    @Rule(Fact(estilo='Flanders Red Ale'), Fact(tpcomida='Aperitivo'))
    def ayy(self):
        print("Sardinha")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Aperitivo'))
    def ayz(self):
        print("Sardinha")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Aperitivo'))
    def aza(self):
        print("Sardinha")

    @Rule(Fact(estilo='Lambic - Gueuze'), Fact(tpcomida='Aperitivo'))
    def azb(self):
        print("Sardinha")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Aperitivo'))
    def azc(self):
        print("Sardinha")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Aperitivo'))
    def azd(self):
        print("Sardinha")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Aperitivo'))
    def aze(self):
        print("Sardinha")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Aperitivo'))
    def azf(self):
        print("Sardinha")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Pratos'))
    def azg(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Pratos'))
    def azh(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Pratos'))
    def azi(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Pratos'))
    def azj(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Pratos'))
    def azk(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Pratos'))
    def azl(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Pratos'))
    def azm(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Pratos'))
    def azn(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Pratos'))
    def azo(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Pratos'))
    def azp(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Pratos'))
    def azq(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Pratos'))
    def azr(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Pratos'))
    def azs(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Pratos'))
    def azt(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Pratos'))
    def azu(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def azv(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Pratos'))
    def azx(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def azy(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Pratos'))
    def azz(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Pratos'))
    def baa(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Pratos'))
    def bab(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Munich Helles'), Fact(tpcomida='Pratos'))
    def bac(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Pratos'))
    def bad(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Pratos'))
    def bae(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Pratos'))
    def baf(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Pratos'))
    def bag(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo='Lite American Lager'), Fact(tpcomida='Pratos'))
    def bah(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Bohemian Pilsener'), Fact(tpcomida='Pratos'))
    def bai(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Classic American Pilsner'), Fact(tpcomida='Pratos'))
    def baj(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Cream Ale'), Fact(tpcomida='Pratos'))
    def bak(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='German Pilsner'), Fact(tpcomida='Pratos'))
    def bal(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Japanese Rice Lager'), Fact(tpcomida='Pratos'))
    def bam(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Premium American Lager'), Fact(tpcomida='Pratos'))
    def ban(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Sem álcool'), Fact(tpcomida='Pratos'))
    def bao(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Standard American Lager'), Fact(tpcomida='Pratos'))
    def bap(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='Vienna Lager'), Fact(tpcomida='Pratos'))
    def baq(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Sobremesa'))
    def bar(self):
        print("Sorvete")

    @Rule(Fact(estilo='Fruit Beer'), Fact(tpcomida='Sobremesa'))
    def bas(self):
        print("Sorvete")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bat(self):
        print("Sorvete")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bau(self):
        print("Sorvete")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bav(self):
        print("Sorvete")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bax(self):
        print("Sorvete")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Pratos'))
    def bay(self):
        print("Soufflé de Couve Flor")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Pratos'))
    def baz(self):
        print("Soufflé de Couve Flor")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Pratos'))
    def bba(self):
        print("Soufflé de Couve Flor")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Pratos'))
    def bbb(self):
        print("Soufflé de Couve Flor")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Pratos'))
    def bbc(self):
        print("Soufflé de Couve Flor")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Pratos'))
    def bbd(self):
        print("Sushi")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def bbe(self):
        print("Sushi")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def bbf(self):
        print("Sushi")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Pratos'))
    def bbg(self):
        print("Sushi")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Pratos'))
    def bbh(self):
        print("Sushi")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Pratos'))
    def bbi(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Pratos'))
    def bbj(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def bbk(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def bbl(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def bbm(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Pratos'))
    def bbn(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='Oatmeal Stout'), Fact(tpcomida='Pratos'))
    def bbo(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='Special/Premium Bitter'), Fact(tpcomida='Pratos'))
    def bbp(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='Traditional Bock'), Fact(tpcomida='Pratos'))
    def bbq(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bbr(self):
        print("Tarte Tatin")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bbs(self):
        print("Tarte Tatin")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bbt(self):
        print("Tarte Tatin")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bbu(self):
        print("Tarte Tatin")

    @Rule(Fact(estilo='Blond Ale'), Fact(tpcomida='Pratos'))
    def bbv(self):
        print("Tempura de Vegetais ou Frutos do Mar")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def bbx(self):
        print("Tempura de Vegetais ou Frutos do Mar")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def bby(self):
        print("Tempura de Vegetais ou Frutos do Mar")

    @Rule(Fact(estilo='Kölsch'), Fact(tpcomida='Pratos'))
    def bbz(self):
        print("Tempura de Vegetais ou Frutos do Mar")

    @Rule(Fact(estilo='Witbier'), Fact(tpcomida='Pratos'))
    def bca(self):
        print("Tempura de Vegetais ou Frutos do Mar")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Pratos'))
    def bcb(self):
        print("Terrine")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Pratos'))
    def bcd(self):
        print("Terrine")

    @Rule(Fact(estilo='Belgian Dubbel'), Fact(tpcomida='Pratos'))
    def bce(self):
        print("Terrine")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Pratos'))
    def bcf(self):
        print("Terrine")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Pratos'))
    def bcg(self):
        print("Terrine")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Sobremesa'))
    def bch(self):
        print("Tiramisu")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bci(self):
        print("Tiramisu")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bcj(self):
        print("Tiramisu")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bck(self):
        print("Tiramisu")

    @Rule(Fact(estilo='Amber Lager'), Fact(tpcomida='Salgado'))
    def bcl(self):
        print("Torta de Cebola")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Salgado'))
    def bcm(self):
        print("Torta de Cebola")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Salgado'))
    def bcn(self):
        print("Torta de Cebola")

    @Rule(Fact(estilo='Oktoberfest/Marzen'), Fact(tpcomida='Salgado'))
    def bco(self):
        print("Torta de Cebola")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Sobremesa'))
    def bcp(self):
        print("Torta de Framboesa")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bcq(self):
        print("Torta de Framboesa")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bcr(self):
        print("Torta de Framboesa")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bcs(self):
        print("Torta de Framboesa")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bct(self):
        print("Torta de Framboesa")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Sobremesa'))
    def bcu(self):
        print("Torta de Frutas")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bcv(self):
        print("Torta de Frutas")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bcx(self):
        print("Torta de Frutas")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bcy(self):
        print("Torta de Frutas")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bcz(self):
        print("Torta de Frutas")

    @Rule(Fact(estilo='Barley Wine'), Fact(tpcomida='Sobremesa'))
    def bda(self):
        print("Torta de Limão")

    @Rule(Fact(estilo='Berliner Weisse'), Fact(tpcomida='Sobremesa'))
    def bdb(self):
        print("Torta de Limão")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bdc(self):
        print("Torta de Limão")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bdd(self):
        print("Torta de Limão")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bde(self):
        print("Torta de Maçã")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bdf(self):
        print("Torta de Maçã")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bdg(self):
        print("Torta de Maçã")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bdh(self):
        print("Torta de Maçã")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Sobremesa'))
    def bdi(self):
        print("Torta de Morangos")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bdj(self):
        print("Torta de Morangos")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bdk(self):
        print("Torta de Morangos")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bdl(self):
        print("Torta de Morangos")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bdm(self):
        print("Torta de Morangos")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Sobremesa'))
    def bdn(self):
        print("Torta de Noz Pecan")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bdo(self):
        print("Torta de Noz Pecan")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def bdp(self):
        print("Torta de Noz Pecan")

    @Rule(Fact(estilo='Russian Imperial Stout'), Fact(tpcomida='Sobremesa'))
    def bdq(self):
        print("Torta de Noz Pecan")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bdr(self):
        print("Torta de Noz Pecan")

    @Rule(Fact(estilo='Dortmunder Export'), Fact(tpcomida='Salgado'))
    def bds(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo='Dry Stout'), Fact(tpcomida='Salgado'))
    def bdt(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Salgado'))
    def bdu(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo='Foreign Extra Stout'), Fact(tpcomida='Salgado'))
    def bdv(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Salgado'))
    def bdx(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Salgado'))
    def bdy(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo='Special/Premium Bitter'), Fact(tpcomida='Salgado'))
    def bdz(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Sobremesa'))
    def bea(self):
        print("Trufa (cogumelo)")

    @Rule(Fact(estilo='Biere de Garde'), Fact(tpcomida='Sobremesa'))
    def beb(self):
        print("Trufa (cogumelo)")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Sobremesa'))
    def bec(self):
        print("Trufa (cogumelo)")

    @Rule(Fact(estilo='American Stout'), Fact(tpcomida='Sobremesa'))
    def bed(self):
        print("Trufa de Chocolate")

    @Rule(Fact(estilo='Fruit Beer'), Fact(tpcomida='Sobremesa'))
    def bee(self):
        print("Trufa de Chocolate")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Sobremesa'))
    def bef(self):
        print("Trufa de Chocolate")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Sobremesa'))
    def beg(self):
        print("Trufa de Chocolate")

    @Rule(Fact(estilo='Russian Imperial Stout	Sobremesa'))
    def beh(self):
        print("Trufa de Chocolate")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Sobremesa'))
    def bei(self):
        print("Trufa de Chocolate")

    @Rule(Fact(estilo='German Dunkelweizen'), Fact(tpcomida='Peixe'))
    def bej(self):
        print("Truta")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Peixe'))
    def bek(self):
        print("Truta")

    @Rule(Fact(estilo='German Roggenbier'), Fact(tpcomida='Peixe'))
    def bel(self):
        print("Truta")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Peixe'))
    def bem(self):
        print("Truta")

    @Rule(Fact(estilo='German Weizenbock'), Fact(tpcomida='Peixe'))
    def ben(self):
        print("Truta")

    @Rule(Fact(estilo='Other Smoked Beer'), Fact(tpcomida='Peixe'))
    def beo(self):
        print("Truta Defumada")

    @Rule(Fact(estilo='Rauchbier'), Fact(tpcomida='Peixe'))
    def bep(self):
        print("Truta Defumada")

    @Rule(Fact(estilo='American Brown Ale'), Fact(tpcomida='Carne Outras'))
    def beq(self):
        print("Veado")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne Outras'))
    def ber(self):
        print("Veado")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Carne Outras'))
    def bes(self):
        print("Veado")

    @Rule(Fact(estilo='English Brown Ale'), Fact(tpcomida='Carne Outras'))
    def bet(self):
        print("Veado")

    @Rule(Fact(estilo='Malzbier'), Fact(tpcomida='Carne Outras'))
    def beu(self):
        print("Veado")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Carne Outras'))
    def bev(self):
        print("Veado")

    @Rule(Fact(estilo='Old Ale'), Fact(tpcomida='Carne Outras'))
    def bex(self):
        print("Veado")

    @Rule(Fact(estilo='Porter'), Fact(tpcomida='Carne Outras'))
    def bey(self):
        print("Veado")

    @Rule(Fact(estilo='Sweet Stout'), Fact(tpcomida='Carne Outras'))
    def bez(self):
        print("Veado")

    @Rule(Fact(estilo='Belgian Tripel'), Fact(tpcomida='Aperitivo'))
    def bfa(self):
        print("Vegetais Crus em Palitos")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Aperitivo'))
    def bfb(self):
        print("Vegetais Crus em Palitos")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Aperitivo'))
    def bfc(self):
        print("Vegetais Crus em Palitos")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Aperitivo'))
    def bfd(self):
        print("Vegetais Crus em Palitos")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def bfe(self):
        print("Vichyssoise")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Pratos'))
    def bff(self):
        print("Vichyssoise")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Pratos'))
    def bfg(self):
        print("Vichyssoise")

    @Rule(Fact(estilo='Belgian Golden Strong Ale'), Fact(tpcomida='Aperitivo'))
    def bfh(self):
        print("Vitela")

    @Rule(Fact(estilo='German Dunkelweizen'), Fact(tpcomida='Aperitivo'))
    def bfi(self):
        print("Vitela")

    @Rule(Fact(estilo='German Kristallweizen'), Fact(tpcomida='Aperitivo'))
    def bfj(self):
        print("Vitela")

    @Rule(Fact(estilo='German Roggenbier'), Fact(tpcomida='Aperitivo'))
    def bfk(self):
        print("Vitela")

    @Rule(Fact(estilo='German Weizen'), Fact(tpcomida='Aperitivo'))
    def bfl(self):
        print("Vitela")

    @Rule(Fact(estilo='Maibock/Helles Bock'), Fact(tpcomida='Aperitivo'))
    def bfm(self):
        print("Vitela")

    @Rule(Fact(estilo='Munich Dunkel'), Fact(tpcomida='Aperitivo'))
    def bfn(self):
        print("Vitela")

    @Rule(Fact(estilo='Saison'), Fact(tpcomida='Aperitivo'))
    def bfo(self):
        print("Vitela")


engine = harmonizacao()
engine.reset()
engine.declare(Fact(estilo='Amber Lager'))
engine.declare(Fact(tpcomida='Mexicana'))
engine.run()