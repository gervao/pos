from random import choice
from pyknow import *

class Obj:
    def __init__(self):
        self.estilo = 'Amber Lager'
        self.tpcomida = 'Mexicana'
obj = Obj()

class Harmonizacao(KnowledgeEngine):
    @Rule(Fact(estilo=L('Amber Lager') | L('American Pale Ale') | L('India Pale Ale (IPA)')), Fact(tpcomida='Mexicana'))
    def a(self):
        print("Abacate (Guacamole ou Salada)")

    @Rule(Fact(estilo=L('American Brown Ale') | L('American Pale Ale')), Fact(tpcomida='Aperitivo'))
    def d(self):
        print("Amêndoas Salgadas")

    @Rule(Fact(estilo=L('Bohemian Pilsener') | L('Cream Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Peixe'))
    def f(self):
        print("Anchovas")

    @Rule(Fact(estilo=L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def n(self):
        print("Appfelstrudel")

    @Rule(Fact(estilo=L('Berliner Weisse') | L('Flanders Brown Ale/Oud Bruin') | L('Flanders Red Ale') | L('Lambic - Gueuze')), Fact(tpcomida='Frutos do Mar'))
    def r(self):
        print("Arenque (Peixe gorduroso)")

    Rule(Fact(estilo=L('American Pale Ale') | L('Saison')), Fact(tpcomida='Frutos do Mar'))
    def v(self):
        print("Atum (massas ou sanduíches)")

    @Rule(Fact(estilo=L('German Kristallweizen') | L('German Weizen') | L('Witbier')), Fact(tpcomida='Frutos do Mar'))
    def y(self):
        print("Atum (salada verde ou cru)")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Pratos'))
    def ab(self):
        print("au poivre guarnecido com batatas au gratinado")

    @Rule(Fact(estilo=L('Belgian Tripel') | L('Biere de Garde') | L('Maibock/Helles Bock')), Fact(tpcomida='Carne de Aves'))
    def ac(self):
        print("Avestruz")

    @Rule(Fact(estilo=L('Belgian Dubbel') | L('Belgian Tripel') | L('Biere de Garde')), Fact(tpcomida='Aperitivo'))
    def af(self):
        print("Azeitonas")

    @Rule(Fact(estilo=L('American Amber Ale') | L('American Brown Ale') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Sem álcool') | L('Special/Premium Bitter') | L('Standard American Lager')), Fact(tpcomida='Peixe'))
    def ai(self):
        print("Bacalhau")

    @Rule(Fact(estilo=L('German Kristallweizen') | L('German Weizen') |L('German Weizenbock') | L('Porter') | L('Russian Imperial Stout')), Fact(tpcomida='Sobremesa'))
    def au(self):
        print("Banana (base para sobremesas)")

    @Rule(Fact(estilo=L('Doppelbock') | L('Munich Dunkel') | L('Oktoberfest/Marzen')), Fact(tpcomida='Pratos'))
    def aaa(self):
        print("Batatas Gratinadas")

    @Rule(Fact(estilo=L('Belgian Blond Ale') | L('Doppelbock') | L('German Kristallweizen') | L('German Weizen') | L('Witbier')), Fact(tpcomida='Saladas'))
    def aad(self):
        print("Beterraba (salada)")

    @Rule(Fact(estilo=L('Altbier') | L('American Amber Ale') | L('American Brown Ale') | L('Belgian Dubbel') | L('Porter')), Fact(tpcomida='Carne de Boi'))
    def aai(self):
        print("Bife Grelhado")

    @Rule(Fact(estilo=L('Blond Ale') | L('German Dunkelweizen') | L('German Kristallweizen') | L('German Roggenbier') | L('German Weizen') | L('Kölsch') | L('Lambic - Gueuze') | L('Munich Helles') | L('Witbier')), Fact(tpcomida='Aperitivo'))
    def aan(self):
        print("Bolinho de Bacalhau")

    @Rule(Fact(estilo=L('Porter') | L('Russian Imperial Stout')), Fact(tpcomida='Sobremesa'))
    def aax(self):
        print("Brownies")

    @Rule(Fact(estilo=L('Altbier') | L('American Brown Ale') | L('American Pale Ale') | L('Irish Red Ale')), Fact(tpcomida='Mexicana'))
    def aaz(self):
        print("Burritos")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('Dortmunder Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('German Kristallweizen') | L('German Pilsner') | L('German Weizen') | L('Japanese Rice Lager') | L('American Lager') | L('Munich Helles') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Frutos do Mar'))
    def abd(self):
        print("Camarão")

    @Rule(Fact(estilo=L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('Kristallweizen') | L('German Pilsner') | L('Weizen') | L('Lite American Lager') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Frutos do Mar'))
    def abp(self):
        print("Caranguejo")

    @Rule(Fact(estilo=L('Altbier') | L('American Brown Ale') | L('American Pale Ale') | L('Extra Special Bitter/English Pale Ale') | L('India Pale Ale (IPA)') | L ('Red Ale')), Fact(tpcomida='Carne de Boi'))
    def acf(self):
        print("Carne Assada")

    @Rule(Fact(estilo=L('American Pale Ale') | L('Dry Stout') | L('Foreign Extra Stout') | L('India Pale Ale (IPA)')), Fact(tpcomida='Pratos'))
    def acl(self):
        print("Carne com Chili")

    @Rule(Fact(estilo=L('Dark Strong Ale') | L('Dortmunder Export') | L('Foreign Extra Stout') | L('Porter')), Fact(tpcomida='Pratos'))
    def acp(self):
        print("Carne de Panela em Cubos")

    @Rule(Fact(estilo=L('Altbier') | L('Belgian Dubbel') | L('Biere de Garde') | L('Doppelbock') | L('Munich Dunkel') | L('Oktoberfest/Marzen')), Fact(tpcomida='Carne Suína'))
    def act(self):
        print("Carne Suína Assada")

    @Rule(Fact(estilo=L('American Pale Ale') | L('Belgian Pale Ale') | L('Extra Special Bitter/English Pale Ale') | L('German Weizenbock') | L('Irish Red Ale')), Fact(tpcomida='Aperitivo'))
    def ada(self):
        print("Carpaccio")

    @Rule(Fact(estilo=L('Belgian Dubbel') | L('Biere de Garde') | L('Doppelbock')), Fact(tpcomida='Pratos'))
    def adg(self):
        print("Cassoulet")

    @Rule(Fact(estilo=L('Ale') | L('Japanese Rice Lager') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Pratos'))
    def adj(self):
        print("Caviar")

    @Rule(Fact(estilo=L('American Wheat/Rye') | L('Blond Ale') | L('German Kristallweizen') | L('German Weizen') | L('Kölsch') | L('Witbier')), Fact(tpcomida='Saladas'))
    def adn(self):
        print("Ceasar Salad")

    @Rule(Fact(estilo=L('Beer') | L('Porter') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def adt(self):
        print("Cheesecake")

    @Rule(Fact(estilo=L('Fruit Beer') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def adx(self):
        print("Chocolate")

    @Rule(Fact(estilo=L('American Pale Ale') | L('India Pale Ale (IPA)') | L('Saison')), Fact(tpcomida='Aperitivo'))
    def aec(self):
        print("Chouriço")

    @Rule(Fact(estilo=L('Belgian Pale Ale') | L('Biere de Garde') | L('Doppelbock') | L('German Weizenbock') | L('Munich Dunkel') | L('Oktoberfest/Marzen')), Fact(tpcomida='Aperitivo'))
    def aeg(self):
        print("Chucrute (conserva de repolho)")

    @Rule(Fact(estilo=L('Belgian Pale Ale') | L('Belgian Tripel') | L('Biere de Garde') | L('Premium Bitter')), Fact(tpcomida='Carne de Aves'))
    def aem(self):
        print("Codorna")

    @Rule(Fact(estilo=L('Belgian Tripel') | L('Extra Special Bitter/English Pale Ale')), Fact(tpcomida='Carne Outras'))
    def aeq(self):
        print("Coelho")

    @Rule(Fact(estilo=L('Belgian Dubbel') | L('Doppelbock') | L('English Brown Ale') | L('Munich Dunkel') | L('Strong Scotch Ale')), Fact(tpcomida='Aperitivo'))
    def aes(self):
        print("Cogumelos (Champignon, Shiitake, Maitake, Porto Bello, Shimeji Preto, Shimeji Branco)")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Belgian Dubbel') | L('Biere de Garde') | L('Old Ale') | L('Strong Scotch Ale')), Fact(tpcomida='Carne Outras'))
    def aey(self):
        print("Cordeiro Assado")

    @Rule(Fact(estilo=L('Amber Ale') | L('Dark American Lager') | L('Oatmeal Stout') | L('Schwarzbier')), Fact(tpcomida='Carne Outras'))
    def afd(self):
        print("Cordeiro Grelhado")

    @Rule(Fact(estilo=L('Other Smoked Beer') | L('auchbier')), Fact(tpcomida='Carne Suína'))
    def afh(self):
        print("Costelinha Suína com Barbecue")

    @Rule(Fact(estilo=L('American Stout') | L('Barley Wine') | L('Doppelbock') | L('Fruit Beer') | L('Old Ale') | L('Porter') | L('Russian Imperial Stout')), Fact(tpcomida='Pratos'))
    def afj(self):
        print("Crème Brulée")

    @Rule(Fact(estilo=L('American Pale Ale') | L('Belgian Golden Strong Ale') | L('German Kristallweizen') | L('German Weizen') | L('Helles')), Fact(tpcomida='Pratos'))
    def afq(self):
        print("Cuscuz")

    @Rule(Fact(estilo=L('American Pale Ale') | L('Cream Ale') | L('German Pilsner') | L('India Pale Ale (IPA)') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Aperitivo'))
    def afv(self):
        print("Empanadas")

    @Rule(Fact(estilo=L('American Pale Ale') | L('Doppelbock') | L('India Pale Ale (IPA)') | L('Dortmunder Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('Irish Red Ale') | L('Oktoberfest/Marzen') | L('Other Smoked Beer') | L('Rauchbier')), Fact(tpcomida='Mexicana'))
    def agg(self):
        print("Enchiladas (Tortilhas)")

    @Rule(Fact(estilo=L('German Kristallweizen') | L('German Weizen') | L('Other Smoked Beer') | L('Rauchbier')), Fact(tpcomida='Peixe'))
    def agq(self):
        print("Enguia Defumada")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Belgian Tripel') | L('Pilsener') | L('German Pilsner') | L('Lite American Lager') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Pratos'))
    def agu(self):
        print("Escargot")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Belgian Dubbel') | L('Biere de Garde') | L('Extra Special Bitter/English Pale Ale') | L('Old Ale')), Fact(tpcomida='Carne de Aves'))
    def ahe(self):
        print("Faisão")

    @Rule(Fact(estilo=L('American Brown Ale') | L('Wine') | L('Doppelbock') | L('Dry Stout') | L('English Brown Ale') | L('Foreign Extra Stout') | L('Stout')), Fact(tpcomida='Pratos'))
    def ahj(self):
        print("Feijão/ Feijoada")

    @Rule(Fact(estilo='Belgian Dark Strong Ale'), Fact(tpcomida='Carne de Boi'))
    def ahq(self):
        print("Fígado")

    @Rule(Fact(estilo='India Pale Ale (IPA)'), Fact(tpcomida='Carne de Boi'))
    def ahr(self):
        print("Filet Mignon")

    @Rule(Fact(estilo=L('Barley Wine') | L('Belgian Dark Strong Ale') | L('Doppelbock') | L('Flanders Brown Ale/Oud Bruin') | L('Flanders Red Ale') | L('Lambic - Fruit') | L('Strong Scotch Ale')), Fact(tpcomida='Sobremesa'))
    def ahs(self):
        print("Foie Gras")

    @Rule(Fact(estilo=L('Biere de Garde') | L('Maibock/Helles Bock') | L('Munich Dunkel') | L('Oktoberfest/Marzen')), Fact(tpcomida='Pratos'))
    def aia(self):
        print("Fondue de Queijo")

    @Rule(Fact(estilo=L('Altbier') | L('American Amber Ale') | L('American Brown Ale')), Fact(tpcomida='Carne de Aves'))
    def aie(self):
        print("Frango a Passarinho")

    @Rule(Fact(estilo=L('Belgian Dubbel') | L('Biere de Garde')), Fact(tpcomida='Pratos'))
    def aih(self):
        print("Frango ao Vinho")

    @Rule(Fact(estilo=L('Standard Bitter') | L('American Amber Ale') | L('American Brown Ale') | L('American Pale Ale') | L('Belgian Dubbel') | L('Belgian Pale Ale') | L('Biere de Garde') | L('Irish Red Ale') | L('Munich Dunkel') | L('Oktoberfest/Marzen') | L('Traditional Bock')), Fact(tpcomida='Carne de Aves'))
    def aij(self):
        print("Frango Assado")

    @Rule(Fact(estilo=L('Other Smoked Beer') | L('Porter') | L('Rauchbier') | L('Amber Lager') | L('American Brown Ale')), Fact(tpcomida='Carne de Aves'))
    def aiu(self):
        print("Frango na Brasa (churrasco)")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Doppelbock') | L('English Brown Ale') | L('Munich Dunkel') | L('Porter')), Fact(tpcomida='Pratos'))
    def aja(self):
        print("Goulash")

    @Rule(Fact(estilo=L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Pilsner') | L('India Pale Ale (IPA)') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Aperitivo'))
    def ajf(self):
        print("Grão de Bico (bolinhos/ Falafel)")

    @Rule(Fact(estilo=L('German Dunkelweizen') | L('German Kristallweizen') | L('German Roggenbier') | L('German Weizen') | L('Other Smoked Beer') | L('Rauchbier')), Fact(tpcomida='Pratos'))
    def ajq(self):
        print("Haddock Assado")

    @Rule(Fact(estilo=L('Altbier') | L('Amber Lager') | L('American Brown Ale') | L('American Pale Ale') | L('Dark American Lager') | L('India Pale Ale (IPA)') | L('Schwarzbier')), Fact(tpcomida='Lanches'))
    def ajx(self):
        print("Hamburger")

    @Rule(Fact(estilo=L('Belgian Pale Ale') | L('English Brown Ale') | L('German Kristallweizen') | L('German Weizen') | L('Munich Dunkel') | L('Oktoberfest/Marzen') | L('Traditional Bock')), Fact(tpcomida='Aperitivo'))
    def ake(self):
        print("Hummus (Patê de Grão de Bico)")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Doppelbock') | L('Munich Dunkel') | L('Other Smoked Beer') | L('Porter') | L('Rauchbier') | L('Strong Scotch Ale')), Fact(tpcomida='Carne Outras'))
    def akl(self):
        print("Javali")

    @Rule(Fact(estilo=L('American Amber Ale') | L('American Brown Ale') | L('Dark American Lager') | L('Dortmunder Export') | L('Dry Stout') | L('English Brown Ale') | L('Extra Special Bitter/English Pale Ale') | L('Foreign Extra Stout') | L('Other Smoked Beer') | L('Rauchbier') | L('Schwarzbier')), Fact(tpcomida='Pratos'))
    def aks(self):
        print("Kebab de Carne")

    @Rule(Fact(estilo=L('Bohemian Pilsener') | L('Cream Ale') | L('Dortmunder Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('German Kristallweizen') | L('German Pilsner') | L('German Weizen') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Munich Helles') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Frutos do Mar'))
    def ale(self):
        print("Lagosta")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Bohemian Pilsener') | L('Cream Ale') | L('German Kristallweizen') | L('German Pilsner') | L('German Weizen') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Munich Helles') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Frutos do Mar'))
    def alt(self):
        print("Lagostim")

    @Rule(Fact(estilo=L('Amber Lager') | L('Belgian Pale Ale')), Fact(tpcomida='Massas'))
    def amh(self):
        print("Lasanha")

    @Rule(Fact(estilo=L('Doppelbock') | L('English Brown Ale') | L('Munich Dunkel') | L('Oktoberfest/Marzen')), Fact(tpcomida='Pratos'))
    def amj(self):
        print("Lentilha")

    @Rule(Fact(estilo=L('English Brown Ale') | L('Munich Dunkel') | L('Special/Premium Bitter')), Fact(tpcomida='Carne de Boi'))
    def amn(self):
        print("Língua")


    @Rule(Fact(estilo=L('Amber Lager') | L('American Pale Ale') | L('Blond Ale') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Kölsch') | L('Lite American Lager') | L('Munich Helles') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Frutos do Mar'))
    def amq(self):
        print("Lula Frita")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('German Kristallweizen') | L('German Weizen') | L('Witbier')), Fact(tpcomida='Pratos'))
    def ang(self):
        print("Lula Recheada")

    @Rule(Fact(estilo=L('Amber Lager') | L('Belgian Pale Ale')), Fact(tpcomida='Massas'))
    def ank(self):
        print("Massa à Bolonhesa")

    @Rule(Fact(estilo=L('Belgian Tripel') | L('Biere de Garde') | L('Doppelbock')), Fact(tpcomida='Massas'))
    def anm(self):
        print("Massa ao Molho Bechamel ou Carbonara")

    @Rule(Fact(estilo=L('Blond Ale') | L('German Kristallweizen') | L('German Weizen') | L('Kölsch') | L('Munich Helles')), Fact(tpcomida='Massas'))
    def anp(self):
        print("Massa ao Molho de Frutos do Mar")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Belgian Tripel')), Fact(tpcomida='Massas'))
    def anu(self):
        print("Massa ao Molho Pesto")

    @Rule(Fact(estilo=L('Berliner Weisse') | L('Fruit Beer') | L('German Kristallweizen') | L('German Weizen')), Fact(tpcomida='Frutas'))
    def anx(self):
        print("Melão")

    @Rule(Fact(estilo=L('Blond Ale') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Kristallweizen') | L('German Pilsner') | L('German Weizen') | L('Japanese Rice Lager') | L('Kölsch') | L('Lambic - Gueuze') | L('Lite American Lager') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Frutos do Mar'))
    def aob(self):
        print("Mexilhões")

    @Rule(Fact(estilo=L('Blond Ale') | L('German Kristallweizen') | L('Weizen') | L('Kölsch') | L('Helles')), Fact(tpcomida='Aperitivo'))
    def aor(self):
        print("Milho Cozido")

    @Rule(Fact(estilo=L('Amber Lager') | L('American Pale Ale') | L('Dortmunder Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('India Pale Ale (IPA)') | L('Marzen')), Fact(tpcomida='Mexicana'))
    def aox(self):
        print("Nachos")

    @Rule(Fact(estilo=L('Belgian Dubbel') | L('Doppelbock') | L('English Brown Ale')), Fact(tpcomida='Aperitivo'))
    def ape(self):
        print("Nozes")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Belgian Dubbel') | L('Doppelbock') | L('Strong Scotch Ale')), Fact(tpcomida='Pratos'))
    def aph(self):
        print("Ossobuco")

    @Rule(Fact(estilo=L('Barley Wine') | L('Blond Ale') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('Flanders Red Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Kölsch') | L('Lite American Lager') | L('Munich Helles') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Frutos do Mar'))
    def apl(self):
        print("Ostras")

    @Rule(Fact(estilo=L('German Dunkelweizen') | L('German Kristallweizen') | L('German Roggenbier') | L('German Weizen') | L('Witbier')), Fact(tpcomida='Pratos'))
    def aqa(self):
        print("Ovos com Bacon")

    @Rule(Fact(estilo=L('Blond Ale') | L('German Kristallweizen') | L('German Weizen') | L('Kölsch') | L('Munich Helles') | L('Witbier')), Fact(tpcomida='Pratos'))
    def aqf(self):
        print("Ovos mexidos ou Omeletes")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Biere de Garde') | L('Maibock/Helles Bock') | L('Special/Premium Bitter')), Fact(tpcomida='Pratos'))
    def aql(self):
        print("Paella")

    @Rule(Fact(estilo=L('Barley Wine') | L('Fruit Beer') | L('Malzbier') | L('Oatmeal Stout') | L('Porter') | L('Russian Imperial Stout') | L('Strong Scotch Ale') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def aqp(self):
        print("Panna Cotta")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Belgian Dubbel') | L('Biere de Garde') | L('Doppelbock') | L('German Dunkelweizen') | L('German Kristallweizen') | L('German Roggenbier') | L('German Weizen')), Fact(tpcomida='Carne Outras'))
    def aqy(self):
        print("Pato Assado")

    @Rule(Fact(estilo=L('American Pale Ale') | L('India Pale Ale (IPA)') | L('Saison')), Fact(tpcomida='Pratos'))
    def arg(self):
        print("Pato au Poivre")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Doppelbock') | L('Fruit Beer') | L('Malzbier') | L('Porter') | L('Sweet Stout')), Fact(tpcomida='Pratos'))
    def arj(self):
        print("Pato com Laranja")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Belgian Dubbel') | L('Biere de Garde') | L('Old Ale')), Fact(tpcomida='Carne de Aves'))
    def arp(self):
        print("Perdiz")

    @Rule(Fact(estilo=L('Amber Lager') | L('Belgian Dubbel') | L('Biere de Garde') | L('Munich Dunkel') | L('Oktoberfest/Marzen')), Fact(tpcomida='Carne de Aves'))
    def art(self):
        print("Peru")

    @Rule(Fact(estilo=L('American Pale Ale') | L('Doppelbock') | L('Dortmunder Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('India Pale Ale (IPA)') | L('Irish Red Ale') | L('Other Smoked Beer') | L('Rauchbier')), Fact(tpcomida='Pratos'))
    def arz(self):
        print("Pimentão Recheado")

    @Rule(Fact(estilo=L('American Pale Ale') | L('India Pale Ale (IPA)') | L('Irish Red Ale') | L('Other Smoked Beer') | L('Rauchbier')), Fact(tpcomida='Massas'))
    def asi(self):
        print("Pizza Calabresa")

    @Rule(Fact(estilo=L('American Stout') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Massas'))
    def asn(self):
        print("Pizza de Banana e Brigadeiro")

    @Rule(Fact(estilo=L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Massas'))
    def ass(self):
        print("Pizza Mussarela/Marguerita")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Belgian Tripel') | L('German Kristallweizen') | L('German Weizen') | L('Witbier')), Fact(tpcomida='Frutos do Mar'))
    def atc(self):
        print("Polvo")

    @Rule(Fact(estilo=L('Belgian Dubbel') | L('Doppelbock') | L('Other Smoked Beer') | L('Rauchbier')), Fact(tpcomida='Saladas'))
    def ath(self):
        print("Preparações Salgadas com sabor pronunciado de Bacon")

    @Rule(Fact(estilo=L('Dark American Lager') | L('Doppelbock') | L('Dortmunder Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('German Weizenbock') | L('Maibock/Helles Bock') | L('Porter') | L('Schwarzbier')), Fact(tpcomida='Aperitivo'))
    def atl(self):
        print("Presunto Crú")

    @Rule(Fact(estilo=L('American Wheat/Rye') | L('Blond Ale') | L('German Kristallweizen') | L('German Weizen') | L('Kölsch') | L('Munich Helles') | L('Witbier')), Fact(tpcomida='Salgado'))
    def atu(self):
        print("Quiche de Queijo")

    @Rule(Fact(estilo=L('American Brown Ale') | L('Barley Wine') | L('Belgian Dark Strong Ale') | L('Belgian Dubbel') | L('Doppelbock') | L('English Brown Ale') | L('Old Ale') | L('Strong Scotch Ale')), Fact(tpcomida='Pratos'))
    def auc(self):
        print("Rabada")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Belgian Tripel') | L('Biere de Garde')), Fact(tpcomida='Pratos'))
    def auk(self):
        print("Risoto de Abobrinha")

    @Rule(Fact(estilo=L('Blond Ale') | L('German Kristallweizen') | L('German Weizen') | L('Kölsch') | L('Munich Helles')), Fact(tpcomida='Pratos'))
    def aun(self):
        print("Risoto de Frutos do Mar")

    @Rule(Fact(estilo=L('Biere de Garde') | L('Vienna Lager')), Fact(tpcomida='Pratos'))
    def aus(self):
        print("Risoto de Funghi")

    @Rule(Fact(estilo='Doppelbock'), Fact(tpcomida='Pratos'))
    def auu(self):
        print("Risoto de Gorgonzola")

    @Rule(Fact(estilo=L('Altbier') | L('American Brown Ale') | L('American Pale Ale') | L('English Brown Ale') | L('Irish Red Ale') | L('Munich Dunkel') | L('Oktoberfest/Marzen') | L('Porter') | L('Special/Premium Bitter')), Fact(tpcomida='Pratos'))
    def auv(self):
        print("Rocambole de Carne")

    @Rule(Fact(estilo=L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Kristallweizen') | L('German Pilsner') | L('German Weizen') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Saladas'))
    def avf(self):
        print("Salada de Folhas Verdes")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('Belgian Tripel') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('Dortmunder Export') | L('Dry Stout') | L('Foreign Extra Stout') | L('German Pilsner') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Aperitivo'))
    def avr(self):
        print("Salame")

    @Rule(Fact(estilo=L('American Wheat/Rye') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Kristallweizen') | L('German Pilsner') | L('German Weizen') | L('India Pale Ale (IPA)') | L('Japanese Rice Lager') | L('Lite American Lager') | L('Premium American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Peixe'))
    def axh(self):
        print("Salmão")

    @Rule(Fact(estilo=L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Dunkelweizen') | L('German Kristallweizen') | L('German Pilsner') | L('German Roggenbier') | L('German Weizen') | L('Japanese Rice Lager') | L('Lambic - Gueuze') | L('Lite American Lager') | L('Other Smoked Beer') | L('Premium American Lager') | L('Rauchbier') | L('Saison') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Pratos'))
    def axx(self):
        print("Salmão Defumado")

    @Rule(Fact(estilo=L('Altbier') | L('Belgian Pale Ale') | L('Biere de Garde') | L('Munich Dunkel') | L('Oktoberfest/Marzen') | L('Saison') | L('Special/Premium Bitter')), Fact(tpcomida='Aperitivo'))
    def ayp(self):
        print("Salsichas")

    @Rule(Fact(estilo=L('Cream Ale') | L('Flanders Red Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Lambic - Gueuze') | L('Lite American Lager') | L('Saison') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Aperitivo'))
    def ayx(self):
        print("Sardinha")

    @Rule(Fact(estilo=L('Blond Ale') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Kölsch') | L('Lite American Lager') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager')), Fact(tpcomida='Pratos'))
    def azg(self):
        print("Sopa (caldo de Piranha)")

    @Rule(Fact(estilo=L('Blond Ale') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Kristallweizen') | L('German Pilsner') | L('German Weizen') | L('Japanese Rice Lager') | L('Kölsch') | L('Lite American Lager') | L('Munich Helles') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager') | L('Witbier')), Fact(tpcomida='Pratos'))
    def azr(self):
        print("Sopa de Legumes")

    @Rule(Fact(estilo=L('Lite American Lager') | L('Bohemian Pilsener') | L('Classic American Pilsner') | L('Cream Ale') | L('German Pilsner') | L('Japanese Rice Lager') | L('Premium American Lager') | L('Sem álcool') | L('Standard American Lager') | L('Vienna Lager')), Fact(tpcomida='Pratos'))
    def bah(self):
        print("Sopa Minestrone")

    @Rule(Fact(estilo=L('American Stout') | L('Fruit Beer') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bar(self):
        print("Sorvete")

    @Rule(Fact(estilo=L('American Stout') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Pratos'))
    def bay(self):
        print("Soufflé de Couve Flor")

    @Rule(Fact(estilo=L('Blond Ale') | L('German Kristallweizen') | L('German Weizen') | L('Kölsch') | L('Witbier')), Fact(tpcomida='Pratos'))
    def bbd(self):
        print("Sushi")

    @Rule(Fact(estilo=L('American Brown Ale') | L('Belgian Dubbel') | L('English Brown Ale') | L('German Kristallweizen') | L('German Weizen') | L('Munich Dunkel') | L('Oatmeal Stout') | L('Special/Premium Bitter') | L('Traditional Bock')), Fact(tpcomida='Pratos'))
    def bbi(self):
        print("Tamboril (peixe)")

    @Rule(Fact(estilo=L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bbr(self):
        print("Tarte Tatin")

    @Rule(Fact(estilo=L('Blond Ale') | L('German Kristallweizen') | L('German Weizen') | L('Kölsch') | L('Witbier')), Fact(tpcomida='Pratos'))
    def bbv(self):
        print("Tempura de Vegetais ou Frutos do Mar")

    @Rule(Fact(estilo=L('American Brown Ale') | L('Belgian Dark Strong Ale') | L('Belgian Dubbel') | L('Biere de Garde') | L('English Brown Ale')), Fact(tpcomida='Pratos'))
    def bcb(self):
        print("Terrine")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Malzbier') | L('Porter') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bch(self):
        print("Tiramisu")

    @Rule(Fact(estilo=L('Amber Lager') | L('Biere de Garde') | L('Munich Dunkel') | L('Oktoberfest/Marzen')), Fact(tpcomida='Salgado'))
    def bcl(self):
        print("Torta de Cebola")

    @Rule(Fact(estilo=L('American Stout') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bcp(self):
        print("Torta de Framboesa")

    @Rule(Fact(estilo=L('American Stout') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bcu(self):
        print("Torta de Frutas")

    @Rule(Fact(estilo=L('Barley Wine') | L('Berliner Weisse') | L('Porter') | L('Russian Imperial Stout')), Fact(tpcomida='Sobremesa'))
    def bda(self):
        print("Torta de Limão")

    @Rule(Fact(estilo=L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bde(self):
        print("Torta de Maçã")

    @Rule(Fact(estilo=L('American Stout') | L('Malzbier') | L("Porter") | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bdi(self):
        print("Torta de Morangos")

    @Rule(Fact(estilo=L('American Stout') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bdn(self):
        print("Torta de Noz Pecan")

    @Rule(Fact(estilo=L('Dortmunder Export') | L('Dry Stout') | L('English Brown Ale') | L('Foreign Extra Stout') | L('Munich Dunkel') | L('Porter') | L('Special/Premium Bitter')), Fact(tpcomida='Salgado'))
    def bds(self):
        print("Torta Madalena (carne moída com purê de batatas gratinado)")

    @Rule(Fact(estilo=L('Belgian Dark Strong Ale') | L('Biere de Garde') | L('Doppelbock')), Fact(tpcomida='Sobremesa'))
    def bea(self):
        print("Trufa (cogumelo)")

    @Rule(Fact(estilo=L('American Stout') | L('Fruit Beer') | L('Malzbier') | L('Porter') | L('Russian Imperial Stout') | L('Sweet Stout')), Fact(tpcomida='Sobremesa'))
    def bed(self):
        print("Trufa de Chocolate")

    @Rule(Fact(estilo=L('German Dunkelweizen') | L('German Kristallweizen') | L('German Roggenbier') | L('German Weizen') | L('German Weizenbock')), Fact(tpcomida='Peixe'))
    def bej(self):
        print("Truta")

    @Rule(Fact(estilo=L('Other Smoked Beer') | L('Rauchbier')), Fact(tpcomida='Peixe'))
    def beo(self):
        print("Truta Defumada")

    @Rule(Fact(estilo=L('American Brown Ale') | L('Belgian Dark Strong Ale') | L('Doppelbock') | L('English Brown Ale') | L('Malzbier') | L('Munich Dunkel') | L('Old Ale') | L('Porter') | L('Sweet Stout')), Fact(tpcomida='Carne Outras'))
    def beq(self):
        print("Veado")

    @Rule(Fact(estilo=L('Belgian Tripel') | L('German Kristallweizen') | L('German Weizen') | L('Munich Dunkel')), Fact(tpcomida='Aperitivo'))
    def bfa(self):
        print("Vegetais Crus em Palitos")

    @Rule(Fact(estilo=L('Doppelbock') | L('German Kristallweizen') | L('German Weizen')), Fact(tpcomida='Pratos'))
    def bfe(self):
        print("Vichyssoise")

    @Rule(Fact(estilo=L('Belgian Golden Strong Ale') | L('German Dunkelweizen') | L('German Kristallweizen') | L('German Roggenbier') | L('German Weizen') | L('Maibock/Helles Bock') | L('Munich Dunkel') | L('Saison')), Fact(tpcomida='Aperitivo'))
    def bfh(self):
        print("Vitela")


engine = Harmonizacao()
engine.reset()
engine.declare(Fact(estilo=obj.estilo))
engine.declare(Fact(tpcomida=obj.tpcomida))
engine.run()