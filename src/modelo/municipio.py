# Archivo donde se define la clase Recinto
# Un Recinto hereda Atributos y metodos de Acta

from recinto import Recinto


class Municipio(Recinto):
    def __init__(self, id, nom, ins, cc, fpv, mts, ucs, mas, f21, pdc, mnr, pan, val, bla, nul):
        self.__idm = id
        self.__nombrem = nom
        self.__inscritosm = ins
        self.__ccm = cc
        self.__fpvm = fpv
        self.__mtsm = mts
        self.__ucsm = ucs
        self.__masm = mas
        self.__f21m = f21
        self.__pdcm = pdc
        self.__mnrm = mnr
        self.__panm = pan
        self.__validosm = val
        self.__blancosm = bla
        self.__nulosm = nul

    @property
    def get_idm(self):
        return self.__idm

    @get_idm.setter
    def set_idm(self, id):
        self.__idm = id

    @property
    def get_nombrem(self):
        return self.__nombrem

    @get_nombrem.setter
    def set_nombrem(self, nom):
        self.__nombrem = nom

    @property
    def get_inscritosm(self):
        return self.__inscritosm

    @get_inscritosm.setter
    def set_inscritosm(self, ins):
        self.__inscritosm = ins

    @property
    def get_ccm(self):
        return self.__ccm

    @get_ccm.setter
    def set_ccm(self, cc):
        self.__ccm = cc

    @property
    def get_fpvm(self):
        return self.__fpvm

    @get_fpvm.setter
    def set_fpvm(self, fpv):
        self.__fpvm = fpv

    @property
    def get_mtsm(self):
        return self.__mtsm

    @get_mtsm.setter
    def set_mtsm(self, mts):
        self.__mtsm = mts

    @property
    def get_ucsm(self):
        return self.__ucsm

    @get_ucsm.setter
    def set_ucsm(self, ucs):
        self.__ucsm = ucs

    @property
    def get_masm(self):
        return self.__masm

    @get_masm.setter
    def set_masm(self, mas):
        self.__masm = mas

    @property
    def get_f21m(self):
        return self.__f21m

    @get_f21m.setter
    def set_f21m(self, f21):
        self.__f21m = f21

    @property
    def get_pdcm(self):
        return self.__pdcm

    @get_pdcm.setter
    def set_pdcm(self, pdc):
        self.__pdcm = pdc

    @property
    def get_mnrm(self):
        return self.__mnrm

    @get_mnrm.setter
    def set_mnrm(self, mnr):
        self.__mnrm = mnr

    @property
    def get_panm(self):
        return self.__panm

    @get_panm.setter
    def set_panm(self, pan):
        self.__panm = pan

    @property
    def get_validosm(self):
        return self.__validosm

    @get_validosm.setter
    def set_validosm(self, val):
        self.__validosm = val

    @property
    def get_blancosm(self):
        return self.__blancosm

    @get_blancosm.setter
    def set_blancosm(self, bla):
        self.__blancosm = bla

    @property
    def get_nulosm(self):
        return self.__nulosm

    @get_nulosm.setter
    def set_nulosm(self, nul):
        self.__nulosm = nul


