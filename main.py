import pygetwindow as pg
import time as t

from ReconhecerObjetos import ReconhecerCelular
from CaptacaoImagensNegativas import ImportarImagens

def ProcuraAbasNaoPermitidas(abas, termo):
    for elements in abas:
        if(termo) in elements:
            if(elements != None):
                elemento_encontrado = elements
                return elemento_encontrado
                break
            else:
                return False
                break

def FechaAbasNaoPermitidas(Google, Firefox, Edge, VisualStudio):
    if(Google != None):
        Google = Google.upper()
        abaCorreta = pg.getWindowsWithTitle(Google)[0]
        if (abaCorreta.title != ''):
            abaCorreta.close()
    if(Firefox != None):
        Firefox = Firefox.upper()
        abaCorreta = pg.getWindowsWithTitle(Firefox)[0]
        if (abaCorreta.title != ''):
            abaCorreta.close()
    if(Edge != None):
        Edge = Edge.upper()
        abaCorreta = pg.getWindowsWithTitle(Edge)[0]
        if (abaCorreta.title != ''):
            abaCorreta.close()

    if(VisualStudio != None):
        VisualStudio = VisualStudio.upper()
        abaCorreta = pg.getWindowsWithTitle(VisualStudio)[0]
        if (abaCorreta.title != ''):
            abaCorreta.close()


def countdown(num_of_secs):
    while num_of_secs:
        AbasAbertas = pg.getAllTitles()
        Google = ProcuraAbasNaoPermitidas(AbasAbertas, 'Google')
        Firefox = ProcuraAbasNaoPermitidas(AbasAbertas, 'Firefox')
        Edge = ProcuraAbasNaoPermitidas(AbasAbertas, 'Edge')
        VisualStudio = ProcuraAbasNaoPermitidas(AbasAbertas, 'Visual Studio')

        FechaAbasNaoPermitidas(Google, Firefox, Edge, VisualStudio)

        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        t.sleep(1)
        num_of_secs -= 1

    print('O Tempo Acabou')
    return False

if __name__ == '__main__':
    countdown(3920)
    #ImportarImagens()




