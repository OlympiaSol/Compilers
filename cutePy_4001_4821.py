# Name:Christina Olympia Soldatou  AM:4001  Username:cs04001
# Name:Aikaterini Tsitsimikli      AM:4821  Username:cs04821

#################################### S X O L I A ################################################
# Exoume ylopoihsei plhrws ton teliko kwdika.
# Otan kanoume "run" ton kwdika paragontai ta arxeia: OutputFile, file_with_quads.int kai finalFile.asm.
# Sas paradidoyme 5 arxeia eisodou ta opoia einai ta ekshs:
# countdigits.cpy, factorial.cpy, fibonacci.cpy, primes.cpy kai to arxeio paradeigmata_mazi.cpy poy periexei
# ola ta programmata mazi.
# To trexoume sta ypologistika systhmata tou Tmhmatos me thn entolh:
#                        python3 cutePy_4001_4821.py (arxeio eisodoy.cpy)
#################################################################################################

import sys
import os

file = open('fibonacci.cpy', 'r', encoding='utf8')

# KATASTASEIS
start = 0  # start
dig = 1  # arithmoi
idk = 2  # grammata/psifia
asgn = 3  # anathesh ison =
smaller = 4  # mikrotero apo
larger = 5  # megalytero apo
hashtag_rem = 6  # hashtag
sxolia = 7  # anoigoun sxolia #$
kleisimo_sxoliwn = 8  # kleinoun sxolia #$
divide = 9  # diairesi //
exclamation = 10  # thavmastiko

# XARAKTHRES
gramma = 0  # a,b,...,z, A,B,...,Z
arithmos = 1  # 0,1,...,9
prosthesi = 2  # +
afairesi = 3  # -
pollaplasiasmos = 4  # *
diairesi = 5  # //
aristeri_parenthesi = 6  # (
deksia_parenthesi = 7  # )
aristeri_agkili = 8  # [
deksia_agkili = 9  # ]
aristero_agkistro = 10  # {
deksi_agkistro = 11  # }
erwtimatiko = 12  # ;
komma = 13  # ,
eisagwgika = 14  # "
anw_katw_teleia = 15  # :
katw_paula = 16  # _
mikrotero = 17  # <
megalytero = 18  # >
ison = 19  # =
hashtag = 20  # #
dolario = 21  # $
tab = 22  # \t
keno = 23  # space
epomeni_grammi = 24  # return
End_of_File = 25  # EoF
mi_apodekto_symbolo = 26
thaumastiko = 27  # !

# Tokens
gramma_token = 50  # a,b,...,z, A,B,...,Z
arithmos_token = 51  # 0,1,...,9
prosthesi_token = 52  # +
afairesi_token = 53  # -
pollaplasiasmos_token = 54  # *
diairesi_token = 55  # //
aristeri_parenthesi_token = 56  # (
deksia_parenthesi_token = 57  # )
aristeri_agkili_token = 58  # [
deksia_agkili_token = 59  # ]
anoigma_block_token = 60  # #{
kleisimo_block_token = 61  # #}
erwtimatiko_token = 62  # ;
komma_token = 63  # ,
eisagwgika_token = 64  # "
anwkatw_teleia_token = 65  # :
mikrotero_token = 66  # <
megalytero_token = 67  # >
mikrotero_iso_token = 68  # <=
megalytero_iso_token = 69  # >=
equal_token = 70  # ==
diaforo_token = 71  # !=
anathesi_token = 72  # =
End_of_File_token = 73  # ''
hashtag_token = 74  # #

# Tokens Desmeumenwn Leksewn
def_token = 500  # function
declare_token = 501  # declare
if_token = 502  # if
else_token = 503  # else
while_token = 504  # while
return_token = 505  # return
and_token = 506  # and
or_token = 507  # or
not_token = 508  # not
input_token = 509  # input
print_token = 510  # print
int_token = 511  # int
name_token = 512  # name
main_token = 513  # main

# Arxikopoihsh ERRORS
Error_Arithmos_Gramma = -1
Error_Ektos_Oriwn = -2
Error_Mono_Ena_Hashtag = -3
Error_Eof_Anoigma_Comment = -4
Error_Mono_Aristero_Agkistro = -5
Error_Mono_Deksi_Agkistro = -6
Error_Mono_Ena_Slash = -7
Error_Mono_Ena_Dollar = -8
Error_Plus_30_Xaraktires = -9
Error_Katw_Paula_Prin_Identifier = -10
Error_Lathos_Symbolo = -11
Error_Mono_Ena_Thaumastiko = -12

# Metavaseis
array = [
    # START - start
    [idk, dig, prosthesi_token, afairesi_token, pollaplasiasmos_token, divide,
     aristeri_parenthesi_token, deksia_parenthesi_token, aristeri_agkili_token, deksia_agkili_token,
     Error_Mono_Aristero_Agkistro, Error_Mono_Deksi_Agkistro, erwtimatiko_token, komma_token,
     eisagwgika_token, anwkatw_teleia_token, idk, smaller, larger, asgn, hashtag_rem, Error_Mono_Ena_Dollar,
     start, start, start, End_of_File_token, Error_Lathos_Symbolo, exclamation],

    # ARITHMOS - dig
    [Error_Arithmos_Gramma, dig, arithmos_token, arithmos_token, arithmos_token, arithmos_token,
     arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token,
     arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token,
     arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token, arithmos_token,
     Error_Lathos_Symbolo, arithmos_token],

    # GRAMMA - idk
    [idk, idk, gramma_token, gramma_token, gramma_token, gramma_token, gramma_token, gramma_token,
     gramma_token, gramma_token, gramma_token, gramma_token, gramma_token, gramma_token, gramma_token,
     gramma_token, idk, gramma_token, gramma_token, gramma_token, gramma_token,
     gramma_token, gramma_token, gramma_token, gramma_token, gramma_token, Error_Lathos_Symbolo, gramma_token],

    # ANATHESI - asgn
    [anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token,
     anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token,
     anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token,
     equal_token,
     anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token, anathesi_token,
     Error_Lathos_Symbolo, anathesi_token],

    # MIKROTERO APO - smaller
    [mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token,
     mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token,
     mikrotero_token,
     mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token,
     mikrotero_iso_token,
     mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token, mikrotero_token,
     Error_Lathos_Symbolo, mikrotero_token],

    # MEGALYTERO APO - larger
    [megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_token,
     megalytero_token,
     megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_token,
     megalytero_token,
     megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_iso_token,
     megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_token, megalytero_token,
     Error_Lathos_Symbolo, megalytero_token],

    # HASHTAG - hashtag_rem
    [idk, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag,
     Error_Mono_Ena_Hashtag,
     Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag,
     anoigma_block_token, kleisimo_block_token,
     Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag,
     Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag,
     Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, sxolia, Error_Mono_Ena_Hashtag,
     Error_Mono_Ena_Hashtag,
     Error_Mono_Ena_Hashtag, Error_Mono_Ena_Hashtag, Error_Lathos_Symbolo, Error_Mono_Ena_Hashtag],

    # SXOLIA
    [sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia,
     sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia,
     sxolia, sxolia, sxolia, sxolia, kleisimo_sxoliwn, sxolia, sxolia,
     sxolia, sxolia, Error_Eof_Anoigma_Comment, sxolia, sxolia],

    # KLEISIMO_SXOLIWN
    [sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia,
     sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia, sxolia,
     sxolia, sxolia, sxolia, sxolia, kleisimo_sxoliwn, start, sxolia,
     sxolia, sxolia, Error_Eof_Anoigma_Comment, sxolia, sxolia],

    # DIAIRESI - divide
    [Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash,
     diairesi_token,
     Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash,
     Error_Mono_Ena_Slash,
     Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash,
     Error_Mono_Ena_Slash,
     Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Mono_Ena_Slash,
     Error_Mono_Ena_Slash,
     Error_Mono_Ena_Slash, Error_Mono_Ena_Slash, Error_Lathos_Symbolo, Error_Mono_Ena_Slash],

    # THAVMASTIKO - exclamation
    [Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko,
     diaforo_token,
     Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko, Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko,
     Error_Mono_Ena_Thaumastiko, Error_Lathos_Symbolo, Error_Mono_Ena_Thaumastiko]
]

grammi = 1


# LEKTIKOS ANALYTHS!!
def lex_analitis():
    global grammi

    mikos_leksis = ''
    katastasi = start
    output = []

    while (katastasi >= 0 and katastasi <= 10):
        xaraktiras = file.read(1)  # Theloume enan-enan xaraktira na epistrefei kai na ton elegxoume

        if (xaraktiras.isalpha()):
            id_token = gramma
        elif (xaraktiras.isdigit()):
            id_token = arithmos
        elif (xaraktiras == '+'):
            id_token = prosthesi
        elif (xaraktiras == '-'):
            id_token = afairesi
        elif (xaraktiras == '*'):
            id_token = pollaplasiasmos
        elif (xaraktiras == '/'):
            id_token = diairesi
        elif (xaraktiras == '('):
            id_token = aristeri_parenthesi
        elif (xaraktiras == ')'):
            id_token = deksia_parenthesi
        elif (xaraktiras == '['):
            id_token = aristeri_agkili
        elif (xaraktiras == ']'):
            id_token = deksia_agkili
        elif (xaraktiras == '{'):
            id_token = aristero_agkistro
        elif (xaraktiras == '}'):
            id_token = deksi_agkistro
        elif (xaraktiras == ';'):
            id_token = erwtimatiko
        elif (xaraktiras == ','):
            id_token = komma
        elif (xaraktiras == '"'):
            id_token = eisagwgika
        elif (xaraktiras == ':'):
            id_token = anw_katw_teleia
        elif (xaraktiras == '_'):
            id_token = katw_paula
        elif (xaraktiras == '<'):
            id_token = mikrotero
        elif (xaraktiras == '>'):
            id_token = megalytero
        elif (xaraktiras == '='):
            id_token = ison
        elif (xaraktiras == '#'):
            id_token = hashtag
        elif (xaraktiras == '$'):
            id_token = dolario
        elif (xaraktiras == '\t'):
            id_token = tab
        elif (xaraktiras == ' '):
            id_token = keno
        elif (xaraktiras == '\n'):
            grammi = grammi + 1
            id_token = epomeni_grammi
        elif (xaraktiras == ''):
            id_token = End_of_File
        elif (xaraktiras == '!'):
            id_token = thaumastiko
        else:
            id_token = mi_apodekto_symbolo

        katastasi = array[katastasi][id_token]

        if (len(mikos_leksis) > 30):
            katastasi = Error_Plus_30_Xaraktires
        else:
            if (katastasi != start and katastasi != sxolia and katastasi != kleisimo_sxoliwn):
                mikos_leksis = mikos_leksis + xaraktiras
            else:
                mikos_leksis = ''

    # OPISTHODROMISH
    if (katastasi == gramma_token or katastasi == arithmos_token or katastasi == megalytero_token or katastasi == mikrotero_token or katastasi == anathesi_token):
        if (xaraktiras == '\n'):
            grammi = grammi - 1
        xaraktiras = file.seek(file.tell() - 1, 0)  # Me thn tell() mas gyrizei thn thesi tou arxeiou kai me thn seek() orizoume th nea thesi
        mikos_leksis = mikos_leksis[:-1]  # Afairw ton teleutaio xaraktira

    # Klhsh synarthshs gia desmeumenes lekseis
    id_final = elegxos_gia_Desmeumenh_leksi(katastasi, mikos_leksis)
    # Klhsh synarthshs gia pithana ERRORS
    elegxos_gia_ERRORS(id_final)

    output.append(id_final)
    output.append(mikos_leksis)
    output.append(grammi)

    # print(output)
    return output


def elegxos_gia_Desmeumenh_leksi(katastasi, mikos_leksis):
    # Elegxos an to TOKEN einai desmeumeni leksi
    if (katastasi == gramma_token):
        if (mikos_leksis == 'def'):
            katastasi = def_token
        elif (mikos_leksis == '#declare'):
            katastasi = declare_token
        elif (mikos_leksis == 'if'):
            katastasi = if_token
        elif (mikos_leksis == 'else'):
            katastasi = else_token
        elif (mikos_leksis == 'while'):
            katastasi = while_token
        elif (mikos_leksis == 'not'):
            katastasi = not_token
        elif (mikos_leksis == 'and'):
            katastasi = and_token
        elif (mikos_leksis == 'or'):
            katastasi = or_token
        elif (mikos_leksis == 'return'):
            katastasi = return_token
        elif (mikos_leksis == 'int'):
            katastasi = int_token
        elif (mikos_leksis == 'input'):
            katastasi = input_token
        elif (mikos_leksis == 'print'):
            katastasi = print_token
        elif (mikos_leksis == '__name__'):
            katastasi = name_token
        elif (mikos_leksis == '__main__'):
            katastasi = main_token
        elif (mikos_leksis[0] == '_'):  # den prepei to identifier na ksekina me katw paula
            katastasi = Error_Katw_Paula_Prin_Identifier

    # elegxos gia orio arithmwn
    if (katastasi == arithmos_token):
        if (mikos_leksis.isdigit() >= pow(2, 32)):
            katastasi = Error_Ektos_Oriwn

    return katastasi


def elegxos_gia_ERRORS(katastasi):
    # ERRORS
    if (katastasi == Error_Arithmos_Gramma):
        print('ERROR: Exw arxika arithmo kai meta emfanizetai gramma !!!')
    elif (katastasi == Error_Ektos_Oriwn):
        print('ERROR: O arithmos vrisketai ektos oriwn !!!')
    elif (katastasi == Error_Mono_Ena_Hashtag):
        print('ERROR: Emfanistike mono ena hashtag (#) xwris na akolouthei kati !!!')
    elif (katastasi == Error_Eof_Anoigma_Comment):
        print('ERROR: Exw telos arxeiou (EOF) kai ta sxolia enw exoun anoiksei, den exoun kleisei !!!')
    elif (katastasi == Error_Mono_Aristero_Agkistro):
        print('ERROR: Emfanistike mono to aristero agkistro ({) xwris hashtag !!!')
    elif (katastasi == Error_Mono_Deksi_Agkistro):
        print('ERROR: Emfanistike mono to deksi agkistro (}) xwris hashtag !!!')
    elif (katastasi == Error_Mono_Ena_Slash):
        print('ERROR: Emfanistike mono ena slash (/) !!!')
    elif (katastasi == Error_Mono_Ena_Dollar):
        print('ERROR: Emfanistike mono ena dollario ($) xwris hastag !!!')
    elif (katastasi == Error_Plus_30_Xaraktires):
        print('ERROR: Emfanistikan panw apo 30 xaraktires sti leksi !!!')
    elif (katastasi == Error_Katw_Paula_Prin_Identifier):
        print('ERROR: Den epitrepetai mia leksi na ksekina me katw paula (_) !!!')
    elif (katastasi == Error_Lathos_Symbolo):
        print('ERROR: Emfanistike mh apodekto symbolo !!!')
    elif (katastasi == Error_Mono_Ena_Thaumastiko):
        print('ERROR: Emfanistike mono ena thaumastiko (!) xwris ison !!!')

    return


# ENDIAMESOS KWDIKAS !!

global all_Quads  # lista me oles tis tetrades
all_Quads = []

countquad = 1  # o arithmos pou mpainei aristera apo tin tetrada


def nextquad():  # Epistrefei ton arithmo ths epomenis tetradas pou prokeitai na paraxthei
    global countquad

    return countquad

all_QuadsFinal = []

def genquad(op, x, y, z):  # Dhmiourgei tin epomeni tetrada (op, x, y, z)
    global countquad
    global all_Quads
    global all_QuadsFinal

    quad = [nextquad(), op, x, y, z]
    all_Quads.append(quad)
    countquad = countquad + 1
    all_QuadsFinal.append(quad)

    return quad

T_i = 0
all_Temp_Var = []  # lista me oles tis proswrines metavlites 


def newtemp():  # Dhmiourgei kai epistrefei mia nea proswrini metavliti
    # oi proswrines metavlites einai tis morfhs T_1, T_2, T_3...
    global all_Temp_Var
    global T_i

    temp_Var = '%' + str(T_i + 1)  # Dhmiourgei nea proswrini metavliti me symvolo %
    all_Temp_Var.append(temp_Var)
    T_i = T_i + 1

    entity = Entity()
    entity.type = 'PROSWRINH_METAVLHTH'
    entity.name = temp_Var
    entity.ProswriniMetavliti.offset = compute_offset()
    new_entity(entity)

    return temp_Var


def emptylist():  # Dhmiourgei mia keni lista etiketwn tetradwn
    empty_List = []

    return empty_List


def makelist(x):  # Dhmiourgei mia lista etiketwn tetradwn pou periexei mono to x
    xlist = [x]

    return xlist


def merge(list1, list2):  # Dhmiourgei mia lista etiketwn tetradwn apo th synenwsh twn listwn list1, list2
    list = []
    list = list + list1 + list2

    return list


def backpatch(list,z):  # H lista list apoteleitai apo deiktes se tetrades twn opoiwn to teleutaio teloumeno den einai symplhrwmeno
    # h backpatch episkeptetai mia mia tis tetrades autes kai sumplirwnei me thn etiketa z
    global all_Quads

    for quad in all_Quads:
        if (quad[0] in list and quad[4] == '_'):
            quad[4] = z

    return


# PINAKAS SYMBOLWN !!

class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.Metavliti = self.Metavliti()
        self.Synartisi = self.Synartisi()
        self.Parametros = self.Parametros()
        self.ProswriniMetavliti = self.ProswriniMetavliti()

    class Metavliti:
        def __init__(self):
            self.offset = 0   # Apostash apo thn arxh tou eggrafhmatos drasthriopoihshs

    class Synartisi:
        def __init__(self):
            self.startQuad = 0  # Etiketa ths prwths tetradas tou kwdika ths synarthshs
            self.list_arguments = []  # Lista parametrwn
            self.framelength = 0  # Mhkos eggrafhmatos drasthriopoihshs
            self.nestingLevel = 0

    class Parametros:
        def __init__(self):
            self.offset = 0  # Apostash apo thn koryfh ths stoivas

    class ProswriniMetavliti:
        def __init__(self):
            self.offset = 0  # Apostash apo thn koryfh ths stoivas

class Scope():
    def __init__(self):
        self.name = ''
        self.list_entities = []  # Lista apo Entities
        self.nestingLevel = 0  # Vathos fwliasmatos
        self.outerScope = None

class Argument():
    def __init__(self):
        self.name = ''
        self.type = 'Int'  # Typos metavlhths


def get_scopes(file_path):  # H get_scopes pairnei tis synarthseis apo to arxeio pou exoume anoiksei kai tis vazei se mia lista
    list_of_scopes = []

    file_obj = open(file_path, "r")
    contents = file_obj.read()
    lines = contents.split("\n")
    current_scope = ""

    for line in lines:
        if line.startswith("def "):  # otan h grammi arxizei me def
            if current_scope:
                list_of_scopes.append(current_scope)
            current_scope = line
        elif current_scope and line.startswith(" "):  # otan arxizoun me opoiodhpote arithmo kenwn
            keno_paragrafou = len(line) - len(line.lstrip())
            if keno_paragrafou > len(current_scope) - len(current_scope.lstrip()):
                current_scope = current_scope + "\n" + line.strip()
        elif line.startswith("if __name__ == \"__main__\":"):  # otan kaleitai h main, dhladh otan diavazetai h sygkekrimenh grammi
            current_scope = current_scope + "\n" + line
            next_line = lines[lines.index(line) + 1]
            if next_line.startswith("    "):
                current_scope = current_scope + "\n" + next_line

    # prosthetw to teleutaio scope
    if current_scope:
        list_of_scopes.append(current_scope)

    globalScope = list_of_scopes[-1]  # to teleutaio stoixeio ths listas
    outerScope = None

    # elegxos
    if len(list_of_scopes) > 1:
        outerScope = list_of_scopes[-2]  # to proteleutaio stoixeio ths listas

    file_obj.close()
    return globalScope, outerScope

globalScope = None

def new_scope(name):  # Dhmiourgoume ena neo scope
    global globalScope

    nextScope = Scope()
    nextScope.name = name
    nextScope.outerScope = globalScope

    if (globalScope != None):
        nextScope.nestingLevel = globalScope.nestingLevel + 1
    else:
        nextScope.nestingLevel = 0

    globalScope = nextScope


def delete_scope():  # Diagrafoume thn eggrafh (record) tou Scope kai oles ts listes me ta Entity kai ta Argument pou eksartwntai apo auth
    global globalScope

    current_scope = globalScope

    while current_scope.list_entities:
        entity = current_scope.list_entities.pop()
        del entity

    globalScope = current_scope.outerScope


def new_entity(obj):  # Dhmiourgoume ena neo entity
    global globalScope

    globalScope.list_entities.append(obj)


def new_argument(obj):  # Dhmiourgoume ena neo argument
    global globalScope

    x = globalScope.list_entities[-1].Synartisi

    x.list_arguments.append(obj)


def compute_offset():   # Ypologizoume ton arithmo twn bytes
    global globalScope

    offset = 12
    if globalScope.list_entities:
        count = 0
        for entity in globalScope.list_entities:
            if (entity.type == 'METAVLHTH' or entity.type == 'PARAMETROS' or entity.type == 'PROSWRINH_METAVLHTH'):
                count = count + 1
        offset = offset + (count * 4)  # auksisi kata 4

    return offset


def compute_startQuad():  # Ypologizoyme to startQuad
    global globalScope

    x = globalScope.outerScope.list_entities[-1]

    x.Synartisi.startQuad = nextquad()


def compute_framelength():  # Ypologizoume to framelength
    global globalScope

    x = globalScope.outerScope.list_entities[-1]

    x.Synartisi.framelength = compute_offset()

def add_Parameters():  # Dhmioyrgoume Entities apo ta Arguments
    global globalScope

    x = globalScope.outerScope.list_entities[-1].Synartisi

    for argument in x.list_arguments:
        entity = Entity()
        entity.name = argument.name
        entity.type = 'PARAMETROS'
        entity.Parametros.mode = 'CV'
        entity.Parametros.offset = compute_offset()
        new_entity(entity)


def print_Symbol_table(OutputFile):  # Ektypwnoume ton pinaka symbolwn
    global globalScope

    with open(OutputFile, "a") as f:
        current_scope = globalScope
        while current_scope != None:
            f.write("-----------------------------------------------------------------------------------------------\n")
            f.write("*Scopes*\n")
            f.write("\tScope: \t" + "  Name: " + current_scope.name + "\t\tNestingLevel: " + str(current_scope.nestingLevel) + "\n")

            f.write("*Entities*\n")
            for entity in current_scope.list_entities:
                if (entity.type == 'METAVLHTH'):
                    f.write("\tEntity: " + "  Name: " + entity.name + "\t\t\tOffset: " + str(entity.Metavliti.offset) + "\n")
                elif (entity.type == 'SYNARTHSH'):
                    f.write("\tEntity: " + "  Name: " + entity.name + "\t\tStartQuad: " + str(entity.Synartisi.startQuad) +
                            "\t\tFramelength: " + str(entity.Synartisi.framelength) + "\n")
                elif (entity.type == 'PARAMETROS'):
                    f.write("\tEntity: " + "  Name: " + entity.name + "\t\t\tOffset: " + str(entity.Parametros.offset) + "\n")
                elif (entity.type == 'PROSWRINH_METAVLHTH'):
                    f.write("\tEntity: " + "  Name: " + entity.name + "\t\t\tOffset: " + str(entity.ProswriniMetavliti.offset) + "\n")

            f.write("*Arguments*\n")
            for argument in entity.Synartisi.list_arguments:
                f.write("\tArgument: " + "Name: " + argument.name + "\n")

            current_scope = current_scope.outerScope
        f.write("-----------------------------------------------------------------------------------------------\n")
        f.write("\n\n\n")

def search_entity(n):  # Anazhtoume ston pinaka simvolwn to onoma ths metavlhths pou dinetai san parametros sth gnlvcode()
    global globalScope

    current_scope = globalScope
    while current_scope != None:
        for entity in current_scope.list_entities:
            if (entity.name == n):
                return (current_scope, entity)
        current_scope = current_scope.outerScope

    print("Error: Den yparxei ston pinaka simbolon entity pou legetai " + str(n))
    exit()



#  TELIKOS KWDIKAS !!

finalFile = open('finalFile.asm', 'w')
finalFile.write("\n\n\n\n")

def gnlvcode(v):  # pairnei san orisma mia metavlhth, ths opoias thn timh h th dieuthynsh theloume na prospelasoume (opou v to onoma ths metavlhths)
    # metaferei ston t0 th dieuthynsh mias mh topikhs metavlhths
    # apo ton pinaka symbolwn vriskei posa epipeda panw vrisketai h mh topikh metavlhth kai mesa apo to syndesmo prospelashs thn entopizei
    global globalScope
    global finalFile

    scope_pin, entity_pin = search_entity(v)  # kaloume th search_entity() gia na entopisoume th metavlhth v

    finalFile.write("\tlw t0,-4(sp)\n")  # stoiva tou gonea

    n = globalScope.nestingLevel - scope_pin.nestingLevel - 1;  # opou n ta epipeda pou prepei na anevei h gnlvcode() gia na entopisei to eggrafhma drasthriopoihshs
    for i in range(n):
        finalFile.write("\tlw t0,-4(t0)\n")  # stoiva tou progonou pou exei th metavlhth

    # pairnw to offset apo ton pinaka simvolwn
    if entity_pin.type == 'METAVLHTH':
        finalFile.write("\taddi t0,t0,-%d\n" % (entity_pin.Metavliti.offset))  # dieuthinsi ths mh topikhs metavlhths
    elif entity_pin.type == 'PARAMETROS':
        finalFile.write("\taddi t0,t0,-%d\n" % (entity_pin.Parametros.offset))  # dieuthinsi ths mh topikhs metavlhths



def loadvr(v, r):  # metafora dedomenwn aton kataxwrhth r
    # h metafora mporei na ginei apo th mnhmh (stoiva) h na ekxwrhthei sto r mia stathera
    global globalScope
    global finalFile

    if v.isdigit():  # an v einai stathera
        finalFile.write("\tli t%d,%s\n" % (r, v))
    else:  # an v einai metavlhth
        scope_pin, entity_pin = search_entity(v)

        # an h v einai katholikh metavlhth, dhladh anhkei sto kyriws programma
        if scope_pin.nestingLevel == 0:  # h v anhkei sto kyriws programma ara to nestinglevel isoutai me 0
            if entity_pin.type == 'METAVLHTH':
                finalFile.write("\tlw t%d,-%d(gp)\n" % (r, entity_pin.Metavliti.offset))
            elif entity_pin.type == 'PROSWRINH_METAVLHTH':
                finalFile.write("\tlw t%d,-%d(gp)\n" % (r, entity_pin.ProswriniMetavliti.offset))

        # an h v exei dhlwthei sth synarthsh pou auth th stigmh ekteleitai kai einai topikh metavlhth, h typikh parametros poy pernaei me timh, h proswrinh metavlhth
        elif scope_pin.nestingLevel == globalScope.nestingLevel:  # nestinglevel iso me to trexon
            if entity_pin.type == 'METAVLHTH':
                finalFile.write("\tlw t%d,-%d(sp)\n" % (r, entity_pin.Metavliti.offset))
            elif entity_pin.type == 'PARAMETROS':
                finalFile.write("\tlw t%d,-%d(sp)\n" % (r, entity_pin.Parametros.offset))
            elif entity_pin.type == 'PROSWRINH_METAVLHTH':
                finalFile.write("\tlw t%d,-%d(sp)\n" % (r, entity_pin.ProswriniMetavliti.offset))

        # an h v exei dhlwthei se kapoio progono kai ekei einai topikh metavlhth, h typikh parametrow poy pernaei me timh
        elif scope_pin.nestingLevel < globalScope.nestingLevel:  # nestinglevel mikrotero apo to trexon
            if entity_pin.type == 'METAVLHTH' or entity_pin.type == 'PARAMETROS':
                gnlvcode(v)
                finalFile.write("\tlw t%d,(t0)\n" % (r))


def storerv(r, v):  # metafora dedomenwn apo ton kataxwrhth r sth mnhmh (metavlhth v)

    global globalScope
    global finalFile

    scope_pin, entity_pin = search_entity(v)

    # an h v einai katholikh metavlhth, dhladh anhkei sto kyriws programma
    if scope_pin.nestingLevel == 0:  # h v anhkei sto kyriws programma ara to nestinglevel isoutai me 0
        if entity_pin.type == 'METAVLHTH':
            finalFile.write("\tsw t%d,-%d(gp)\n" % (r, entity_pin.Metavliti.offset))
        elif entity_pin.type == 'PROSWRINH_METAVLHTH':
            finalFile.write("\tsw t%d,-%d(gp)\n" % (r, entity_pin.ProswriniMetavliti.offset))

    # an h v einai topikh metavlhth, h typikh parametros poy pernaei me timh kai vathos fwliasmatos iso me to trexon, h proswrinh metavlhth
    elif scope_pin.nestingLevel == globalScope.nestingLevel:  # nestinglevel iso me to trexon
        if entity_pin.type == 'METAVLHTH':
            finalFile.write("\tsw t%d,-%d(sp)\n" % (r, entity_pin.Metavliti.offset))
        elif entity_pin.type == 'PARAMETROS':
            finalFile.write("\tsw t%d,-%d(sp)\n" % (r, entity_pin.Parametros.offset))
        elif entity_pin.type == 'PROSWRINH_METAVLHTH':
            finalFile.write("\tsw t%d,-%d(sp)\n" % (r, entity_pin.ProswriniMetavliti.offset))

    # an h v einai topikh metavlhth, h typikh parametros poy pernaei me timh kai vathos fwliasmatos mikrotero apo to trexon
    elif scope_pin.nestingLevel < globalScope.nestingLevel:  # nestinglevel mikrotero apo to trexon
        if entity_pin.type == 'METAVLHTH' or entity_pin.type == 'PARAMETROS':
            gnlvcode(v)
            finalFile.write("\tsw t%d,(t0)\n" % (r))


i = 0  # o aukswn arithmos ths parametrou, ton arxikopoioume sto -1 prin to perasma ths prwths parametrou

def finalCode():

    global globalScope
    global all_Quads
    global finalFile
    global i


    for q in range(len(all_Quads)):
        finalFile.write("\nL" + str(all_Quads[q][0]) + ": \n")  # L (label)

        # eisodos dedomenwn
        if (all_Quads[i][1] == 'inp'):
            finalFile.write("\tli a7,5\n")
            finalFile.write("\tecall\n")
            finalFile.write("\tmv t1,a0\n")  # o akeraios tha topotheththei ston a0

        # eksodos dedomenwn
        elif (all_Quads[i][1] == 'out'):
            finalFile.write("\tli a0,44\n")  # to 44 emfanizetai sthn othoni
            finalFile.write("\tli a7,1\n")
            finalFile.write("\tecall\n")

        # termatismos programmatos
        elif (all_Quads[i][1] == 'halt'):
            finalFile.write("\tli a0,0\n")  # epistrofi timhs 0
            finalFile.write("\tli a7,93\n")
            finalFile.write("\tecall\n")

        # entoles almatwn (jump, relop)
        # jump
        elif all_Quads[q][1] == 'jump':
            finalFile.write("\tj L" + str(all_Quads[q][4]) + "\n")
        # relop
        elif all_Quads[q][1] in ['==', '!=', '>', '<', '>=', '<=']:
            loadvr(all_Quads[q][2], 1)
            loadvr(all_Quads[q][3], 2)

            if all_Quads[q][1] == '==':
                finalFile.write("\tbeq,t1,t2,L" + str(all_Quads[q][4]) + "\n")
            elif all_Quads[q][1] == '!=':
                finalFile.write("\tbne,t1,t2,L" + str(all_Quads[q][4]) + "\n")
            elif all_Quads[q][1] == '>':
                finalFile.write("\tbgt,t1,t2,L" + str(all_Quads[q][4]) + "\n")
            elif all_Quads[q][1] == '<':
                finalFile.write("\tblt,t1,t2,L" + str(all_Quads[q][4]) + "\n")
            elif all_Quads[q][1] == '>=':
                finalFile.write("\tbge,t1,t2,L" + str(all_Quads[q][4]) + "\n")
            elif all_Quads[q][1] == '<=':
                finalFile.write("\tble,t1,t2,L" + str(all_Quads[q][4]) + "\n")

        # ekxwrhsh
        elif all_Quads[q][1] == '=':
            loadvr(all_Quads[q][2], 1)
            storerv(1, all_Quads[q][4])

        # entoles arithmhtikwn praksewn
        elif all_Quads[q][1] in ['+', '-', '*', '//']:
            loadvr(all_Quads[q][2], 1)
            loadvr(all_Quads[q][3], 2)

            if all_Quads[q][1] == '+':
                finalFile.write("\tadd,t1,t1,t2\n")
            elif all_Quads[q][1] == '-':
                finalFile.write("\tsub,t1,t1,t2\n")
            elif all_Quads[q][1] == '*':
                finalFile.write("\tmul,t1,t1,t2\n")
            elif all_Quads[q][1] == '//':
                finalFile.write("\tdiv,t1,t1,t2\n")

            storerv(1, all_Quads[q][4])

        # epistrofh timhs synarthshs
        elif all_Quads[q][1] == 'retv':
            loadvr(all_Quads[q][2], 1)
            finalFile.write("\tlw t0,-8(sp)\n")
            finalFile.write("\tsw t1,(t0)\n")
            finalFile.write("\tlw ra,(sp)\n")
            finalFile.write("\tjr ra\n")

        # parametroi synarthshs
        elif all_Quads[q][1] == 'par':
            if all_Quads[q][3] == 'CV':
                loadvr(all_Quads[q][2], 0)
                finalFile.write("\tsw t0,-%d(fp)\n" % (12 + 4 * i))
                i = i + 1
            elif all_Quads[q][3] == 'RET':
                scope_pin, entity_pin = search_entity(all_Quads[q][2])
                finalFile.write("\taddi t0,sp,-%d\n" % (entity_pin.ProswriniMetavliti.offset))
                finalFile.write("\tsw t0,-8(fp)\n")

        # klhsh synarthshs
        elif all_Quads[q][1] == 'call':
            i = -1
            scope_pin, entity_pin = search_entity(all_Quads[q][2])

            # an h kalousa kai h klhtheisa synarthsh exoun to idio nestinglevel, tote exoun ton idio gonea
            if globalScope.nestingLevel == entity_pin.Synartisi.nestingLevel:
                finalFile.write("\tlw t0,-4(sp)\n")
                finalFile.write("\tsw t0,-4(fp)\n")
            # an h kalousa kai h klhtheisa synarthsh exoun diaforetiko nestinglevel, tote h kalousa einai o goneas ths klhtheisas
            elif globalScope.nestingLevel < entity_pin.Synartisi.nestingLevel:
                finalFile.write("\tsw sp,-4(fp)\n")

            finalFile.write("\taddi sp,sp,%d\n" % (entity_pin.Synartisi.framelength))  # metaferoume to deikth stoivas sthn klhtheisa
            finalFile.write("\tjal L%d\n" % (entity_pin.Synartisi.startQuad))  # kaloume th synarthsh
            finalFile.write("\taddi sp,sp,-%d\n" % (entity_pin.Synartisi.framelength))  # otan epistrepsoume pairnoume pisw to deikth stoivas sthn kalousa


        elif all_Quads[q][1] == 'begin_block':
            # mesa sthn klhtheisa sthn arxh kathe synarthshs
            if globalScope.nestingLevel != 0:
                finalFile.write("\tsw ra,(sp)\n")
            else:
                # arxh programmatos kai kyriws programma
                finalFile.seek(0,0)  # sthn arxh tou programmatos
                finalFile.write("\tj L%d\n" % (all_Quads[q][0]))  # xreiazetai ena alma pou na odhgei sthn prwth etiketa toy kyriws programmatos
                finalFile.seek(0,2)
                finalFile.write("\taddi sp,sp,%d\n" % (compute_offset()))  # katevazoume ton sp kata framelength ths main
                finalFile.write("\tmv gp,sp\n")  # na shmeiwsoume ston gp to eggrafhma drasthriopoihshs wste na exoume eukolh prosvash stis global metavlhtes

        # mesa sthn klhtheisa sto telos kathe synarthshs
        elif all_Quads[q][1] == 'end_block':
            if globalScope.nestingLevel != 0:
                finalFile.write("\tlw ra,(sp)\n")
                finalFile.write("\tjr ra\n")


    all_Quads = []  # adeiazw th lista all_Quads giati thn epomeni fora pou tha kalesoume th finalCode() prepei na einai adeia apo tetrades


# EDW KSEKINAEI O SYNTAKTIKOS ANALYTHS!!!!!!!

def syntax_analitis():
    global eksodos
    global grammi

    eksodos = lex_analitis()
    grammi = eksodos[2]

    def startRule():
        new_scope('main')

        def_main_part()
        call_main_part()

    def def_main_part():
        global eksodos

        def_main_function()
        while (eksodos[0] == def_token):
            def_main_function()

    def def_main_function():
        global grammi
        global eksodos

        if (eksodos[0] == def_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == gramma_token):
                name = eksodos[1]
                eksodos = lex_analitis()
                grammi = eksodos[2]

                if (eksodos[0] == aristeri_parenthesi_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (eksodos[0] == deksia_parenthesi_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]

                        if (eksodos[0] == anwkatw_teleia_token):
                            eksodos = lex_analitis()
                            grammi = eksodos[2]

                            if (eksodos[0] == anoigma_block_token):
                                eksodos = lex_analitis()
                                grammi = eksodos[2]

                                entity = Entity()
                                entity.type = 'SYNARTHSH'
                                entity.name = name
                                entity.Synartisi.type = 'Function'
                                entity.Synartisi.nestingLevel = globalScope.nestingLevel + 1
                                new_entity(entity)

                                new_scope(name)

                                declarations()

                                while (eksodos[0] == def_token):
                                    def_function()

                                compute_startQuad()

                                genquad('begin_block', name, '_', '_')
                                statements()

                                compute_framelength()
                                genquad('end_block', name, '_', '_')

                                print_Symbol_table("OutputFile")

                                finalCode()

                                delete_scope()

                                if (eksodos[0] == kleisimo_block_token):
                                    eksodos = lex_analitis()
                                    grammi = eksodos[2]
                                else:
                                    print('ERROR: Den emfanizetai "#}" meta ta statements.', 'Grammi:', grammi)
                                    exit(-1)
                            else:
                                print('ERROR: Den emfanizetai "#{" prin ta declarations.', 'Grammi:', grammi)
                                exit(-1)
                        else:
                            print('ERROR: Den emfanizetai ":" meta thn ")".', 'Grammi:', grammi)
                            exit(-1)
                    else:
                        print('ERROR: Den emfanizetai h ")" meta thn "(" .', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai h "(" meta apo to onoma function.', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai kapoio onoma function ths synarths.', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai h leksh "def" sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    def def_function():
        global eksodos
        global grammi

        if (eksodos[0] == def_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == gramma_token):
                name = eksodos[1]
                eksodos = lex_analitis()
                grammi = eksodos[2]

                if (eksodos[0] == aristeri_parenthesi_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    entity = Entity()
                    entity.type = 'SYNARTHSH'
                    entity.name = name
                    entity.Synartisi.type = 'Function'
                    entity.Synartisi.nestingLevel = globalScope.nestingLevel + 1  # gia TELIKO
                    new_entity(entity)

                    id_list(0)

                    if (eksodos[0] == deksia_parenthesi_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]

                        if (eksodos[0] == anwkatw_teleia_token):
                            eksodos = lex_analitis()
                            grammi = eksodos[2]

                            if (eksodos[0] == anoigma_block_token):
                                eksodos = lex_analitis()
                                grammi = eksodos[2]

                                new_scope(name)
                                add_Parameters()

                                declarations()

                                while (eksodos[0] == def_token):
                                    def_function()

                                compute_startQuad()
                                genquad('begin_block', name, '_', '_')

                                statements()
                                compute_framelength()
                                genquad('end_block', name, '_', '_')

                                print_Symbol_table("OutputFile")

                                finalCode()

                                delete_scope()

                                if (eksodos[0] == kleisimo_block_token):
                                    eksodos = lex_analitis()
                                    grammi = eksodos[2]
                                else:
                                    print('ERROR: Den emfanizetai "#}" meta ta statements.', 'Grammi:', grammi)
                                    exit(-1)
                            else:
                                print('ERROR: Den emfanizetai "#{" prin ta declarations.', 'Grammi:', grammi)
                                exit(-1)
                        else:
                            print('ERROR: Den emfanizetai ":" meta thn ")".', 'Grammi:', grammi)
                            exit(-1)
                    else:
                        print('ERROR: Den emfanizetai h ")" meta thn id_list.', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai h "(" meta apo to onoma function.', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai kapoio onoma function.', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai h leksh "def" sthn arxh ths synartisis.', 'Grammi:', grammi)
            exit(-1)

    def declarations():
        global eksodos

        while (eksodos[0] == declare_token):
            declaration_grammi()

    def declaration_grammi():
        global eksodos
        global grammi

        if (eksodos[0] == declare_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            id_list(1)

    def statement():
        global eksodos
        global grammi

        if (eksodos[0] == gramma_token or eksodos[0] == return_token or eksodos[0] == print_token):
            simple_statement()
        elif (eksodos[0] == if_token or eksodos[0] == while_token):
            structured_statement()
        else:
            print('ERROR: Den emfanizetai swsto statement.', 'Grammi:', grammi)
            exit(-1)

    def statements():
        global eksodos

        statement()
        while (eksodos[0] == gramma_token or eksodos[0] == return_token or eksodos[0] == print_token or eksodos[0] == if_token or eksodos[0] == while_token):
            statement()

    def simple_statement():
        global eksodos

        if (eksodos[0] == gramma_token):
            assignment_stat()
        elif (eksodos[0] == print_token):
            print_stat()
        elif (eksodos[0] == return_token):
            return_stat()

    def structured_statement():
        global eksodos

        if (eksodos[0] == if_token):
            if_stat()
        elif (eksodos[0] == while_token):
            while_stat()

    def assignment_stat():
        global eksodos
        global grammi

        if (eksodos[0] == gramma_token):
            myid = eksodos[1]

            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == anathesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                if (eksodos[0] == int_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    genquad('inp', myid, '_', '_')

                    if (eksodos[0] == aristeri_parenthesi_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]

                        if (eksodos[0] == input_token):
                            eksodos = lex_analitis()
                            grammi = eksodos[2]

                            if (eksodos[0] == aristeri_parenthesi_token):
                                eksodos = lex_analitis()
                                grammi = eksodos[2]

                                if (eksodos[0] == deksia_parenthesi_token):
                                    eksodos = lex_analitis()
                                    grammi = eksodos[2]

                                    if (eksodos[0] == deksia_parenthesi_token):
                                        eksodos = lex_analitis()
                                        grammi = eksodos[2]

                                        if (eksodos[0] == erwtimatiko_token):
                                            eksodos = lex_analitis()
                                            grammi = eksodos[2]
                                        else:
                                            print('ERROR: Den emfanizetai ";" meta thn teleutaia ")" .', 'Grammi:',
                                                  grammi)
                                            exit(-1)
                                    else:
                                        print('ERROR: Den emfanizetai ")" prin to ";" .', 'Grammi:', grammi)
                                        exit(-1)
                                else:
                                    print('ERROR: Den emfanizetai ")" meta thn "(" .', 'Grammi:', grammi)
                                    exit(-1)
                            else:
                                print('ERROR: Den emfanizetai "(" meta to input .', 'Grammi:', grammi)
                                exit(-1)
                        else:
                            print('ERROR: Den emfanizetai input meta thn prwth "(" .', 'Grammi:', grammi)
                            exit(-1)
                    else:
                        print('ERROR: Den emfanizetai "(" meta to int .', 'Grammi:', grammi)
                        exit(-1)
                else:
                    Eplace = expression()
                    genquad('=', Eplace, '_', myid)

                    if (eksodos[0] == erwtimatiko_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]
                    else:
                        print('ERROR: Den emfanizetai ";" meta to expression .', 'Grammi:', grammi)
                        exit(-1)
            else:
                print('ERROR: Den emfanizetai "=" meta to ID .', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai ID sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    def print_stat():
        global eksodos
        global grammi

        if (eksodos[0] == print_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == aristeri_parenthesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                Eplace = expression()
                genquad('out', Eplace, '_', '_')

                if (eksodos[0] == deksia_parenthesi_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (eksodos[0] == erwtimatiko_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]
                    else:
                        print('ERROR: Den emfanizetai ";" meta apo thn ")" .', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai ")" meta apo to expression .', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai "(" prin apo to expression .', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai print sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    def return_stat():
        global eksodos
        global grammi

        if (eksodos[0] == return_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == aristeri_parenthesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                Eplace = expression()
                genquad('retv', Eplace, '_', '_')

                if (eksodos[0] == deksia_parenthesi_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (eksodos[0] == erwtimatiko_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]
                    else:
                        print('ERROR: Den emfanizetai ";" meta apo thn ")" .', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai ")" meta apo to expression .', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai "(" prin apo to expression .', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai h leksh return sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    def if_stat():
        global eksodos
        global grammi

        if (eksodos[0] == if_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == aristeri_parenthesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                C = condition()
                backpatch(C[0], nextquad())

                if (eksodos[0] == deksia_parenthesi_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (eksodos[0] == anwkatw_teleia_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]

                        if (eksodos[0] == anoigma_block_token):
                            eksodos = lex_analitis()
                            grammi = eksodos[2]

                            statements()

                            list_if = makelist(nextquad())
                            genquad('jump', '_', '_', '_')
                            backpatch(C[1], nextquad())

                            if (eksodos[0] == kleisimo_block_token):
                                eksodos = lex_analitis()
                                grammi = eksodos[2]
                            else:
                                print('ERROR: Den emfanizetai "#}" meta ta statements.', 'Grammi:', grammi)
                                exit(-1)
                        else:
                            statement()

                            list_if = makelist(nextquad())
                            genquad('jump', '_', '_', '_')
                            backpatch(C[1], nextquad())

                        if (eksodos[0] == else_token):
                            eksodos = lex_analitis()
                            grammi = eksodos[2]

                            if (eksodos[0] == anwkatw_teleia_token):
                                eksodos = lex_analitis()
                                grammi = eksodos[2]

                                if (eksodos[0] == anoigma_block_token):
                                    eksodos = lex_analitis()
                                    grammi = eksodos[2]

                                    statements()

                                    backpatch(list_if, nextquad())

                                    if (eksodos[0] == kleisimo_block_token):
                                        eksodos = lex_analitis()
                                        grammi = eksodos[2]
                                    else:
                                        print('ERROR: Den emfanizetai "#}" meta ta statements.', 'Grammi:', grammi)
                                        exit(-1)
                                else:
                                    statement()

                                    backpatch(list_if, nextquad())

                            else:
                                print('ERROR: Den emfanizetai ":" meta to else.', 'Grammi:', grammi)
                                exit(-1)
                        else:
                            backpatch(list_if, nextquad())
                    else:
                        print('ERROR: Den emfanizetai ":" meta thn ")".', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai ")" meta to condition.', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai "(" prin to condition.', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai h leksh if sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    def while_stat():
        global eksodos
        global grammi

        if (eksodos[0] == while_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == aristeri_parenthesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                Cquad = nextquad()
                C = condition()
                backpatch(C[0], nextquad())

                if (eksodos[0] == deksia_parenthesi_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (eksodos[0] == anwkatw_teleia_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]

                        if (eksodos[0] == anoigma_block_token):
                            eksodos = lex_analitis()
                            grammi = eksodos[2]

                            statements()
                            genquad('jump', '_', '_', Cquad)
                            backpatch(C[1], nextquad())

                            if (eksodos[0] == kleisimo_block_token):
                                eksodos = lex_analitis()
                                grammi = eksodos[2]
                            else:
                                print('ERROR: Den emfanizetai "#}" meta ta statements.', 'Grammi:', grammi)
                                exit(-1)
                        else:
                            statement()
                            genquad('jump', '_', '_', Cquad)
                            backpatch(C[1], nextquad())
                    else:
                        print('ERROR: Den emfanizetai ":" meta thn ")".', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai ")" meta to condition.', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai "(" prin to condition.', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai h leksh while sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    def id_list(flag):
        global eksodos
        global grammi

        if (eksodos[0] == gramma_token):
            name = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (flag == 1):
                entity = Entity()
                entity.type = 'METAVLHTH'
                entity.name = name
                entity.Metavliti.offset = compute_offset()
                new_entity(entity)
            else:
                argument = Argument()
                argument.name = name
                argument.parMode = 'CV'
                new_argument(argument)

            while (eksodos[0] == komma_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                if (eksodos[0] == gramma_token):
                    name = eksodos[1]
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (flag == 1):
                        entity = Entity()
                        entity.type = 'METAVLHTH'
                        entity.name = name
                        entity.Metavliti.offset = compute_offset()
                        new_entity(entity)
                    else:
                        argument = Argument()
                        argument.name = name
                        argument.parMode = 'CV'
                        new_argument(argument)
                else:
                    print('ERROR: Den emfanizetai id meta apo ",".', 'Grammi:', grammi)
                    exit(-1)

    def expression():
        global eksodos
        global grammi

        optional_sign()

        T1place = term()

        while (eksodos[0] == prosthesi_token or eksodos[0] == afairesi_token):
            prosthesi_afairesi = ADD_OP()
            T2place = term()

            w = newtemp()
            genquad(prosthesi_afairesi, T1place, T2place, w)
            T1place = w

        Eplace = T1place

        return Eplace

    def term():
        global eksodos
        global grammi

        F1place = factor()

        while (eksodos[0] == pollaplasiasmos_token or eksodos[0] == diairesi_token):
            pollaplasiasmos_diairesi = MUL_OP()
            F2place = factor()

            w = newtemp()
            genquad(pollaplasiasmos_diairesi, F1place, F2place, w)
            F1place = w

        Tplace = F1place

        return Tplace

    def factor():
        global eksodos
        global grammi

        if (eksodos[0] == arithmos_token):
            Eplace = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        elif (eksodos[0] == aristeri_parenthesi_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            Eplace = expression()

            if (eksodos[0] == deksia_parenthesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

            else:
                print('ERROR: Den emfanizetai ")" meta to expression.', 'Grammi:', grammi)
                exit(-1)

        elif (eksodos[0] == gramma_token):
            fact_temp = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

            Eplace = idtail(fact_temp)

        else:
            print('ERROR: Den emfanizetai stathera INTEGER h expression h metabliti.', 'Grammi:', grammi)
            exit(-1)

        return Eplace

    def idtail(name):
        global eksodos
        global grammi

        if (eksodos[0] == aristeri_parenthesi_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            actual_par_list()
            w = newtemp()
            genquad('par', w, 'RET', '_')
            genquad('call', name, '_', '_')

            if (eksodos[0] == deksia_parenthesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]
                return w
            else:
                print('ERROR: Theloume ) stin IDTAIL', grammi)
                exit(-1)
        else:

            return name

    def actual_par_list():
        global eksodos
        global grammi

        if (eksodos[0] == arithmos_token or eksodos[0] == aristeri_parenthesi_token or eksodos[0] == gramma_token):

            thisExpression = expression()
            genquad('par', thisExpression, 'CV', '_')

            while (eksodos[0] == komma_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                thisExpression = expression()
                genquad('par', thisExpression, 'CV', '_')

    def optional_sign():
        global eksodos
        global grammi

        if (eksodos[0] == prosthesi_token or eksodos[0] == afairesi_token):
            ADD_OP()

    def ADD_OP():
        global eksodos
        global grammi

        if (eksodos[0] == prosthesi_token):
            addOp = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]


        elif (eksodos[0] == afairesi_token):
            addOp = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        return addOp

    def MUL_OP():
        global eksodos
        global grammi

        if (eksodos[0] == pollaplasiasmos_token):
            oper = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        elif (eksodos[0] == diairesi_token):
            oper = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        return oper

    def condition():
        global eksodos
        global grammi

        Ctrue = []
        Cfalse = []

        BT1 = bool_term()

        Ctrue = BT1[0]
        Cfalse = BT1[1]

        while (eksodos[0] == or_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            backpatch(Cfalse, nextquad())

            BT2 = bool_term()

            Ctrue = merge(Ctrue, BT2[0])
            Cfalse = BT2[1]

        return Ctrue, Cfalse

    def bool_term():
        global eksodos
        global grammi

        BTtrue = []
        BTfalse = []

        BF1 = bool_factor()

        BTtrue = BF1[0]
        BTfalse = BF1[1]

        while (eksodos[0] == and_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]
            backpatch(BTtrue, nextquad())

            BF2 = bool_factor()

            BTfalse = merge(BTfalse, BF2[1])
            BTtrue = BF2[0]

        return BTtrue, BTfalse

    def bool_factor():
        global eksodos
        global grammi

        BFtrue = []
        BFfalse = []

        if (eksodos[0] == not_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == aristeri_agkili_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                C = condition()

                if (eksodos[0] == deksia_agkili_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    BFtrue = C[1]
                    BFfalse = C[0]

                else:
                    print('ERROR: Den emfanizetai "]" meta to condition.', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai "[" meta to not.', 'Grammi:', grammi)
                exit(-1)
        elif (eksodos[0] == aristeri_agkili_token):

            eksodos = lex_analitis()
            grammi = eksodos[2]

            C = condition()

            if (eksodos[0] == deksia_agkili_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                BFtrue = C[0]
                BFfalse = C[1]

            else:
                print('ERROR: Den emfanizetai "]" meta to condition.', 'Grammi:', grammi)
                exit(-1)
        else:
            Eplace1 = expression()

            relop = REL_OP()

            Eplace2 = expression()

            BFtrue = makelist(nextquad())
            genquad(relop, Eplace1, Eplace2, '_')
            BFfalse = makelist(nextquad())
            genquad('jump', '_', '_', '_')

        return BFtrue, BFfalse

    def REL_OP():
        global eksodos
        global grammi

        if (eksodos[0] == equal_token):
            relop = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        elif (eksodos[0] == mikrotero_token):
            relop = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        elif (eksodos[0] == mikrotero_iso_token):
            relop = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        elif (eksodos[0] == diaforo_token):
            relop = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        elif (eksodos[0] == megalytero_token):
            relop = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        elif (eksodos[0] == megalytero_iso_token):
            relop = eksodos[1]
            eksodos = lex_analitis()
            grammi = eksodos[2]

        else:
            print('ERROR: Den emfanizetai "=" h "<" h "<=" h "!=" h ">" h ">=" sth synarthsh.', 'Grammi:', grammi)
            exit(-1)
        return relop

    def call_main_part():
        global eksodos
        global grammi

        if (eksodos[0] == if_token):
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == name_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                if (eksodos[0] == equal_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (eksodos[0] == eisagwgika_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]

                        if (eksodos[0] == main_token):
                            eksodos = lex_analitis()
                            grammi = eksodos[2]

                            if (eksodos[0] == eisagwgika_token):
                                eksodos = lex_analitis()
                                grammi = eksodos[2]

                                if (eksodos[0] == anwkatw_teleia_token):
                                    eksodos = lex_analitis()
                                    grammi = eksodos[2]

                                    genquad('begin_block', 'main', '_', '_')
                                    main_function_call()
                                    while (eksodos[0] == gramma_token):
                                        main_function_call()
                                    genquad('halt', '_', '_', '_')
                                    genquad('end_block', 'main', '_', '_')

                                    print_Symbol_table("OutputFile")

                                    finalCode()   # sto telos tis "final" kanw reset ti lista listOfAllQuads me tis tetrades. Krataw antigrafo stin listOfAllQuadsFinal mesa stin genquad, wste na paragw sto telos kai to ".int" poy ebgaz

                                    delete_scope()

                                else:
                                    print('ERROR: Den emfanizetai ":" meta ta ".', 'Grammi:', grammi)
                                    exit(-1)
                            else:
                                print('ERROR: Den emfanizetai " meta th main.', 'Grammi:', grammi)
                                exit(-1)
                        else:
                            print('ERROR: Den emfanizetai main meta ta ".', 'Grammi:', grammi)
                            exit(-1)
                    else:
                        print('ERROR: Den emfanizetai " prin th main.', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai "==" meta to name.', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai "__name__" meta to if.', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai h leksi if sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    def main_function_call():
        global eksodos
        global grammi

        if (eksodos[0] == gramma_token):
            genquad('call', eksodos[1], '_', '_')
            eksodos = lex_analitis()
            grammi = eksodos[2]

            if (eksodos[0] == aristeri_parenthesi_token):
                eksodos = lex_analitis()
                grammi = eksodos[2]

                if (eksodos[0] == deksia_parenthesi_token):
                    eksodos = lex_analitis()
                    grammi = eksodos[2]

                    if (eksodos[0] == erwtimatiko_token):
                        eksodos = lex_analitis()
                        grammi = eksodos[2]
                    else:
                        print('ERROR: Den emfanizetai ";" meta thn ")".', 'Grammi:', grammi)
                        exit(-1)
                else:
                    print('ERROR: Den emfanizetai ")" meta thn "(".', 'Grammi:', grammi)
                    exit(-1)
            else:
                print('ERROR: Den emfanizetai "(" meta to id.', 'Grammi:', grammi)
                exit(-1)
        else:
            print('ERROR: Den emfanizetai h leksh id sthn arxh ths synarthshs.', 'Grammi:', grammi)
            exit(-1)

    startRule()


def intCode(written_file):
    for i in range(len(all_QuadsFinal)):
        quad = all_QuadsFinal[i]
        written_file.write(str(quad[0]))
        written_file.write(":  ")
        written_file.write(str(quad[1]))
        written_file.write("  ")
        written_file.write(str(quad[2]))
        written_file.write("  ")
        written_file.write(str(quad[3]))
        written_file.write("  ")
        written_file.write(str(quad[4]))
        written_file.write("\n")


file_with_quads = open('file_with_quads.int', 'w')
syntax_analitis()

print("Compilation completed successfully!!")
intCode(file_with_quads)
file_with_quads.close()
finalFile.close()
