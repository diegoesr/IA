#Estados: ST, TCS, TSS
#Acciones: pedir-tarjeta, verificando, esperar-sin saldo
#Percepciones: Cerrado, Pase, ingrese una tarjeta valida o recargue, Sin tarjeta

REGLAS={'ST':'pedir-tarjeta',
        'TCS':'Pase',
        'TSS':'esperar-sin saldo'
}

MODELO={('ST','pedir-tarjeta','TCS'):'TCS',
        ('TCS','verificar','ST'):'ST',
        ('ST','pedir-tarjeta','TSS'):'TS'        
}

class ARBM:
        def __init__(self,modelo,reglas,estado_inicial="",accion_inicial=""):
                self.modelo = modelo
                self.reglas = reglas
                self.estado_inicial = estado_inicial
                self.accion_inicial = accion_inicial
                self.accion=None
                self.estado = self.estado_inicial
                self.ult_accion = self.accion_inicial
        
        def actuar(self,percepcion):
            if not percepcion:
                return self.accion_inicial
            clave=(self.estado,self.ult_accion,percepcion)
            if clave not in self.modelo.keys():
                self.estado=self.estado_inicial
                self.accion=self.accion_inicial
                self.ult_accion=self.accion_inicial
                return self.accion_inicial
            self.estado=self.modelo[clave]
            if self.estado not in self.reglas.keys():
                self.estado=self.estado_inicial
                self.accion=self.accion_inicial
                self.ult_accion=self.accion_inicial
                return self.accion_inicial

exp=ARBM(MODELO,REGLAS,'ST','Cerrado, ingrese una tarjeta valida o recargue')
percepcion=input("Indicar percepcion: ")
while percepcion:
       accion=exp.actuar(percepcion)
       print(accion)
       percepcion=input("Indicar percepcion: ")