# Archivo donde se define la clase Acta


class Acta(object):
    def __init__(self, id, nm, ins, cc, fpv, mts, ucs, mas, f21, pdc, mnr, pan, val, bla, nul, est, p, dep, pro, loc):
        self.__id = id
        self.__nromesa = nm
        self.__inscritos = ins
        self.__cc = cc
        self.__fpv = fpv
        self.__mts = mts
        self.__ucs = ucs
        self.__mas = mas
        self.__f21 = f21
        self.__pdc = pdc
        self.__mnr = mnr
        self.__pan = pan
        self.__validos = val
        self.__blancos = bla
        self.__nulos = nul
        self.__estado = est
        self.__pais = p
        self.__departamento = dep
        self.__provincia = pro
        self.__localidad = loc

    @property
    def get_id(self):
        return self.__id

    @get_id.setter
    def set_id(self, id):
        self.__id = id

    @property
    def get_nromesa(self):
        return self.__nromesa

    @get_nromesa.setter
    def set_nromesa(self, nm):
        self.__nromesa = nm

    @property
    def get_inscritos(self):
        return self.__inscritos

    @get_inscritos.setter
    def set_inscritos(self, ins):
        self.__inscritos = ins

    @property
    def get_cc(self):
        return self.__cc

    @get_cc.setter
    def set_cc(self, cc):
        self.__cc = cc

    @property
    def get_fpv(self):
        return self.__fpv

    @get_fpv.setter
    def set_fpv(self, fpv):
        self.__fpv = fpv

    @property
    def get_mts(self):
        return self.__mts

    @get_mts.setter
    def set_mts(self, mts):
        self.__mts = mts

    @property
    def get_ucs(self):
        return self.__ucs

    @get_ucs.setter
    def set_ucs(self, ucs):
        self.__ucs = ucs

    @property
    def get_mas(self):
        return self.__mas

    @get_mas.setter
    def set_mas(self, mas):
        self.__mas = mas

    @property
    def get_f21(self):
        return self.__f21

    @get_f21.setter
    def set_f21(self, f21):
        self.__f21 = f21

    @property
    def get_pdc(self):
        return self.__pdc

    @get_pdc.setter
    def set_pdc(self, pdc):
        self.__pdc = pdc

    @property
    def get_mnr(self):
        return self.__mnr

    @get_mnr.setter
    def set_mnr(self, mnr):
        self.__mnr = mnr

    @property
    def get_pan(self):
        return self.__pan

    @get_pan.setter
    def set_pan(self, pan):
        self.__pan = pan

    @property
    def get_validos(self):
        return self.__validos

    @get_validos.setter
    def set_validos(self, val):
        self.__validos = val

    @property
    def get_blancos(self):
        return self.__blancos

    @get_blancos.setter
    def set_blancos(self, bla):
        self.__blancos = bla

    @property
    def get_nulos(self):
        return self.__nulos

    @get_nulos.setter
    def set_nulos(self, nul):
        self.__nulos = nul

    @property
    def get_estado(self):
        return self.__estado

    @get_estado.setter
    def set_estado(self, est):
        self.__estado = est

    @property
    def get_pais(self):
        return self.__pais

    @get_pais.setter
    def set_pais(self, p):
        self.__pais = p

    @property
    def get_departamento(self):
        return self.__departamento

    @get_departamento.setter
    def set_departamento(self, dep):
        self.__departamento = dep

    @property
    def get_provincia(self):
        return self.__provincia

    @get_provincia.setter
    def set_provincia(self, pro):
        self.__provincia = pro

    @property
    def get_localidad(self):
        return self.__localidad

    @get_localidad.setter
    def set_localidad(self, loc):
        self.__localidad = loc

