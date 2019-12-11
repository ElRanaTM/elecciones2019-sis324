# Archivo donde se define la clase Recinto
# Un Recinto hereda Atributos y metodos de Acta

from acta import Acta


class Recinto(Acta):
    def __init__(self, id, nom, ins, cc, fpv, mts, ucs, mas, f21, pdc, mnr, pan, val, bla, nul):
        self.__idr = id
        self.__nombrer = nom
        self.__inscritosr = ins
        self.__ccr = cc
        self.__fpvr = fpv
        self.__mtsr = mts
        self.__ucsr = ucs
        self.__masr = mas
        self.__f21r = f21
        self.__pdcr = pdc
        self.__mnrr = mnr
        self.__panr = pan
        self.__validosr = val
        self.__blancosr = bla
        self.__nulosr = nul

    @property
    def get_idr(self):
        return self.__idr

    @get_idr.setter
    def set_idr(self, id):
        self.__idr = id

    @property
    def get_nombrer(self):
        return self.__nombrer

    @get_nombrer.setter
    def set_nombrer(self, nom):
        self.__nombrer = nom

    @property
    def get_inscritosr(self):
        return self.__inscritosr

    @get_inscritosr.setter
    def set_inscritosr(self, ins):
        self.__inscritosr = ins

    @property
    def get_ccr(self):
        return self.__ccr

    @get_ccr.setter
    def set_ccr(self, cc):
        self.__ccr = cc

    @property
    def get_fpvr(self):
        return self.__fpvr

    @get_fpvr.setter
    def set_fpvr(self, fpv):
        self.__fpvr = fpv

    @property
    def get_mtsr(self):
        return self.__mtsr

    @get_mtsr.setter
    def set_mtsr(self, mts):
        self.__mtsr = mts

    @property
    def get_ucsr(self):
        return self.__ucsr

    @get_ucsr.setter
    def set_ucsr(self, ucs):
        self.__ucsr = ucs

    @property
    def get_masr(self):
        return self.__masr

    @get_masr.setter
    def set_masr(self, mas):
        self.__masr = mas

    @property
    def get_f21r(self):
        return self.__f21r

    @get_f21r.setter
    def set_f21r(self, f21):
        self.__f21r = f21

    @property
    def get_pdcr(self):
        return self.__pdcr

    @get_pdcr.setter
    def set_pdcr(self, pdc):
        self.__pdcr = pdc

    @property
    def get_mnrr(self):
        return self.__mnrr

    @get_mnrr.setter
    def set_mnrr(self, mnr):
        self.__mnrr = mnr

    @property
    def get_panr(self):
        return self.__panr

    @get_panr.setter
    def set_panr(self, pan):
        self.__panr = pan

    @property
    def get_validosr(self):
        return self.__validosr

    @get_validosr.setter
    def set_validosr(self, val):
        self.__validosr = val

    @property
    def get_blancosr(self):
        return self.__blancosr

    @get_blancosr.setter
    def set_blancosr(self, bla):
        self.__blancosr = bla

    @property
    def get_nulosr(self):
        return self.__nulosr

    @get_nulosr.setter
    def set_nulosr(self, nul):
        self.__nulosr = nul


