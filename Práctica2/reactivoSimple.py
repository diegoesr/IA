ACCIONES={'ST':'Cerrado, ingrese una tarjeta valida o recargue',
        'TCS':'Pase',
        'TSS':'Saldo insuficiente'
}

class AgenteRS:
    def __init__(self,reglas):
        self.reglas = reglas
    
    def actuar(self,percepcion,accion_basica=""):
        if not percepcion:
            return accion_basica
        if percepcion in self.reglas.keys():
            return self.reglas[percepcion]
        return accion_basica

torniquete=AgenteRS(ACCIONES)
percepcion=input("Indicar percepcion: ")
while percepcion:
    accion=torniquete.actuar(percepcion, 'Espera')
    print(accion)
    percepcion=input("Indicar percepcion: ")
